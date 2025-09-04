# Omron FINS

Most of the work done by the IOCs for the various FINS PLCs at ISIS consists of reading and writing to various places in the memory of that particular PLC. Some IOCs also perform some internal logic.

The manuals referenced on this page can be found on the shares drive, in Manuals\OMRON_FINS_PLCs. There you can also find the images on this page.

The Omron FINS is a PLC controlled via a driver first written at Diamond, see [here](https://github.com/ISISComputingGroup/EPICS-FINS). The IOC works by loading an instrument specific `FINS_01.cmd` in `configurations/fins`, which will load an instrument specific `db` from `ioc/master/FINS/db`. The dbs in here are usually created from a number of templates matching specific PLC memory addresses to PVs. This is the case because PLCs used for different applications have different things stored in their memory, and to read/write various pieces of data the IOC needs to know the exact memory address for that data. Each individual PLC has its own memory map, which shows what memory address stores what thing, and each specific IOC is based on that.

Currently the following specific FINS PLC installations are supported in IBEX:

* IMAT FINS PLC
* LARMOR air PLC
* [SANS2D vacuum PLC](SANS2D-vacuum-PLC)
* WISH vacuum PLC
* ZOOM vacuum PLC
* [Helium Recovery PLC](Helium-Recovery-PLC) - stores information needed for the Helium Level Monitoring project
* SANDALS Gate Valve PLC

{#omron_fins_writing_ioc}
## Writing IOCs for FINS PLCs

IOCs for FINS PLCs at ISIS use the EPICS asyn driver support to communicate with the PLC. For getting input from hardware, you need DB records to have an INP field such as:

`
field(INP,  "@asyn($(PORT), $(MEMORY_ADDRESS), 5.0) FINS_DM_READ")
`

where the value of `$(PORT)` should usually be PLC, `$(MEMORY_ADDRESS)` is the memory address of the data you want to read/write in the PLC and should be taken from the PLCs memory map, and 5.0 is a timeout. `FINS_DM_READ` is an example FINS command supported by the asyn driver we have from Diamond, and different methods need to be used for different types of data. All the commands supported by the driver are listed [here](https://github.com/ISISComputingGroup/EPICS-FINS/blob/master/FINSApp/src/finsUDP.c).

Some examples of correct DTYP and INP fields for different situations are:

1. `field(DTYP, "asynInt32")`

   `field(INP,  "@asyn(PLC, $(MEMORY_ADDRESS), 5.0) FINS_DM_READ")`

This should be used by mbbi and bi records and also longin records that read 16 bit signed integers from 0 to 32767 or unsigned 16 bit integers.         The asynInt32 interface provides support for 32 bit integers, and the `FINS_DM_READ` command asks the PLC for a 16 bit integer, which is then put into a 32 bit integer in the driver. When that is done, the number is left padded with 8 zeroes, which means it will lose its sign if it is signed and be read as a positive number. Therefore, records that need to read negative integers should not use this pattern.

2. `field(DTYP, "asynInt16ArrayIn")`

   `field(INP,  "@asyn(PLC, $(MEMORY_ADDRESS), 5.0) FINS_DM_READ")`

This should be used for reading 16 bit signed integers. Using the 16 bit integer array support means the 16 bit signed value will be put into an array of signed 16 bit integers as the first element. This means you will read a one element integer array, and therefore the record reading from hardware needs to be a waveform and have `field(NELM, "1") field(FTVL, "SHORT")`. You can then have a user-facing longin record to read from the waveform and store the standalone 16 bit value.

3. `field(DTYP, "asynInt32")`

   `field(INP,  "@asyn(PLC, $(MEMORY_ADDRESS), 5.0) FINS_DM_READ_32")`

This is used for reading 32 bit signed integers.

4. `field(DTYP, "asynFloat64")`

   `field(INP,  "@asyn(PLC, $(MEMORY_ADDRESS), 5.0) FINS_DM_READ_32")`

This is used for reading 32 bit floating point numbers. The asyn interface has support only for 64 bit floating point numbers, but the FINS command asks for 4 bytes (32 bits) and then casts the result to a double.

## The FINS protocol

The FINS protocol is an applications layer communications protocol designed for industrial applications and made by Omron. FINS stands for Factory Interface Network Service.

Throughout this guide, when I mention a manual, it can be found on the shares drive in Manuals/OMRON_FINS_PLCs .

FINS communications can be done over a serial connection or over a network. For serial connections, it uses the Host Link protocol on the Data Link layer of the OSI model. If used over a network, FINS can be used over a wide variety of Data Link layer protocols, including Controller Link and Ethernet. At ISIS, FINS PLC communication is done via Ethernet. FINS PLCs also supports another protocol instead of FINS, called C-mode, which is specialised for Host Link, but we do not use that. For more information, see Section 1 of the Comms Reference manual.

When using FINS over Ethernet, it can work with both TCP and UDP. FINS over TCP though is only supported on the CS1W-ETN21 and CJ1W-ETN21 models. The default UDP/TCP port number is 9600.

### FINS Frames

When using FINS over UDP, the FINS frame is the part of the UDP packet after the UDP protocol specific header. The first 10 bytes of the FINS command frame represent the FINS frame header, and the rest of the frame represent either a command or a response, which have different formats. For FINS over TCP, after the TCP header and before the FINS frame there is a special FINS/TCP header used by FINS to handle TCP connections.

Most of the FINS PLCs at ISIS use FINS over TCP, The Helium recovery PLC uses UDP. For more information about FINS in general, look at section 7-1 of the Ethernet manual. Section 7-3 offers detailed information about FINS over UDP.

There are some very useful diagrams showing the structure of FINS frames and FINS/TCP headers in the same folder as the manuals on the shares drive.

### FINS header

The first 10 bytes of the FINS command frame represent the FINS frame header, and the rest of the frame represent the command.

The structure of the FINS frame header is as follows (each of the elements take up one byte):

- Information Control Field or ICF: Displays whether the frame is for a command or a response, and whether a response is required or not. For our purposes, this byte should `0x80` for a command and `0xC1` for a reply.
- Reserved or RSV byte: should always be 0.
- Gate Count or GCT: The number of network bridges the frame needs to pass through. For our purposes, it should always be `0x02`.
- Destination Network Address or DNA: The address of the network to which the receiver belongs. This address is of the entire network, and not of just the machine, and is different from the IP address. It is 0 for Local Network, and 1 to 127 for remote networks.
- Destination Node Address or DA1: The node of the receiver, which is an address needed by the FINS protocol, and is different from the IP address. It has values from 0 to 256, with 0 for the local PLC unit and 256 for broadcasting.
- Destination Unit Address or DA2: The number of the unit of the destination node to which the command is addressed. It will typically be 0, for the CPU unit. A unit is one of the modules mounted on rails that make up the PLC.
- Source network address or SNA: The network address of the sender. The possible values of SNA are the same as of DNA.
- Source node address or SA1: The node of the sender. The possible values of SA1 are the same as for DA1.
- Source unit address or SA2: The unit address of the sender. It will typically be 0, for the CPU unit.
- Service ID or SID: a number used to identify the FINS processes generating the transmission. It can have values from 0 to 255.

If you need more detail about the FINS header, look at section 7-2 of the Ethernet manual.

### FINS Command body

The first two bytes after the header represent the command code. All the FINS command codes can be found in section 5-1 of the Comms Reference manual. Most of the commands used at ISIS are Memory Area Read, with code `0x0101`, and Memory Area Write, with code `0x0102`.

The rest of the body consists of command parameters and perhaps data. It can be up to 2000 words in length. The length and format depends on the command code. For reference, in section 5-3 of the Comms Reference Manual you can find the parameter formats and other details for each command.

The first byte after the command code represents the I/O memory area code. The next three bytes indicate the start address from which it will read or write. Of these three, the first two bytes indicate the memory address of the first word from where to read/write, and the third byte indicates the individual bit from where reading or writing starts. This third byte is 0 for word designated memory addresses, where each word is considered an element. If it is not 0, then each individual bit is considered an element. After this address, two more bytes represent the number of elements to read/write. For write commands, what follows after is the data which you want to write.

You can find a list of all I/O memory area codes in section 5-2-2 of the Comms Reference manual, and more details about the memory start address in section 5-2-1 of the same manual.

### FINS response body

Just as with the command body, the first two bytes represent the code of the command which is being replied to. After that, two bytes represent the error code. It is 0 for no errors, and all the other error codes are detailed in section 5-1-3 of the Comms Reference Manual. Following the error codes are a number of words equal to the number of words given in the read command representing the data you want to read. For write commands, the response ends with the error code.

### FINS/TCP header

Unlike UDP, TCP is a connection based protocol. Since a virtual connection needs to be established before you can send packets, for FINS over TCP there is an extra FINS/TCP header before the FINS frame that helps to handle the virtual connection. For establishing a connection, besides the usual TCP packets, the client and server need to exchange FINS node addresses so that the PLC can manage the connections properly.

The structure of the of the FINS/TCP header is as follows, with each element taking up 4 bytes:

- Header: is always `0x46494E53`, which is ASCII for `FINS`.
- Length: specifies length of data from the FINS/TCP command code onwards, including the FINS frame as well.
- Command code: There a couple of commands for FINS/TCP for exchanging node addresses, sending FINS frames and managing errors and connections. 
- Error code: It is 0 for no errors, and for some commands it is not even used.
- Client Node address: only part of the FINS/TCP header for some commands.
- Server Node address: only part of the FINS/TCP header for the FINS NODE ADDRESS DATA SEND (SERVER TO CLIENT) command.

The FINS/TCP connections and commands should be handled by the C driver originally written at Diamond and we should not worry about the FINS/TCP header. If you need more information, section 7-4-2 of the Ethernet Manual gives details for each command, and section 7-4-1 gives a more detailed overview about FINS over TCP.

## Connection

### PLC init

The fins PLC communication is set up with the following:

```
finsUDPInit(<port Name>, <address>, <protocol>, <simulate>)
```
where:

- port name: ASYN port name (usually PLC)
- address: ip address of the PLC 
- protocol: which protocol to use
    - "TCP": use TCP communication
    - "TCPNOHEAD": use TCP comms, but without FINS-TCP header. This is required (and should only be used for) the devsim IOC tests. This mode was added because the emulator framework does not support UDP, only TCP or serial. Normally, using FINS over TCP requires an extra header, but we did not want to complicate the emulator and deal with a header and FINS/TCP commands that EPICS code does not change at all. Therefore, this mode was added as a "hack" to make testing the Helium Recovery PLC easier.
    - anything else: use UDP protocol
- simulate: whether to simulate calls
    - 0: Do not simulate (real device or devsim)
    - 1: Simulate (don't send commands), this is required for recsim as it lets device initialisation complete successfully with no device

{#omron_fins_configuration}
## Configuration

In order to run this IOC and talk to the real PLC, you need to have the correct instrument specific `FINS_01.cmd` in `configurations/fins`. See below an example:

```
#Init and connect
finsUDPInit("PLC", "$(PLC_IP)", "UDP", 0, "$(PLC_NODE=)")

## Load our record instances
dbLoadRecords("${TOP}/db/he-recovery.db","P=$(MYPVPREFIX),Q=EXAMPLE:")

```

In the IBEX GUI, make sure to set the two macros for the FINS IOC, PLC_IP and PLC_NODE. PLC_IP refers to the IP address of the PLC, and the node is a FINS protocol application layer specific address that differentiates between nodes (such as PLCs or host computers). By default, it corresponds to the last byte of the IP address, but for some FINS PLCs this is not the case.

For running the IOC for testing, see below.



## Testing the FINS IOC in the Ioc Test Framework

In contrast to the normal operation of a FINS PLC, the instrument specific `FINS_01.cmd` file that should be used for the IOC Tests for a FINS PLC should be placed in an instrument specific folder in [`ioc\master\FINS\exampleSettings`](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/FINS/exampleSettings). This cmd file should have the appropriate `finsUDPInit` calls for devsim or recsim, as detailed below, and also the usual `dbLoadRecords` call to load the instrument specific db.

### Testing the FINS IOC in DevSim

If you want to test the IOC for a FINS PLC in devsim mode, you need to add to the FINS_01.cmd file used by that specific FINS IOC the line:
```
$(IFDEVSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 0, "$(PLCNODE=)")
```  

At the same time, the file should either not have any other `finsUDPInit` call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.

### Testing the FINS IOC in RecSim

If you want to test the IOC for a FINS PLC in recsim mode, you need to add to the FINS_01.cmd file used by that specific FINS IOC the line:
```
$(IFRECSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 1, "$(PLCNODE=)")
```  

At the same time, the file should either not have any other `finsUDPInit` call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.

## Emulator

The emulator for FINS PLCs uses the pattern used by the SKF MB340 chopper. 

Because it was written as part of https://github.com/ISISComputingGroup/IBEX/issues/5333, currently this emulator only works with the Helium Recovery PLC. The stream interface and response utilities should work with all other FINS PLCs at ISIS, but the device module is specific to helium recovery because it has dictionaries emulating the memory map of that PLC. Currently, there is no way to specify what device to use when testing.

**Note:** The FINS protocol involves reading 16 bit integers, a 32bit read from the driver is actually two consecutive 16 bit reads, similarly for a 32bit float. Though the PLC uses big endian format for its 16bit integers, the least significant part of a 32 bit number is stored first. So we have two big endian 16 bit integers stored in little endian order. The emulator needs to perform some extra logic to handle this.


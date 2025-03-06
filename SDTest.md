# Introduction

The SDTEST IOCs allow us to set up communications with an arbitrary device on-the-fly. This often happens if an instrument acquires a bit of equipment to achieve a short term goal. We should try and ensure that if a device is to be used long-term that we find out about it early enough to provide a dedicated IOC, or deliver it as soon as practical.

The serial device test module consists of IOCs called SDTEST_01, SDTEST_02 etc. Each of these can control up to 8 separate serial devices.

Configuration of the devices is via EPICS macros, which can be defined in the globals.txt file located in c:/Instrument/settings/config/NDXLARMOR/configurations
This globals.txt file is loaded on IOC startup, so you will need to stop/start the IOC after making a change. 

All macros in globals.txt start with the IOC name followed by two underscores, so SDTEST_01\_\_ for IOC SDTEST_01   Defining a macro  SDTEST_01__NAME3 here will create one that can be referenced as $(NAME3) by IOC SDTEST_01

Each SDTEST IOC supports 8 devices numbered 1 to 8. Settings for each of these have the device number appended e.g. $(PORT3) is COM/serial port for the third device attached etc.

Arbitrary string commands can be sent to the device via EPICS process variables, but it is also possible to define a way to send and receive a particular numeric value through a PV. The format of how to send this value and how often to poll for it need to be specified and this is described later.

By way of example we will consider a power supply. In globals.txt we have:


# Macros

Each SDTest IOC supports communication with 8 separate devices on 8 ports. Macros should be suffixed by the device number in the range `1` to `8` inclusive (e.g. `PORT1`):

- `PORT`: Communications port (e.g. COM1)
- `BAUD`: Baud rate (default: 9600)
- `BITS`: Message bits (default: 8)
- `PARITY`: Message parity (default: none)
- `STOP`: Number of stop bits (default: 1)
- `CLOCAL`: Output flow control using DSR signal (Y/N, default: Y)
- `CRTSCTS`: Hardware flow control (Y/N, default: N)
- `IXON`: Software flow control for output (Y/N, default: N)
- `IXOFF`: Software flow control for input (Y/N, default: N)
- `OEOS`: Output terminator (default: \r\n)
- `IEOS`: Input terminator (default: \r\n)
- `NAME`: Name of the device
- `SCAN`: Scan rate (Any valid EPICS scan value (Passive, .1 second, .2 second, .5 second, 1 second, 2 second, 5 second or 10 second)
- `GETOUT`: Command for getting the readback
- `GETIN`: Format of the readback
- `SETOUTA`: Command for setpoint
- `SETOUTB`: Secondary setpoint value
- `SETOUTC`: Tertiary setpoint value
- `SETIN`: Format of the setpoint
- `INITOUT`: Initialisation command
- `INITIN`: Format of init response
- `INITP`: Send an initialisation command (default: NO)
- `PROTO`: Path to custom protocol file, (default: SDTEST-default.proto)


## Example

This is an example of `globals.txt` for using SDTest for talking to a Keithley 2000:

```
SDTEST_01__NAME1=Kiethley2000_1
SDTEST_01__PORT1=COM5
SDTEST_01__BAUD1=9600
SDTEST_01__BITS1=8
SDTEST_01__PARITY1=none
SDTEST_01__STOP1=1
SDTEST_01__IEOS1=\\r       # end of line terminator for input (note \\ to escape \)
SDTEST_01__OEOS1=\\r       # end of line terminator for output (note \\ to escape \)
SDTEST_01__SCAN1=.5 second     # scan (polling) rate for reading special numeric value. 
SDTEST_01__GETOUT1=:MEAS:CURR:DC?    # string to send to read the special numeric value   
SDTEST_01__GETIN1="%f"     # expected format of reply to sending string specified in GETOUT
SDTEST_01__SETOUTA3=PC           # first part of string to send for setting special numeric value
SDTEST_01__SETOUTB3=0x20         # second part of string to send for setting special numeric value
SDTEST_01__SETOUTC3=%f           # third part of string to send for setting special numeric value
SDTEST_01__SETIN3=OK             # expected reply from SETOUT* Use e.g. %*40c to ignore reply
```

As these all start SDTEST_01\_\_ and end in 3 they refer to the third device attached to IOC SDTEST_01
You do not need to specify all values, here are defaults

# Process variables

Process variables defined are of the form {instrument prefix}{ioc name}{device index}{variable} e.g. for the first device (P1) on IOC SDTEST_01

```
IN:LARMOR:SDTEST_01:P1:NAME          (read)  short name of device 
IN:LARMOR:SDTEST_01:P1:DEVICE        (read)  COM port of device
IN:LARMOR:SDTEST_01:P1:INIT          (write) initialise device
IN:LARMOR:SDTEST_01:P1:COMM          (write) send arbitrary string to device
IN:LARMOR:SDTEST_01:P1:REPLY         (read)  reply from device after sending COMM string above
IN:LARMOR:SDTEST_01:P1:REPLY:ASYNC   (read)  continuously monitors serial port for 
                                             .. asynchronous output (40 char epics string)
IN:LARMOR:SDTEST_01:P1:REPLYWF:ASYNC (read)  continuously monitors serial port for asynchronous 
                                             .. output (epics 1024 char waveform)
IN:LARMOR:SDTEST_01:P1:SETVAL        (write) write a numeric value to device using previously 
                                             .. specified command format
IN:LARMOR:SDTEST_01:P1:GETVAL        (read)  numeric value read from device (ususally because 
                                             .. of a periodic SCAN)
IN:LARMOR:SDTEST_01:P1:ASYNREC       (write) Access to an EPICS 
                                             .. _ASYN Record: http://www.aps.anl.gov/epics/modules/soft/asyn/R4-26/asynRecord.html 
```

When polling the GETVAL process variable, the the IOC will send `$(GETOUT)` and expect to receive `$(GETIN)`  Within `$(GETIN)` can be printf style format characters to match
the value being read. For valid format converters see __ http://epics.web.psi.ch/software/streamdevice/doc/formats.html

When writing to the SETVAL process variable, the IOC will construct a string from concatenating `$(SETOUTA)`, `$(SETOUTB)` and `$(SETOUTC)`. The writing format character (e.g. %f)
must be in SETOUTC, normally only SETOUTA and SETOUTC are specified, sometimes just SETOUTC. SETOUTB is for sending a special character between these two values, such as a space.
SETOUTA and SETOUTC are quoted strings as per __ http://epics.web.psi.ch/software/streamdevice/doc/protocol.html whereas SETOUTB can be a byte number such as 0x20 for a space character.  Only use SETOUTB is you have trouble with using SETOUTA and SETOUTC - in particular needing to send a space character between and string
and a format converter that seems to get stripped otherwise.

For INIT, macros INITOUT and INITIN 
 
The ASYN record PV can be useful for diagnostics

# Logging

Typically you would point a block at `IN:LARMOR:SDTEST_01:P1:GETVAL` to get values logged

# SDTEST Synoptic OPI

An OPI file SDTEST.opt exists that opens a display for managing the serial device, which
includes the option to open an asyn record OPI - see screenshots at bottom 
of _ASYN Record: http://www.aps.anl.gov/epics/modules/soft/asyn/R4-26/asynRecord.html

# More complex cases

Can use `PROTO` macro to specify another stream device protocol file rather than  `SDTEST-default.proto`

See http://epics.web.psi.ch/software/streamdevice/doc/  

because you will load the same DB file, you will need to provide the same functions as `SDTEST-default.proto`  i.e. `getValue()` and `setValue()`
Place files in `$(ICPCONFIGROOT)/SDTEST` on the machine



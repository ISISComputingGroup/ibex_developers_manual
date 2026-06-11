# NGPS Power Supply

Controls the new PSUs that are going to be used on the Muon Front End.

## Communications

### Serial comms

See comments on https://github.com/ISISComputingGroup/IBEX/issues/3447 for details of what was tried. Short version is that a USB-422/485 adapter plugged into a laptop works but a moxa does not.

### Ethernet comms

See details of setup [here](/specific_iocs/magnets/Muon-NGS-Power-Supply-Firewall)

### Status of the device

The status of the device is encoded in 32 bits. The status of the device depending on which bits are turned on. See page 30 of the manual. 

The device returns its status as an 8 digit 0-padded hexadecimal number. Each digit is directed into its own `mbbiDirect` PV from which the individual bits can be accessed.

### Faults

Currently (2018-07-31) there is a single binary input PV that is '1' if there is a fault and '0' if not. 

A fault corresponds to one of the ones below with the bit corresponding to them in the device's internal status:
- Fault condition (bit #1)
- Mains fault (bit #21)
- Earth Leakage (bit #22)
- Earth Fuse (bit #23
- Regulation Fault (bit #24)
- DCCT fault (bit #30)

### Errors

The device has no error state but will return error codes if it cannot process the command you have given it. The list of error codes can be found on page 49 of the manual. Currently, the IOC captures the last error code as a string and displays it in the OPI.

If the device is talking slowly i.e. getting lots of command mismatches, only doing writes when on trace then it may need a route deleting. As admin run:
```
route delete 130.246.52.0
```

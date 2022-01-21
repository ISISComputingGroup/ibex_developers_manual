This page documents an "idealised" communication protocol for communicating with new sample environment drivers at ISIS. It is intended as a useful starting point if new protocols are being developed from scratch and as a set of nice-to-haves for new equipment being purchased.

# Transport layer

### Serial (RS232, RS422, RS485)

This is the most common transport layer at ISIS. Serial settings are flexible in all of our drivers but the most common configuration is:

- Baud rate: 9600
- Data bits: 8
- Parity: None
- Stop bits: 1
- Flow control: Off

RS232 is preferable, RS422 and RS485 are avoided as far as reasonable. Note that distances can be extreme if higher baud rates are required.  Preferred socket is DB-9, but DB-25 also acceptable.

### Ethernet

Ethernet is a commonly used and well-supported transport layer at ISIS using RJ45 ports (AKA 8P8C sockets). Any other port type is to be avoided. It is also preferable that devices use DHCP to find their IP address rather than being issued a static address.

### USB

USB devices are difficult to integrate into the Experiment Control System, so should be avoided.

### Manufacturer software / DLLs

We prefer not to use these interfaces.  However, in some cases, we may be able to work with these.

### MODBUS

MODBUS is more difficult for us than ASCII protocols but we can deal with this.

### Connection Hardware

Use “standard”, easily maintainable and available connection hardware where possible, so no unusual or bespoke sockets, cables or adapters preferred.

# Protocol

### Termination characters

It is very helpful for devices to terminate their messages with a unique set of characters that do not appear elsewhere in the message. A common example of a terminator is a carriage-return, line-feed pair (`<CR><LF>`, `/r/n`, HEX: `0D 0A`).

### Readability/encoding

Commands to a device are ideally human-readable so that they can be used via terminal emulators and the device interacted with. Many protocols use an ASCII encoding.

For example, a temperature controller might implement commands similar to the following:

```
Driver to device:
temp?<CR><LF>
(HEX: 74 65 6D 70 3F 0D 0A)

Device to driver:
temp=30.5<CR><LF>
(HEX: 74 65 6D 70 3D 33 30 2E 35 0D 0A)
```

### Replies

All commands to a device should ideally return some form of reply. This helps the control system to distinguish between a device which is unplugged and an incorrect or invalid command.

Where no data needs to be returned, a device could generate an "ACK" or "OK" or similar response. Commands which are invalid or rejected could return a "NAK" or "NOK" or "error" or similar responses.

### Unsolicited messages

We prefer not to receive unsolicited messages. It is better for a driver to explicitly ask for a parameter each time it is required.

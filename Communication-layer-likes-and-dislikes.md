This page documents an "idealised" communication protocol for communicating with new sample environment drivers at ISIS. It is intended as a useful starting point if new protocols are being developed from scratch, and as a set of nice-to-haves for new equipment being purchased.

# Transport layer

### Serial (RS232, RS422, RS485)

This is the most common transport layer at ISIS. Serial settings are flexible in all of our drivers but the most common configuration is:
- Baud rate: 9600
- Data bits: 8
- Parity: None
- Stop bits: 1
- Flow control: Off

### Ethernet

Ethernet is a commonly used and well-supported transport layer at ISIS.

### USB

USB devices are difficult to implement for ISIS, and we prefer not to have to use USB wherever possible

# Protocol

### Termination characters

It is very helpful for devices to terminate their messages with a unique set of characters that do not appear elsewhere in the message. A common example of a terminator is a carriage-return line-feed pair (HEX: `0D 0A`).

### Readability/encoding

Commands to a device are ideally human readable, so that they can be used via terminal emulators. Many protocols use an ASCII encoding.

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

All commands to a device should return some form of reply. This helps the control system to distinguish between a device which is unplugged and an incorrect or invalid command.

Where no data needs to be returned, a device could generate an "ACK" or "OK" or similar response. Commands which are invalid or rejected could return a "NAK" or "NOK" or "error" or similar responses.

### Unsolicited messages

We prefer not to receive unsolicited messages. It is better for a driver to explicitly ask for a parameter each time the driver wants to read it.
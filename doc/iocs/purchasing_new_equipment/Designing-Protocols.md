{#designing_comms_protocol}
# Designing protocols

```{important}
If you are considering purchasing a new device or designing a new protocol, please read the
{doc}`../Purchasing-New-Equipment` page before continuing with this guide.
```
 
Ideally the transport layer will be one of those listed in the {doc}`../Purchasing-New-Equipment` guide. If a protocol needs to be developed, we would advocate using {external+secop:doc}`SECoP <index>`. If that is not an option for you, then the following guidelines allow for easier integration. 

## Termination characters 

It is very helpful for devices to terminate their messages with a unique set of characters that do not appear elsewhere in the message. A common example of a terminator is a carriage-return, line-feed pair (`<CR><LF>`, `\r\n`, HEX: `0D 0A`). 

## Readability/encoding 

Commands to a device are ideally human-readable so that they can be used via terminal emulators and the device interacted with. Many protocols use an ASCII encoding. 

For example, a temperature controller might implement commands like the following: 

``` 
Driver to device: 
temp?<CR><LF> 
(HEX: 74 65 6D 70 3F 0D 0A) 

Device to driver: 
temp=30.5<CR><LF> 
(HEX: 74 65 6D 70 3D 33 30 2E 35 0D 0A) 
``` 

## Replies 

All commands to a device, whether setting or reading a value, should ideally return some form of reply. This helps the control system to distinguish between a device which is unplugged and an incorrect or invalid command. 

Where no data needs to be returned, a device could generate either an `ACK` ASCII control code or a reply string like `OK` or similar response. Commands which are invalid or rejected could return a `NAK` ASCII control code, or a text string like `NOK` or `error` or similar responses. 

## Unsolicited messages 

We prefer not to receive unsolicited messages. It is better for a driver to explicitly ask for a parameter each time it is required. 
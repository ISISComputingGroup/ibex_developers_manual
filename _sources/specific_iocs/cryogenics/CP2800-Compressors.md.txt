# CP2800 Compressors

There are 2 independent CP2800 Compressors on HIFI_CRYOMAG. These provide high pressure helium gas to 2 independent pulse tube cold heads via a valve which allows high pressure gas in and low pressure gas out. The valve is driven by the control circuits in the compressors.
Each cold head has 2 stages, with the hot end of stage 2 linked to the cold end of stage 1. The 1st stages of the cold heads get to around 40K and are used to cool the thermal shields surrounding the magnet coils. The 2nd stages cool the coils to around 4K, just below the superconducting threshold. 

### Command data packet

This gist is that a command looking something like `<STX> <ADR> <CMD_RSP> <DATA> <CKSUM1> <CKSUM2> <CR>` is sent.
- `STX` is the start of text character, or hex 0x02. This serves to sync the receiver to receive a new message, and purges any data received since the previous `STX` or carriage return was received.
- `ADR` is the address field, which is a macro in the proto file. This is a one byte field that can range from `0x10` to `0xFE`.
- `CMD_RSP` is the command response field. Essentially this tells the protocol and the device which type of message is being received/sent, a command or a response status.
- `DATA` is the optional data. `STX` and carriage returns cannot appear in the data field. to get around this, the format converter `%!` is used. See below for more info. 
- `CKSUM1,2` are checksum characters for the message.
- `CR` is a carriage return.

The reference manual for the communications is the 'data dictionary' on the CP2800 manuals share.

### SMDP Converter 

CP2800 communications use a format converter `%!`, used to remove escape characters from commands sent to the device. Details of this can be found in the CP2800 manuals folder in the controls group manuals share in the file `Sycon Multi Drop Protocol II`. 

### Error codes
The machine can send the following error codes:

|Code|Error                                                                                              |
|----|---------------------------------------------------------------------------------------------------|
| 0  | No Error                                                                                          |
| 1  |IC2 bus failure. Cycle power if this occurs. If this persists, contact factory.                    |
| 2  |5V power too high - occurs if power is above 5.25V. Contact factory                                |
| 3  |5V power too high - occurs if power is below 4.75V. Contact factory                                |
| 4  |Compressor is in lockout mode due to too many errors in a certain time. Cannot restart until a code is entered. Contact factory                                                                                          |
| 5  |Order of phase power is wrong. Rewire the compressor input by switching around 2 of the power wires|
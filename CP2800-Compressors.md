### Command data packet

This gist is that a command looking something like `<STX> <ADR> <CMD_RSP> <DATA> <CKSUM1> <CKSUM2> <CR>` is sent.
- `STX` is the start of text character, or hex 0x02. This serves to sync the receiver to receive a new message, and purges any data received since the previous `STX` or carriage return was received.
- 'ADR' is the address field, which is a macro in the proto file. This is a one byte field that can range from `0x10` to `0xFE`.
- `CMD_RSP` is the command response field. Essentially this tells the protocol and the device which type of message is being received/sent, a command or a response status.
- `DATA` is the optional data. `STX` and carriage returns cannot appear in the data field. to get around this, the format converter `%!` is used. See below for more info. 
- `CKSUM1,2` are checksum characters for the message.
- `CR` is a carriage return.

### SMDP Converter 

CP2800 communications use a format converter `%!`, used to remove escape characters from commands sent to the device. Details of this can be found in the CP2800 manuals folder in the controls group manuals share in the file `Sycon Multi Drop Protocol II`. 
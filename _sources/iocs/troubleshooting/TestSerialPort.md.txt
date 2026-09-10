# TestSerialPort

TestSerialPort.exe is built as part of asyn and should be in your path after a config_env.bat

For full list of options run
```
TestSerialPort.exe --help
```
general syntax is
```
testSerialPort [options] COMPORT [outputString] [outputEos] [inputEos]
```
Note that is COMPORT doesn't start with the letters `COM` it is considered an IP address and a connection will be made there as per `drvAsynIPPortCOnfigure`

Also asyn only allows up to 2 characters for `inputEos`/`outputEos` (`streamDevice` itself can do more)
 
To write a string with \\r\\n terminator and print reply
```
testserialport COM5 "stuff_to_write" "\r\n"
```
To write string, see reply and also log all serial events (as per WIN32 SetCommMask())
```
testserialport COM5 "stuff_to_write" "\r\n" --eventmask=0x1ff
```
To see serial port status (need to have stopped IOC)
```
testserialport COM5 --noread --report=5
```
The command uses escaped characters as per `printf/epicsStrnRawFromEscaped` e.g. for Eurotherm the Stream device `\\x05` (hex) would be written as `\\005` (octal)
```
testserialport COM7 "\0040011PV" "\005" "\003" --eventmask=0x1ff
```

This program is built using VS2017 and so will not be on the instruments as standard. To use it on a deployment built with VS2010 you will to copy a static VS2017 build of `testserialport.exe` from jenkins.
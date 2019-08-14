TestSerialPort.exe is built as part of asyn and should be in your path after a config_env.bat

For full list of options run
```
TestSerialPort.exe --help
```
general syntax is
```
testSerialPort [options] COMPORT [outputString] [outputEos] [inputEos]
```
To write a string with \\r\\n terminator and print reply
```
testserialport com5 "stuff_to_write" "\r\n"
```
To write string, see reply and also log all serial events (as per WIN32 SetCommMask())
```
testserialport com5 "stuff_to_write" "\r\n" --eventmask=0x1ff
```
To see serial port status (need to have stopped IOC)
```
testserialport com5 --noread --report=5
```
The command uses escaped characters as per printf/epicsStrnRawFromEscaped e.g. for eurotherm
```
testserialport COM7 "\0040011PV" "\005" "\003" --eventmask=0x1ff
```

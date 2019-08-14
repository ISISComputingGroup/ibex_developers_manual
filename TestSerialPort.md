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
The command uses escaped characters as per printf/epicsStrnRawFromEscaped e.g. for eurotherm the Stream device \\x05 (hex) would be written as \\005 (octal)
```
testserialport COM7 "\0040011PV" "\005" "\003" --eventmask=0x1ff
```
The command line --option uses CLI11 so with visual studio 2010 you will only be able to pass the positional arguments mentioned above
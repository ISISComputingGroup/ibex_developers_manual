TestSerialPort.exe is built as part of asyn and should be in your path after a config_env.bat

Run
```
TestSerialPort.exe --help
```
for options. To write a string and print reply
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

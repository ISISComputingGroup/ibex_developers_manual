TestSerialPort.exe is built as part of asyn and should be in your path after a config_env.bat

Run
```
TestSerialPort.exe --help
```
for options. 

write string and see reply
```
testserialport com5 "stuff_to_write" "\r\n"
```
write string and see reply, also log all serial events
```
testserialport com5 "stuff_to_write" "\r\n" --eventmask=0x1ff
```
See serial port status
```
testserialport com5 --noread --report=5
```

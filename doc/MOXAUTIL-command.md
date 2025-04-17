> [Wiki](Home) > [The Backend System](The-Backend-System) > [Useful tools](Useful-tools) > Moxa Utils

The `moxautil` command will allow you to control a moxa box in a limited way. Type:
```
moxautil.exe --help
```
for full details. Examples are:
``` 
moxautil.exe --ip=130.246.49.42 --resetserver --password=themoxapassword
```
to reboot the server or 
```
moxautil.exe --ip=130.246.49.42 --alive
```
To check an IP is alive and really a moxa. 

## Interrogate Specific ports 

The command also supports interrogating individual ports:
```
moxautil.exe --ip=130.246.49.42 --port=1 --resetport --password=themoxapassword
```
and
```
moxautil.exe --ip=130.246.49.42 --port=1 --status --password=themoxapassword
```
Unfortunately these do not work unless the the COM port in "TCP server" mode. We normally run in "real com" and may also run in "RFC2217".
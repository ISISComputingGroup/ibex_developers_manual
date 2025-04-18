# Using IP rather than NPORT (RFC 2217)

nPORT will create serial ports on the computer and these are accessed using `drvAsynSerialPortConfigure()` in the `st.cmd`

An alternative is to directly talk IP to the moxa, which bypasses the nPORT windows software. This option can be configured on a port by port basis, though the moxa will restart when changes are made.

To enable this option you need to change the mode of the moxa port from "Real COM" (which uses windows nPort) to "RFC 2217". On the moxa web page look under "operational settings" for the port to change the mode.   

Port 1 of the MOXA is served at IP port 4001, so to connect with asyn you would use something like:
```
drvAsynIPPortConfigure("L0", "130.246.49.42:4001 COM", 0, 0, 0, 0)
```
The "COM" after the address:port indicates the RFC 2217 mode, this mode means that `asynSetOption()` will work as before and there is no need to set baud etc. via the moxa web page. 
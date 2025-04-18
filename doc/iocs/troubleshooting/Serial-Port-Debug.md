# Serial Port Debug

This is a temporary page for fault finding with changes from [ticket 4435](https://github.com/ISISComputingGroup/IBEX/issues/4435)

symptoms: com port stuck, no reads work, dbior hangs.

Until this PR is deployed you will first need to update `asyn.dll` for the IOC concerned
* stop IOC concerned
* copy `asyn.dll` from Ticket4435 build (`asyn_ovio` jenkins job) to same directory as `.exe` for IOC (so it will load in preference to existing `asyn.dll`)
* start IOC
* when done, remove new `asyn.dll` from the IOC `bin/windows-x64` directory

After restarting with new asyn you should be able to type
```
dbior drvAsyn 5
```
without it hanging. The new ASIO may even fix the issue, but should at least give you more output. If the IOC is not fixed, can you try adding:
```
epicsEnvSet("WAITFORBYTES",1)
```
to the st.cmd, this will enable another sort of read mode to test.

It would also be worth adding
```
asynSetOption("L0", -1, "eventmask", "0x11b")	
```
to startup, this will print all com events except writes – to see writes too use:
```
asynSetOption("L0", -1, "eventmask", "0x11f")
```
You can also stop IOC and try using the [`testSerialPort` command](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TestSerialPort)

It is also possible to use the new "escape" and "purge" options with asynSetOption at runtime to manipulate the various things about the send and receive buffers and line status.  
> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Emulating devices

## Introduction

So you've created an IOC to talk to a device, and you want to test it: just borrow an actual piece of hardware and test with that. What if that's not possible? 

*The only way to know an IOC will work with an actual device is to use an actual device.*

 However, we can try and get as close as possible at the development stage. We also might want to make minor changes to an IOC we know that works without all the effort of tracking down an actual piece of hardware. The above principle still applies, but we can still take steps to improve our odds.

This page describes the process by which we can write an emulator that will run on our local machine and imitate an actual device. We'll be talking to a local IP port via a simple Telnet server.

## Get the framework

The emulation framework can be found in [this repo](https://github.com/ISISComputingGroup/EPICS-DeviceEmulator) and should be synced to your local EPICS directory at `C:\Instrument\Apps\EPICS\support\deviceEmulator`.

## Set up a new emulator

1. Create a copy of the directory `C:\Instrument\Apps\EPICS\support\deviceEmulator\example_emulator` for your new device, e.g. `myNewDevice_emulator`.
1. Modify the function `process` to give the correct return for the incoming data.
    1. The incoming data will be the command defined in the `out` field of the protocol file. It's the command you would expect to send to the actual device.
    1. Change the function to return the data you want subject to specific input.
    1. TODO: Note that it's possible to modify the emulator on the fly as it's running in case you want to push it into a specific state. I haven't tried that yet. 
1. Run the emulator python file (preferably with genie_python).
    1. You will need to know the port the emulator is running on. If you just run the emulator as-is, it will pick a free port and report the port number from the console. Alternatively you can run `...\myNewDevice_emulator.py [PORT]` where `[PORT]` is the port number you want to run on.

Congratulations! Your emulator is now running. Give it a try by navigating to `http://localhost:[PORT]` in your web browser, substituting `[PORT]` for the port number. You should see the http GET request content echoed to the terminal

## Connecting your IOC

So, we've got our emulator running, now we need to get our IOC talking to it. Go to `st.cmd` for your IOC and find where the serial port communication is configured, for instance:

```
drvAsynSerialPortConfigure("$(DEVICE)", "$(PORT)", 0, 0, 0, 0)
asynSetOption("$(DEVICE)", -1, "baud", "$(BAUD=9600)")
asynSetOption("$(DEVICE)", -1, "bits", "$(BITS=8)")
asynSetOption("$(DEVICE)", -1, "parity", "$(PARITY=none)")
asynSetOption("$(DEVICE)", -1, "stop", "$(STOP=1)")
asynOctetSetInputEos("$(DEVICE)", -1, "$(OEOS=\n)")
```

comment out that block (`#`) and replace it with:

```
drvAsynIPPortConfigure("$(DEVICE)", "localhost:[PORT]")
```

where again `[PORT]` is replaced with the port number we're running on. We could factor this out into a non-hard-coded macro in `globals.txt` but a lot of the time it's easier just to do it here.

## GO!

Start the IOC as normal by running `runIOC.bat st.cmd`. If everything's hooked up correctly, you should see the incoming and response data being echoed to the emulated device console. With any luck, that data should then be updated to your PVs.

## Troubleshooting

We haven't done much with emulators yet, so not much has gone wrong, so please add to this section as you can.

* Telnet server is running, but is not receiving any data from the IOC: Is your st.cmd correct? Try removing the 4 `< $(IOCSTARTUP)...` lines, and the `drvAsyn{IP,Serial}PortConfigure` lines and run `runIOC.bat st.cmd`. Are you getting any error or warning messages? Sort those out first.
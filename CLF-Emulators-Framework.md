> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Emulating devices](Emulating-Devices) > CLF framework

This page describes the process by which we can write an emulator that will run on our local machine and imitate an actual device, using the CLF framework. We'll be talking to a local IP port via a simple Telnet server.

Note that new emulators should be written using the [Lewis framework](Emulating-Devices) instead.

## Get the framework

The emulation framework can be found in [this repo](https://github.com/ISISComputingGroup/EPICS-DeviceEmulator) and should be synced to your local EPICS directory at `C:\Instrument\Apps\EPICS\support\DeviceEmulator\master`.

## Set up a new emulator

1. Create a copy of the directory `C:\Instrument\Apps\EPICS\support\DeviceEmulator\master\clf_framework_emulators\example_emulator` for your new device, e.g. `myNewDevice_emulator`.
1. Modify the function `process` to give the correct return for the incoming data.
    1. The incoming data will be the command defined in the `out` field of the protocol file. It's the command you would expect to send to the actual device.
    1. Change the function to return the data you want subject to specific input.
	
## Run the emulator

Run the emulator python file (preferably with genie_python).

You will need to know the port the emulator is running on. If you just run the emulator as-is, it will pick a free port and report the port number from the console, and also print it to a local `.port` file. Alternatively you can run `...\myNewDevice_emulator.py [PORT]` where `[PORT]` is the port number you want to run on.

Congratulations! Your emulator is now running. Give it a try by navigating to `http://localhost:[PORT]` in your web browser, substituting `[PORT]` for the port number. You should see the http GET request content echoed to the terminal

### The backdoor

Note that it's possible to modify the emulator's state on the fly as it's running in case you want to push it into a specific state (as a backdoor). You can do this by connecting a telnet client like PuTTY to the running emulator, and any change in its state will be picked up by the IOC. The port for the backdoor is the same as the main port.

## Connecting your IOC

This section is the same as [here](Emulating-Devices).

## GO!

Start the IOC as normal by running `runIOC.bat st.cmd`. If everything's hooked up correctly, you should see the incoming and response data being echoed to the emulated device console. With any luck, that data should then be updated to your PVs.
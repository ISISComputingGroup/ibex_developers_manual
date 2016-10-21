> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Emulating devices

## Introduction

So you've created an IOC to talk to a device, and you want to test it: just borrow an actual piece of hardware and test with that. What if that's not possible? 

*The only way to know an IOC will work with an actual device is to use an actual device.*

However, we can try and get as close as possible at the development stage. We also might want to make minor changes to an IOC we know that works without all the effort of tracking down an actual piece of hardware. The above principle still applies, but we can still take steps to improve our odds.

Our emulators are written within the Plankton framework developed at ESS. The purpose of this page is not to replicate the full Plankton documentation, which can be found [here](https://github.com/DMSC-Instrument-Data/plankton/blob/master/README.md), but to give quick pointers to common actions and describe how it all fits within IBEX.

Note: we initially wrote a few emulators using the basic framework introduced at CLF. Documentation for that framework can be found [here](CLF-Emulators-Framework) until we decide to retire it.

## Get the framework

The Plankton source code we're currently using can be found in [this submodule](https://github.com/ISISComputingGroup/EPICS-plankton) and should be synced to your local EPICS directory at `C:\Instrument\Apps\EPICS\support\plankton\master`. Note that is has a vendor branch for the original ESS source code.

Our emulators can be found in [this submodule](https://github.com/ISISComputingGroup/EPICS-DeviceEmulator) and should be synced to your local EPICS directory at `C:\Instrument\Apps\EPICS\support\DeviceEmulator\master`.

### PyCharm setup tips

To make our life easier, within PyCharm we have named the Plankton and DeviceEmulator python projects as `plankton` and `isis_emulators`, respectively, and made `isis_emulators` depend on `plankton`. This means you should be able to have them both open in the same PyCharm window (open a new project, and when prompted, select `Open in current window` and tick the `Add to currently opened projects` check box) and PyCharm should resolve references to the Plankton code.

## Set up a new emulator

1. Create a subdirectory for your new emulator under `support/DeviceEmulator/master/plankton_emulators/`.
1. Documentation for how to write a plankton emulator can be found [here](https://github.com/DMSC-Instrument-Data/plankton/blob/master/docs/Contributing.md), and you can refer to the examples in the plankton submodule, under `devices/` (e.g. `linkam_t95` for a full realistic emulator) and under `examples/` (e.g. `simple_device` for a basic emulator, and `example_motor` for a simple state machine).
1. NOTE: the simple examples `simple_device` and `example_motor` have all the code in a single `__init__.py` file, but we should stick to a consistent tidy structure like that of the `linkam_t95` emulator, i.e. with separate files for the device itself, its states (if it's a state machine), and its interfaces.
1. Don't forget to add `__init__.py` files in all of your folders!
1. At the time of writing, the Plankton `StreamAdapter.handle_error()` method does nothing. Please make sure your interface class deriving from `StreamAdapter` prints the content of the error, which makes it easier to understand what's going on (see for example the `iris_cryo_valve` emulator).

## Run the emulator

The emulator runs by launching the `plankton.py` file under `/support/plankton/master/`, as described [here](https://github.com/DMSC-Instrument-Data/plankton/blob/master/docs/AdapterSpecifics.md). Note that in our case, where the emulators live outside the Plankton source code, we need to specify where the emulators code is, with the `-a` and `-k` arguments:

```
python plankton.py -p stream -a C:\Instrument\Apps\EPICS\support\DeviceEmulator\master -k plankton_emulators iris_cryo_valve -- --bind-address localhost --port 57677
```

where we have picked port 57677 (see Plankton's doc for defaults).

Congratulations! Your emulator is now running. You can test it by connecting to it via a telnet client such as PuTTY (please see the troubleshooting note below).

### The backdoor

Note that it's possible to modify the device's state on the fly as it's running in case you want to push it into a specific state (as a backdoor). The backdoor can also be used to alter simulation paramters, e.g. to simulate a loss of connection or speed up the simulation time. Full documentation can be found [here for device access](https://github.com/DMSC-Instrument-Data/plankton/blob/master/docs/RemoteAccessDevices.md) and [here for simulation access](https://github.com/DMSC-Instrument-Data/plankton/blob/master/docs/RemoteAccessSimulation.md).

The host and port for the backdoor are specified in the `-r` argument to `plankton.py`:

```
python plankton.py -p stream -r 127.0.0.1:10000 -a C:\Instrument\Apps\EPICS\support\DeviceEmulator\master -k plankton_emulators iris_cryo_valve -- --bind-address localhost --port 57677
```

NOTE: at the time of writing, you can't type `localhost` for the `-r` argument, but it should be fixed soon.

The backdoor can be operated either via the command line through `control.py` or can be scripted, as described in the Plankton documentation.

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

Replace it with a macro defined by IBEX backend which comments it out when set

```
$(IFNOTDEVSIM) drvAsynSerialPortConfigure("$(DEVICE)", "$(PORT)", 0, 0, 0, 0)
$(IFNOTDEVSIM) asynSetOption("$(DEVICE)", -1, "baud", "$(BAUD=9600)")
$(IFNOTDEVSIM) asynSetOption("$(DEVICE)", -1, "bits", "$(BITS=8)")
$(IFNOTDEVSIM) asynSetOption("$(DEVICE)", -1, "parity", "$(PARITY=none)")
$(IFNOTDEVSIM) asynSetOption("$(DEVICE)", -1, "stop", "$(STOP=1)")
$(IFNOTDEVSIM) asynOctetSetInputEos("$(DEVICE)", -1, "$(OEOS=\n)")
```

and then add

```
$(IFDEVSIM) drvAsynIPPortConfigure("$(DEVICE)", "localhost:[PORT]")
```

where again `[PORT]` is replaced with the port number we're running on. We could factor this out into a non-hard-coded macro in `globals.txt` but a lot of the time it's easier just to do it here.

## GO!

Start the IOC as normal by running `runIOC.bat st.cmd`. If everything's hooked up correctly, you should see a `Client connected` message in the emulated device console. At the time of writing, Plankton emulators don't echo requests from the client, but this should be implemented soon. With any luck, the data from the emulator should then be updated to your PVs.

## Troubleshooting

We haven't done much with emulators yet, so not much has gone wrong, so please add to this section as you can.

* Telnet server is running, but is not receiving any data from the IOC: Is your st.cmd correct? Try removing the 4 `< $(IOCSTARTUP)...` lines, and the `drvAsyn{IP,Serial}PortConfigure` lines and run `runIOC.bat st.cmd`. Are you getting any error or warning messages? Sort those out first.
* When connecting to a Plankton emulator via a Telnet client such as PuTTY, beware that Telnet uses `\r\n` as a terminator. If your emulator interface has a different one (like for the `linkam_t95`), the protocol won't work. You could temporarily use the Telnet terminator instead. Note also that PuTTY sends some extra characters at the start of the communication, so the very first command you send probably won't work.
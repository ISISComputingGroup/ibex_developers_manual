> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Emulating devices

## Introduction

So you've created an IOC to talk to a device, and you want to test it: just borrow an actual piece of hardware and test with that. What if that's not possible? 

*The only way to know an IOC will work with an actual device is to use an actual device.*

However, we can try and get as close as possible at the development stage. We also might want to make minor changes to an IOC we know that works without all the effort of tracking down an actual piece of hardware. The above principle still applies, but we can still take steps to improve our odds.

Our emulators are written within the Lewis framework developed at ESS. The purpose of this page is not to replicate the full Lewis documentation, which can be found [here](http://lewis.readthedocs.io/en/latest/), but to give quick pointers to common actions and describe how it all fits within IBEX.

Note: we initially wrote a few emulators using the basic framework introduced at CLF. Documentation for that framework can be found [here](CLF-Emulators-Framework) until we decide to retire it.

## Get the framework

Lewis is included as an installed module in genie_python.

## Set up a new emulator

1. Create a subdirectory for your new emulator under `support/DeviceEmulator/master/lewis_emulators/`.
1. Documentation for how to write a Lewis emulator can be found [here](http://lewis.readthedocs.io/en/latest/developer_guide/contributing.html), and you can refer to the examples in the Lewis library (i.e. `C:\Instrument\Apps\Python\Lib\site-packages\lewis\devices` and `...\examples`).
1. NOTE: the simple examples `simple_device` and `example_motor` have all the code in a single `__init__.py` file, but we should stick to a consistent tidy structure like that of the `linkam_t95` emulator, i.e. with separate files for the device itself, its states (if it's a state machine), and its interfaces.
1. Don't forget to add `__init__.py` files in all of your folders!
1. At the time of writing, the Lewis `StreamAdapter.handle_error()` method does nothing. Please make sure your interface class deriving from `StreamAdapter` prints the content of the error, which makes it easier to understand what's going on (see for example the `iris_cryo_valve` emulator).

## Run the emulator

To run from the command line, use

```
lewis -p stream -a C:\Instrument\Apps\EPICS\support\DeviceEmulator\master -k lewis_emulators iris_cryo_valve -- --bind-address localhost --port 57677
```

where we have picked port 57677 (see Lewis's doc for defaults). Note that the lewis executable is located in `C:\Instrument\Apps\Python\Scripts`, at time of writing we don't add the directory to our standard EPICS environment PATH variables, so you may need to provide a fully qualified file path.

Congratulations! Your emulator is now running. You can test it by connecting to it via a telnet client such as PuTTY (please see the troubleshooting note below) or with a simple Python script like so:

```python
import socket

OUT_TERMINATOR = "\r"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 57677))

while True:
    cmd = raw_input()
    s.sendall(cmd + OUT_TERMINATOR)
    data = s.recv(4096)  # Needs to be longer than the returned message
    print data

s.close()
```

### The backdoor

It's possible to modify the device's state on the fly as it's running in case you want to push it into a specific state (as a backdoor). The backdoor can also be used to alter simulation paramters, e.g. to simulate a loss of connection or speed up the simulation time. Full documentation can be found [here for device access](http://lewis.readthedocs.io/en/latest/user_guide/remote_access_devices.html) and [here for simulation access](http://lewis.readthedocs.io/en/latest/user_guide/remote_access_simulation.html).

The host and port for the backdoor are specified in the `-r` argument at startup:

```
lewis -p stream -r 127.0.0.1:10000 -a C:\Instrument\Apps\EPICS\support\DeviceEmulator\master -k lewis_emulators iris_cryo_valve -- --bind-address localhost --port 57677
```

NOTE: at the time of writing, you can't type `localhost` for the `-r` argument.

The backdoor can be operated either via the command line through `lewis-control` or can be scripted, as described in the Lewis documentation.

**NOTE**: The simulation command `disconnect_device` seems to simulate the device not responding to the port, which is different from a lost connection: the IOC reports `No reply from device within xxx ms`. When the emulator is actually stopped, with the simulation `stop` command, the IOC detects that there is really no connection and reports `Can't connect to localhost:<port>`.

## Connecting your IOC

So, we've got our emulator running, now we need to get our IOC talking to it. For this to work it needs to use the standard st.cmd setup so it works with the IOC testing framework. Then in your `globals.txt` do the following:

 - Add a line to set the IOC into dev sim `<IOC name>__DEVSIM=1` (this can go in the configuration)
 - Set the port it should be communicating on (must be free) `<IOC name>__EMULATOR_PORT=57677`

IOC name is the name of the ioc e.g. `EUROTHRM_01`

## GO!

Start the IOC as normal by running `runIOC.bat st.cmd`. If everything's hooked up correctly, you should see a `Client connected` message in the emulated device console. At the time of writing, Lewis emulators don't echo requests from the client, but this should be implemented soon. With any luck, the data from the emulator should then be updated to your PVs.

## Connecting an Emulator to LabView

If we have a pre-existing VI it might be useful to connect it to an emulator to test the emulator functionality is as expected. If the VI talks TCP then just ensure that the port it is talking to is the one that Lewis is served on. If the VI is attempting to talk to a serial connection this is a bit harder and you must do the following:
1. Find a MOXA box
2. Create a physical loopback on the MOXA by connecting one port into another using one male serial cable connected to one female serial cable (a plain network cable won't do)
3. Use NPort to connect to these two ports, noting which COM ports correspond to the loopback
4. Run the com2tcp.py script found in https://github.com/ISISComputingGroup/EPICS-DeviceEmulator/ to create a connection between one COM port and Lewis e.g. `python com2tcp.py 57677 COM12`
5. Connect the VI to the COM port that you haven't run com2tcp.py on

If the above is not working check that the baud rates/stop bits etc. set in the VI, NPort and com2tcp are all the same.

## Troubleshooting

We haven't done much with emulators yet, so not much has gone wrong, so please add to this section as you can.

* Telnet server is running, but is not receiving any data from the IOC: Is your st.cmd correct? Try removing the 4 `< $(IOCSTARTUP)...` lines, and the `drvAsyn{IP,Serial}PortConfigure` lines and run `runIOC.bat st.cmd`. Are you getting any error or warning messages? Sort those out first.
* When connecting to a Lewis emulator via a Telnet client such as PuTTY, beware that Telnet uses `\r\n` as a terminator. If your emulator interface has a different one (like for the `linkam_t95`), the protocol won't work. You could temporarily use the Telnet terminator instead. Note also that PuTTY sends some extra characters at the start of the communication, so the very first command you send probably won't work.
* `An error occurred:
The setup 'default' you tried to load does not specify a valid device type, but
the device module 'neocera_ltc21' provides multiple device types so that no mean
ingful default can be deduced.`. Possible solutions:
    - Add device to `__init__` file of package so it can be imported.
    - Ensure that the initial state is one of the states returned by get_state_handlers.
* When I try to launch `lewis.exe` I get the error `Fatal error in launcher: Unable to create process using '"'`. When you build Python on Windows, the Python path is baked into the `lewis.exe` exectuable. If you subsequently say move `Python-build` to `Python` then the path will be incorrect and the executable doesn't know where to launch from. You can either open the executable in a text editor and change the path by hand or instead explicitly point it at the Python executable by running `..\Python.exe lewis.exe ...`
> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Emulating devices

## Introduction

You've created an IOC to talk to a device, and you want to test it: just borrow an actual piece of hardware and test with that. What if that's not possible? 

*The only way to know an IOC will work with an actual device is to use an actual device.*

However, we can try and get as close as possible at the development stage. We also might want to make minor changes to an IOC we know that works without all the effort of tracking down an actual piece of hardware. The above principle still applies, but we can still take steps to improve our odds.

Our emulators are written within the Lewis framework developed at ESS. The purpose of this page is not to replicate the full Lewis documentation, which can be found [here](https://isiscomputinggroup.github.io/lewis/index.html), but to give quick pointers to common actions and describe how it all fits within IBEX.

Due to some staff turnover Lewis is now maintained by ISIS and ESS collaboratively. Dom has access to pushing release versions of Lewis to pypi. 

## Get the framework

Lewis is included as an installed module in genie_python (for Python 3).

## Set up a new emulator

1. Create a subdirectory for your new emulator under `support/my_device/master/system_tests/lewis_emulators/`, for an example see the CCD100.
1. Documentation for how to write a Lewis emulator can be found [here](https://isiscomputinggroup.github.io/lewis/developer_guide/writing_devices.html), and you can refer to the examples in the Lewis library (i.e. `C:\Instrument\Apps\Python3\Lib\site-packages\lewis\devices` and `...\examples`).
1. NOTE: the simple examples `simple_device` and `example_motor` have all the code in a single `__init__.py` file, but we should stick to a consistent tidy structure like that of the `linkam_t95` emulator, i.e. with separate files for the device itself, its states (if it's a state machine), and its interfaces.
1. Don't forget to add `__init__.py` files in all of your folders!
1. At the time of writing, the Lewis `StreamAdapter.handle_error()` method does nothing. Please make sure your interface class deriving from `StreamAdapter` prints the content of the error, which makes it easier to understand what's going on (see for example the `iris_cryo_valve` emulator).

## Run the emulator

To run from the command line, use

```
%PYTHON3% -u -m lewis -p "stream: {bind_address: localhost, port: 57677}" -r 127.0.0.1:10000 -a C:\Instrument\Apps\EPICS\support\cryValve\master\system_tests -k lewis_emulators iris_cryo_valve
```

where we have picked port 57677 (see Lewis's doc for defaults). Note that the lewis executable is located in `%PYTHON3DIR%\Scripts`.

**Note:** emulators used to be stored in one repository in `support\DeviceEmulator\` since https://github.com/ISISComputingGroup/IBEX/issues/6555 emulators should start being moved to live in the support directory for the IOCs that they are testing.

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

It's possible to modify the device's state on the fly as it's running in case you want to push it into a specific state (as a backdoor). The backdoor can also be used to alter simulation parameters, e.g. to simulate a loss of connection or speed up the simulation time. Full documentation can be found [here for device access](https://isiscomputinggroup.github.io/lewis/user_guide/remote_access_devices.html) and [here for simulation access](https://isiscomputinggroup.github.io/lewis/user_guide/remote_access_simulation.html).

The host and port for the backdoor are specified in the `-r` argument at startup:

```
%PYTHON3% -u -m lewis -p "stream: {bind_address: localhost, port: 57677}" -r 127.0.0.1:10000 -a C:\Instrument\Apps\EPICS\support\cryValve\master\system_tests -k lewis_emulators iris_cryo_valve
```

NOTE: at the time of writing, you can't type `localhost` for the `-r` argument.

Once the emulator is running, the backdoor can be operated either via the command line through `lewis-control`:
```
%PYTHON3DIR%\scripts\lewis-control.exe -r localhost:<PORT> device <EMULATOR FUNCTION/COMMAND/VARIABLE> "<ARG1>" "<ARG2>" "<ARG...>"
```
or can be scripted, as described in the Lewis documentation.

Replace each of the sections in `<>`s with the relevant values, not including the angle brackets. For example, to call the `backdoor_set_channel_property(self, channel_id, property_name, value)` method on an emulator running on port `59254`, you would write:

```
%PYTHON3DIR%\scripts\lewis-control.exe -r localhost:59254 device backdoor_set_channel_property "MB1.H0"  "voltage"  "10"
```

If you want to control an emulator running from a test, look at the lewis log for the device in `Instrument\Var\logs\IOCTestFramework` and use the port that the `ControlServer` is listening on. 

**NOTE**: If an argument is a string that contains words separated by white space characters, then you need to use "'argument'" instead of "argument", since otherwise the command line will not interpret it correctly and crash with a SyntaxError.

**NOTE**: The simulation command `disconnect_device` seems to simulate the device not responding to the port, which is different from a lost connection: the IOC reports `No reply from device within xxx ms`. When the emulator is actually stopped, with the simulation `stop` command, the IOC detects that there is really no connection and reports `Can't connect to localhost:<port>`.

**NOTE**: The backdoor does not give access to private variables, so anything prefixed with `_` can not be changed in this way, or through the backdoor in python scripts.

## Connecting your IOC

We've got our emulator running, now we need to get our IOC talking to it. For this to work it needs to use the standard st.cmd setup so it works with the IOC testing framework. Then in your `globals.txt` do the following:

 - Add a line to set the IOC into dev sim `<IOC name>__DEVSIM=1` (this can go in the configuration)
 - Set the port it should be communicating on (must be free) `<IOC name>__EMULATOR_PORT=57677`

IOC name is the name of the ioc e.g. `EUROTHRM_01`

## GO!

Start the IOC as normal by running `runIOC.bat st.cmd`. If everything's hooked up correctly, you should see a `Client connected` message in the emulated device console. At the time of writing, Lewis emulators don't echo requests from the client, but this should be implemented soon. With any luck, the data from the emulator should then be updated to your PVs.

## Connecting an Emulator to LabView

If we have a pre-existing VI it might be useful to connect it to an emulator to test the emulator functionality is as expected. If the VI talks TCP then just ensure that the port it is talking to is the one that Lewis is served on. If the VI is attempting to talk to a serial connection this is a bit harder and you must do the following:
1. Find a MOXA box
2. Create a physical loopback on the MOXA by connecting one port into another using one male serial cable connected to one female serial cable (a plain network cable won't do)
3. Use NPort (which can be found under `\kits$\CompGroup\Utilities`) to connect to these two ports, noting which COM ports correspond to the loopback
4. Run the emulator (instructions above in "Run the emulator" section)
5. Run the com2tcp.py script found in https://github.com/ISISComputingGroup/EPICS-DeviceEmulator/ to create a connection between one COM port and Lewis e.g. `python com2tcp.py 57677 COM12`
6. Connect the VI to the COM port that you haven't run com2tcp.py on

If the above is not working check that the baud rates/stop bits etc. set in the VI, NPort and com2tcp are all the same. otherwise, look in NI MAX and confirm that the COM ports are showing up under devices and interfaces on the left, if they are not you may need to update NI MAX. Also, note that the port you want to set in the driver VI is the one highlighted below (which can occasionally differ from the actual COM port)
![NI MAX](emulating_devices/ni_max.JPG)

If you want to test against the LabVIEW VI and you aren't in a position to create a loopback in the MOXA, there is a VI available which you can use within the communication VI instead of the serial connections.
1. Create some room inside the main case
2. On the block diagram, move the reply to the far right of the main case, the read reply button and the command to the far left of the main case
3. Drop a `disable diagram` structure around the serial communications section
4. In the enabled state, drop in an instance of `IBEX Integration - Connect to TCP.vi`, which can be found in the `IBEX Integration.llb` in the `Labview Modules\Common\Utilities` directory (if the VI isn't there, then you need to get an updated version of the repo)
5. Connect the errors, reply, command and so on in the obvious fashion, connect the COM port to the Port In, and create a constant for the mode
6. Change the COM port in the setup dialog to the port of the emulator (this has to be running on localhost at the moment)
7. Run the emulator and VI and they should be talking to each other

## Troubleshooting

We haven't done much with emulators yet, so not much has gone wrong, so please add to this section as you can.

* Telnet server is running, but is not receiving any data from the IOC: Is your st.cmd correct? Try removing the 4 `< $(IOCSTARTUP)...` lines, and the `drvAsyn{IP,Serial}PortConfigure` lines and run `runIOC.bat st.cmd`. Are you getting any error or warning messages? Sort those out first.
* When connecting to a Lewis emulator via a Telnet client such as PuTTY, beware that Telnet uses `\r\n` as a terminator. If your emulator interface has a different one (like for the `linkam_t95`), the protocol won't work. You could temporarily use the Telnet terminator instead. Note also that PuTTY sends some extra characters at the start of the communication, so the very first command you send probably won't work.
* Note that lewis can't deal with not having a termination character. If your device doesn't use a termination character then you will have to temporarily use one while talking to the emulator.
* `An error occurred:
The setup 'default' you tried to load does not specify a valid device type, but
the device module 'neocera_ltc21' provides multiple device types so that no meaningful default can be deduced.`. Possible solutions:
    - Add device to `__init__` file of package so it can be imported.
    - Ensure that the initial state is one of the states returned by get_state_handlers.
* When I try to launch `lewis.exe` I get the error `Fatal error in launcher: Unable to create process using '"'`. When you build Python on Windows, the Python path is baked into the `lewis.exe` executable. If you subsequently say move `Python-build` to `Python` then the path will be incorrect and the executable doesn't know where to launch from. You can either run lewis as a module e.g. `%PYTHON3% -u -m lewis` or run it by importing it into a python script.
* When I try to print something from the device emulator, nothing happens. Why?
Print statements in the device emulator can not print anything to a console when they are ran as part of the IocTestFramework.
* I want to log something how do I do that?
    1. include `@has_log` at the top of the class (don't forget to `from lewis.core.logging import has_log`)
    1. use self.log.info(message), self.log.warning(message), self.log.error(message), etc
* When I try to run a device I get the error `Failed to find protocol stream...`. This is due to one of the imports in the stream_interface not being valid. Check that they are all correct.
* When I try to access a variable that I know exists in my emulator, I get an error saying that variable does not exist?
    1. The lewis backdoor does not give access to private variables, so anything prefixed with `_` cannot be changed in this way.
* If you are using `CmdBuilder` be aware that you should use `.eos()` before `.build()`, _especially_ if you have commands that 'overlap'. And example of this would be on the Keithley 2700, which has a buffer auto clear setting command, `TRAC:CLE:AUTO`, and a buffer clear command, `TRAC:CLE`. `.eos()` essentially tells the built regex to match the exact command string, rather than some of it.
* When running the IOC tests with `make ioctests` you get no output until all the tests are run. This is set in general for all `Makefiles` to avoid interleaved printing when doing a parallel build. To fix this you need to remove the `-Otarget` from the `MAKEFLAGS` environment variable. e.g. run `set "MAKEFLAGS=-w -j 6"` before running the test. This environment variable will be reset back every time you start a new EPICS terminal.
* Use of `@property` python decorator is not supported within `stream_interface.py` and will cause the emulator to fail. Please try to avoid using such decorators in your python scripts for use with emulators as they will cause issues when trying to construct Func-object instances during the build process.

#### When using an emulator with a VI

* If you are having problems getting data into or out of your emulator when using a VI, it could be a comms issue.
  * Check the baud rate and other serial parameters if using serial
  * Double check the port that your VI is connected to
* The VI may be polling/looping too fast for your emulator. Some VIs are written to go flat out as fast as possible. This may be faster than your python emulator can handle. If you are getting no data from/into the VI, try slowing it down and increasing its loop delays. e.g. the VI controlling the Keithley 2700 was looping every 2ms, and when data was inserted into the emulated device buffer, the VI showed no change. This is because the loop was too fast for the data to be processed properly by the emulator and then VI. The delay was increased to 20ms (still extremely fast for the intended purpose), and the VI and emulator worked (make sure that the increased delay is not unreasonable and the device can still be expected to work properly).

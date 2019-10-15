I've added the EPICS Lua support module to our build system. Lua is a scripting language
designed to be embedded, it has a small footprint and is reasonably powerful. It would
provide an alternative to jumping through hoops in st.cmd syntax but also provides a 
few other options. All `iocsh` commands are imported into lua and so you can do things
like:

```
for index=1,10,1
do
    print(string.format("Loading instance: %d", index))
    iocsh.dbLoadRecords("test.db", string.format("P=xxx:,Q=%d", index))
end
```

You execute files from st.cmd using:

```
epicsEnvSet("LUA_PATH", "${UTILITIES}/lua")
epicsEnvSet("LUA_SCRIPT_PATH","${TOP}/iocBoot/${IOC}")
luash("file.lua")
```

or just typing `luash` puts you into an interactive lua shell.

The lua script record is like a calcout record but can execute lua script. It might be
an alternative to e.g. aSub records for parsing stream device strings when writing C is 
a bit overkill.

As well as being able to read/write PVs there is also some asyn integration into lua, 
so you can read/write/set asyn parameters 
from lua command line or script record, or even talk to a device by creating an asyn IP port
and sending strings. See the documentation directory in lua support module  and the 
example scripts directory in iocBoot

To use 
  
```
add    LUA=$(SUPPORT)/lua/master     to configure/RELEASE
add    luaSupport.dbd                to the IOC Makefile DBD list
add    lua   and   asyn              to the IOC Makefile   _LIBS    list
```

There are examples of a lua script used in the DETADC, Attocube and OERCONE iocs.

There is a powerpoint about lua here: https://indico.cern.ch/event/766611/contributions/3438291/attachments/1856812/3050126/Lang-Lua_Integrating_Scripting_Language.pdf

See also the documentation on our [epics-lua module](https://github.com/ISISComputingGroup/EPICS-lua) or the actual [epics module](https://github.com/epics-modules/lua) for more information on using lua in EPICS.

## Using our Lua utility functions

Currently we have four functions available as utilities for booting iocs using lua: getMacroValue, setAsynOptions, setHardwareFlowControl, setSoftwareFlowControl.

To be able to use these you need to add this to the top of your lua file:

```
package.path = package.path .. ';' .. os.getenv("UTILITIES") .. '/lua/luaUtils.lua;'
local utils = require("luaUtils")
local getMacroValue = utils.getMacroValue
local setAsynOptions = utils.setAsynOptions
local setHardwareFlowControl = utils.setHardwareFlowControl
local setSoftwareFlowControl = utils.setSoftwareFlowControl
```
### getMacroValue(options)

Getting a macro from the environment. If the macro cannot be retrieved from the environment the default options value is returned. If there is no default given and the macro cannot be retrieved an error is raised.

- macro: String, the macro to look up in the 
- default: String, the value to return if the macro if the macro is not set in the environment

Example call: `getMacroValue{macro="RECSIM", default="0"}`
CMD equivalent: `$(RECSIM=0)`

### setAsynOptions(device, port, baud, bits, parity, stop)

For a real device configure the asyn serial port and set the baud, bits, parity and stop options for it.

- device: String, the name of the asyn port
- port: String, the name of the physical port the device is connected to
- baud: Integer, The baud rate of the device
- bits: Integer, the number of data bits
- parity: String, the device parity
- stop: Integer, the number of stop bits.

Example call: 
```
if (not isRecsim and not isDevsim) then
    local port = getMacroValue{macro="PORT", default="NO_PORT_MACRO"}
    local baud = getMacroValue{macro="BAUD", default="9600"}
    local bits = getMacroValue{macro="BITS", default="8"}
    local parity = getMacroValue{macro="PARITY", default="none"}
    local stop = getMacroValue{macro="STOP", default="1"}
    setAsynOptions(device, port, baud, bits, parity, stop)
...
```

CMD eqivalent: 
```
$(IFNOTDEVSIM) $(IFNOTRECSIM) drvAsynSerialPortConfigure("$(DEVICE)", "$(PORT=NO_PORT_MACRO)", 0, 0, 0, 0)
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "baud", "$(BAUD=9600)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "bits", "$(BITS=8)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "parity", "$(PARITY=none)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "stop", "$(STOP=1)")
```

### setHardwareFlowControl(device, flowControlOn)

Set the hardware flow control for when it is off or on. 

- device: String, the name of the asyn port.
- flowControlOn: Boolean, true if hardware flow control is on.

### setSoftwareFlowControl(device, flowControlOn)

Sets the software flow control for when it is off or on.

- device: String, the name of the asyn port
- flowControlOn: Boolean, true if software flow control is on.

## Adding to our Lua utility functions

Things to do:
- Add your function to the globals set in std.utils in the .luacheckrc file both locally and on this page for others to use (the plan is to have a .luacheckrc on github, but first it needs to be worked out how to edit the luacheck.path correctly to point at it)
- Add documentation in this page (the plan is to have documentation closer to the code, but that also needs to be worked out first)
- Add it to the imports in "Using our Lua utility functions" section above

## Style Guide

We are using the style guide from LuaRocks as documented in https://github.com/luarocks/lua-style-guide#conditional-expressions

## Installing LuaCheck

Either install via the hererocks python script or luacheck by itself. The hererocks way is longer but will integrate with your environment and favourite text editor nicely as it sets up parts such as luacheck.path and luarocks 

Via the hererocks python script:
- Download hererocks:
    - Open powershell and navigate to somewhere you would like hererocks to download to
    - Run `wget https://raw.githubusercontent.com/mpeterv/hererocks/latest/hererocks.py -OutFile hererocks.py`
- Install and activate lua and luarocks:
    - In an EPICS terminal navigate to where you downloaded hererocks.py and run `python hererocks.py lua53 -l5.3 -rlatest` which installs lua 5.3 into `$current directory$\lua53`
    - Add `$current directory$\lua53\bin` to your PATH where current directory is the directory you installed lua 5.3 in
    - Close and reopen your EPICS terminal to allow your PATH to update
- Install luacheck:
    - In your new EPICS terminal run `luarocks install luacheck`
- Luacheck is now installed

OR install luacheck by itself:
- Go to the [luacheck GitHub page](https://github.com/mpeterv/luacheck/tree/76bb56736702e8651537b2a9c10ae55ab7dc1d5d) and under Windows binary download click the download link which will download the file luacheck.exe
- Place the luacheck.exe file in a useful place e.g. Program Files and add that location to your PATH.
- Restart any command lines you have open.
- Luacheck is now installed

## Using luacheck:

Post-install step:
- Set luacheck config:
    - Create a new file .luacheckrc in %LOCALAPPDATA%\Luacheck as this is where luacheck looks for config files
    - Add the below information to the file to set the config
```
stds.epics_lib = {
    read_globals = {"iocsh", "asyn", "client", "driver", "epics"}
}
stds.utils = {
    globals = {"getMacroValue", "setAsynOptions", "setHardwareFlowControl", "setSoftwareFlowControl"}
}
std = "min+epics_lib+utils"
```

Note: If you add any functions to our utilities you must add the name of the function to the globals set in std.utils in the .luacheckrc file. Please also add it to our list here, or to one on the repository if we have added it to the repo by then.

Basic usage: `luacheck file.lua`

For more detailed instructions on the use of luacheck see the [luacheck documentation](https://luacheck.readthedocs.io/en/stable/).

The [luacheck GitHub page](https://github.com/mpeterv/luacheck/tree/76bb56736702e8651537b2a9c10ae55ab7dc1d5d) also has information about how to use luacheck in your favourite editor.
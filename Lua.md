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

## Style Guide

We are using the style guide from LuaRocks as documented in https://github.com/luarocks/lua-style-guide#conditional-expressions

## Installing LuaCheck

Go to the [luacheck GitHub page](https://github.com/mpeterv/luacheck/tree/76bb56736702e8651537b2a9c10ae55ab7dc1d5d) and under Windows binary download click the download link which will download the file luacheck.exe

Place the luacheck.exe file in a useful place e.g. Program Files and add that location to your PATH.

Restart any command lines you have open, and then you can run `luacheck file.lua` against a Lua file.

For more detailed instructions on the use of luacheck see the [luacheck documentation](https://luacheck.readthedocs.io/en/stable/)
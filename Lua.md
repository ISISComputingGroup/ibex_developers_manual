I've added the EPICS Lua support module to our build system. Lua is a scripting language
designed to be embedded, it has a small footprint and is reasonably powerful. It would
provide an alternative to jumping through hoops in st.cmd syntax but also provides a 
few other options. All `iocsh` commands are imported into Lua and so you can do things
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

or just typing `luash` puts you into an interactive Lua shell.

The Lua script record is like a calcout record but can execute Lua script. It might be
an alternative to e.g. aSub records for parsing stream device strings when writing C is 
a bit overkill.

As well as being able to read/write PVs there is also some asyn integration into Lua, 
so you can read/write/set asyn parameters 
from Lua command line or script record, or even talk to a device by creating an asyn IP port
and sending strings. See the documentation directory in Lua support module  and the 
example scripts directory in iocBoot

To use 
  
```
add    LUA=$(SUPPORT)/lua/master     to configure/RELEASE
add    luaSupport.dbd                to the IOC Makefile DBD list
add    lua   and   asyn              to the IOC Makefile   _LIBS    list
```

There are examples of a Lua script used in the DETADC, Attocube and OERCONE IOCs.

There is a powerpoint about Lua here: https://indico.cern.ch/event/766611/contributions/3438291/attachments/1856812/3050126/Lang-Lua_Integrating_Scripting_Language.pdf

See also the documentation on our [epics-lua module](https://github.com/ISISComputingGroup/EPICS-lua) or the actual [epics module](https://github.com/epics-modules/lua) for more information on using Lua in EPICS.

## Lua utility functions

We have a few Lua utility functions available in our utilities submodule. For usage and how to add to them see [this page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Our-Lua-Utility-Functions).

## Style Guide

We are using the style guide from LuaRocks as documented in https://github.com/luarocks/lua-style-guide#conditional-expressions

## LuaCheck

For installation, usage and troubleshooting see the [luacheck page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/LuaCheck)

## Issues with Epics Lua and some answers

Whilst during the conversion of the oercone IOC to Lua we came across a few issues with the epics Lua library.

The process for resolving names in epics Lua starts with looking for a variable with that name, if it does not find one it looks in the running EPICS environment and then if it cannot find anything there it looks for a matching function name.

This is great so that we can access macros easily by instead of doing `$(MYMACRO)` from cmd we can just do `MYMACRO`. However, we cannot stipulate a default. There is a Lua utility function we have written, `getMacroValue(options)`, which expects to be called like this `getMacroValue{macro="MYMACRO", default="VAL"}` or `getMacroValue{macro="MYMACRO"}`.

There is a strange issue due to the way epics Lua runs Lua scripts that sometimes a local variable will drop out of scope, seemingly for no reason. We expect variables to be local and are thus kept to the namespace of the Lua script itself, we do not want to use global variables for no reason.

You may see that a variable was once the value you expect and then changes to something like `func_meta: 008...`. This is because the variable name has dropped out of scope and epics Lua attempts to look for a macro and fails, so then looks for a function and returns the func_meta string.

Fortunately, if we have a multiline chunk such as in a function we can use local variables. Thus to limit the amount of global variables we have to use we have decided to surround our lua code in functions. There are two caveats to this:

- The functions themselves become global variables, so we must take care to not give the same names to functions in the same iocBoot.
    - I suggest if we have a main function for each lua file we give it the name `<filename>_main` e.g. for st: `st_main` or for st-common: `stcommon_main`.
- Our package.path setup and [lua utility](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Our-Lua-Utility-Functions) imports MUST occur outside of the function but also MUST be declared as local variables.
# Lua
I've added the EPICS Lua support module to our build system. Lua is a scripting language
designed to be embedded, it has a small footprint and is reasonably powerful. It would
provide an alternative to jumping through hoops in st.cmd syntax but also provides a 
few other options. There are examples of a Lua script used in the DETADC, Attocube and OERCONE IOCs.

## To add the Lua support module to an IOC
  
```
add    LUA=$(SUPPORT)/lua/master     to configure/RELEASE
add    luaSupport.dbd                to the IOC Makefile DBD list
add    lua   and   asyn              to the IOC Makefile   _LIBS    list
```

## How to use it 

All `iocsh` commands are imported into Lua and so you can do things
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


There is a powerpoint about Lua here: https://indico.cern.ch/event/766611/contributions/3438291/attachments/1856812/3050126/Lang-Lua_Integrating_Scripting_Language.pdf

See also the documentation on our [epics-lua module](https://github.com/ISISComputingGroup/EPICS-lua) or the actual [epics module](https://github.com/epics-modules/lua) for more information on using Lua in EPICS.

## Importing Lua Functions from Other Files

When importing functions from other files you must be very careful not to pollute your scope as by default anything declared in lua is in the global scope. This means that if I have a file `importable_script.lua` of

```
function my_func()
   print("Hello world")
```

and I import this file from elsewhere using:

```
require "importable_script.lua"
my_func()
```

I can call `my_func` as it will be in the global variables of my new script. This means the require statement is polluting my namespace, to get around this we can change `importable_script.lua` to read:

```
local available_functions = {}

local function available_functions.my_func()
   print("Hello world")

return available_functions
```

when I do the import I can do:

```
my_import = require "importable_script.lua"
my_import.my_func()
```

now the only think in my global namespace will be `my_import`, which I specifically put in there, which contains all the functions I've imported for later reference.

We have a few Lua utility functions available in our utilities submodule. For usage and how to add to them see [this page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Our-Lua-Utility-Functions).

## Style Guide

We are using the style guide from LuaRocks as documented in https://github.com/luarocks/lua-style-guide#conditional-expressions

## LuaCheck

For installation, usage and troubleshooting see the [luacheck page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/LuaCheck)

## Issues with Epics Lua and some answers

Whilst during the conversion of the oercone IOC to Lua we came across a few issues with the epics Lua library.

The process for resolving names in epics Lua starts with looking for a variable with that name, if it does not find one it looks in the running EPICS environment and then if it cannot find anything there it looks for a matching function name.

This is great so that we can access macros easily by instead of doing `$(MYMACRO)` from cmd we can just do `MYMACRO`. However, we cannot stipulate a default. There is a Lua utility function we have written, `getMacroValue(options)`, which expects to be called like this `getMacroValue{macro="MYMACRO", default="VAL"}` or `getMacroValue{macro="MYMACRO"}`.

The way that EPICs calls lua scripts causes local variables to fall out of scope between lines such that a script where you have written
``` 
local text = "Hello"
print(text)
```
will print `nil` as `text` has not been defined but
```
local text = "Hello";print(text)
```
will successfully print `Hello`. 

Fortunately, if we have a multiline chunk such as in a function we can use local variables. Thus to limit the amount of global variables we have to use we have decided to surround our lua code in functions. This means that:

- Anything outside of a function must be declared as global for it to be used later on in the script. We think [this](https://epics-lua.readthedocs.io/en/latest/using-lua-shell.html#common-lua-environments) might `fix` the use of local variables outside of functions but it's effectively putting them in a global scope anyway.
- This includes the functions themselves, so we must take care to not give the same names to functions in the same iocBoot.
- I suggest if we have a main function for each lua file we give it the name `<iocname>_<filename>_main` e.g. for the oercone devices st.lua: `oercone_st_main` and it's st-common.lua: `oercone_stcommon_main`. 

You may see that a variable was once the value you expect and then changes to something like `func_meta: 008...`. This is because the variable name has dropped out of scope and epics Lua attempts to look for a macro and fails, so then looks for a function and returns the func_meta string.
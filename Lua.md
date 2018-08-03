I've added the EPICS Lua support module to our build system. Lua is a scripting language
designed to be embedded, it has a small footprint and is reasonably powerful. It would
provide an alternative to jumping through hoops in st.cmd syntax but also provides a 
few other options. All iocsh commands are imported into lua and so you can do things
like:

'''
for index=1,10,1
do
    print(string.format("Loading instance: %d", index))
    iocsh.dbLoadRecords("test.db", string.format("P=xxx:,Q=%d", index))
end
'''

You execute files from st.cmd using:

'''
luash("file.lua")
'''

or just typing "luash" puts you into an interactive lua shell.

The lua script record is like a calcout record but can execute lua script. It might be
an alternative to e.g. aSub records for parsing stream device strings when writing C is 
a bit overkill.

As well as being able to read/write PVs there is also some asyn integration into lua, 
so you can read/write/set asyn parameters 
from lua command line or script record, or even talk to a device by creating an asyn IP port
and sending strings. See the documentation directory in lua support module  and the 
exampel scripts directory in iocBoot

To use 
  
'''
add    LUA=$(SUPPORT)/lua/master     to configure/RELEASE
add    luaSupport.dbd                to the IOC Makefile DBD list
add    lua   and   asyn              to the IOC Makefile   _LIBS    list
'''

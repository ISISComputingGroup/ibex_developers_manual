# Introduction
aSub records are useful when the output of a device is too complicated to be reasonably parsed in .protocol files.


# DB records



# Build files
Declare a `.dbd` file with the names of all the functions declared in the `C` file which will be called by EPICS.

```
function(function_name)
function(another_function_name)
[...]
```

In the make file references need to be added for the `.dbd` file and the `C` code:

```
LIBRARY_IOC = APPNAME
DBD += appname.dbd

APPNAME_DBD += asyn.dbd
APPNAME_DBD += asubFunctions.dbd

APPNAME_SRCS += c_sources.c

APPNAME_LIBS += $(EPICS_BASE_IOC_LIBS)
APPNAME_LIBS += asyn utilities
APPNAME_LIBS += asubFunctions
```
Where `APPNAME` is to be replaced with the name of the new support module being built.

In the support/{...}/configure/RELEASE file reference all libraries which will be required to compile the new support module.

For example, a minimum set required will be:
```
ASYN=$(SUPPORT)/asyn/master
ONCRPC=$(SUPPORT)/oncrpc/master
SNCSEQ=$(SUPPORT)/seq/master
UTILITIES=$(SUPPORT)/utilities/master
ASUBFUNCTIONS=$(SUPPORT)/asubFunctions/master
```

The **IOC** makefile will now need to be updated with the files that have just been produced

```
$(APPNAME)_DBD += LIBRARY_NAME.dbd

$(APPNAME)_LIBS += LIBRARY_NAME
```
Here, `$(APPNAME)` _is_ a macro, and `LIBRARY_NAME` will need to be replaced with the name of the support module that was just created.


# C code
Need to define a C function which will be called by the aSub record:

```
static long function_name(aSubRecord *prec)
{
    return 0;
}
```

Need to tie in this function to the epics database with a call to `epicsRegisterFunction`:
```
epicsRegisterFunction(function_name);
```

# Escaping to C++

# C++ code
# Introduction
EPICS aSub records are a powerful tool that allows you to write arbitrary C or C++ code that interacts with EPICS DB records.

Circumstances where you may need to use aSub records include:
- A device responds with a very complex status string which is too complex to decode using streamdevice
- There are complex checks required before a command can be sent to a device, or complex logic required to interpret the state of a device.
- The device responds with completely different responses based on it's physical configuration, and the IOC needs to handle all possible circumstances
- You need to interact with files from within an IOC (first consider whether [autosave](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Autosave) or [ReadASCII](https://github.com/ISISComputingGroup/EPICS-ReadASCII) cover the functionality you need)

### Examples
- `FZJ Fermi Chopper` (`EPICS/ioc/master/FERMCHOP`)
  * This contains five scripts: Two to parse sets of status packets from a device, two to choose values to send to a device, and one to check that a command is allowed to be sent at the current time.
- `Keithley 2700` (`EPICS/support/Keithley_2700/master`)
  * This contains a script to parse buffer readings from a device and put them into the appropriate DB records.
- `Keyence TM-3001P`
  * This contains scripts to parse complex response strings from a device.
- ReadASCII metadata (`EPICS/support/ReadASCII/master`)
  * This contains scripts to read metadata from a filepath provided in EPICS DB records.


# DB records
Define some aSub records which may look like:
```
record(stringin, "$(P)STATUS:RAW")
{
    field(DESC, "Reads from the device")
    field(DTYP, "stream")
    field(INP, "...")
    field(SCAN, "1 second")
    field(FLNK, "$(P)STATUS:PARSE")
}

record(aSub, "$(P)STATUS:PARSE")
{
    field(SNAM, "function_name")

    field(INPA, "$(P)STATUS:RAW")
    field(FTA, "STRING")

    field(OUTA, "$(P)STATUS PP")
    field(FTVA, "STRING")

}

record(stringin, "$(P)STATUS")
{
}
```


# Build files

Create a `.dbd` file with the names of all the functions declared in the `C` file which will be called by EPICS. Your DBD file should look like the following:

```
function(function_name)
function(another_function_name)
[...]
```

In the same directory as your C source code and the DBD file, adjust the makefile to reference the newly created `.dbd` and `.c` files, as well as adding necessary dependencies. It should look something like the following:

```
LIBRARY_IOC = APPNAME
DBD += appname.dbd

APPNAME_DBD += asyn.dbd
APPNAME_DBD += asubFunctions.dbd

APPNAME_SRCS += c_source.c

APPNAME_LIBS += $(EPICS_BASE_IOC_LIBS)
APPNAME_LIBS += asyn utilities
APPNAME_LIBS += asubFunctions
```
Where `APPNAME` is to be replaced with the name of the new support module being built.

In the `configure/RELEASE`, ensure you have listed all required dependencies. A minimum set for an aSub record is shown below, but your support module may also require additional dependencies.

```
ASYN=$(SUPPORT)/asyn/master
ONCRPC=$(SUPPORT)/oncrpc/master
SNCSEQ=$(SUPPORT)/seq/master
UTILITIES=$(SUPPORT)/utilities/master
ASUBFUNCTIONS=$(SUPPORT)/asubFunctions/master
```

Finally, the **IOC** makefile (`build.mak`) will now need to be updated to include the DBD and Library produced by the support module. The following lines will add the dependency:

```
$(APPNAME)_DBD += LIBRARY_NAME.dbd
$(APPNAME)_LIBS += LIBRARY_NAME
```

Here, `$(APPNAME)` _is_ a macro, and `LIBRARY_NAME` will need to be replaced with the names of the library and DBD file that you have created above.

You will also need to ensure that the support module location is mentioned in `ioc/{iocname}/configure/RELEASE`. However for most IOCs this should already be the case, as they will get their stream protocol from that location.

# C code

Define a C function which will be called by the aSub record. This must have the same name as the `SNAM` field in EPICS DB. You also need to tie this function in to the epics database with a call to `epicsRegisterFunction`. At this stage your C source file should look like the following:

```C
#include <stdlib.h>
#include <registryFunction.h>
#include <aSubRecord.h>
#include <epicsExport.h>

static long function_name(aSubRecord *prec)
{
    /* Either call a C++ function (see below) or implement logic here. */
    return 0;
}

epicsRegisterFunction(function_name);
```

# Escaping to C++

Note: escaping to C++ is not strictly necessary, it is possible to implement the logic in C. However it is often easier to work with C++ due to it's larger standard library and [boost](https://www.boost.org/).

### Create a c/c++ header file

In the same directory as the `C` source code file, create a header (`.h` extension) like the following:

```C
#ifdef __cplusplus
extern "C" {
#endif

extern long function_name_impl(aSubRecord *prec);
extern long another_function_name_impl(aSubRecord *prec);

#ifdef __cplusplus
}
#endif
```

### Reference the header file from the C code

In C code which is called by the EPICS records, call the C++ functions which will be parsing the data. Your C source file should now look something like the following:

```C
#include <stdlib.h>
#include <registryFunction.h>
#include <aSubRecord.h>
#include <epicsExport.h>

#include "header_file.h"

static long function_name(aSubRecord *prec) 
{
	return function_name_impl(prec);
}

epicsRegisterFunction(function_name); 
```

Note that C and C++ functions cannot share the same name. Here we have appended `_impl` to the name of the C++ function to indicate that it is the implementation.

### Reference the header file from C++

Create a C++ source file (`.cpp` extension, cannot share the same name as the `.c` file). The following is an example of a skeletal C++ source file which simply sets the output data (`VALA`, which goes to `OUTA`) to the input value (`A`, which is pulled from `INPA` in the EPICS database file):

```C++
#include <string.h>
#include <stdlib.h>
#include <registryFunction.h>
#include <aSubRecord.h>
#include <menuFtype.h>
#include <errlog.h>
#include <epicsString.h>
#include <epicsExport.h>

#include <string>
#include <vector>
#include <sstream>
#include <iostream>

#include "header_file.h"

long function_name_impl(aSubRecord *prec) 
{
    /* Returns the first input value back */
    prec->vala = prec->a;
    return 0; /* process output links */
}

```

The function takes one argument, `prec`, which is as a pointer to the EPICS aSub record. Changes made to `prec` will set the value of the corresponding EPICS fields once the aSub function returns (return 0 to indicate success, or 1 to indicate failure).

### Add the C++ source file to the support module makefile.

The makefile should now contain a line that looks like:

```
APPNAME_SRCS += c_source.c cpp_source.cpp
```
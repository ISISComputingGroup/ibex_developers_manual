# Introduction
aSub records are useful when the output of a device is too complicated to be reasonably parsed in .protocol files.


# DB records
Define some aSub records which may look like:
```
record(aSub, "$(P)STATUS:PARSE")
{
    field(SNAM, "function_name")
    field(INPA, "$(P)STATUS:RAW")
    field(FTA, "STRING")
    field(NOA, "1")

    field(OUTA, "$(P)STATUS PP")
    field(FTVA, "STRING")

}

record(stringin, "$(P)STATUS:RAW")
{
    field(DESC, "Reads from the device")
    field(DTYP, "stream")
    field(INP, "...")
    field(SCAN, "1 second")
    field(FLNK, "$(P)STATUS:PARSE")
}

record(stringin, "$(P)STATUS")
{
}
```


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
### Create a c/c++ header file

In support module/library_name.h:
```
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
In C code which is called by the EPICS records, call the C++ functions which will be parsing the data:
```
#include <stdlib.h>
#include <registryFunction.h>
#include <aSubRecord.h>
#include <epicsExport.h>

#include "library_name.h"

static long function_name(aSubRecord *prec) 
{
	return function_name_impl(prec);
}

epicsRegisterFunction(function_name); 
```
Note that C and C++ functions cannot share the same name.

### Reference the header file from C++

Create a C++ file (which cannot share the same name as the C file), with extension `.cpp`.

```
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

#include "library_name.h"

long function_name_impl(aSubRecord *prec) 
{
    /* Returns the first input value back */
    prec->vala = prec->a;
    return 0; /* process output links */
}

```

`prec` has been passed through here as a reference to the aSub record. Changes made to this variable will influence the values in EPICS PVs.

### Add the C++ header file to the support module makefile
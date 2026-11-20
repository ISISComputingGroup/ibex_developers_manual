# Asub records

## Introduction

EPICS aSub records are a powerful tool that allows you to write arbitrary C or C++ code that interacts with EPICS DB records.

Circumstances where you may need to use aSub records include:
- A device responds with a very complex status string which is too complex to decode using streamdevice
- There are complex checks required before a command can be sent to a device, or complex logic required to interpret the state of a device.
- The device responds with completely different responses based on its physical configuration, and the IOC needs to handle all possible circumstances
- You need to interact with files from within an IOC (first consider whether [autosave](Autosave) or [ReadASCII](https://github.com/ISISComputingGroup/EPICS-ReadASCII) cover the functionality you need)

### Examples
- `FZJ Fermi Chopper` (`EPICS/ioc/master/FERMCHOP`)
  * This contains five scripts: Two to parse sets of status packets from a device, two to choose values to send to a device, and one to check that a command is allowed to be sent at the current time.
- `Keithley 2700` (`EPICS/support/Keithley_2700/master`)
  * This contains a script to parse buffer readings from a device and put them into the appropriate DB records.
- `Keyence TM-3001P`
  * This contains scripts to parse complex response strings from a device.
- ReadASCII metadata (`EPICS/support/ReadASCII/master`)
  * This contains scripts to read metadata from a filepath provided in EPICS DB records.

## IOC files

### DB records
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


### Build files

Create a `.dbd` file with the names of all the functions declared in the `C` file which will be called by EPICS. Your DBD file should look like the following:

```
function(function_name)
function(another_function_name)
[...]
```

>__**NOTE: Make sure there is a newline at the end of this file**__

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

Finally, the **IOC** makefile (`-IOC-01App\src\build.mak`) will now need to be updated to include the DBD and Library produced by the support module. The following lines will add the dependency:

```
$(APPNAME)_DBD += LIBRARY_NAME.dbd
$(APPNAME)_LIBS += LIBRARY_NAME
```

Here, `$(APPNAME)` _is_ a macro, and `LIBRARY_NAME` will need to be replaced with the names of the library and DBD file that you have created above.

You will also need to ensure that the support module location is mentioned in `ioc/{iocname}/configure/RELEASE`. However, for most IOCs, this should already be the case, as they will get their stream protocol from that location.

## Writing an aSub Function

### C code

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

### Escaping to C++

Note: escaping to C++ is not strictly necessary, it is possible to implement the logic in C. However it is often easier to work with C++ due to it's larger standard library and [boost](https://www.boost.org/).

#### Create a c/c++ header file

In the same directory as the `C` source code file, create a header (`.h` extension) like the following:

```C++
#ifdef __cplusplus
extern "C" {
#endifit

extern long function_name_impl(aSubRecord *prec);
extern long another_function_name_impl(aSubRecord *prec);

#ifdef __cplusplus
}
#endif
```

#### Reference the header file from the C code

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

#### Reference the header file from C++

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
    /*
     * Returns the first input value back, assuming both have been 
     * declared as LONG in the db file. You can check the fta and 
     * ftva fields to confirm the data types 
     */
    *(epicsInt32*)prec->vala = *(epicsInt32*)prec->a;
    return 0; /* process output links */
}

```

The function takes one argument, `prec`, which is as a pointer to the EPICS aSub record. Changes made to `prec` will set the value of the corresponding EPICS fields once the aSub function returns (return 0 to indicate success, or 1 to indicate failure).

#### Add the C++ source file to the support module Makefile.

The makefile should now contain a line that looks like:

```
APPNAME_SRCS += c_source.c cpp_source.cpp
```

## aSub Record Function Tips and Tricks

It is advised that when writing an aSub record, you escape to C++ as soon as possible so that you can use the C++ standard libraries and error handling capacity to improve the robustness of your IOC to errors arising from the aSub record.

### GoogleTest unit tests

GoogleTest can be used to write unit tests for you aSub functions. Details on how to set up GoogleTest to compile under EPICS can be found [here](#googletest_intro).

### Error catching

To reduce the chances of the IOC crashing due to an exception being, it is best practice to wrap the logic of your function in a `try-catch` block to log these exceptions and return a non-zero value. E.g. to catch a stand
```C++
try {
    // Your code here
}
catch (std::exception& e) {
    errlogSevPrintf(errlogMajor, "%s exception: %s", prec->name, e.what());
    return 1;
}
```

### Defensive Type Checking

As any field of the aSub record can be written to, it is best practice to check types of input and output fields before reading and writing. 

To check that the type of the input field `a` is a `STRING`, use

```C++
if (prec->fta != menuFtypeSTRING)
    {
        errlogSevPrintf(errlogMajor, "%s incorrect input argument type A", prec->name);
        return 1;
    }
```
To check that the type of the output field `a` is of type `STRING` use

```C++
if (prec->ftva != menuFtypeSTRING)
    {
        errlogSevPrintf(errlogMajor, "%s incorrect output argument type A", prec->name);
        return 1;
    }
```

### Reading from a waveform of strings

If you need to read from a waveform of strings, then you need to be extra careful with types. The best way we have found is to read the waveform into a `vector<std::string>` in the following way:

```C++
std::vector<std::string> args;
for (unsigned int i = 0; i < prec->noa; ++i) {
    std::string s(((epicsOldString*)(prec->a))[i], sizeof(epicsOldString));
    args.push_back(s);
}
```

This takes into account that the type of each element of the waveform is not a `char*` but a` epicsOldString`.

### Decoupling from the aSub record pointer

You may find it useful to decouple the logic of writing to the output fields of the aSub record from the main aSub record it self. This makes it easier to test how you write to the aSub record without needing a pointer to a real aSub record. You can encapsulate the values you need in a `struct`.

```C++
struct aSubOutputParameters{
    void* outputPointer;
    epicsEnum16 outputType;

    // Struct constructors
    aSubOutputParameters() {}
    aSubOutputParameters(void* output_pointer, epicsEnum16 output_type)
    : outputPointer(output_pointer), outputType(output_type) {}
};
```
You can then use this `struct` to create a map which associates a value (a integer channel number in the example below) to the specific aSub output data that value corresponds to.

```C++
std::map<int, aSubOutputParameters> asub_channel_output(aSubRecord *prec) {
    std::map<int, aSubOutputParameters> channel_outputs;
    
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(1,   aSubOutputParameters(prec->vala, prec->ftva)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(2,   aSubOutputParameters(prec->valb, prec->ftvb)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(3,   aSubOutputParameters(prec->valc, prec->ftvc)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(4,   aSubOutputParameters(prec->vald, prec->ftvd)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(5,   aSubOutputParameters(prec->vale, prec->ftve)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(6,   aSubOutputParameters(prec->valf, prec->ftvf)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(7,   aSubOutputParameters(prec->valg, prec->ftvg)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(8,   aSubOutputParameters(prec->valh, prec->ftvh)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(9,   aSubOutputParameters(prec->vali, prec->ftvi)));
    channel_outputs.insert(std::pair<int, aSubOutputParameters>(10,  aSubOutputParameters(prec->valj, prec->ftvj)));

    return channel_outputs;
}
```

When testing you need to create mock versions of the `asub_channel_output` map rather than the whole aSub record.

### Parsing functions as arguments

If you find yourself needing to pass a function as an argument, you can do so using:

1. `boost::function<return_value (arguments)> func` (remember to include `boost/function.hpp`)
1. `std::function<return_value (arguments)> func` (remember to include `functional, C++11 and later only)
1. Using a `template<typename F>` and passing the function as a parameter `F func`. **N.B.**: Types are checked at runtime not compile time when using templates (more details [here](https://stackoverflow.com/questions/1174169/function-passed-as-template-argument)).
1. Function pointers - try to use the above safer ways first.

This technique can be useful if you have multiple aSub functions that are similar apart from the logic to parse a value from the waveform. You can then pass a different functions as arguments to a base aSub record function to generate your aSub record functions.

### Record doesn't seem to work

Add in some debug lines:

```
errlogSevPrintf(errlogMajor, "Start");
```

If you don't see this in the log (works even under the testing framework) do a `caget -a` and make sure all the links are valid; an invalid link specification will cause the record not to process.

### Tips

* LONG in epics DB world is 32 bit, while the C long type is 32bit on Windows and 64bit on Linux. When casting from aSub you should use the `epicsInt32` type and not "long"
* Do not assign directly to aSub record argument such as "prec->vala = result". Rather copy into the pre-allocated space as shown below 
* Remember all aSub arguments are arrays of the type even if the type is an array, so `epicsOldString*`
```
epicsInt32 i = *(epicsInt32*)prec->a;
epicsOldString* result = (epicsOldString*)prec->vala;
strcpy_s(*result, MAX_STRING_SIZE, "Unknown")
```

## aSub Functions

* [`splitCharWaveform`](https://github.com/ISISComputingGroup/EPICS-asubFunctions/blob/master/asubFunctionsApp/src/splitCharWaveform.c#L108)

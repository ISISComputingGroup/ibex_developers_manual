# Compile Errors

## Using `callback.h`
If you get
```
c:\instrument\apps\epics2\support\hvcaenx527\master\libhvcaenx527app\src\hvcaenx527.h(79): error C2059: syntax error: '__cdecl'
c:\instrument\apps\epics2\support\hvcaenx527\master\libhvcaenx527app\src\hvcaenx527.h(80): error C2059: syntax error: '}'
c:\instrument\apps\epics2\support\hvcaenx527\master\libhvcaenx527app\src\hvcaenx527chaio.c(42): error C2223: left of '->evntno' must point to struct/union
```
when including `callback.h` it is because EPICS defines CALLBACK as a structure, windows defines it as `__cdecl`. If you need to include `windows.h` you must include it before epics redefines `CALLBACK` in `callback.h`
Including `osiSock.h` is a workaround as that pulls in `windows.h` but it may be better to be explicit with
```
#ifdef _WIN32
#include <windows.h> /* we need to make sure EPICS callback.h is loaded after windows.h */
#endif
```

## `cmake error: could not load cache` seen during build

Try deleting any `CMakeCache.txt` files in the appropriate directory

## Can't build any IOCS

When trying to use Make to build IOCs you might encounter an Error 2. The failing Make will look something like this:
```
process_begin: CreateProcess(NULL, echo Generating runIOC.bat, ...) failed.
make (e=2): The system cannot find the file specified.
```
This can be a result of having an environment path for git that points to `git/bin`. If it is, then make will think you are on linux and then the build will fail. You must change this to be `git/cmd` to point at the Windows binaries.

See also [Ticket 4201](https://github.com/ISISComputingGroup/IBEX/issues/4201) for a potential fix.

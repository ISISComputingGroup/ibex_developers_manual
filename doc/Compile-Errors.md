# Using `callback.h`
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
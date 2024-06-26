This is following a bit on from https://devblogs.microsoft.com/oldnewthing/20160302-00/?p=93103
```
Faulting application name: JULABO-IOC-01.exe, version: 0.0.0.0, time stamp: 0x65a785c3 Faulting module name: asyn.dll, version: 0.0.0.0, time stamp: 0x65a75e35 Exception code: 0xc0000005 Fault offset: 0x00000000000066c0 Faulting process ID: 0x1b0c0 Faulting application start time: 0x01dac65ace0ce665 Faulting application path: C:\Instrument\Apps\EPICS\ioc\master\JULABO\bin\windows-x64\JULABO-IOC-01.exe Faulting module path: C:\INSTRU~1\Apps\EPICS\support\asyn\master\bin\windows-x64\asyn.dll Report ID: 772b96c7-21cc-4753-9db9-cea1b0655858 Faulting package full name: Faulting package-relative application ID:
```
so we want to find out what is at offset `0x66c0` in `asyn.dll`

* vnc onto instrument
* create cmd window and cd to iocBoot for ioc
* run `dllpath.bat`
* now run `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe`
* file -> open executable and browse to ioc exe in bin
* look at debug ->modules window and note load address of DLL of interest e.g. `00007ffeb6da0000`
* if offset was `0x66c0` then type `u 0x00007ffeb6da0000 + 0x66c0 L1` and you'll get something like
```
0:000> u 0x00007ffeb6da0000 + 0x66c0 l1
asyn!findDpCommon [C:\Instrument\Apps\EPICS\support\asyn\master\asyn\asynDriver\asynManager.c @ 2620] [inlined in asyn!getTraceMask [C:\Instrument\Apps\EPICS\support\asyn\master\asyn\asynDriver\asynManager.c @ 2620]]:
00007ffe`b6da66c0 488b41e0        mov     rax,qword ptr [rcx-20h]
```

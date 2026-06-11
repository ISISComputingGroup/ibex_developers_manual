# Deploying a Debug IOC

**NOTE**: if you are a developer wishing to develop on your desktop with a debug build, the debug version of the [Developer server build](/iocs/compiling/Developer-Server-Build) may be easier to work with. The builds below do not ship `.lib` or intermediate `O.*` object directories so if you wish to rebuild with changes after having run the debugger it is a little more time consuming.

DEBUG DLL builds are kept in `EPICS_DEBUG_CLEAN_win7_x64` in the usual kits deployment area. If you wish to deploy only a single IOC in debug mode rather than replace the whole installation with the above debug build then:
1. You need to build the `dllCopy.bat` by running ```make dllCopy.bat``` in the ioc boot area.
1. Double-click on the **`dllCopy.bat`** file in the `iocBoot` area of the IOC you want to deploy on kits, this will copy the dependent DLL and `.pdb` files to the {ioc}/bin/windows-x64-debug directory
1. Backup the `{ioc}/bin/windows-x64` directory on the target computer to be tested.
1. Copy the `.EXE` and all `.DLL`/`.pdb` files from the `kits/{ioc}/bin/windows-x64-debug` directory to the `bin/windows-x64` of the target IOC.
1. Also copy the files in `kits/EPICS/crtl/windows-x64-debug` to the target `{ioc}/bin/windows-x64` directory.

When you start the IOC it should now start the debug build you have copied over.  

Note: there is also a EPICS_STATIC_DEBUG_CLEAN_win7_x64 build - this would only require copying the single `.EXE` and `.pdb` file as all DLLs are bundled into the `.EXE` in a static build; however static builds have sometimes behaved differently to DLL builds in the past and so the above DLL option is a better test of the eventual mechanism, though trying a static EXE may be enough for diagnostics. The files here will be in a `windows-x64-static-debug` directory.

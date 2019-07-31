> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Debug Builds

DEBUG builds are kept in `EPICS_STATIC_DEBUG_CLEAN_win7_x64` in the usual kits deployment area. If you wish to deploy only a single IOC in debug mode rather than replace the installation with the above debug build then:

1. Double-click on the **`dllCopy.bat`** file in the `iocBoot` area of the IOC you want to deploy on kits, this will copy the dependent DLLs to the IOC kits area.
1. Backup the `{ioc}/bin/windows-x64` directory on the target computer to be tested.
1. Copy the EXE and all DLL files from the `kits/{ioc}/bin/windows-x64-debug` directory to the `bin/windows-x64` of the target IOC.
1. Also copy the files in `kits/EPICS/crtl/windows-x64-debug` to the target `{ioc}/bin/windows-x64` directory.

When you start the IOC it should now start the debug build you have copied over.  

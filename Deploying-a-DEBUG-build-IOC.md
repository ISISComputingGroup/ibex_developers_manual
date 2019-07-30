DEBUG builds are kept in EPICS_STATIC_DEBUG_CLEAN_win7_x64 in the usual kits deployment area. If you wish to deploy only a single IOC in debug mode rather than replace the installation with the above debug build then:

- double click on the **dllCopy.bat** file in the iocBoot area of the IOC you want to deploy on kits, this will copy the dependent DLLS to the ioc kits area.
- backup the {ioc}/bin/windows-x64 directory on the target computer to be tested  
- copy the exe and all dll files from the kits/{ioc}/bin/windows-x64-debug directory to the windows-x64 on the target  
- Copy the files in kits/EPICS/crtl/windows-x64-debug to the {ioc}/bin/windows-x64 directory

When you start the IOC it should now start the debug build you have copied over.  

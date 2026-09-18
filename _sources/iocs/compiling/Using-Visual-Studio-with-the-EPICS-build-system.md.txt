# Using VS with EPICS

Some of the EPICS modules are written in C++ and so it makes sense to use Visual Studio to edit these. To correctly set up Visual Studio to edit a project you should do the following:

1. Start an EPICS terminal e.g. `C:\Instrument\Apps\epics\EPICSTerm.bat`
1. Start Visual Studio in this EPICS terminal by running `devenv`
1. Go to File -> New -> Project from Existing Code
1. Select C++ and press Next
1. Select the top directory for the project file location e.g. `C:\Instrument\Apps\epics\support\sampleChanger\master`
1. Give the project a sensible name and press Next
1. Select `Use external build system` and press Next
1. As the build command line type `make` and as the clean command type `make clean uninstall` and press Finish

The code will now be in Visual Studio and you should be able to Build it from the Build menu at the top. To point Visual Studio at the dependencies of the code do the following:

1. Open the RELEASE file for the project e.g. `C:\Instrument\Apps\epics\support\sampleChanger\master\configure\RELEASE`
1. In VS right click on the project and select properties -> VC++ Directories
1. In the include directories add an entry for each line in the RELEASE file (apart from the optional extras ones) that points to the include directory of that submodule (remembering that `$(SUPPORT)` is `C:\Instrument\apps\epics\support`) e.g. you will add `C:\Instrument\Apps\epics\support\asyn\master\include` (note that in reality a lot of these includes will not be needed for the C++ code, the following will definitely not: `AUTOSAVE`, `CAPUTLOG`, `DEVIOCSTATS`, `ICPCONFIG`, `MYSQL`, `SQLITE`, `PVDUMP`)
1. Add `C:\Instrument\Apps\epics\base\include` to the include directories

Visual Studio should now pick up all the dependencies and so give you `intellisense`/autocomplete etc.
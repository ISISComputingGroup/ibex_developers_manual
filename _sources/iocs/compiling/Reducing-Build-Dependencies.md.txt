# Reducing build dependencies

This is a page describing how to reduce dependencies in our EPICS build. Currently we have a MASTER_RELEASE file at the top level that, though convenient, means the build system does a lot of cross-checking for things it doesn't need, disabling checkRelease can speed this up.  

A simple way to reduce dependencies is to remove the 
```
include $(TOP)/../../../configure/MASTER_RELEASE
-include $(TOP)/../../../configure/MASTER_RELEASE.$(EPICS_HOST_ARCH)
-include $(TOP)/../../../configure/MASTER_RELEASE.private
-include $(TOP)/../../../configure/MASTER_RELEASE.private.$(EPICS_HOST_ARCH)
```
lines and replace them by the lines that were in MASTER_RELEASE that are needed for the build and runtime (e.g. ioc loading db files) e.g.
```
ASYN=$(SUPPORT)/asyn/master
```
To determine what you need to add: 
* look at the Makefile to see what DBD and library files are used when building an IOC and then add the relevant macro definitions from MASTER_RELEASE to the new RELEASE to allow these to be located. See the _LIB and _DBD macros 
* Look at DB template *.substitution files in the App/Db directory to see where DB files are included from, you'll need any macros from here too
* Check st.cmd for use of such macros e.g. `$(ACCESSSECURITY)` and other DB files it may load and add these macros to the new RELEASE too

For the first step you can use the script in `ibex_utils/developer_support_script` which will add the lines to RELEASE based on libs and dbd files in you build.mak which it knows about. This script can be run multiple times. To run use:

    python build_dependencies.py <ioc directory>

If you get it wrong / miss something, it will usually just break the build due to a missing file; however if you miss a macro used in st.cmd it will not be noticed until the IOC is run. So you will need to run the IOC up in simulation mode and check for any warnings about undefined macros or commands. 

If the module you are changing is using AREA_DETECTOR or EPISC_V4 then things a little more complicated, I'll add extended notes at a later point.
  
after any change to RELEASE do a "make clean uninstall" followed by "make" to check

Something I mean to look more closely at for ideas is http://epics-sumo.sourceforge.net/


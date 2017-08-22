This is a page describing how to reduce dependencies in our EPICS build. Currently we have a MASTER_RELEASE file that though convenient means the build system does a lot of cross-checking for things it doesn't need, disabling checkRelease can speed this up.  

A simple way to reduce dependencies is to remove the 
```
include $(TOP)/../../../configure/MASTER_RELEASE
-include $(TOP)/../../../configure/MASTER_RELEASE.$(EPICS_HOST_ARCH)
-include $(TOP)/../../../configure/MASTER_RELEASE.private
-include $(TOP)/../../../configure/MASTER_RELEASE.private.$(EPICS_HOST_ARCH)
```
lines and replace them by the lines that were in MASTER_RELEASE that are needed for the build and run e.g.
```
ASYN=$(SUPPORT)/asyn/master
```
To determine what you need to add: 
* look at the Makefile to see what DBD and library files are used when building an IOC and then add the relevant definitions to allow these to be located. See the _LIB and _DBD macros 
* Look at DB template substitution files to see where DB files are included from, you'll need any macros from here too
* Check st.cmd for use of such macros e.g. $(ACCESSSECURITY) and add these too
 
If you get it wrong / miss something, it will usually just break the build due to a missing file; however if you miss a macro used in st.cmd it will not be noticed until the IOC is run. So you will need to run the IOC up in simulation mode and check for any warnings about undefined macros or commands. 

If the module you are changing is using AREA_DETECTOR or EPISC_V4 then things a little more complicated, I'll add extended notes at a later point.
  
Something I mean to look more closely at for ideas is http://epics-sumo.sourceforge.net/


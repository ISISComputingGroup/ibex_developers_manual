This is a page describing how to reduce dependencies in our EPICS build. Currently we have a MASTER_RELEASE file that though convenient means the build system does a lot of cross-checking for things it doesn't need, disabling checkRelease can speed this up.  

A simple way to reduce dependencies is to remove the 
```
include $(TOP)/../../../configure/MASTER_RELEASE
-include $(TOP)/../../../configure/MASTER_RELEASE.$(EPICS_HOST_ARCH)
-include $(TOP)/../../../configure/MASTER_RELEASE.private
-include $(TOP)/../../../configure/MASTER_RELEASE.private.$(EPICS_HOST_ARCH)
```
lines and replace them by the lines that were in MASTER_RELEASE that are needed for the build e.g.
```
ASYN=$(SUPPORT)/asyn/master
```
To determine what you need to add, look at the Makefile to see what DBD and library files are used and then add the relevant definitions to allow these to be located. If you get it wrong / miss something, it will just break the build due to a missing file, it will not introduce a subtle bug. And we can migrate in stages, no need to do all at once. 

If the module you are changing is using AREA_DETECTOR or EPISC_V4 then things a little more complicated, I'll add extended notes at a later point.
  
Something I mean to look more closely at for ideas is http://epics-sumo.sourceforge.net/


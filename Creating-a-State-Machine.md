> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Creating a State Machine

## Introduction
Does your IOC require definitive states? If the logic of your IOC will go beyond calc fields you may wish to implement a Finite State Machine. 

EPICS supports State Machine creation with a set of [Sequencer tools.](http://www-csr.bessy.de/control/SoftDist/sequencer/index.html) The state file, which controls the states the system can be in and the transitions between them, is written in C-based State Notation Language.
This is a how-to guide to create and implement a state machine into your IOC.

## Create State File 

Enter the support directory of your IOC, e.g:
```
C:\Instrument\Apps\EPICS\support\HFMAGPSU\master\HFMAGPSUSup
```
Create a state file in this directory (e.g. fsm.st).
The EPICS manual for SNL files can be found [here.](http://www-csr.bessy.de/control/SoftDist/sequencer/index.html)

If you will be reading or changing PV values, the following must be included in your `fsm.st` file
```
#include "seqPVmacros.h"
```
A copy of `seqPVmacros.h` can be found [here](https://github.com/ISISComputingGroup/EPICS-motor/blob/7080600a752478f9fa23301a7e99d7ea081df453/motorApp/NewportSrc/seqPVmacros.h) and should be in the folder alongside the `fsm.st` file.

Create an  `fsm.dbd` file, which contains the following:
```
registrar(fsmRegistrar)
```
Edit the `Makefile` in this folder, to reference your new `.dbd` and `.st` files and add the libraries needed for them.
```
TOP=..
include $(TOP)/configure/CONFIG
#=======================================

# Install .dbd and .db files
DATA += devHFMAGPSU.proto
DBD += fsm.dbd

# Sequence file
SRCS += fsm.st
LIBRARY_IOC = HFMAGPSU
HFMAGPSU_LIBS += seqDev seq pv
HFMAGPSU_LIBS += $(EPICS_BASE_IOC_LIBS)

#=======================================
include $(TOP)/configure/RULES
```
### Call State file from IOC
Enter IOC folder, e.g.
```
(cd …EPICS\ioc\master\HFMAGPSU\iocBoot\iocHFMAGPSU-IOC-01)
```
Add the following to the end of the `st-common.cmd` file:
```
< $(IOCSTARTUP)/postiocinit.cmd
epicsEnvSet(P,$(MYPVPREFIX)$(IOCNAME))

## Start any sequence programs
seq fsm, "P=$(P)"
```
In the above example, we are passing the name of the IOC through to the `fsm.st` file so we can reference PVs in it with `{P}:`.

Enter the IOC source folder (e.g ``HFMAGPSU-IOC-01App\src``)

Edit `build.mak` to ensure the needed libraries are included:
```
# Add all the support libraries needed by this IOC
## ISIS standard libraries ##

$(APPNAME)_LIBS += seqDev seq pv
```
### Notes

Whenever an edit is made to the `fsm.st` file, rebuild the support module:
```
cd …EPICS\support\HFMAGPSU\master
make
```

> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Creating a State Machine

## Contents
- [Introduction](#introduction)
- [Create State File](#create-state-file)
    - [Call State file from IOC](#call-state-file-from-ioc)
- [Start any sequence programs](#start-any-sequence-programs)
    - [Notes](#notes)
- [Passing macros into the sequencer](#passing-macros-into-the-sequencer)

## Introduction
Does your IOC require definitive states? If the logic of your IOC will go beyond calc fields, you may wish to implement a Finite State Machine. 

EPICS supports State Machine creation with a set of [Sequencer tools.](https://epics-modules.github.io/sequencer/Manual.html) The state file, which controls the states the system can be in and the transitions between them, is written in C-based State Notation Language.
This is a how-to guide to create and implement a state machine into your IOC.

## Create State File 

Enter the support directory of your IOC, e.g.:
```
C:\Instrument\Apps\EPICS\support\HFMAGPSU\master\HFMAGPSUSup
```
Create a state file in this directory (e.g. `fsm.st`).
The EPICS manual for SNL files can be found [here.](https://epics-modules.github.io/sequencer/Manual.html)

If you are reading or changing PV values, the following must be included in your `fsm.st` file:
```
#include "ibexSeqPVmacros.h"
```
You may also need to add a line to your `configure/RELEASE` file to allow inclusion of these PV utility macros:
```
UTILITIES=$(SUPPORT)/utilities/master
```

Create a `fsm.dbd` file, which contains the following:
```
registrar(fsmRegistrar)
```
Make sure that your `.dbd` file has a different name to the IOC `.dbd` file. Otherwise, your IOC `.dbd` file will be overwritten.

Edit the `Makefile` in this folder, to reference your new `.dbd` and `.st` files and add the libraries needed for them.
```
TOP=..
include $(TOP)/configure/CONFIG
#=======================================

# Install .dbd and .db files
DATA += devHFMAGPSU.proto
DBD += fsm.dbd

# Sequence file
HFMAGPSU_SRCS += fsm.st
LIBRARY_IOC = HFMAGPSU
HFMAGPSU_LIBS += seq pv
HFMAGPSU_LIBS += $(EPICS_BASE_IOC_LIBS)

#=======================================
include $(TOP)/configure/RULES
```

Be sure to include the library location for seq in the support `RELEASE` file.
```
# Macros required for basic ioc/stream device
SNCSEQ=$(SUPPORT)/seq/master
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

Enter the IOC source folder (e.g. ``HFMAGPSU-IOC-01App\src``)

Edit `build.mak` to ensure the needed libraries are included:
```
# Add all the support libraries needed by this IOC
## ISIS standard libraries ##

$(APPNAME)_LIBS += seq pv
```
### Notes

Whenever you make an edit  to the `fsm.st` file, rebuild the support module:
```
cd …EPICS\support\HFMAGPSU\master
make
```

## Passing macros into the sequencer

You can pass macros into your sequencer by including them in brackets after you define the program. E.g.

```
program keithley_2001 ("P, channels")
```

Here `P` and `channels` are passed as macros to the state machine. You pass these to the state machine in the `st.cmd` file when calling the state machine. E.g.

```
seq keithley_2001, "P=$(MYPVPREFIX)$(IOCNAME):, channels=10"
```

To access these macros in your state machine, create a variable to hold your macro, e.g. `char *P` for the macro `P`, and call `macValueGet` on your macro, e.g. `P =  macValueGet("P")`, within your state machine to allow you to use the macro "P" within your code as the variable "P".

Note that the macros you pass into the state machine **must** match up with those in your `.db` files. Otherwise your state machine will not be able to assign variables to PVs and the state machine won't run.

## Using `epicsThreadSleep`

From https://www-csr.bessy.de/control/SoftDist/sequencer/Tutorial.html#common-pitfalls-and-misconceptions

*If your action statements have any sort of polling loops or calls to `epicsThreadSleep` you should reconsider your design. The presence of such operations is a strong indication that you’re not using the sequencer as intended.*

Long sleeps will hang the thread and then other things may happen. An example was an SNL program to check that a setpoint had been actioned by waiting 30 seconds and then comparing setpoint and readback. While it was waiting, the setpoint may change again, and the wait is now redundant, and if it doesn't check for a change in original setpoint it may do the wrong thing. Using delay() is better as that does not block the thread and allows other checks in the state to continue.     
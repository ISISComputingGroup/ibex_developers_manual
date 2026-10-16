# ZOOM Polariser, Guide and Collimator

## Introduction

This is a single-axis Galil-controlled device that has 3 pre-defined stop positions.

## Setup

To set up the PGC, complete the following steps:

### Create the Galil axis configuration

Go to `C:\Instrument\Settings\Config\NDX[DEVICE_NAME]\configurations\galil` and create a file called `motionsetpoints.cmd` if one doesn't already exist. Add the following:

```
$(IFDMC01) epicsEnvSet "LOOKUPFILE2" "$(ICPCONFIGROOT)/motionSetPoints/pgc.txt"
$(IFDMC01) motionSetPointsConfigure("LOOKUPFILE2","LOOKUPFILE2")
$(IFDMC01) dbLoadRecords("$(MOTIONSETPOINTS)/db/motionSetPoints.db","P=$(MYPVPREFIX)LKUP:PGC:,TARGET_PV1=$(MYPVPREFIX)MOT:MTR0102,TARGET_RBV1=$(MYPVPREFIX)MOT:MTR0102.RBV,TARGET_DONE=$(MYPVPREFIX)MOT:MTR0102.DMOV,TOL=1,LOOKUP=LOOKUPFILE2")

```

**Don't forget to add a new line at the end of the final or the final line won't be read**

Note that there are several points of customisation here:
    1. The `01` in `IFDMC01` refers to the Galil number. If you are using IOC `GALIL_02` then this should instead be `IFDMC02`
    1. References to `MTR0102` should point to the motor you wish to use. If, for instance, you are using `GALIL_06`, axis 3, this should be `MTR0603`. Be careful to replace all the references, there are 3.
    1. Make sure that the lookup file, `LOOKUPFILE2` is unique in this file. You might have to use a difference name if `LOOKUPFILE2` is already taken. So long as the name is consistent, it will work.

### Set up the motion set points
Create a file called `C:\Instrument\Settings\Config\NDX[DEVICE_NAME]\configurations\motionSetPoints\pgc.txt`. You may have to create the directory as well if it doesn't exist already. Add the following:

```
Polariser -2
Guide 0
Collimator 2
```

There are several points of customisation:

1. The names provide a guide to which position corresponds to which component. You can name these however you like and will be used to populate the buttons in the OPI.
1. The second column is for the motor positions corresponding to each component. These will have to be set corresponding to the device setup.

### Set up the OPI

Open a PGC OPI as normal either via a synoptic of the devices screen. Typical value for the macros are

1. `PGC`: `PGC`. This will only be different if you've changed the prefix in `motionsetpoints.cmd`. That is not recommended.
1. `MM`: `MOT:MTR0102`. This corresponds to the motor record being used for the PGC and, combined with the `MOT` prefix, will correspond to the value you used when setting up `motionsetpoints.cmd`
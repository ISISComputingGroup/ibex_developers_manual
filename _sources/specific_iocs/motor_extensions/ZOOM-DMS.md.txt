# ZOOM Detector motion system

## Setup

In your config folder, set up a file `NDWxxxx\configurations\galil\axes.cmd` with the following content:

```
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=DISK:BEAMSTOP1:X,mAXIS=MTR0101")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=DISK:BEAMSTOP1:Y,mAXIS=MTR0102")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=DISK:BEAMSTOP2:X,mAXIS=MTR0103")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=DISK:BEAMSTOP2:Y,mAXIS=MTR0104")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STRIP:BEAMSTOP,mAXIS=MTR0105")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=DETECTORS,mAXIS=MTR0106")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=BAFFLE,mAXIS=MTR0107")
```

This allows us to create "aliases" for the DMS axes. It assumes we are using IOC `GALIL_01`. If using `GALIL_0n`, change `IFDMC01` to `IFDMC0n` and `MTR010m` to `MTR0n0m` (i.e. `MTR0101` becomes `MTR0201` for `n=2`). Unless otherwise stated, we'll assume we're working with `GALIL_01`.

**Don't forget the new line at the end of the file or the final line will not be processed and the Baffle will appear disconnected.**

Start `GALIL_01`. Don't forget to set the appropriate macros.

Create a synoptic with component `detector motion system`, no synoptic macros are required.
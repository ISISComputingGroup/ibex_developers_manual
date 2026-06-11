# ZOOM Sample Stack

The sample stack is set up on zoom using an `axes.cmd` file. The file should be in `Instrument/Settings/config/NDWxxxx/configurations/galil/axes.cmd`

An example of an `axes.cmd` file is given below:
```
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:X,mAXIS=MTR0101")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:Y,mAXIS=MTR0102")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:ZHI,mAXIS=MTR0103")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:THETA,mAXIS=MTR0104")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:PSI,mAXIS=MTR0105")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:CHI,mAXIS=MTR0106")
$(IFDMC01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:ZLO,mAXIS=MTR0107")
$(IFDMC02) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:XRAIL,mAXIS=MTR0201")
$(IFDMC02) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:YRAIL,mAXIS=MTR0202")
```
This will set up the first 7 motors on one GALIL controller, and the last two motors (which relate to movement along/perpendicular to a set of rails) on another GALIL controller. Depending on the final setup, these values will need to be adjusted so that each PV points at the correct controller.

NOTE: `STACK:XRAIL` is not actually a galil controller, but a Beckhoff motor controller. From IBEX's perspective, this is a read only device (a separate, independent system will be used to set the values). 
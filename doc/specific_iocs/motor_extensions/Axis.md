# Axis

Axis records add a layer of indirection between the user and the low level motor. This means if the underlying motor needs to change it only need to change in one place, all blocks, motion set points etc use this axis and so don't need to change.

The record is setup in the configuration directory in the motor directory in a file called axes.cmd (e.g. for galil it would by `galil/axes.cmd` for SM300 it would be `SM300_01/axes.cmd` (NB Galil are not based on the IOC number so you need an extra macro to make sure you only add the axis to the correct galil).

An example of adding an axis to a galil is:

```
$(IFIOC_GALIL_01) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=MOT:APERTURE,mAXIS=MTR0101")
```

More examples can be found motion [set points directory](https://github.com/ISISComputingGroup/EPICS-motionSetPoints/tree/master/settings).

The parameters needed are:

* `P` - prefix of the axis
* `AXIS` - name of the axis
* `mAXIS` - underlying motor from the table of motors

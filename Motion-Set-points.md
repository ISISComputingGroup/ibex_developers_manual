Motion set points allow you to label set positions for a motor, current either 1 axis or 2 axes. The code for this is in support in the directory [motionSetPoints](https://github.com/ISISComputingGroup/EPICS-motionSetPoints). The configuration for a motion set point is in to parts:

1. St file called `motionsetpoints.cmd` which sets up the db file which is stored in the configuration under the motor name:
    - galil is `Settings\config\<host name>\configurations\galil`
    - mcleanan is `Settings\config\<host name>\configurations\mcleanan`
    - sm300 is `Settings\config\<host name>\configurations\<sm300 ioc name e.g. SM300_01>`
1. The positions which are referenced from the st file. are stoed in  `Settings\config\<host name>\configurations\motionSetPoints`

The  `motionsetpoints.cmd` contains the following lines:

* motion setpoint config:
    `epicsEnvSet "LOOKUPFILE<X>" "$(ICPCONFIGROOT)/motionSetPoints/<motion setpoint file>"`
    `motionSetPointsConfigure("LOOKUPFILE<X>","LOOKUPFILE<X>")`
* *For 1D setpoint not using an axis macros* `dbLoadRecords("$(MOTIONSETPOINTS)/db/motionSetPoints.db","P=<motion set point prefix>,TARGET_PV1=<motor prefix>,TARGET_RBV1=<motor prefix>.RBV,TARGET_DONE=<motor prefix>.DMOV,TOL=<tolerance>,LOOKUP=LOOKUPFILE<X>")`
* *For 2D setpoint not using an axis macro* `dbLoadRecords("$(MOTIONSETPOINTS)/db/motionSetPoints.db","P=<motion set point prefix>,TARGET_PV1=<motor prefix>,TARGET_RBV1=<motor prefix>.RBV,TARGET_PV2=<motor prefix2>,TARGET_RBV2=<motor prefix2>.RBV,TARGET_DONE=<motor prefix>.DMOV,TARGET_DONE2=<motor prefix2>.DMOV,TOL=<tolerance>,LOOKUP=LOOKUPFILE<X>")`
* *For 1D setpoints using an axis* `dbLoadRecords("$(MOTIONSETPOINTS)/db/motionSetPoints.db","P=<motion set point prefix>,NAME1=<name1>,AXIS1=<axis1>,TOL=<tolerance>,LOOKUP=LOOKUPFILE<X>)`
* *For 2D setpoints using axes* `dbLoadRecords("$(MOTIONSETPOINTS)/db/motionSetPoints.db","P=<motion set point prefix>,NAME1=<name1>,AXIS1=<axis1>,NAME2=<name2>,AXIS2=<axis2>,TOL=<tolerance>,LOOKUP=LOOKUPFILE<X>)`
Where:
    * `X` - enumeration of lookup files, e.g. 1, 2
    * `motion setpoint file` - the lookup motion setpoint file
    * `motion set point prefix` - the prefix you want for the motion setpoint, e.g. `$(MYPVPREFIX)LKUP:MON3:`, `$(MYPVPREFIX)LKUP:SAMPLE`, `$(MYPVPREFIX)LKUP:ANALYSER`
    * `motor prefix` - the prefix of the first/only motor e.g. $(MYPVPREFIX)MOT:MTR0601
    * `motor prefix2` -the prefix of the second motor e.g. `$(MYPVPREFIX)MOT:MTR0601`, `$(MYPVPREFIX)MOT:ANALYSER:THETA` 
    * `tolerance` - tolerance with which the position has to comply with the positions in the lookup file
    * `axis1` - the axis to use for the first/only motor e.g. `$(MYPVPREFIX)MOT:SAMPLE:LIN`
    * `name1` -  the name of axis 1, defaults to `axis1` e.g. linear
    * `axis2` - the axis to use for the second motor e.g. `$(MYPVPREFIX)MOT:SAMPLE:ROT`
    * `name2` -  the name of axis 2, defaults to `axis2` e.g. rotational

For examples see Larmor, Demo or SANDALS.

The lookup motion setpoint file has the following format:

    # Commnet, lines starting with hashes are comments
    <label> <coord 1> <coord 2>
    <label> <coord 1> <coord 2>
    ...
    <label> <coord 1> <coord 2>

Field are seperated by spaces. The fields are:

    - `label` is the text label for the setpoint
    - `coord 1` is the set point for the first/only motor
    - `coord 2` is the set point of the second motor (or not included if it is 1D set point)

Often these files are calculated from xml files using the sample changer support module.

# OPI

If you want to see the monitor point on a synoptic. Create a synoptic with a component of type "movingmonitor" with the component target name of "In Out Monitor". To use monitor 3 which is currently set up for motor MTR0601 the macros should be set to:
* M = 3
* CHANNUM = ? (I set it to 3)
* MM = MOT:MTR0601
(check the `motionsetpoints.cmd` file to see what corresponds to what)

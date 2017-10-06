The PI rotation stage is run over serial from a MOXA and should be as simple as just plugging it in. After a power on, the first thing you must do is HOME the device. The IOC to run is called PIMOT_01 and the following macros need to be specified in either the configuration or globals.txt  

```
PORT1 # COM port to use
MTRCTRL # motor controller number for the motor record
```

For ENGINX I have used globals.txt and set:

```
PIMOT_01__PORT1=COM22
PIMOT_01__MTRCTRL=11
```

So the stage was on port 2 of the MOXA in the counting house, and on EPICS would show as MTR1101 in the table of motors. The PORT number will need changing when it moves into the blockhouse, but everything else should be OK. 

 
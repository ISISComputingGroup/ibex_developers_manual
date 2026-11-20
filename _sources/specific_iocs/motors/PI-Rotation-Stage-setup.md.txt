# PI Rotation Stage

The PI rotation stage is run over serial from a MOXA and should be as simple as just plugging it in. After a power on, **the first thing you must do is HOME the device**. The IOC to run is called PIMOT_01 and the following macros need to be specified in either the configuration or globals.txt  

```
PORT # COM port to use
MTRCTRL # motor controller number for the motor record
```

For ENGINX I have used globals.txt and set:

```
PIMOT_01__PORT=COM22
PIMOT_01__MTRCTRL=11
```

So the stage was on COM22 (which was physical port 2 of the MOXA in the counting house), and on EPICS would show as MTR1101 in the table of motors. The PORT number will need changing when it moves into the blockhouse, but everything else should be OK. 

If you have trouble communicating, see the `README_baud.txt` document in the `EPICS/ioc/PIMOT` directory for how to check the dip switch settings. We normally use 38400 baud, I've only ever had problems with 115200 but if there was a particularly long run to the MOXA you might need to drop this below 38400 I guess.

The is a macro called `BAUD` that defaults to 38400, so you only need to set the `BAUD` macro if you are using a different speed. 
 
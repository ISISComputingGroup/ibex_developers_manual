> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Galil](Galil)

The galil motors can be configured to run one of the multiple homing routines. These routines are documented in the [readme of the galil repository](https://github.com/ISISComputingGroup/EPICS-galil/tree/master/GalilSup/Db); there is extra documentation on the [oscillating collimator page for those routines](MERLIN,-LET-and-WISH-Oscillating-radial-collimators).

The whole consideration for the routine has to include the default header and footer for the Galil, with the following basic structure:
Header
Home routine for axis A
Home routine for axis B
Home routine for axis C
Home routine for axis D
Home routine for axis E
Home routine for axis F
Home routine for axis G
Home routine for axis H
Footer

Typically we then append any other code for specific functions we need after the footer, see [the Galil page](Galil) for more information.

The loading of the homing routines uses a macro to define the axis based on the location in the start controller setup (see [Galil](Galil) for more detailed information), for brevity and ease of reading this will be replaced by X throughout the descriptions below. 

Further command docs can be found in the share manuals in manc2xxx.pdf

### Variables

There are a number of variables used within these routines.


| Variable Name | Variable Purpose |
| --- | --- |
| `homeX` | Indicates that a home has been requested (1) |
| `hjogX` | Indicates which step of the homing routine is to be completed next |
| `inhomeX` | Indicates that the axis is in the process of homing | 
| `slimflX` | Soft limit in the forward direction set for general motor use, used as an interim holder whilst homing |
| `slimblX` | Soft limit in the reverse direction set for general motor use, used as an interim holder whilst homing |
| `mlock` | ? |
| `dpon` | ? |
| `dvalues` | ? |
| `homedX` | This is set to 1 before being returned as a message |


### Header

This relates to `galil_Default_Header.gmc` as that relates to the home routines, and does the same task for each axis.
Set `homeX = 0`, `hjogX = 0`, and `inhomeX = 0`

### Home routine structure for axis X

The basic structure of a homing routine is as follows:

```
If a home has been requested (homeX = 1)
   Indicate that we are in a homing routine (inhomeX = 1)
   If a home has been requested (homeX = 1) and we have not yet started the homing steps (hjogX = 0)
      Store the soft limits in the variables slimflX and slimblX
      Set the soft limits to their maximum values
      Indicate that we can go to step 1 of the homing routine (hjogX = 1)
   If both limits are active and a home has been requested (homeX = 1)
      Clear the home request (homeX = 0), send a message to the remote system
   If we are about to start the homing routine (hjogX = 1) AND the motor is in motion AND a home has been requested (homeX = 1)
      Stop the motor
   Undertake appropriate homing steps
   If we have completed all the homing steps (hjogX = number of steps in homing routine + 1) AND the motor isn't moving AND a home has been requested    (homeX = 1) AND in certain cases that the reason for the motor stop is the appropriate value
      Indicate that we are have reached the end of the homing steps (hjogX = 0)
      Clear the home request (homeX = 0), send a message to the remote system
      Set the homedX varirable to 1, send a message to the remote system
Else
   Indicate that we are have reached the end of the homing steps (hjogX = 0)
If the home request has been cleared (homeX = 0) AND we have not completed the homing routine (inhomeX = 1)
   Revert the soft limits to their original values
   Indicate that we have finished the homing routine (inhomeX = 0)
If the variable mlock = 0
   Set the interrupt masks to dpon and dvalues
```

The code to use is as follows, be sure to change the items in square brackets as appropriate, and consider the need or not for a stop code check:
```
NO*****************AXIS ${AXIS}********************
NO*********HOME - [Homing routine title]************
[NO*********Describe homing routine steps if not obvious**********]
#HOME${AXIS}
IF (home${AXIS}=1)
        inhome${AXIS}=1
	IF ((home${AXIS}=1) & (hjog${AXIS}=0))
	    slimfl${AXIS}=_FL${AXIS};FL${AXIS}=2147483647
		slimbl${AXIS}=_BL${AXIS};BL${AXIS}=-2147483648
		hjog${AXIS}=1
	ENDIF
	IF ((_LR${AXIS}=0) & (_LF${AXIS}=0) & (home${AXIS}=1))
		home${AXIS}=0;MG "home${AXIS}", home${AXIS};ENDIF
	IF ((hjog${AXIS}=1) & (_BG${AXIS}=1) & (home${AXIS}=1))
		ST${AXIS};ENDIF
        [Undertake the appropriate homing steps]
	IF ((hjog${AXIS}=[number of homing steps + 1]) & (_BG${AXIS}=0) & (home${AXIS}=1) [& (_SC${AXIS}=10)])
		hjog${AXIS}=0;home${AXIS}=0;homed${AXIS}=1
		MG "home${AXIS}", home${AXIS};MG "homed${AXIS}", homed${AXIS}
	ENDIF
ELSE
	hjog${AXIS}=0
ENDIF
IF ((home${AXIS}=0) & (inhome${AXIS}=1))
    FL${AXIS}=slimfl${AXIS}
	BL${AXIS}=slimbl${AXIS}
	inhome${AXIS}=0
ENDIF
IF (mlock=1)
	II ,,dpon,dvalues
ENDIF
```

### Home routine steps

So for homing step n you would need to follow this basic pattern in the code and update as appropriate, be sure to change the items in square brackets as appropriate, and consider the need or not for a stop code check:

```
IF ((hjog${AXIS} = n) & (_BG${AXIS}=0) & (home${AXIS}=1) [& (_SC${AXIS}=[value])])
   [Homing Routine Step]
   hjog${AXIS} = n + 1
ENDIF
```

The existing steps are detailed in [Galil Homing Routine Steps](Galil-Homing-Routine-Steps)

### The Home No Home routine

This is a variation on the above, as it does not include the standard items relating to the soft limits or stopping the motor
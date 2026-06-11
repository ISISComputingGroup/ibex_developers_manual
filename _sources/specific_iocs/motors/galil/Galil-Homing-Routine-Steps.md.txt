# Galil Homing Routine steps

A number of steps are already available for homing Galils and these are used in various routines. Below is the code to use, so ${AXIS} refers to the macro for the axis, and n will indicate the step number.
There are a number of variables used whose source is not detailed here.

## Do nothing

This isn't quite nothing, it waits 100 ms

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (home${AXIS}=1))
	WT100;hjog${AXIS}=n+1
ENDIF
```

## Find Index

If `hjog${AXIS} = 1` then the stop code check at the end can be omitted, and the speed multiplier (`sm`) should be greater as this would be the first move to the index, e.g. use 1 for the initial index find and 0.1 for the detailed index find
If the index is behind your current location then the speed multiplier (`sm`) should be negative, otherwise, it is positive.

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (home${AXIS}=1) & (_SC${AXIS}=1))
	DC${AXIS}=(@ABS[hjgdc${AXIS}])
	JG${AXIS}=((@ABS[hjgsp${AXIS}])*sm)
	FI${AXIS};SH${AXIS};WT100;BG${AXIS};hjog${AXIS}=n+1
ENDIF
```

## Move to a relative position

If coming off an index, the relative position value (`rp`) should be the same sign as the last move

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (home${AXIS}=1) & (_SC${AXIS}=10))
	DC${AXIS}=(@ABS[hjgdc${AXIS}])
	PR${AXIS}=((@ABS[hjgsp${AXIS}])*rp)
	SH${AXIS};WT100;BG${AXIS};hjog${AXIS}=n+1
ENDIF
```

## Jog on to a limit

The limit in use will need to be specified (`frl`)
The speed and direction will depend on the limit being moved towards and the stage in the routine (`sm`)
The limit switch behaviours should stop the motor, but the interim state should be used to simplify execution

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (_Lfrl${AXIS}=0) & (home${AXIS}=1))
	DC${AXIS}=@ABS[hjgdc${AXIS}]
	JG${AXIS}=@ABS[hjgsp${AXIS}]*sm
	SH${AXIS};WT50;BG${AXIS};hjog${AXIS}=n+1
ENDIF
```

## Jog off a limit

The limit in use will need to be specified (`frl`)
The speed and direction will depend on the limit being moved towards and the stage in the routine (`sm`)
This is really two steps, but coming off the limit always requires a reaction once the limit is no longer engaged

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (_Lfrl${AXIS}=0) & (home${AXIS}=1))
	DC${AXIS}=@ABS[hjgdc${AXIS}]
	JG${AXIS}=@ABS[hjgsp${AXIS}]*sm
	SH${AXIS};WT50;BG${AXIS};hjog${AXIS}=n+1
ENDIF
IF ((hjog${AXIS}=n+1) & (_BG${AXIS}=1) & (_LF${AXIS}=1) & (home${AXIS}=1))
	ST${AXIS}
	hjog${AXIS}=n+2
ENDIF
```

## Go to the home position

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (home${AXIS}=1))
	DC${AXIS}=(@ABS[hjgdc${AXIS}])
	SP${AXIS}=(@ABS[hjgsp${AXIS}])
	HM${AXIS};SH${AXIS};WT100;BG${AXIS};hjog${AXIS}=n+1
ENDIF
```

## Find the edge of a transition

```
IF ((hjog${AXIS}=n) & (_BG${AXIS}=0) & (home${AXIS}=1))
	DC${AXIS}=(@ABS[hjgdc${AXIS}])
	SP${AXIS}=(@ABS[hjgsp${AXIS}])
	FE${AXIS};SH${AXIS};WT100;BG${AXIS};hjog${AXIS}=n+2
ENDIF
```
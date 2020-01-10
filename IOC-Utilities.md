> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > IOC utilities

The utilities comprise of useful IOC db templates and IOC shell utilities.

## DB Templates

Below are available utility templates for [substitution](Template-Substitutions). In order to allow Make to build these, you need to add the following to your `Device/master/configure/RELEASE` file: `UTILITIES=$(SUPPORT)/utilities/master`.

### Field setter
This copies the specified field from a PV and sets it on a different PV. E.g.

    file $(UTILITIES)/db/field_setter.template { 
      pattern 
        {P,    FROM, TO, FIELD}
    
        {"\$(P)", "UNITS", "READING", "EGU"}
        {"\$(P)", "UNITS", "SP", "EGU"}
	
    }

This example copies the `EGU` field from `$(P)READING` to `$(P)UNITS.EGU` and `$(P)SP.EGU`.

### Unit setter

This copies units from a PV and sets them on a different PV. E.g.

    file $(UTILITIES)/db/unit_setter.template { 
      pattern 
        {P,    FROM, TO}
    
        {"\$(P)", "UNITS", "READING"}
        {"\$(P)", "UNITS", "SP"}
	
    }

This will copy units from the value of the PV `$(P)UNITS` to `$(P)READING` and `$(P)SP`.

### Error Setting

Creates a raw PV that can be written to by a stream protocol and then transfer the stream protocols PV error and value to the real PV.

For example:

    file $(UTILITIES)/db/error_setter.template {
        pattern {P, STREAM_PV, PV_NAME}
    
        {"\$(P)", "FREQ:REF", "FREQ:SP:RBV"}
        {"\$(P)", "FREQ:REF", "FREQ"}

    }

In this example, the PV `FREQ:REF` reads the values from a status and then set the values, via the protocol file, in the `FREQ:SP:RBV:RAW.A` PV. This value and any error that occurs in the `FREQ:REF` is then set on the `FREQ:SP:RBV` PV. This allows you to easily show a disconnected error in PVs that are set from the protocol file.

If you need to use the error setter for PVs that are defined in a .db file instead of .template file, the .substitutions file for that .db file needs to have a different name than the .db file, otherwise the error setter will not work.

### Calibration Range

Calculates the maximum and minimum values of a selected calibration file. You can load this db with macros using 
```
dbLoadRecords("$(UTILITIES)/db/calibration_range.db","P=$(P),BDIR=TEMP.BDIR,TDIR=TEMP.TDIR,SPEC=TEMP.SPEC,HIGH_PV=TEMP:RANGE:OVER.B,LOW_PV=TEMP:RANGE:UNDER.B")
```
Where `TEMP` is a `cvt` record which uses the calibration file. The max value is outputted to `HIGH_PV` and the minimum to `LOW_PV`.

### check stability

This is a generic utility for verifying that a value has been within tolerance of a setpoint and without any invalid alarms for N samples.

The implementation is defined in `$(UTILITIES)/db/check_stability.db`.

First load the DB records, e.g. 

```
dbLoadRecords("$(UTILITIES)/db/check_stability.db", "P=$(MYPVPREFIX)$(IOCNAME):,INP_VAL=$(MYPVPREFIX)$(IOCNAME):FIELD,SP=$(MYPVPREFIX)$(IOCNAME):FIELD:SP:RBV,NSAMP=5,TOLERANCE=$(TOLERANCE=0)")
```

And then, from an existing DB, forward link to `$(P)STAB:SCANNOW` when it should take new samples (e.g. Forward-link from the readback PV).

Whether the value is stable or not is then published in `$(P)STAB:IS_STABLE` - 1 if stable, 0 otherwise.

## Shell Utilities

There are some IOC shell utilities defined in `C:\Instrument\Apps\EPICS\support\utilities` which can be used in an IOC shell to help startup IOCs. The doxygen docs are here http://epics.isis.rl.ac.uk/doxygen/main/support/utilities/.

### Pausing an IOC at startup

You can pause an IOC at startup in the st.cmd using `msgBox`. This is imported in `IOC_NAME_registerRecordDeviceDriver pdbbase` so must come after that line. 

Usage: `msgBox "title" "text"`. Bring up a message box at the point in your startup that it is placed and pause the boot until you click the button.

This could be useful if you want to run a debugger on the IOC, which you attach whilst the IOC boot is paused.

## calc

Performs an arithmetic operation on an expression and return the integer value to a specific environment variable:

`calc("ENV1","1+1",1,2)`

The arguments are as follows:

1. The output environment variable
2. The expression to be evaluated
3. Options
4. The output length

My best guess is that the expression is evaluated using the `calcPerform` method from the EPICS standard library so the expression should match the syntax as used in a calc record.

The options are detailed in `ioccalc.cpp` in the utilities directory.

Examples can be seen in the Galil and McLennan motor records.

## dcalc

As calc, but returns a double value. The 4th argument is for the number of decimal places, not the value length.

`dcalc("ENV1","0.1*0.2",1,2)`

An example can be seen in the Eurotherm IOC, file `st-timing.cmd`.

## stringtest

TODO

## `stringiftest(resultvar, lhs, operation, rhs)`

Defines an environment variables as empty or a comment depending on if lhs is empty. The variables defined are:
- `IF<resultsvar>` '#' if empty; otherwise ' ' 
- `IFNOT<resultsvar>` ' ' if empty; otherwise '#'

parameters

1. `resultvar` - the basename of the environment variable to set
1. `lhs` - the string to test
1. `operation` - set the first bit for verbose mode
1. `rhs` - used in `lhs==rhs` opertion

The operation argument is given as a decimal representation of binary flags:

| Operation       | Flag  |
|:---------------:|:-----:|
| Verbose         | `0x1` |
| length > 0      | `0x2` (default) |
| lhs == rhs      | `0x4` |
| Inverse output  | `0x8` |

To get the operation that you require, add the flag value in decimal. For example, to check if a string has finite length, your operation would be `2`. However, if you would like your flag to check if a string has a zero length, then add the inverse flag value `8`, meaning your operation would be `10 (8+2)`. To add a log for this operation, add the verbose flag of value `1`, so the total value is `11`.

For debugging purposes it is advisable to add the verbose/logging flag of value `1` to your operation.

### Example 
From the DKFPS IOC:
```
stringiftest("POLAR" "$(POLARITY="BIPOLAR")" 5 "BIPOLAR")
```
The operation value is `5`, or `4+1`, so this checks the lhs (`$(POLARITY)`, which defaults to `"BIPOLAR"`) equals the right hand side `"BIPOLAR"`, and puts the result in the `$(POLAR)`.

## setIOCName

TODO

## getIOCName

TODO

## getIOCGroup

TODO

## mkdir

TODO
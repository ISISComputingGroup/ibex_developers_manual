> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > IOC utilities

The utilities comprise of useful IOC db templates and IOC shell utilities.

## DB Templates

Below are available utility templates for [substitution](Template-Substitutions).

### Unit Setter

This copies units from a pv and sets them on a different pv. E.g.

    file $(UTILITIES)/db/unit_setter.template { 
      pattern 
        {P,    FROM, TO}
    
        {"\$(P)", "UNITS", "READING"}
        {"\$(P)", "UNITS", "SP"}
	
    }

This will copy units from the value of the pv `$(P)UNITS` to `$(P)READING` and `$(P)SP`.

### Error Setting

Creates a raw pv that can be written to by a stream protocol and then transfer the stream protocols pv error and value to the real pv.

For example:

    file $(UTILITIES)/db/error_setter.template {
        pattern {P, STREAM_PV, PV_NAME}
    
        {"\$(P)", "FREQ:REF", "FREQ:SP:RBV"}
        {"\$(P)", "FREQ:REF", "FREQ"}

    }

In this example the PV `FREQ:REF` reads the values from a status and then set the values, via the protocol file, in the `FREQ:SP:RBV:RAW.A` pv. This value and any error that occurs in the `FREQ:REF` is then set on the `FREQ:SP:RBV` pv. This allows you to easily show a disconnected error in PVs that are set from the protocol file.

## Shell Utilities

There are a number of IOC shell utilities defined in `C:\Instrument\Apps\EPICS\support\utilities` which can be used in an IOC shell to help startup IOCs. The doxygen docs are here http://epics.isis.rl.ac.uk/doxygen/main/support/utilities/.

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
1. `rhs` - does nothing

The operation argument is given as a decimal representation of binary flags:

| Operation       | Flag  |
|:---------------:|:-----:|
| Verbose         | `0x1` |
| length > 0      | `0x2` |
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
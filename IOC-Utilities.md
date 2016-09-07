> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > IOC utilities

There are a number of IOC shell utilities defined in `C:\Instrument\Apps\EPICS\support\utilities` which can be used in an IOC shell to help startup IOCs.

## calc

Performs an arithmetic operation on an expression and return the value to a specific environment variable:

`calc("ENV1","1+1",1,2)`

The arguments are as follows:

1. The output environment variable
2. The expression to be evaluated
3. Options
4. The output length

My best guess is that the expression is evaluated using the `calcPerform` method from the EPICS standard library so the expression should match the syntax as used in a calc record.

The options are detailed in `ioccalc.cpp` in the utilities directory.

Examples can be seen in the Galil and McLennan motor records.

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

## setIOCName

TODO

## getIOCName

TODO

## getIOCGroup

TODO

## mkdir

TODO
There are a number of IOC shell utilities defined in `C:\Instrument\Apps\EPICS\support\utilities` which can be used in an IOC shell to help startup IOCs.

## calc

TODO 

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
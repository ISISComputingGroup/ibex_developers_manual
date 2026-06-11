# LabVIEW Remote

IOC to allow remote connection LabVIEW VI's via ISIS Remote LabVIEW services.

## Templates
There are pre-existing templates that can be implemented via substitution files for doubles, buttons, strings, and enums.
Once a DB file has been generated, create a file called `st-<device>.cmd` in the devices folder of the ioc that loads the db, and set the `DEVCMD1` macro to the name of this file to load it.

## Ports
This IOC requires two ports for full functionality, if you are only interacting with string values then it only requires TCP port 64008. if it only uses binary (i.e. doubles or booleans) then it only requires 64009, Enums and combinations of both require both ports be opened however.


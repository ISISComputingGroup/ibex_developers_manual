# ISIS modules for file handling

There are currently two ISIS modules that may help select and read files via PVs.

## FileList

This module will take a base directory and PCRE expression. It will return a compressed JSON list of the files that match the expression within that directory (non-recursively).

Currently, the constructor for the module must be given the starting PCRE and directory. This method was chosen, rather than defaults being set via PVs, as the directory must be set prior to the PCRE.

There are three FileList variables that can be connected to PVs:

- DIRBASE - Gives the base directory to search
- SEARCH - Gives the PCRE expression to search for
- JARR - Gives the JSON compressed list of valid files
To connect the list of files to an OPI there is a common script called UpdateFileList.py which should be attached to a combo control. For an example of this see the Kepco OPI.

There is also a db file for selecting calibration files for a record, which is used in the Eurotherm and the Kepco.

For examples of this modules use see the test IOC within the FileList folder or see the DAE IOC where this is used to select wiring, detector and spectra tables. 

## ReadASCII

This module has two main functions:
* Ramp a set point linearly from it's current value to a new one. This can be controlled through a ramp rate (in EGU/min) and a step rate (in steps/min)
* Change a selection of other PVs when a set point changes. This is done by opening a file at a given location and using the table within it to change PVs. The module uses one PV as a lookup on the first column of the table and subsequently changes other PVs to match the values in the other columns. 

These functions can be turned off and on independently but can be used in conjunction to ramp the lookup PV and change other PVs when it crosses a threshold of the table. Both functions are used in the Eurotherm IOC to change PID and MaxHeater values when the temperature SP is changed. The Kepco IOC only uses the ramping functionality.

To configure ReadASCII you must have the following in your `*.cmd`:
```
ReadASCIIConfigure(port_name, PID_folder, steps_per_minute, quiet_on_SP)
```
where:
* `port_name` is a string of the port name, used to refer to ReadASCII in the db
* `PID_folder` is the initial folder used to search for PID lookup files (can be blank if just using ramping)
* `steps_per_minute` is the number of steps the ramp will take per minute (note that the step size is dependant on the rate set at runtime)
* `quiet_on_SP` *optional* can be set to 1 to stop ReadASCII logging on every new set point. This can be useful if you think the set point may end up being changed rapidly e.g. the zero field controller. Defaults to 0 i.e. logging on every set point

### Behaviour
Upon startup, ReadASCII will use lookup file to create asynPortDriver parameters and associate them with
settings table values created also from lookup value.
IMPORTANT - for ReadASCII to work correctly, the column names (headers) in lookup file must match PV names from .db file.
For example given field(INP,  "@asyn($(READ),0,1)MH") the correct header in lookup file should be 'MH'.
.db file can be usually found in master/db folder, otherwise no PV will be read/written to.
ReadASCII has many checks written into it to prevent crashing if lookup file is incorrectly formatted or other unexpected situations occur and allows continued use without crashing, however there are currently no warnings displayed to the user - only errors printed in logs.

### Extending
It is possible to extend functionality of ReadASCII to use more parameters than currently used (1 setpoint and 4 values - P, I, D, Max).
If the lookup file contains more columns with proper header names then corresponding PVs will be written to using lookup value table.
There can be only one setpoint column however. Other parameters, such as LUTON (Check if reading lookup file is on) or RAMPON (Check if ramping is on) are currently hard-coded.
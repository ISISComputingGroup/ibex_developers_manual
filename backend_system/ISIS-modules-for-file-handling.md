> [Wiki](Home) > [The Backend System](The-Backend-System) > [Useful tools](Useful-tools) > ISIS modules for file handling

There are currently two ISIS modules that may help select and read files via PVs.

# FileList

This module will take a base directory and PCRE expression. It will return a compressed JSON list of the files that match the expression within that directory (non-recursively).

Currently, the constructor for the module must be given the starting PCRE and directory. This method was chosen, rather than defaults being set via PVs, as the directory must be set prior to the PCRE.

There are three FileList variables that can be connected to PVs:

- DIRBASE - Gives the base directory to search
- SEARCH - Gives the PCRE expression to search for
- JARR - Gives the JSON compressed list of valid files
To connect the list of files to an OPI there is a common script called UpdateFileList.py which should be attached to a combo control. For an example of this see the Kepco OPI.

There is also a db file for selecting calibration files for a record, which is used in the Eurotherm and the Kepco.

For examples of this modules use see the test IOC within the FileList folder or see the DAE IOC where this is used to select wiring, detector and spectra tables. 

# ReadASCII

This module has two main functions:
* Ramp a set point linearly from it's current value to a new one. This can be controlled through a ramp rate (in EGU/min) and a step rate (in steps/min)
* Change a selection of other PVs when a set point changes. This is done by opening a file at a given location and using the table within it to change PVs. The module uses one PV as a lookup on the first column of the table and subsequently changes other PVs to match the values in the other columns. 

These functions can be turned off and on independently but can be used in conjunction to ramp the lookup PV and change other PVs when it crosses a threshold of the table. Both functions are used in the Eurotherm IOC to change PID and MaxHeater values when the temperature SP is changed. The Kepco IOC only uses the ramping functionality.
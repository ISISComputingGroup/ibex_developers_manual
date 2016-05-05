There are currently two ISIS modules that may help select and read files via PVs.

#FileList

This module will take a base directory and PCRE expression. It will return a compressed JSON list of the files that match the expression within that directory (non-recursively).

Currently, the constructor for the module must be given the starting PCRE and directory. This method was chosen, rather than defaults being set via PVs, as the directory must be set prior to the PCRE.

There are three FileList variables that can be connected to PVs:

- DIRBASE - Gives the base directory to search
- SEARCH - Gives the PCRE expression to search for
- JARR - Gives the JSON compressed list of valid files
To connect the list of files to an OPI there is a common script called UpdateFileList.py which should be attached to a combo control. For an example of this see the Eurotherm OPI.

For examples of this modules use see the test IOC within the FileList folder or see the DAE IOC where this is used to select wiring, detector and spectra tables.

#ReadASCII

This module opens a file at a given location and uses the table within it to change PVs. The module uses one PV as a lookup on the first column of the table and subsequently changes other PVs to match the values in the other columns. The module can also be set to ramp the lookup PV and change other PVs when it crosses a threshold of the table.

This module is currently used specifically in the Eurotherm IOC to change PID and MaxHeater values when the temperature SP is changed.
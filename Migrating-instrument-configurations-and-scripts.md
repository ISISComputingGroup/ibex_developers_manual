# Migration

Under seci, configurations are stored as XML in the following location: `\\NDXxxxxxx\c$\Program Files (x86)\STFC ISIS Facility\SECI\Configurations`. You will need to log in using an admin password if you are accessing an instrument machine remotely.

Settings for individual devices are typically in the following location (example for a Eurotherm):
`\\NDXxxxxx\c$\LABVIEW MODULES\Drivers\Eurotherm` e.g. Baud rate, COM ports, etc.

Some devices have settings in `\\NDXxxxxx\c$\LABVIEW MODULES\Instrument`

GALILs are more complicated.

# Seci "automatic" blocks

SECI used to create an `_Status.txt` file for you "free of charge", it looks like a block but you didn't need to add it. All it contained was the run state. When migrating an instrument's configuration, check with the scientists if they need a block defined for the run state.

If so, point it at the `DAE:RUNSTATE_STR` process variable and add it as "monitor with deadband" rather than periodic change

# Where to find instrument scripts

First, it's best to ask instrument scientists which scripts they want migrated. Typically they will have built up lots of Open Genie scripts over the years, not all of which are still in use.

Scripts can generally be found in the following locations:

- `C:\scripts`
    - This will sometimes contain a symbolic link into a shared drive that may also contain scripts
- `C:\Users\[standard_user]\Documents\Configurations\COMMON\gcl\[instrument_name]_routines.gcl`

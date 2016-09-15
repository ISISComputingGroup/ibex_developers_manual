These are tests/checks that should be performed on the IBEX client after a release. They are split into those things that *must* be done and those that should be done (the only reason for not doing these is if the instrument scientists say it is ok not to perform these tests). These tests are things which are important for the running of the instrument and things which we have missed in previous releases which should not be missed again.

## Tests that must be done

### All Instruments

1. (After installing both the server and the client) Start the IBEX client. Connect to an instrument. Check Menu -> Help -> About. The client number should be the version you just released and should match that on the page (https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)
1. Make sure genie python works both from the GUI and when launched from the `genie_python.bat` shortcut under `C:/Instrument/Apps/Python` (e.g. try a `get_blocks()` command).

### LARMOR

1. None

### IMAT

1. None

## Tests that should be done

### All Instruments

1. 

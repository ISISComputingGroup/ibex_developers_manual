# Client release tests

These are tests/checks that should be performed on the IBEX client after a release. They are split into those things that *must* be done and those that should be done (the only reason for not doing these is if the instrument scientists say it is ok not to perform these tests). These tests are things which are important for the running of the instrument and things which we have missed in previous releases which should not be missed again.

## Tests that must be done

### All Instruments

1. (After installing both the server and the client) Start the IBEX client. Connect to an instrument. Check Menu -> Help -> About. The client number should be the version you just released and should match that on the page (https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)
1. Make sure genie python works both from the GUI and when launched from the `genie_python.bat` shortcut under `C:/Instrument/Apps/Python`
    1. Verify that no issues arise on starting a scripting window (e.g. `init_[INST]` is loaded correctly)
    1. Genie is available via the `g` prefix: try `g.get_blocks()`
    1. Instrument scripts are available via the `inst` prefix. **DO NOT** use one of the existing instrument scripts as it could trigger unwanted changes on the instrument. Create a test script in `C:\Instrument\Settings\config\NDX[INST]\Python\inst` and run that.
1. View the current config make sure it looks sensible.

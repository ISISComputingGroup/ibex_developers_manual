# Server Release Tests

These are tests/checks that should be performed on the IBEX server after a release. They are split into those things that *must* be done and those that should be done (the only reason for not doing these is if the instrument scientists say it is ok not to perform these tests). These are things which are important for the running of the instrument and things which we have missed in previous releases which should not be missed again.

## Tests that must be done

### All Instruments

1. Start an IBEX client. Connect to the instrument. Check Menu -> Help -> About. The Server number should be the version you just released and should match that on the page (https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)

1. Ensure that the configuration is being pushed. 
    1. go to settings directory in git bash (/c/Instrument/Settings/config/\<Instrument\>)
    1. `git fetch`
    1. `git status`
    1. Ensure that the message says `up-to-date with 'origin/<Instrument Name>'`.
1. Ensure that a block PV is being logged. Do this by right-clicking a PV (one which would be expected to change a little) and select `Display block history -> create a new plot`. There should be data on the plot from after the instrument was upgraded.
1. Confirm that the web dashboard is working for the specific instrument (http://dataweb.isis.rl.ac.uk/)

### Instruments which are having their first IBEX installation
1. Setup or find a block which is logging itself. Ensure that a log file with this block value in appears in `c:\data\*.log`. If this doesn't happen see [DAE troubleshooting](/specific_iocs/dae/DAE-Trouble-Shooting)

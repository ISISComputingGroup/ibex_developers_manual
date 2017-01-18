These are tests/checks that should be performed on the IBEX server after a release. They are split into those things that *must* be done and those that should be done (the only reason for not doing these is if the instrument scientists say it is ok not to perform these tests). These are things which are important for the running of the instrument and things which we have missed in previous releases which should not be missed again.

## Tests that must be done

### All Instruments

1. Start an IBEX client. Connect to the instrument. Check Menu -> Help -> About. The Server number should be the version you just released and should match that on the page (https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)
1. Setup or find a block which is logging itself. Ensure that a log file with this block value in appears in `c:\data\*.log`. If this doesn't happen see [DAE troubleshooting](DAE-Trouble-Shooting)
1. Ensure that the configuration is being pushd. 
    1. go to settings dir in git bash (/c/Instrument/Settings/config/<Instrument>)
    1. `git fetch`
    1. `git status`
    1. Ensure that the message says `up-to-date with 'origin/<Instrument Name>'`.

### LARMOR

1. None

### IMAT

1. None

## Tests that should be done

### All Instruments

1. Confirm that the web dashboard is working for the specific instrument (http://dataweb.isis.rl.ac.uk/)

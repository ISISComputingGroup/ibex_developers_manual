These are tests/checks that should be performed on the IBEX server after a release. They are split into those things that *must* be done and those that should be done (the only reason for not doing these is if the instrument scientists say it is ok not to perform these tests). These are things which are important for the running of the instrument and things which we have missed in previous releases which should not be missed again.

## Tests that must be done

### All Instruments

1. Start an IBEX client. Connect to the instrument. Check Menu -> Help -> About. The Server number should be the version you just released and should match that on the page (https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)
1. Setup or find a block which is logging itself. Ensure that a log file with this block value in appears in `c:\data\*.log`. If this doesn't happen see [DAE troubleshooting](DAE-Trouble-Shooting)

### LARMOR

1. Larmor has 3 mk3choppers, ensure that there are three Choppers enabled in the ioc/mk3chopper st.cmd file and that you can see three choppers connected in the GUI 

### IMAT

1. None

## Tests that should be done

### All Instruments

1. None

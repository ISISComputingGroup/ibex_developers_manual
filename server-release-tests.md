These are tests/checks that should be performed on the IBEX server after a release. They are split into those things that *must* be done and those that should be done (the only reason for not doing these is if the instrument scientists say it is ok not to perform these tests). These are things which are important for the running of the instrument and things which we have missed in previous releases which should not be missed again.

## Tests that must be done

### All Instruments

1. Start an IBEX client. Connect to the instrument. Check Menu -> Help -> About. The Server number should be the version you just released and should match that on the page (https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)

### LARMOR

1. Ensure that the Chopers are not commented out in the configuration file

### IMAT

1. None

## Tests that should be done

### All Instruments

1. 

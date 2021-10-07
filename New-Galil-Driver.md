# Galil driver selection during ibex install

during install/deploy you will be asked to select OLD or NEW galil driver, default is OLD for the moment but **Seek advice** if you are not sure what to select as we will be doing a phased testing schedule. If the instrument is not currently running the new driver then you probably want to select OLD unless testing is planned. Note that both drivers are installed, this choice is what to make the default one on ibex startup. When ibex is not running you can run
```
C:\Instrument\Apps\EPICS\swap_galil.bat OLD
```
from a command window to swap to the old driver, pass `NEW` as the argument to swap to the new driver instead.

To help with automatic Jenkins system testing `instrument_install_latest_build_only.bat` selects the NEW driver and does not prompt. 

## notes on new driver

The new galil driver has been merged to master, the old driver is currently on a galil-old branch of the EPICS-galil repository. The new driver does not build with VS2010, the old driver does not work if compiled with anything other than VS2010. As we have moved to VS2019 compilers, the new driver is now the default on master.

The new driver has not yet been tested fully on an ISIS beamline, though things have changed between the old and new versions changes have been added to make them (hopefully) compatible at the PV and autosave level, thus you should be able to swap between them without issue. The only incompatible changes are:
* the hardware home motor position must now be zero and a motor record offset used to have a non-zero user home value. We had planned to do this change on remaining instruments, we need to complete this work.
* motor on/off cannot use PREM/POST
see below for notes on these

Currently an EPICS_galil_old Jenkins job runs on ndhspare53, it builds the galil-old branch with vs2010, deploys this to kits$, and this then gets included in other builds giving you ioc/master/GALIL-OLD etc. A get_old_galil.bat script at top level lets a developer get these files. A swap_galil.bat script will swap between galil drivers on instrument or developer machine, it basically renames directories.

# Testing of new galil driver

## Testing galil-old via swap-galil 

* Record motor setup
* Shutdown ibex
* Update instrument
* Run Swap_galil to put on old driver
* Start ibex
* check positions etc. all look ok
* compare current autosave files with ones pre-upgrade.

## Testing galil-new via swap galil

* Record motor setup
* Shutdown ibex
* Run Swap_galil to put on new driver
* Start ibex
* check positions etc. all look ok
* compare current autosave files with ones pre-upgrade.
* Shutdown ibex
* Run Swap_galil to put back old driver
* Start ibex
* check positions etc. all look ok
* compare current autosave files with ones pre-upgrade.

in `ioc/master/GALIL` there is a file  `utils/SetupR3Axis.bat`  that will initialise the Galil in the ibex office with appropriate parameters so you can move it, run it after you have started the `ioc/master/GALIL` ioc (likely you will only need to run it once as things should then get autosaved locally and applied subsequently)
 
## Changes from previous driver

* turning motors on using the motor record PREM field no longer works (the on state is now tested before PREM is run). If you were using PREM/POST to turn on/off the motor during a move then set MTR0101_AUTOONOFF_CMD etc. to "On" (this has been adjusted in `SetupR3Axis.bat`). If PREM turned a motor on and it remained on (POST did not turn it off) then set MTR0101_ON_CMD instead.
* In the upstream code GalilStartController() has lost the "display code" argument, for compatibility we have added this back so we **do not** currently need to move the "Thread mask" argument (usually value "3" for us) one position earlier in your local settings/galil/galil*.cmd files. When we have completed the migration on all instruments we may revise this. 
* Home position is now always set to 0, so PVs like MTR0101_HOMEVAL_SP and MTR0101_PHOME_CMD have been removed. See [Resetting-HOMEVAL](Resetting-HOMEVAL)

## TODO (from earlier testing)

* Unsolicited messages are currently using UDP only, I need to look at adding TCP support
* Loading the Profile and kinematic axes DBs cause streams of errors (may now be fixed?) 
* Running GalilTest IOC from support/galil/master does not work (may not fix, not really needed)
  
## Test Strategy (Assuming testing on EMMA)

To confirm that the new driver works we will need to do the following.

## Before testing
- [x] Copy the autosave files
- [x] Note down all current motor positions (ideally in raw steps)

### General Tests

For comparison, use the old driver to take the following data on an axis:
- [x] Home the device  
- [x] Run it to the upper physical limit, measure how long this takes
- [x] Note the position of the upper limit
- [x] Re-home, measure how long this takes
- [x] Run to lower limit and note the lower limit position

Upon switching to new driver 
- [ ] Power cycle the galil **Not tried**
- [ ] Reapply the motor positions as previously noted 

Under the new driver:
- [x] Repeat the above, confirm the values are the same (to within 0.1 mm for distances and 1 second for time)
- [x] Confirm the GUI shows high and low limits engaged when the physical switches are activated
- [x] Home one of axes 1-4 and confirm it runs to forward limit then home. Confirm the GUI displays home
- [ ] Home axis 5 and confirm it runs straight to home. Confirm the GUI displays home **Home routine did nothing**
- [x] Home one of 7-8 and confirm nothing happens. Confirm the GUI displays home **No movement occurs but the motor counts/encoder counts are reset to zero. This is the same behaviour in both drivers**
- [ ] Confirm that you can move the chopper lifter in and out of the beam **Not tried due to unsure state of the lifter**
- [x] Attempt to move an axis beyond it's physical limit, confirm that it stops
- [x] Set soft limits on an axis, confirm that you cannot go outside them
- [ ] Move the galil over to serial comms as per the procedure in https://github.com/ISISComputingGroup/IBEX/issues/3546 and confirm it still communicates **Could not connect to the com port**

### Tests specific to areas the new driver has changed
- [ ] Turn on WLP, physically press a limit switch and confirm that you cannot move the motor in either direction **WLP now appears to not work**
- [x] Set both soft limits to zero, confirm that you can move. **Movement is possible but all motor fields go into an alarm state**

### Test Communication Errors
- [ ] Turn off Galil control and start IOC: IOC should report comms error on all motors
- [ ] Connect IOC and then turn off galil: IOC should report comms error on all motors

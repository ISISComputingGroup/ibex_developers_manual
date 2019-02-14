This page covers initial testing of the new Galil driver, this driver does not use the Galil provided DLL and so should work with all Visual Studio versions. The code is not submitted for review as a PR yet, but as some developers are unable to talk to the Galil reliably at all it may be useful in its current state. Please let @FreddieAkeroyd know of any issues you see.

To use the new driver you need to switch both your support/galil/master and ioc/master submodules onto the "update_to_3_4" branch and remake support/galil/master and ioc/master/GALIL.

in `ioc/master/GALIL` there is a file  `utils/SetupR3Axis.bat`  that will initialise the Galil in the ibex office with appropriate parameters so you can move it, run it after you have started the `ioc/master/GALIL` ioc (likely you will only need to run it once as things should then get autosaved locally and applied subsequently)
 
## Changes from previous driver

* turning motors on using the motor record PREM field no longer works (the on state is now tested before PREM is run) so you need to set MTR0101_AUTOONOFF_CMD etc. to "On" (this has been adjusted in `SetupR3Axis.bat`)
* GalilStartController() has lost the "display code" argument, so you need to move the "Thread mask" argument (usually value "3" for us) one position earlier in your local settings/galil/galil*.cmd files 
* Home position is now always set to 0, so PVs like MTR0101_HOMEVAL_SP and MTR0101_PHOME_CMD have been removed. See [Resetting-HOMEVAL](Resetting-HOMEVAL)

## TODO

* Unsolicited messages are currently using UDP only, I need to look at adding TCP support
* Loading the Profile and kinematic axes DBs cause streams of errors 
* Running GalilTest IOC from support/galil/master does not work (may not fix)
  
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

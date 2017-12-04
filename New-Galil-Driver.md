This page covers initial testing of the new Galil driver, this driver does not use the Galil provided DLL and so should work with all Visual Studio versions. The code is now submitted for review as a PR yet, but as some developers as unable to talk to the Galil reliably at all it may be useful in its current state. Please let @FreddieAkeroyd know of any issues you see.

To use the new driver you need to switch both your support/galil/master and ioc/master submodules onto the "update_to_3_4" branch and remake support/galil/master and ioc/master/GALIL.

in ioc/master/GALIL there is a file  utils/SetupR3Axis.bat  that will initialise the Galil in the ibex office with appropriate parameters so you can move it, run it after you have started the ioc/master/GALIL ioc
 
## Changes from previous driver versions

* turning motors on/off using motor record PREM/POST fields no longer works, you need to set e.g. MTR0101_AUTOONOFF_CMD to "On" (this has been adjusted in SetupR3Axis.bat)
* GalilStartController() has lost the "display code" argument, so you need to move the "Thread mask" argument (ususally "3" for us) one position earlier
* Home position is always 0, PVs like MTR0101_HOMEVAL_SP and MTR0101_PHOME_CMD have been removed 

## TODO

* Unsolicited messages are currently using UDP only, I need to look at adding TCP support
* Loading the Profile and kinematic axes DBs cause streams of errors 
* Running GalilTest IOC from support/galil/master does not work (may not fix)
  
Previously we used a non-zero HOMEVAL (e.g. MTR0101_HOMEVAL_MON and MTR0101_HOMEVAL_SP) with the Galil. To avoid issues where this clashed with the motor record offset, and also for compatibility with the newer Galil driver version, we have decided to always have a HOMEVAL of 0 and use the Motor record OFF field. To convert an existing system into the new scheme, the steps needed are (assuming MTR0101 is being done):

First Steps:
* Make a note of the current motor record user position (RBV)
* Find the current HOMEVAL (e.g. MTR0101_HOMEVAL_MON which should be the same as MTR0101_HOMEVAL_SP)
* Add this  HOMEVAL to any existing offset in motor record user offset (OFF) field
* Set MTR0101_HOMEVAL_SP to 0

The readback will currently be in error by the HOMEVAL we have just added, you can either rehome the axis or redefine the current axis position to be what it was before (i.e. the value you initially recorded above). To redefine in the GUI:
 
* Change calibration mode from "use" to "set" (leave offset as "frozen")
* Enter the previous motor user position in the move absolute box
* Change calibration mode from "set" back to "use"

This could likey be accomplished programatically by:

* writing 1 to MTR0101.SET   (this enters calibration mode)
* writing the previous motor position to MTR0101
* writing 0 to MTR0101.SET   (this leaves calibration mode and redefines motor position in hardware)



 

 



  
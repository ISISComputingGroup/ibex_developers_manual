Previously we used a non-zero HOMEVAL (e.g. MTR0101_HOMEVAL_MON and MTR0101_HOMEVAL_SP) with the Galil. To avoid issues where this clashed with the motor record offset (OFF) field, and also for compatibility with the newer Galil driver version, we have decided to move to a HOMEVAL of 0 and using the Motor record OFF field to adjust position displayed to the user. To convert an existing system into the new scheme, the steps needed are (assuming MTR0101 is being done):

First Steps:
* Check the motor record direction (DIR) field (in the calibration part of the motor record screen) is positive. If is isn't, stop now as a different procedure may be needed. I believe at ISIS it is always positive at this level. 
* Make a note of the current motor record user position (RBV) and HIGH/LOW (HLM/LLM) limits
* Find the current HOMEVAL (e.g. MTR0101_HOMEVAL_MON which should be the same as MTR0101_HOMEVAL_SP)
* Add this  HOMEVAL to any existing offset in motor record user offset (OFF) field
* Set MTR0101_HOMEVAL_SP to 0

The readback and limits will currently be in error by the HOMEVAL we have just added. You will need to manually reset the limits, but for the position you can either rehome the axis or redefine the current axis position to be what it was before (i.e. the RBV value you initially recorded above). To redefine in the GUI:
 
* Change calibration mode from "use" to "set" (leave offset as "frozen")
* Enter the previously recorded motor RBV user position in the move absolute box
* Change calibration mode from "set" back to "use"

This final sequence could be accomplished programmatically by:

* writing 1 to MTR0101.SET   (this enters calibration mode)
* writing the previously recorded RBV motor position to MTR0101.VAL (loads new position into hardware)
* writing 0 to MTR0101.SET   (this leaves calibration mode)

Then setting (or adjusting) of any limits (HLM/LLM) should be performed  
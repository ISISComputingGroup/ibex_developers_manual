## Description

This device is used at ISIS to set or ramp distinct DC voltage levels at the 
output channels, which can be used for controlling industrial equipment requiring
0-10 VDC unipolar or bipolar control signal.


## Command Set


| Title | Command | Description |
| ---  | ---  | --- |
| VOLTAGE     | `V chn value` | Sets the voltage on an output channel. `chn` = A-D, value = 0 to ±1000 and is listed in 1/100 of a volt.
| TRAPEZOID   | `T chn value` | Ramps the voltage on an output channel to a desired level using a trapezoidal shaped profile. Slope is determined by RAMP-RATE. `chn` = A-D, value = 0 to ±1000 and is listed in 1/100 of a volt
| RAMP-RATE      | `R chn value` | Sets the ramp rate used in the TRAPEZOID and S-CURVE functions for a specific channel. `chn` = A-D, `value` = 1 to 255 and is listed in 1/100 of a volt/sec. Example: 125 = 1.25 V/sec. Default = 50

## In-build ramping and why it is not used

The device has in-build ramp generator to follow a slope at a user-defined ramp rate. 
However, when this feature is used, the device stops communicating with the user while it is ramping.
Due to this, the user won't be able to read what voltage is being given out and the device will appear
disconnected.

To avoid this issue, ramping in ReadASCII is used to perform ramping.

## Device Manual
https://weedtech.com/wtdac-m.pdf
 


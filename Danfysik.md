A way of controlling power supplies for magnets.

Current three models supported: 8800, 8000 and XXXX

All can be in calibrated or uncalibrated mode. Calibration is done within the IOC
All can be unipolar or bipolar.

## Testing

### All

Set voltage with `%MYPVPREFIX%DFKPS_0X:SIM:VOLT`
Set current %MYPVPREFIX%DFKPS_01:SIM:RAW


### 8000

Interlock and power status can be testing by setting status PV: `%MYPVPREFIX%DFKPS_0X:SIM:STATUS`. To switch the power on put a `!` as the first character to turn the interlock on place a `!` as the 10th character.

### 8800/XXXX

Interlock and power status can be testing by setting status PV: `%MYPVPREFIX%DFKPS_0X:SIM:STATUS`. To switch the power off it must be a binary value with 2 digit set (e.g. 2) for the interlock it must be any value which is greater than 3 digit (e.g. 4). The value 6 would trigger both.


# Danfysik

A type of large power supply for magnets.

Current four models supported: 8800, 8000, 8500, 9100 and 9700. The [RIKEN](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Riken-power-supplies) power supplies are also controlled by Danfysiks but these are a special case. Although the 9700 should work with the opi it uses a baud rate of 115200, unlike the 9600 used by other devices. The baud rate macro is not exposed to the GUI and so must be set in the globals.txt, the power supply group are working on getting them switched to 9600 baud.

All can be in calibrated or uncalibrated mode. Calibration is done within the IOC and enabled via macro. Additionally there is a macro to switch to a local calibration repository instead of the default common one. (see [Calibration Files](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Calibration-Files) for more info)

All can be unipolar or bipolar (controlled by the `POLARITY` macro).

## Testing

### All

Set voltage with `%MYPVPREFIX%DFKPS_0X:SIM:VOLT`
Set current %MYPVPREFIX%DFKPS_01:SIM:RAW


### 8000

Interlock and power status can be testing by setting status PV: `%MYPVPREFIX%DFKPS_0X:SIM:STATUS`. To switch the power on put a `!` as the first character to turn the interlock on place a `!` as the 10th character.

### 8800/8500

Interlock and power status can be testing by setting status PV: `%MYPVPREFIX%DFKPS_0X:SIM:STATUS`. To switch the power off it must be a binary value with 2 digit set (e.g. 2) for the interlock it must be any value which is greater than 3 digit (e.g. 4). The value 6 would trigger both.

## Connecting to an 8500 series through serial

The serial standard (RS232, 422 OR 485) used by a danfysik 8500 series is determined by the position of a jumper on the control board. This may need to be put in place for a new power supply.

As the MCR network uses RS422, the jumper position will need to be changed if the PSU was previously controlled by the MCR.

Only change the **remote line**. The local line changes how the PSU communicates with its front panel.

The steps to change the serial standard to RS232:

1. Contact a technician responsible for the PSU. They will open the control panel for you (behind the built-in display).
1. Move the jumper from either `ST10` or `ST11` to position `ST9` (RS232 only).
   - The position of the jumper is illustrated in figure 13 of the 8500 series user manual on the manuals share
   - Which jumpers to short circuit `(S/C)` or leave as open circuit `(O/C)` are given in table 12.
   - Do not change the jumpers listed in table 11.

Note: There are two 8500 series which required a null modem on the 25-way connector. 

## Value Scaling

It is worth noting that some Danfysik devices read and write `RAW` values at different scales: given the same `CURRENT` the ratio of `RAW` read:write is 1:10 **except for Danfysik model 8800** where the ratio is 1:1. Configuring the IOC to take this into account is done via two macros `factor_read_i` and `factor_write_i`. The thing to note here is that they are the inverse of each other, i.e. `factor_read_i` = 1 / `factor_write_i` * `r:w ratio`. 

To give an example, for an uncalibrated Danfysik model 8500:
- `factor_write_i` is `1000`
- `factor_read_i` is `0.01` (1/1000 * 10)

## Auto On/Off

As the name suggests, this setting in the Danfysik IOC controls whether the device should automatically power itself on and off. If auto on/off is disabled, the device should stay in whatever state it is in unless explicitly instructed otherwise. If auto on/off is enabled, the device:
- Should power off if both:
    - The setpoint readback value is within `OFF_TOLERANCE` of 0 
    - The readback value is stable (i.e. has held its value for
at least 5 seconds)
- Should power on if: 
    - The setpoint readback value is greater than 0 + `OFF_TOLERANCE`

Auto on/off gets automatically enabled when using the "sweep to zero and turn off" functionality.

Auto on/off is part of the workflow for muon instruments, but it is not desired on neutron instruments using Danfysiks and can in fact turn the power supplies off in unsafe ways if configured badly. Thus it should always be switched off on neutron instruments. Note: The DISABLE_AUTOONOFF macro prevents auto on/off from being turned on at all and hides the GUI elements for setting it on. This macro is on by default, but is turned off by the config upgrade script for the EMU instrument, where this feature is desired.

## Initialization

At ioc start, some models of danfysik need to be explicitly changed into remote mode and/or addressed. The last setpoint and power status must also be resent to the device so that the magnet does not change state as a result of an IOC restart. This is currently being done using autosave. Further details in https://github.com/ISISComputingGroup/IBEX/issues/1209

## LOQ/SANS2D Goudsmit magnet

- This magnet is driven by a 750A power supply, but can only actually take ~600A. The scientists have asked us to apply a limit of 738666 parts per million on this Danfysik (which corresponds to a current of 554A)
  * This is true on both LOQ and SANS2D (as of May 2019)
- The magnet is calibrated. Calibration tables are start with `Goudsmit_magnet` and are located in `C:\Instrument\Settings\config\common\magnets`
- The magnet can be run in transverse or solenoid modes. As far as IBEX is concerned, this corresponds to a change of calibration files.

## Troubleshooting

### Getting no bytes back from the device
The power supply group have some test software they wrote for communicating with the device. Ask them to try this software and if it doesn't work it's likely a wiring issue.
 
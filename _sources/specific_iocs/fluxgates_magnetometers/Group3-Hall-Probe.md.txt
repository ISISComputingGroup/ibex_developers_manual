# Group3 Hall Probe

| - | - |
| - | - |
| IOC | `G3HALLPR` |
| OPI | `Group3 Hall Probe` |
| Manual | `\\isis\shares\ISIS_Experiment_Controls\Manuals\Group3__Hall_Probe` |

## Description

This is a hall probe IOC, which is used as part of HIFI's zero-field system. The HIFI zero-field uses two devices (and correspondingly, will use two `G3HALLPR` IOCs), which are on separate serial ports.

Each IOC can talk to 3 probes, which can be named via the `NAME0`..`NAME2` macros (e.g. `X` or `-Y`).

A multiplier can be set for each field via the `SCALE0`..`SCALE2` macros (usually this will be either `1` or `-1`).

The scan rate for both field and temperature are independently specified as IOC macros.

## State machine

An SNL program is in use to automatically change the measurement range of each probe.

The thresholds at which this SNL program moves up/down a range are specified in PVs of the form `$(P)$(SENSORID):STATEMACHINE:R0:UP` - which in this case would be the threshold, in Gauss, at which to move up from `r0` (Range 0, 0.3 Tesla) to `r1` (Range 1, 0.6 Tesla). These thresholds may be modified via PV sets in the configuration, if needed.

To allow the device to settle in a new range, there is also a minimum delay after changing states before the next state change - this is in PVs of the form `$(P)$(SENSORID):STATEMACHINE:STATE_CHANGE_DELAY`, which again can be modified by PV sets in the configuration if desired. By default it is 2 seconds.
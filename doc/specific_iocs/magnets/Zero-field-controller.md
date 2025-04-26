# Zero field controller

This page describes some practical troubleshooting information about the muon zero field compensation system. For detailed discussion of the software design, see [Zero field controller design](Zero-field-controller-design).

## IOC setup

On EMU, the following IOCs should be running:
- Zero-field compensation power supplies: [KEPCO_01, KEPCO_02, KEPCO_03](../power_supplies/Kepco). These power supplies drive currents around the zero field compensation coils, producing a magnetic field which cancels out stray fields from neighbouring magnets.
- Zero-field magnetometer: [ZFMAGFLD_01](../fluxgates_magnetometers/Zero-Field-Magnetometer-IOC). This measures the magnetic field near the sample position, using probes connected to an NI-DAQ box.
- Zero-field controller: ZFCNTRL_01. This implements the control logic which links the magnetometer and the power supplies.

The zero-field controller implements most of the control logic using an SNL (sequencer) program. It talks via channel access reads and writes to the magnetometer and power supply IOCs.

## Controller error states

### No new magnetometer data

The zero field controller talks to the magnetometer IOC via channel access. Each time the controller takes a reading, it processes `$(MAGNETOMETER):TAKEDATA` (`$(MAGNETOMETER)` is an IOC macro passed in from the configuration). The zero field controller IOC then expects the `ZFCNTRL_01:INPUTS_UPDATED` pv to be processed when new readings are ready. 

This error state indicates that the `INPUTS_UPDATED` pv was not processed. This may be because:
- The magnetometer IOC is not started or has crashed.
- The magnetometer IOC is taking too long to get new readings (the timeout is defined in `ZFCNTRL_01:STATEMACHINE:READ_TIMEOUT`)

### Magnetometer overloaded

The magnetometers have a finite range of fields which they can measure accurately. The magnetometer IOC will attempt to detect this condition and flag an error.

This error state can be caused by:
- One of the external magnets being switched on - either the longitudinal or transverse fields can overload the magnetometer. Suggested solution: switch off the external magnets
- One of the power supplies used by the zero-field system has been driven too high, and is producing a field which overloads the magnetometer. Suggested solution: 
  * Put the zero field control system into manual mode 
  * Manually set the currents in all three zero-field power supplies to zero. 
  * Check that the zero field no longer reports an overload
  * Put controller back into auto mode 
  * Check that it can stabilize the field to zero. 
  * Consult with the scientists to define appropriate limits on the Kepcos such that they can no longer overload the magnetometer.

If neither of the above steps works, consult the scientists. There may be a physical problem with the magnetometer probes or an external field which is too strong to be compensated. The scientists have independent hall probes which can be used to check for large fields at the sample position.

### Magnetometer data invalid

This error state is caused when the magnetometer returns data marked with an INVALID alarm to the zero field controller. Check that the magnetometer can talk correctly with the hardware. If it is a DAQMX ioc, the ioc may need restarting after a connection to the hardware is reestablished. See [Zero field magnetometer ioc](../fluxgates_magnetometers/Zero-Field-Magnetometer-IOC) for further troubleshooting details on the magnetometer.

### Power supply invalid

One of the readbacks from the power supplies was marked with an INVALID alarm. Check the zero field controller OPI's "advanced" panel to see which power supply is having issues communicating - the readbacks will be highlighted with purple invalid alarms.

### Power supply on limits

One of the power supplies has been driven onto a limit, and it's output capped. This may indicate:
- That there is a strong external field present, which the zero-field system is unable to compensate for. Solution: talk with scientists to find out if there is a large external field
- That there is a problem with the magnetometer readbacks. Erroneous magnetometer data can cause the zero field controller to attempt large compensations which would drive the power supplies beyond the limits.
- That one or more of the `AMPS_PER_MG_*` macros has an incorrect sign. This will cause the controller to attempt to compensate for fields in the wrong direction, which will cause out-of-bounds setpoints to be written. If you need to re-determine these macros, see the [calibration](#zero_field_controller_calibration) section below.

### Power supply write failed

The zero-field controller writes to the power supply IOCs and then waits for the setpoint readbacks to be within a tolerance of the setpoint. This tolerance is defined by `ZFCNTRL_01:OUTPUT:PSU_WRITE_TOLERANCE` and it will wait with a timeout given by `ZFCNTRL_01:STATEMACHINE:READ_TIMEOUT`.

This error state means that writes were sent to the power supply but the setpoint readbacks did not get within tolerance. Things to check:
- Is the power supply communicating properly? You can put the zero field controller into manual mode and manually set setpoints
- Is the tolerance too tight?
- If it looks like the readbacks are getting within tolerance but slower than the read timeout, try to update the setpoint readback from hardware immediately after sending a new setpoint in the protocol file. If it's still too slow the read timeout can be increased, but beware that very slow readbacks can affect the stability of the system and only use this as a last resort.
- If the power supply appears to write correctly for a short time, and then one of the Kepcos goes into a non-clearable comms error, verify that `REMOTE_ON_SET=NO` is set in the IOC macros for the three relevant Kepcos. This settings MUST be set for zero-field Kepcos.

### PSU high limit < low limit

This state is triggered if the power supply limits have been defined incorrectly in the configuration. Check the configuration macros for sign errors.

### PSU out of range

This state is triggered if the power supply setpoint readback value is outside of the power supply limits.

## Miscellaneous troubleshooting

### Zero field controller reports "unstable" when the instrument is running at field.

The "stability" indicator does not truly indicate stability - instead, it indicates that the measured field is within a tolerance of the setpoint. The tolerance is defined in `ZFCNTRL_01:TOLERANCE`. 

This behaviour was specified in the [initial design document - see flowchart](#zero_field_implementation) which was agreed with the muon scientists, and should only be changed by agreement with all scientists using this system.

### Zero field controller always goes into manual after being restarted (e.g. on config load)

This behaviour was requested in the [initial design document](Zero-field-controller-design).

> On IOC start up I’d suggest <...>, and then go into Manual.

### A 'magnetometer overload' does not always trigger an alarm

In [ticket 5132](https://github.com/ISISComputingGroup/IBEX/issues/5132), it was requested that the alarms on the magnetometer being overloaded should be suppressed if the zero-field controller is in manual mode. This is because, while the controller is in manual mode, the scientists will intentionally apply large external fields (which overload the magnetometer), but they do not want their users to be worried by alarms.

In auto mode, the magnetometer being overloaded triggers a MAJOR alarm.

### The "loop time" is in minor alarm

The state machine measures the total time it takes for all of it's actions to complete. If this takes too long, a minor alarm is triggered on loop time. This usually suggests that one of the steps in the loop is taking much longer than expected (for example, hitting a timeout when trying to acquire data).

This is highlighted as an alarm because a very slow loop time can affect the stability of the system and it's response to external fields. However, if the system appears to be operating correctly despite this alarm, then it may be safely ignored.

### The zero field system is generating large channel access put logs

Because the zero-field controller IOCs does channel access writes to the power supply IOCs, these writes would usually be logged. However the zero field controller can perform these writes several times per second, causing large put logs to build up.

To solve this, the power supply setpoint PVs should be placed in the `NOTRAPW` (no trap write) EPICS access security group. This can be done in the configuration using the PV sets mechanism, for example:
```
IN:EMU:KEPCO_01:CURRENT:SP.ASG NOTRAPW
```

In future we may choose to implement a solution which only hides writes initiated by the zero field system, while preserving writes generated by a user.

### Voltage limits set incorrectly or being reset in auto mode

The voltage limits are specified via IOC macros. The IOC sends the limits whenever the controller is in auto-feedback mode and the limits read back from the power supply are not within tolerance of the macro value (the tolerance is given in `ZFCNTRL_01:VOLT_LIMIT_TOLERANCE`).

### Requested current is not being delivered by power supply

Check that the voltage limits are set high enough. If the readback voltage is equal to the limit, the power supply will not be able to produce any more current and this will impact the stability of the system. Check voltage limit settings in the IOC macros and consult with scientists if you need to raise them.

IBEX may not have set remote mode correctly or something along those lines (noticed as part of checks on EMU). As a workaround until we have a fix, stop the Kepco X, Y and Z, Zero field controller and magnetometer IOCs and then start up the `zerofield.vi` in `LabView Modules\Muon Magnets\Zero Field Controller` for a few seconds. Then stop the `zerofield.vi` and first start up the Kepcos and then the Zero field controller and magnetometer IOCS.

### I can set the gas flow to a larger percentage but not to a smaller one

The needle valve may not be connected correctly, ask the scientists

{#zero_field_controller_calibration}
## Calibration

The zero-field controller IOCs has macros for the number of Amps per mG expected of each power supply. These values are obtained by running a calibration routine, which is defined in the [`InstrumentScripts`](https://github.com/ISISNeutronMuon/InstrumentScripts/tree/master/technique/muon) repository and loaded into the instrument scripts.

The calibration routine will create several plots:
- Plots of Amps against measured mG for each axis. 
  * These plots should be linear. 
  * If there is a non-linear section in the graph, you will need to set power supply limits such that the non-linear sections are excluded and then re-run the script. 
  * The gradient of these lines are the numbers you will need for the `AMPS_PER_MG_*` macros.
- Plots of measured field against time in both auto and manual mode. 
  * The main thing to look for in these plots is that they contain no particular trend - the values should look like noise. The graphs in auto mode and manual mode should look very similar.
  * On EMU a noise level less than 5 mG should be achievable.
  * If you see a trend of convergence towards zero, you can try making the feedback factor larger to make the zero field system compensate more aggressively. A value of 0.5 has been found to be a good starting point. Do not make feedback greater than 1 as this is highly likely to create oscillations.
  * If you observe oscillations (particularly in auto mode), you can try reducing the feedback factor, however this will make the system slower to respond to real changes.
  * If you see a trend of divergence away from zero, it is likely that there is a sign error in one of the Amps per mG numbers or in the magnetometer sensor matrix.

## cDAQ zero field smoothing

Averaging can be applied with the use of the `NUM_SAMPLES` macro in the `ZFMAGFLD` IOC. This can help with noise from the magnetometer quickly giving feedback to the zero field controller. 

To apply averaging, set the `NUM_SAMPLES` macro to however many samples you would like to compress. The default is 1, which doesn't do anything and leaves the field values as-is. 

## Debug mode

The zero-field controller includes a very verbose debug mode, which is off by default. To enable it, use `caput %MYPVPREFIX%ZFCNTRL_01:DEBUG 1`. This will log messages at various points in the state machine, to aid debugging.

**With debug mode enabled, the zero field controller may log debug messages at the rate of ~100 messages/sec.** This option should not be left on long-term, else the messages will quickly fill available disk space.

## Autosaving feedback-mode
To autosave the feedback mode so it persists on an IOC restart add `ZFCNTRL_01__SAVEFEEDBACKMODE=YES` to your `globals.txt`. 
This is done with a `pass0` autosave which checks for changes every 5 seconds rather than the default when using `autosaveFields` which is 30 seconds. 
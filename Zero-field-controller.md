> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > [Zero field controller](Zero-field-controller)

This page describes some practical troubleshooting information about the muon zero field compensation system. For detailed discussion of the software design, see [Zero field controller design](Zero-field-controller-design).

# IOC setup

On EMU, the following IOCs should be running:
- Zero-field compensation power supplies: [KEPCO_01, KEPCO_02, KEPCO_03](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Kepco). These power supplies drive currents around the zero field compensation coils, producing a magnetic field which cancels out stray fields from neighbouring magnets.
- Zero-field magnetometer: [ZFMAGFLD_01](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Zero-Field-Magnetometer-IOC). This measures the magnetic field near the sample position, using probes connected to an NI-DAQ box.
- Zero-field controller: ZFCNTRL_01. This implements the control logic which links the magnetometer and the power supplies.

# Controller error states

### No new magnetometer data

The zero field controller talks to the magnetometer IOC via channel access. Each time the controller takes a reading, it processes `$(MAGNETOMETER):TAKEDATA` (`$(MAGNETOMETER)` is an IOC macro passed in from the configuration). The zero field controller IOC then expects the `ZFCNTRL_01:INPUTS_UPDATED` pv to be processed when new readings are ready. 

This error state indicates that the `INPUTS_UPDATED` pv was not processed. This may be because:
- The magnetometer IOC is not started or has crashed.
- The magnetometer IOC is taking too long to get new readings (the timeout is defined in `ZFCNTRL_01:STATEMACHINE:READ_TIMEOUT`)

### Magnetometer overloaded

The magnetometers have a finite range of fields which they can measure accurately. The magnetometer IOC will attempt to detect this condition and flag an error.

This error state can be caused by:
- One of the external magnets being switched on - either the longitudinal or transverse fields can overload the magnetometer. Suggested solution: switch off the external magnets
- One of the power supplies used by the zero-field system has been driven too high, and is producing a field which overloads the magnetometer. Suggested solution: put the zero field control system into manual mode and manually set the currents in all three zero-field power supplies to zero. Check that the zero field no longer reports an overload, and then put it back into auto control and check that it can stabilize the field to zero. Consult with the scientists to define appropriate limits on the kepcos such that they can no longer overload the magnetometer.

If neither of the above steps works, consult the scientists. There may be a physical problem with the magnetometer probes or an external field which is too strong to be compensated. The scientists have independent hall probes which can be used to check for large fields at the sample position.

### Magnetometer data invalid

This error state is caused when the magnetometer returns data marked with an INVALID alarm to the zero field controller. Check that the magnetometer can talk correctly with the hardware. If it is a DAQMX ioc, the ioc may need restarting after a connection to the hardware is reestablished. See [Zero field magnetometer ioc](Zero-Field-Magnetometer-IOC) for further troubleshooting details on the magnetometer.

### Power supply invalid

One of the readbacks from the power supplies was marked with an INVALID alarm. Check the zero field controller OPI's "advanced" panel to see which power supply is having issues communicating - the readbacks will be highlighted with purple invalid alarms.

### Power supply on limits

One of the power supplies has been driven onto a limit, and it's output capped. This may indicate:
- That there is a strong external field present, which the zero-field system is unable to compensate for. Solution: talk with scientists to find out if there is a large external field
- That there is a problem with the magnetometer readbacks. Erroneous magnetometer data can cause the zero field controller to attempt large compensations which would drive the power supplies beyond the limits.

### Power supply write failed

The zero-field controller writes to the power supply IOCs and then waits for the setpoint readbacks to be within a tolerance of the setpoint. This tolerance is defined by `ZFCNTRL_01:OUTPUT:PSU_WRITE_TOLERANCE` and it will wait with a timeout given by `ZFCNTRL_01:STATEMACHINE:READ_TIMEOUT`.

This error state means that writes were sent to the power supply but the setpoint readbacks did not get within tolerance. Things to check:
- Is the power supply communicating properly? You can put the zero field controller into manual mode and manually set setpoints
- Is the tolerance too tight?
- If it looks like the readbacks are getting within tolerance but slower than the read timeout, try to update the setpoint readback from hardware immediately after sending a new setpoint in the protocol file. If it's still too slow the read timeout can be increased, but beware that very slow readbacks can affect the stability of the system and only use this as a last resort.


### PSU high limit < low limit

This state is triggered if the power supply limits have been defined incorrectly in the configuration. Check the configuration macros for sign errors.

# Calibration

The zero-field controller IOCs has macros for the number of Amps per mG expected of each power supply. These values are obtained by running a calibration routine, which is defined in the [InstrumentScripts](https://github.com/ISISNeutronMuon/InstrumentScripts/tree/master/technique/muon) repository and loaded into the instrument scripts.

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
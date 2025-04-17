> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [In situ DSC](In-Situ-DSC)

There is a requirement to provide in situ calorimetry, with it being in use on a beamline, most likely HRPD, in early 2020.

This will be achieved by providing temperature heating control from a Eurotherm.
The temperatures will be monitored by a Lakeshore 336.

This will be made up of a bracket, which will have 4 heater bores and a number of sensors.

The temperature of the whole bracket will be controlled, based on the differential temperature from the sensors above and below the sample. As such it would be beneficial if that differential could be loaded as a block.

The system needs to read 4 sensors from a Lakeshore 336 and read and control 2 Eurotherms in a standard 3 Eurotherm crate. 
Ideally, the differential (the value of one sensor - the value of another sensor) will also be available to be logged. There are 4 of these differentials to consider. Ticket [#4987](https://github.com/ISISComputingGroup/IBEX/issues/4987) has a suggested GUI in the comments. Note that a plot was not included in the mock, but is desirable. An extra tab with the sensor values all visible may also be necessary.

Initial testing can be arranged for beam off days and shutdowns. Longer-term there is a need for HRPD Setup to exist, which would gather the data for the calorimetry. Ideally, this data would then be archived and dealt with as any experimental data, but at least initially it is acceptable to merely provide a way to access it and the storage and archiving are the responsibility of the experiment team.

## Software implementation notes (https://github.com/ISISComputingGroup/IBEX/issues/4987)

- There are 10 blocks
  - 6 for the Eurotherm (heater)
    - 2 for the heater, 2 for the heater setpoint and 2 for the ramp rate
  - 4 for the Lakeshore 336 (monitoring the temperature at 4 points)
- The Eurotherm and lakeshore 336 must be specified as macros (in globals.txt) using DSC_EUROTHERM and DSC_LKSH336 e.g. DSC_EUROTHERM=03
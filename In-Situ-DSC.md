> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [In situ DSC](In-Situ-DSC)

There is a requirement to provide in situ calorimetry, this is being designed and built with the expectation of testing at the end of the January shutdown, with it being in use on a beamline, most likely HRPD, next year.

This will be achieved by providing temperature heating control from a Eurotherm.
The temperatures will be monitored by a Lakeshore 336.

Much of the requirements can be achieved using blocks, but may also need to be run offline in time. Ideally, the scanning rate would be 0.1s, but 0.5s should be OK.

This will be made up of a bracket, which will have 4 heater bores and 14 sensors.

The temperature of the whole bracket will be controlled, based on the differential temperature from the sensors above and below the sample. As such it would be beneficial if that differential could be loaded as a block.

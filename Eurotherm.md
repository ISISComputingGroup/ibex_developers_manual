The eurotherm is one of the most common temperature controllers at ISIS. Most beamlines have at least one eurotherm if not more.

Eurotherms can be calibrated by selecting a calibration file in the OPI (`None.txt` for uncalibrated). By default this looks at a common calibrations repository, but can be set to a instrument-specific local one via IOC macro. See [Calibration Files](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Calibration-Files) for more info.

# Gotchas

- If the protocol timeouts are increased too much the IOC will go into alarm states as some scans depend on the timeout. Do not increase the timeout beyond the tested value in the protocol file!
- The eurotherm protocol uses variable terminators.

# Connections

There are many different models of eurotherm with mutliple connections. This is a guide only:

HRPD: serial cable needs to be pluged into the RH 9 pin port labelled "J" not the 25 pin one labelled "H"

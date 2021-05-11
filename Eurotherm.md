> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Temperature Controllers](Temperature-Controllers) > [Eurotherm](Eurotherm)

The eurotherm is one of the most common temperature controllers at ISIS. Most beamlines have at least one eurotherm if not more.

Eurotherms can be calibrated by selecting a calibration file in the OPI (`None.txt` for uncalibrated to read voltage/millivolt). By default this looks at a common calibrations repository, but can be set to a instrument-specific local one via IOC macro. See [Calibration Files](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Calibration-Files) for more info.

# Gotchas

- The IOC needs to be told which sensors it is using via macros otherwise it will not communicate with any of them
- If the protocol timeouts are increased too much the IOC will go into alarm states as some scans depend on the timeout. Do not increase the timeout beyond the tested value in the protocol file!
- The eurotherm protocol uses variable terminators and the checksum comes after the termination character.
  * Because of this, most commands do not read to a terminator but instead depend on getting a read timeout to terminate messages. This is achieved in streamdevice by setting `InTerminator = ""`.
- There is custom timing logic in `st-timing.cmd` which attempts to set the command rate of the eurotherm such that it can keep up with the message rate. If this logic is changed it should be tested against eurotherms with different numbers of sensors connected (especially 6-sensor crates) to make sure that the eurotherm can keep up in the worst-case scenario with setpoints and readbacks updating rapidly on all sensors.

# Connections

There are many different models of eurotherm so they may have different connections. 

General:

- Connection: Serial 9 Pin
- Null terminator?: Unknown
- Gender?: Unknown

HRPD: 

- Port: serial cable needs to be plugged into the RH 9 pin port labelled "J" not the 25 pin one labelled "H"

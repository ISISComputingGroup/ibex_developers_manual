> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Temperature Controllers](Temperature-Controllers) > [Eurotherm](Eurotherm)

The eurotherm is one of the most common temperature controllers at ISIS. Most beamlines have at least one eurotherm if not more.

Eurotherms can be calibrated by selecting a calibration file in the OPI (`None.txt` for uncalibrated to read voltage/millivolt). By default this looks at a common calibrations repository, but can be set to a instrument-specific local one via IOC macro. See [Calibration Files](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Calibration-Files) for more info.

**To use the IOC one of the ADDR_X macros should be defined**

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

# Comms modes

As of [ticket 4240](https://github.com/ISISComputingGroup/IBEX/issues/4240), we can communicate with Eurotherms via either Modbus or EI-BISYNCH protocol. The EI-BISYNCH protocol is the default and is currently used for most eurotherms at ISIS.

### Changing comms mode in IOC

The modbus protocol takes the same serial comms settings as EI-BISYNCH. The `BITS` macro is ignored and hardcoded to 8 bits because this is part of the modbus specification. Note that baud rate and parity may change when changing the comms settings physically on a eurotherm, so this should be double checked.

To choose MODBUS, set the `COMMS_MODE` macro to `modbus`. To choose `EI-bisynch`, set the `COMMS_MODE` macro to `eibisynch`. If the macro is not set, EI-bisynch will be used.

### Changing comms mode on physical device

To change the comms settings on a physical eurotherm box:
- Power cycle the unit while holding down the up & down arrow keys simultaneously
- Once the unit comes up asking for a passcode, enter the configuration password (for office eurotherm, this is in keeper. For other eurotherms on a beamline, it is probably a similar password)
- Navigate to the "comms" menu section, scroll down to "protocol" and select EI-BISYNCH or MODBUS as appropriate
- Check the baud rate and parity in the comms menu as this sometimes changes as you change between comms modes
- Navigate back to the config section of the menu, and select "GOTO" -> "Level 3".
  * Note that the eurotherm **WILL NOT** communicate while it is in the config mode
- The eurotherm should now communicate on the selected protocol.


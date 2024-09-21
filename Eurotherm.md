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
- The 2400 model has a maximum OUTPUT_RATE of 99.9 %/min, whereas the 3500 model has a maximum OUTPUT_RATE of 9999.9 %/min. The user manual for the 3500 specifies this available range, but the manual for the 2400 does not.
- 16-bit data limits mean that OUTPUT_RATE is further limited to 3276.7 %/min when modbus mode is used and the required OUTPUT_RATE_SCALING is 0.1.

# Connections

There are many different models of eurotherm so they may have different connections. 

General:

- Connection: Serial 9 Pin
- Null terminator?: Unknown
- Gender?: Unknown

HRPD: 

- Port: serial cable needs to be plugged into the RH 9 pin port labelled "J" not the 25 pin one labelled "H"

# Comms modes

As of [ticket 4240](https://github.com/ISISComputingGroup/IBEX/issues/4240), we can communicate with Eurotherms via either Modbus or `EI-BISYNCH` protocol. The `EI-BISYNCH` protocol is the default and is currently used for most eurotherms at ISIS.

### Changing comms mode in IOC

The modbus protocol takes the same serial comms settings as `EI-BISYNCH`. The `BITS` macro is ignored and hardcoded to 8 bits because this is part of the modbus specification. Note that baud rate and parity may change when changing the comms settings physically on a eurotherm, so this should be double checked.

To choose MODBUS, set the `COMMS_MODE` macro to `modbus`. To choose `EI-bisynch`, set the `COMMS_MODE` macro to `eibisynch`. If the macro is not set, `EI-bisynch` will be used.

Note: if changing from `ei-bisynch` to modbus, ensure you carefully read the section below entitled "modbus scaling"

### Changing comms mode on physical device

To change the comms settings on a physical eurotherm box:
- Power cycle the unit while holding down the up & down arrow keys simultaneously
- Once the unit comes up asking for a passcode, enter the configuration password (for office eurotherm, this is in keeper. For other eurotherms on a beamline, it is probably a similar password)
- Navigate to the "comms" menu section, scroll down to "protocol" and select `EI-BISYNCH` or `MODBUS` as appropriate
- Check the baud rate and parity in the comms menu as this sometimes changes as you change between comms modes
- Navigate back to the config section of the menu, and select "GOTO" -> "Level 3".
  * Note that the eurotherm **WILL NOT** communicate while it is in the config mode
- The eurotherm should now communicate on the selected protocol.

### Comms mode implementation details

- The comms mode is passed to the `.db` file as an `IFUSES_BISYNCH` and `IFNOTUSES_BISYNCH` macros, which are mutually exclusive. This macro is used to select between `INP` links that use streamdevice (for `EI-bisynch`) and `INP` links that use modbus (via asyn).
- The modbus addresses are defined in `generate_substitutions.py`, which is a helper file for generating a set of `.substitutions` files for each channel. This provides substitutions for the `GAD` and `LAD` macros (needed in bisynch mode) and also the modbus addresses.
- 10 `.db` files, for each sensor number that IBEX supports, are created by the `.substitutions` files. These files correspond to a physical sensor, not a sensor number in IBEX.
- `st-comms-eibisynch.cmd` and `st-comms-modbus.cmd` contain protocol-specific comms setup code in the `st.cmd`. Only one of these files will be called, depending on the value of the `COMMS_MODE` macro.
- Both protocols are supported (via two stream interfaces) in lewis, and the same set of tests run against the eurotherm in both modes, using a set of base tests in the IOCTestFramework.


# Modbus scaling

When setting up a eurotherm in modbus, macros need to be set in `globals.txt` for each sensor describing the scaling.

The macros are:

| Macro | Meaning |
| --- | --- |
| `TEMP_SCALING_1` | Scaling factor used on sensor 1 for temperature setpoints and readbacks |
| `P_SCALING_1` | Scaling factor used on sensor 1 for "P" PID parameter |
| `I_SCALING_1` | Scaling factor used on sensor 1 for "I" PID parameter |
| `D_SCALING_1` | Scaling factor used on sensor 1 for "D" PID parameter |
| `OUTPUT_SCALING_1` | Scaling factor on sensor 1 used for output parameters (e.g. `MAX_OUTPUT`) |
| `OUTPUT_RATE_SCALING_1` | Scaling factor on sensor 1 used for OUTPUT_RATE parameter |
| ... | As above, for all other sensors |

Because of the large number of macros, these have not been added to `config.xml`, and so are only settable via `globals.txt`.

Note that the scaling factors can differ between sensors on a eurotherm crate, and there is not necessarily any relationship between each of the individual scaling factors within a sensor.

The scaling factors are always powers of 10.

To determine the scaling factors, start the IOC in modbus mode, then for each parameter on each sensor, check using the eurotherm menus that the number in the eurotherm itself equals what IBEX reports. **Check carefully** as, for example, a PID parameter of `1.5` looks quite similar to `15`, but will cause temperature control to be entirely incorrect! 

# Troubleshooting

 - If you're having trouble with the Eurotherm-based automatic needle valve controller (i.e. on WISH), see [Automatic needle valve controller wiki](Automatic-Needle-Valve-Controller)

## eurothem not heating

If the P,I,D, Max Output all look OK, and the setpoint readback suggests a setpoint has been sent, but the heater output remains 0, then one possibility is that the eurotherm is in Manual not automatic mode - there is a Manual/Automatic switch on the front panel on the eurotherm hardware

    

# The Problem

EMU is the only beamline to be fully controlled by new Mercury iTCs as opposed to ITC503s as of 03/11/2021. The Mercury iTCs are newer and will become replacements to the ITC503s for more beamlines as time goes on, particularly on WISH and RIKEN initially. The problem with the new Mercury iTCs is that they have two modes:

- Pressure control mode
  - Controls needle valve based on the pressure
- Automatic needle valve control mode
  - Controls needle valve based on heater power, affecting the pressure but ignoring the pressure set by the user

It is difficult to switch between the two modes and requires multiple Mercurys which cost thousands of pounds. For optimal control, scientists need the needle valve to be controlled based on the pressure (done automatically by the Mercury in Pressure Control Mode), but they also need the pressure to be controlled automatically based on the temperature setpoint (to be implemented in IBEX).

# Design

Implementation is to be done by modifying the existing MERCURY_ITC IOC in IBEX (https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/MERCURY_ITC, https://github.com/ISISComputingGroup/EPICS-MercuryiTC). This implementation will enable the mercury hardware to be always configured for Pressure Control Mode, whilst we add an automated pressure control behaviour to optimise the pressure for given temperature setpoints. This automated pressure control behaviour sets the pressure based on the temperature and the temperature setpoint. My recommendation would be to build the logic with a small state machine in snl, with new PVs where required and the lookup table functionality using [ReadASCII](https://github.com/ISISComputingGroup/EPICS-ReadASCII).

![Flowchart design](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_developers_manual/MercuryEnhancedCryo.drawio.png)

## Switching the automated pressure control on and off

The automated pressure control behaviour needs to be able to be turned on and off. The IOC should behave as if no changes had been made to the IOC when this behaviour is turned off. The behaviour should be turned on and off by a boolean checkbox in the OPI, which controls a PV whose value is persisted through autosave.

The benefits of using autosave over a macro:

- Makes the IOC more testable (not requiring a restart of the IOC in the IOCTestFramework to switch modes)
- Enables switching between modes in a script
- Prevents the requirement for configurations to be changed

However, it would also increase the complexity of the IOC.

## Temperature cutoff

There will need to be two modes of operation, one at high temperatures which uses a lookup table and one at low temperatures which would set a constant pressure. We define high temperatures as any temperature above a user-defined cutoff point, and low temperatures as anything below it. This cutoff point should default to 5 Kelvin.

### Low-temperature operation

Another problem with the Mercury iTCs is that when in automated needle valve control at a temperature of less than 5 Kelvin the needle valve is fully opened, which is not optimal for temperature control. When operating below the cutoff temperature our automated pressure control behaviour will set should do is "When below the temperature cutoff point then set the pressure to a constant value which is defined by the user with a default of 5 mbar".

### High-temperature operation

When operating above the cutoff temperature the MERCURY_ITC IOC should use a lookup table to decide what to set the pressure setpoint to. There should be a reasonable default lookup table in the common configs area, but a user should be able to set their own lookup table stored in the instruments config area. The lookup table is a key-value pair. The key is the difference between the temperature and the temperature setpoint. The value is the pressure setpoint to set when the temperature - temperature setpoint is within the range of the values given key.

### Operation delay

After setting a pressure setpoint we can choose to delay by a given amount this 

## Questions whilst designing

- I have used temperature and temperature setpoint here as it seems logical to me. It was mentioned in the meeting that the mercury algorithm set the needle valve based on the heater power. Is using the difference between the temperature and temperature setpoint correct? As far as I can tell we only seem to be able to get one value for the heater power, not a target and a current value.
- This design expects a single temperature channel and a single pressure channel set by the user, does this match the requirements? If so are the single temperature cards and pressure cards fixed or do they vary?

## Device Screen

![Device screen design](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_developers_manual/MercuryEnhancedCryoDeviceScreen.png)

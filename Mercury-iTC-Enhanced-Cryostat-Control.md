# The Problem

EMU is the only beamline to be fully controlled by new Mercury iTCs as opposed to ITC503s as of 03/11/2021. The Mercury iTCs are newer and will become replacements to the ITC503s for more beamlines as time goes on, particularly on WISH and RIKEN initially. The problem with the new Mercury iTCs is that they have two modes:

- Pressure control mode
  - Controls needle valve based on the pressure
- Automatic needle valve control mode
  - Controls needle valve based on heater power, affecting the pressure but ignoring the pressure set by the user

It is difficult to switch between the two modes and requires multiple Mercurys which cost thousands of pounds. For optimal control, scientists need the needle valve to be controlled based on the pressure (done automatically by the Mercury in Pressure Control Mode), but they also need the pressure to be controlled automatically based on the temperature setpoint (to be implemented in IBEX).

# Design

Implementation is to be done by modifying the existing MERCURY_ITC IOC in IBEX (https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/MERCURY_ITC, https://github.com/ISISComputingGroup/EPICS-MercuryiTC). The changes will add an automated pressure control behaviour on top of the existing behaviour.

## Switching the automated pressure control on and off

The automated pressure control behaviour needs to be able to be turned on and off. The IOC should behave as if no changes had been made to the IOC when this behaviour is turned off. There are two options to switching on and off the control:

- The behaviour is turned on and off by a macro in a configuration
- The behaviour is turned on and off by a boolean checkbox in the OPI, which controls a PV whose value is persisted through autosave
  - Unlike a macro this would:
    - make the IOC more testable (not requiring a restart of the IOC in the IOCTestFramework to switch modes)
    - enable switching between modes in a script
    - prevent the requirement for configurations to be changed
  - However, it would also increase the complexity of the IOC


## Automated pressure control modes of operation

There will need to be two 
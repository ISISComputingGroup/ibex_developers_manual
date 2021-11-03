# The Problem

EMU is the only beamline to be fully controlled by new Mercury iTCs as opposed to ITC503s as of 03/11/2021. The Mercury iTCs are newer and will become replacements to the ITC503s for more beamlines as time goes on, particularly on WISH and RIKEN initially. The problem with the new Mercury iTCs is that they have two modes:

- Pressure control mode
  - Controls needle valve based on the pressure
- Automatic needle valve control mode
  - Controls needle valve based on heater power, affecting the pressure but ignoring the pressure set by the user

It is difficult to switch between the two modes and requires multiple Mercurys which cost thousands of pounds. For optimal control, scientists need the needle valve to be controlled based on the pressure (done automatically by the Mercury in Pressure Control Mode), but they also need the pressure to be controlled automatically based on the temperature setpoint (to be implemented in IBEX).

# Design

Implementation is to be done by modifying the existing MERCURY_ITC IOC in IBEX (https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/MERCURY_ITC, https://github.com/ISISComputingGroup/EPICS-MercuryiTC)

- Automated 
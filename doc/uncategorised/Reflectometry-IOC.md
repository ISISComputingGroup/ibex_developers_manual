> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC)

> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers) > [Reflectometry IOC](Reflectometry-IOC)

## High level Requirements

As described in the physics background page ([Reflectometers Science](Reflectometers-Science)), we need to calculate where a beamline should physically be based on higher level parameters, and track a changing beam path with multiple components. The user workflows we need to support are:

1. Delayed move (the user wants to move one or multiple devices on the beamline and they want to confirm the entered value(s) before committing to the move):
    1. Set a parameter (or multiple)
    1. Ensure the value is correct by reading it
    1. Move to the set value – either:
        1. Trigger move for a single parameter – the new value is applied for this parameter, all others retain their current values.
        1. Trigger move for all parameters – any new values are applied for all parameters
1. Immediate move (the user knows the value is correct and just wants to move):
    1. Set a single parameter
    1. Beamline immediately moves parameter to that position, while keeping all other parameters at their current value
1. Readback values (so the user knows where the beamline actually is)
    1. When any component moves, the actual position of the parameters should be reported
1. Visual indicators (so the user has extra information on the state of parameters without thought, usually indicated on the GUI via a colour)
    1. If a parameter setpoint is changed but not moved to (default colour yellow)
    1. If an underlying motor of a parameter is moving (default colour green)
    1. If a setpoint readback and readback are different from each other and not moving (default colour red)
    1. If a setpoint and setpoint readback are different and the setpoint is not changed (default colour red)
        1. TBD - we are not sure, we don't just want to copy values up from lower components.
1. Synchronised moves: To avoid clash conditions it is desirable that most axes move together so that they reach their final destinations at the same time. This means setting the velocity of the axis before a move is started. There is no initial requirement to actively monitor the motors themselves to ensure continual crash avoidance, e.g. in the event of a motor stall.
    - a caveat on this is that some axes should not be synchronised. Either because the motor velocities should not be changed (piezo motors) or they take a long time and have no clash conditions (e.g. multi-detector heights).

## Design Details

Reflectometry IOC sits on top of:
- **Motor Driver Layer:** This layer is responsible for communicating with the galil and other motors.  This is complete.
- **Motor Group Layer:** This layer groups together motors from the motor driver layer into more natural groups. For instance a jawset, which allows a user to set jaw gaps and height, not just positions of individual blades. 

The reflectometry IOC is composed of layers, each layer talking to the layer below and above it:

- **[Beamline Parameters](Reflectometry-Beamline-Parameters):** In this layer, the user is specifying where they want a component to be positioned in relation to the incoming beam. The user will specify theta, for instance, which will then set the position of the geometry component related to theta. They will also read whether the geometry component has changed and report a readback of the positions on the actual beamline. The beamline parameters are calculated in a strict order starting with those closest to the source to ensure the path is correct. Parameters can be disabled in which case they do not automatically track the beam. 

- **[Geometry Components](Reflectometry-Geometry-Components):** This layer calculates the beam path, and handles the conversion of positions between parameter values (relative to current beam path) and motor values (absolute room coordinates). The beamline parameters set the positions from above and the composite driving layers sets the parameters from below.

- **[Composite Driving Layer](Reflectometry-Composite-Driving-Layer):** This layer pushes values from the parameters into the motor group and motor driver PVs. They also push the readbacks up to the geometry layer. This layer contains some logic to allow concurrent moves with very simple synchronization (complete all moves in time with the slowest axis).

The whole system is coordinated by the [Beamline object](Reflectometry-Beamline-Object), which represents a complete model of the beamline from a motion point of view. This model is defined for each individual instrument by the [Reflectometry Configuration](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Configuration).

## Set Point Propagation

The values that the user sets on the reflectometry IOC only ever get transferred downward between the layers. This is true of setpoints and set-point readbacks. The only time this is violated is on start-up where the state is read from the underlying hardware for initial values. This means if a user sets a motor position it will not be reflected in the setpoint and the next time the reflectometry IOC is moved it will set it back to its original position even if it hasn't been changed. 
Readbacks flow in the opposite direction they are always read from the lower levels and set upwards. To help identify where set points and readbacks are not the same indicators on the GUI will be set.
This is controversial but is signed off as per [ticket 4307](https://github.com/ISISComputingGroup/IBEX/issues/4307).

## Server Status Feedback

The reflectometry server provides feedback on its status to the user at 3 different levels:
- **Error Log:** At this level, we just collect error messages in the reflectometry server and expose them via a PV in addition to writing them to the log file. In order to do this, we should conventionally use `SERVER_STATUS_MANAGER.update_error_log(<message>)` in place of `logger.error(<message>)`. The PV with the list of errors is then displayed in a tab on the reflectometry front panel OPI. The log is stored in a 10,000 element char waveform and thus the string returned is truncated to that limit.
- **Problems:** These are slightly higher level and intended to be fairly general just as an indication of the area where a problem occurred. For more detailed information, the user should refer to the error log. Problems are comprised of a type of issue, a severity and a list of sources that are reporting it. Examples:
    - Problem: Configuration is invalid; Severity: Major; Source(s): Configuration
    - Problem: Velocity cannot be restored; Severity: Minor; Source(s): MTR0304, MTR0305
- **Status:** This is the overall server status. The status is derived from the problems (the highest error level is the error level of the server)

The intention of this system is to provide useful feedback to the user in case things go wrong **in addition to** handling exceptions programmatically in a sensible way as one would usually.

The status, log and active problems get cleared every time a "move" is issued. This keeps the log PV size reasonable and the reported status up to date. E.g. if an error was thrown because of a disconnected motor IOC, and the motor has since been reconnected, the errors should be cleared on a successful move. If there are any persistent problems, they will just be thrown again.

## Other Concepts

#### Footprint Calculator

The footprint calculator calculates the resolution and footprint on the sample based on the slit gaps, distances between slits and sample length. This object is owned by the beamline. Currently, the footprint and resolution values are read-only.

**For more implementation details see the [Beamline Configuration page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Configuration#footprint-calculator)**

#### Long Axis

The long axis can be set like any other parameter to control movement of a component along the beam. It is currently set assuming the provided `IOCDriver` moves exactly parallel to the natural beam. Moving a component so far in the long axis that it reorders components in the beam is not currently supported.

## Design Changes

Potential design changes:

1. Add component for slit gap parameter
1. Move displacement from movement strategy and place it in beam path calc

## Specific Reflectometers

Information pertaining to specific reflectometry setups on the instruments.

- [CRISP](Reflectomtery-IOC-CRISP)
- [INTER](Reflectomtery-IOC-INTER)
- [POLREF](Reflectomtery-IOC-POLREF)
- [SURF](Reflectomtery-IOC-SURF)


## Troubleshooting

see [Reflectometry Troubleshooting and FAQ](Reflectometry-Troubleshooting-and-FAQ)

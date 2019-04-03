> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC)

> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers) > [Reflectometry IOC](Reflectometry-IOC)

### High level Requirements

As described in the physics [Reflectometers Science](Reflectometers-Science) we need to calculate where a beamline is set and track it with multiple components. The user workflows we need to support are:

1. Delayed move (the user is doing an ad-hoc move of the beamline and they want to think about the value before committing to the move):
    1. Set a parameter
    1. Ensure the value is correct by reading it
    1. Move to the set value either:
        1. Click move to this single parameter all others retain their current values.
        1. Click and move to all new parameter values
1. Immediate move (the user knows the move is correct and just wants to move):
    1. Set a parameter
    1. Beamline immediately moves to that position, while keeping all other parameters at their current value
1. Readback (so the user knows where the beamline is)
    1. When any component moves the position of the parameters should be reported
1. Visual indicators (so the user has extra information on the state of parameters without thought, usually indicated on the GUI via a colour)
    1. If a parameter setpoint is changed but not moved to (default colour yellow)
    1. If a parameter is based on a motor which is moving (default colour green)
    1. If a setpoint readback and readback are different from each other and not moving (default colour red)
    1. If a setpoint and setpoint readback are different and setpoint is not changed (default colour red)
        1. TBD we are not sure we don't just want to copy values up from lower components.

### Design Details

Reflectometry IOC sits on top of:
- **Composites Layer:** This layer help group together motors into composites which can be relabelled. For example, in the slits the North and South jaw motors can be composited to make the vertical gap and vertical centre. Doing this can be helpful because these are reused in other parts of the system. Most of these components are written; the bench is the component we haven’t tackled yet. 
- **Motor Driver Layer:** This layer is responsible for communicating with the galil and other motors.  This is complete.

The reflectometry IOC is composed of layers:

- **Beamline Parameters:** In this layer the user is specifying where they want a component to lie in relation to the beam. The user will specify theta, for instance, this will then set the geometry component related to theta. They will also read changed in the geometry components and report a readback of the positions on the actual beamline. The beamline parameters are calculated in a strict order so that the path of the beam is correct. The order and parameters will depend on the mode selected. 

- **Geometry Components:** In this layer the beam path is calculated. The beamline parameters set the positions from above and the composite driving layers sets the parameters from below.

- **Composite Driving Layer:** This layer pushes values from the parameters into composite PVs. They also push the readbacks up to the geometry layer.

The whole system is coordinated by the Beamline object.

### Beamline Parameters

Beamline parameters store something a user wishes to set. They can have blocks pointed at them or the GUI components. Each contains:

- Name: name of the parameter
- Read back: the value as calculated from the motors
- Set point: when set the reflectometry will move to this value
- Set point read-back: the last value that was requested
- Set point and no move: if this is set the set point is stored but the reflectometer does not move to it
- Move: makes the reflectometry to the set point 
- Changed: set when the set point no move has been set but not moved to

Types of parameter:

- `AngleParameter`: a parameter which controls the angle of a component
- `TrackingPosition`: a parameter which controls a linear position relative to the beam intercept. E.g. How from the beam a slit should be, the position is measured along the movement axis
- `InBeamParameter`: a parameter which controls whether a component is in or out of the beam. Some components can be parked out of the beam so they don't change its path e.g. the super mirror
- `SlitGapParameter`: a parameter which changes the gap of a slit set. This does not talk to a component but directly to the underlying PV. It is also used within the footprint calculator.

### Geomtry Component

A component represents a point of interaction on the beamline; for example, a slit set or mirror. They form the relationship between:

- the incoming beam: the position in space and angle of the beam which will intersect the components movement
- outgoing beam: the beam path after the beam has interacted with the component.
- user set value relative to the beam: where the user would like an object relative to the beam (e.g. for something on the beam 0mm above the beam)
- PV value: the value for the underlying PV (often a motor)

The relationships are captured for both set points and readbacks separately. 

The types of component currently are:

- `Component`: Component manages the distance between the beam and the component without affecting the beam (e.g. a slit).
- `TiltingComponent`: Component manages the angle and distance between the incoming beam and the component without affecting the beam (e.g. a slit with a rotation stage).
- `ReflectingComponent`: Component manages the angle and distance between the incoming beam and the component, outgoing beam is reflected from this angle (assume infitely long reflector at angle and distance from the incoming beam)
- `ThetaComponent`: Component manages the angle between the incoming beam and the outgoing beam at the sample position. 
    - The readback calculates the angle to the beam intercept of another component. Note that if that component has a beam offset it will not be the position of the component but the position without the offset. The component used is the first component which is in the beam on its list in its configuration. For a beam line may contain an analyser followed by a detector if the analyser is in the beam it will be the angle to the analyser otherwise it is the angle to the detector. 
    - The setpoint works in the same way as the `ReflectingComponent` except that it will update the beam path of disabled components which define its angle.

### Composite Driving Layer

The composite driving layer set the PV values which will make the moves happen. 

The layer consists of Drivers which take values from components and push these values into PV wrapper and take readback value and push them into the components. There are various types are:

- `DisplacementDrivers`: Set the position of the motor based on the displacement, this includes moving to a parked value if the component is out of the beam
- `AngleDriver`: Set the position of the motor based on the angle.

The PV wrapper objects are:

- `PVWrapper`: read from and write to a single PV
- `MotorPVWrapper`: read and write to a motor pv
- `AxisPVWrapper`: read and write to an axis
- `VerticalJawsPVWrapper`: read and write to a jaw set

TODO: I think we need a parameter driver and then we can more easily separate SlitGapParameter from their pv wrappers.

### Beamline Object

This is the coordinating object for the system, it performs the correct movements based on the beamline parameters and mode which is currently active. There are a number of modes which need to be supported in the system; for example NR mode, polarised, disabled etc. There is also a natural ordering of beamline parameters and components when it comes to calculations, i.e. the polarising mirror and all calculation to do with it should be done before the sample point calculations. The architecture is that a beamline object holds the order of both the components and beamline parameters. The composite drivers do not have a natural order but these are also contained by the beamline object. It makes sure that all calculations are done in the order in which they are held. The mode dictates which parameters are active in the calculation and pre-sets for some of those beamline parameters.
The following is a subsection of the configuration showing beamline parameters at the top, components in the middle and drivers at the bottom. 

 ![beamline diagram](reflectometers/Beamline.png)

#### Whole Beamline Move

When move for the whole beam line is activated the new positions of the motors are calculated using the following procedure. 

1. Each of the sample parameter are considered in turn, going down the beam. 
2. The beamline parameter is "moved to" if it has changed or if it is in the mode and a previous beamline parameter in this mode has changed.
3. When the beamline parameter is "moved to" the result of the calculation will be passed down to the component it controls.
    1. At this point the set point readback value will read the same as the set point
    1.The component will then recalculate the beam path and instruct those components down beam to recalculate their beam paths.
4. Once all beamline parameters have finished calculating along with new component positions all the composite driving layer calculates the slowest movement and performs the move at that speed for all components.

#### Single Beamline Parameter Move

When a single beamline parameter is set and moved on its own then:

If the beamline parameters is in the current mode:

1. Each beamline parameter in the mode is considered in turn, going down the beam starting from the beamline parameter which just moved.
2. If the parameters is in the mode the beamline parameters moves to it last set point (i.e. the one in the set point readback). This will pass down the calculation to the component it controls.
3. Then we are back to above.

If it is not in the mode:

1. That beamline parameters sends its move to the component it controls.
2. Then the beamline is recalculated
3. Motors are then moved

#### Changing the Mode

When the mode is changed to (not disable mode) the following happens:
1. In beamline parameter order each pre-set is applied to the set-point.
    1. This include setting whether the components are in the beam or not
2. The beamline parameters in the mode just set are used as the mode parameters.

#### Disabled Mode

Disabled mode is special because in this mode the movements are relative to the positions when the mode was entered into. This is done by disabling the beam calculation for each component. Only theta related parameters should be in the current mode. 





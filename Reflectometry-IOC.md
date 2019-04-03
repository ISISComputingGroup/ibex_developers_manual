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

The user will interact with the IOC through beamline parameters.

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

### Component

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





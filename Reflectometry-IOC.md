> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC)

> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers) > [Reflectometry IOC](Reflectometry-IOC)

IBEX IOC sits on top of:
- **Composites Layer:** This layer help group together motors into composites which can be relabelled. For example in the slits the North and South jaw motors can be composited to make vertical gap and vertical centre. Doing this can be helpful because these are reused in other parts of the system. Most of these components are written; the bench is the component we haven’t tackled yet. 
- **Motor Driver Layer:** This layer is responsible for communicating with the galil and other motors.  This is complete.

The IOC is composed of layers:

- **Beamline Parameters:** In this layer the user is specifying where they want a component to lie in relation to the beam. The user will specify theta for instance this will then set the geometry component related to theta. They will also read changed in the geometry components and report a readback of the positions on the actual beamline. The beamline parameters are calculated in a strict order so that the path of the beam is correct. The order and parameters will depend on the mode selected. 

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

- AngleParameter: a parameter which controls the angle of a component
- TrackingPosition: a parameter which control a linear position relative to the beam intercept. E.g. How from the beam a slit should be, the position is measured along the movement axis
- InBeamParameter: a parameter which controls whether a component is in or out of the beam. Some components can be parked out of the beam so they don't change its path e.g. the super mirror
- SlitGapParameter: a parameter which changes the gap of a slit set. This does not talk to a component but directly to the underlying PV. It is also used within the footprint calculator.

### Component

A component represents a point of interaction on the beamline; for example a slit set or mirror. They form the relationship between:

- the incoming beam: the position in space and angle of the beam which will intersect the components movement
- outgoing beam: the beam path after the beam has interacted with the component.
- user set value relative to the beam: where the user would like a object relative to the beam (e.g. for something on the beam 0mm above the beam)
- pv value: the value for the underlying pv (often a motor)

`TODO: Finish`
> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Geometry Components](Reflectometry-Geometry-Components)

A component represents a point of interaction with the beam on the beamline; for example, a slit set or mirror. They form the relationship between:

- the incoming beam: the position in space and angle of the beam which will intersect the components movement
- outgoing beam: the beam path after the beam has interacted with the component.
- user set value relative to the beam: where the user would like an object relative to the beam (e.g. for something on the beam 0mm above the beam)
- PV value: the value for the underlying PV (often a motor)

Each component captures the relationships for both set points (where the user wants the beamline to be) and readbacks (where the beamline actually is) separately i.e. the system maintains two separate models of the beam path. 

The types of component currently are:

- `Component`: Component manages the distance between the incoming beam and the component without affecting the beam (e.g. a slit).
- `TiltingComponent`: Component manages the angle and distance between the incoming beam and the component without affecting the beam (e.g. a slit with a rotation stage).
- `ReflectingComponent`: Component manages the angle and distance between the incoming beam and the component, outgoing beam is reflected from this angle (assumes infinitely long reflector at angle and distance from the incoming beam)
- `ThetaComponent`: Component manages the angle between the incoming beam and the outgoing beam at the sample position. 
    - The readback calculates the angle to the theoretical beam intercept of another component (ignoring any positional offset on that component). The component used is the first component on the list of the theta component (as defined in the configuration) that is in the beam. For example, a beamline may contain an analyser followed by a detector. If the analyser is in the beam, theta is the angle of the beam to the analyser, otherwise it is the angle to the detector.
    - The setpoint works in the same way as the ReflectingComponent except that it will update the beam path of disabled components which define its angle.


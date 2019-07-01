> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Beamline Parameters](Reflectometry-Beamline-Parameters)

Beamline parameters store something a user wishes to set. They can have blocks or the GUI controls pointed at them. These parameters are transformations of low-level motor values. Each contains:

- Name: name of the parameter
- Readback: the value as calculated from the low-level motor positions.
- Setpoint: when set, the reflectometry server will move the parameter this value
- Setpoint read-back: the last value that this parameter was moved to.
- Setpoint and no move: if this is set the setpoint is stored but not applied to the motor until the next time a move is triggered on this parameter.
- Move: moves this parameter to the setpoint
- Changed: true if the setpoint has been changed via setpoint no move, and has not yet been applied to the motor.


Types of beamline parameter:

- `AngleParameter`: a parameter which controls the angle of a component relative to the incoming beam angle.
- `TrackingPosition`: a parameter which controls a linear position relative to the incoming beam intercept. E.g. How far from the beam a slit should be, the position is measured along the movement axis. This is useful e.g. for scanning over this parameter for alignment.
- `InBeamParameter`: a parameter which controls whether a component is in or out of the beam. Some components can be parked out of the beam so they don't change its path e.g. the super mirror
- `SlitGapParameter`: a parameter which changes the gap of a slit set. Since this does not care about tracking the beam path, it does not talk to a geometry component, but directly to the underlying jaws PV. It is also used within the footprint calculator.

## Theta Readback Calculation

The theta beam line parameter is special because it depends on other items in the beamline. All other components are independent except for the incoming beam from a previous component. 

**Theta readback is**: Half the sum of the incoming angle and outgoing angle at the point where the incoming beam hits the sample axis (this is the axis in the theta component setup). The incoming beam is calculated from the component before the theta component. The outgoing angle is calculated by using the list of components set on the theta component in the configuration. It find the first component in that list which is in the beam, it then reads its actual position and takes away any setpoint offset.

For example, on CRISP it is the angle to the detector which is in the beam. If both detectors are in the beam the point detector is used. The offset to that detector is then taken away from the current position and this is the angle used to calculate theta. From a coding point of view, this means when the readback or setpoint position of a component in this list is updated then the readback is updated.


## Theta Setpoint Calculation

The setpoint for theta is special because all it does is change the beam path it does not affect any underlying PVs. However in disabled mode, the incoming beam is no longer altered and this means changing theta would have no effect on the component it is pointing at, e.g. changing Theta would not alter the position of the detector. To fix this there is a special route to force an incoming beam path to be set. This should allow the component defining theta to move when theta is changed.

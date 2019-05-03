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

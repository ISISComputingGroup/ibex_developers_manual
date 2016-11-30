The limiter is a configurable IOC which will limit the setting of values depending on different values. For example of ZOOM the motors should not be movable when the detector is switched on and vice-versa.

The following states and transitions are possible for two state limiter. This describes motor movement `M` and detector `D` on or off:


Where
- Darklines: Initial set of transitions
- Dotted Lines: Transitions for the future

The easiest support is for transitions where only one of the motor moving or detectors are on can ever be true. Therefore the motor can be switched on only if the detector is off and the detector can only be switched on when the motor is stationary. If this is violated then the request is ignored.

#TODO finish this
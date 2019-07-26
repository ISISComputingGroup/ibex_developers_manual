> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Composite Driving Layer](Reflectometry-Composite-Driving-Layer)

The composite driving layer sets the PV values which will make the moves happen. 

The layer consists of drivers which take setpoint values from components and push these values into a PV wrapper, and take readback values and push them into the components. The types we currently have are:

- `DisplacementDrivers`: Set the position of the motor based on the displacement, this includes moving to a parked value if the component is out of the beam
- `AngleDriver`: Set the position of the motor based on the angle.

both are derived from a common base `IocDriver`.

There are various PV wrapper types which handle the mapping of parameters to the correct PVs based on different conventions. These are:
- PVWrapper: base wrapper that has all the utility functions (e.g. monitors and change listeners) but will not point at a real PV
- MotorPVWrapper: read and write to a motor PV
- AxisPVWrapper: read and write to an axis
- VerticalJawsPVWrapper: read and write to a jaw set without a height stage (height defined by vertical centre)


TODO: I think we need a parameter driver and then we can more easily separate SlitGapParameter from their PV wrappers.

### Synchronisation

To enable synchronisation of axes this layer:

- can report the minimum time taken for individual IOC driver to finish a move
- can be told to make a move in a given duration. 

The user can turn this off in the configuration file. In which case the time reported to finish a move is 0, and the axis's speed is not changed on move.

### Engineering Offset

Engineering offsets correct the value sent to a PV because of inaccuracies in the engineering. For instance, if we set theta to 0.3 we will be setting the height of the jaw so that the jaws centre is in the middle of the beam. However, because of needing to tilt the jaws and the centre of rotation not being in the middle of the jaws, we need to add a correction to the geometry of 0.1mm. The best place to do this is at the point at which the value is sent to the driver. The form of the corrections can multiple but we will start by catering for:

1. pure function based on the value and values of other components
1. an interpolated table based on a set point

Note that in this case, the zero motor position is no longer necessarily zero, while this does not affect the maths, users will probably want to ensure that in the straight-through case the motor is zero.

The configuration for this is to add an engineering offset object to the IOCDriver. The engineering offset object will do the following:

1. Convert readbacks from the IOC PVWrapper to the uncorrected value 
1. Convert set-points from the component to the correct value that get sent to the PV
1. On initialisation to convert PV to set-point value to be initialised
    1. This is hard because to calculate the value you need a beamline parameter value which is not yet set because it is being calculated. To avoid this we introduce the constraint that engineering corrections may only be functions of an autosaved beamline parameter or the motor position/PV on which the driver is based.

### User Function Engineering Correction

To apply a user function engineering correction yo an axis we must first define the function in the configuration file. In this example case, we have a function which depends on a single beamline parameter, `theta`:

```
def my_correction(value, theta):
   ...
   return calulated_offse
```

When called by the reflectometry IOC this function will be given:

-`value` which is the position that would be sent to the axis if the correction was 0
-`theta` which is the value of the first beamline parameter set in `UserFunctionCorrection`

If there are more beamline parameters set in `UserFunctionCorrection` these would be additional arguments. The function should return a correction which will be added onto the value before being sent to the PV.
The next step is to add the engineering correction to the IOC driver. We show the definition of the theta beamline parameter to make it clear what the arguments are:

```
theta_param_angle = add_parameter(AngleParameter("THETA", theta_comp))

...

add_driver(DisplacementDriver(
    component, 
    PVWrapper, 
    engineering_correction=UserFunctionCorrection(my_correction, theta_param_angle))
```

The `UserFunctionCorrection` takes:

- `user_correction_function`: reference to the function to use
- beamline parameters: 0 or more beamline parameters whose set point readback values should be passed to the `user_correction_function`

If you wish to write your own `engineering_correction` you must:

1. **either** inherit from `SymmetricEngineeringCorrection`: then override `correction(self, setpoint)` which returns the correction to apply based on the setpoint
1. **or** inherit from `EngineeringCorrection`: then override 
    - `to_axis(self, setpoint)`: given a setpoint return the correct value to send to the axis
    - `from_axis(self, value, setpoint)`: given the `value` read from the axis and `setpoint` for the axis return the `value` without the correction


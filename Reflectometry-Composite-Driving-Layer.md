> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Composite Driving Layer](Reflectometry-Composite-Driving-Layer)

The composite driving layer sets the PV values which will make the moves happen. 

The layer consists of drivers which take setpoint values from components and push these values into a PV wrapper, and take readback values and push them into the components. The types we currently have are:

- `DisplacementDrivers`: Set the position of the motor based on the displacement, this includes moving to a parked value if the component is out of the beam
- `AngleDriver`: Set the position of the motor based on the angle.

There are various PV wrapper types which handle the mapping of parameters to the correct PVs based on different conventions. These are:
- PVWrapper: base wrapper that has all the utility functions (e.g. monitors and change listeners) but will not point at a real PV
- MotorPVWrapper: read and write to a motor PV
- AxisPVWrapper: read and write to an axis
- VerticalJawsPVWrapper: read and write to a jaw set without a height stage (height defined by vertical centre)


TODO: I think we need a parameter driver and then we can more easily separate SlitGapParameter from their PV wrappers.


### Engineering Offset

Engineering offsets correct the value sent to a PV because of inaccuracies in the engineering. For instance, if we set theta to 0.3 we will be setting the height of the jaw so that the jaws centre is in the middle of the beam. However, because of the inaccuracies in the height stage, we need to add a correction to the geometry of 0.1mm. The best place to do this is at the point at which the value is sent to the driver. The form of the corrections can multiple but we will start by catering for:

1. pure function based on the value and values of other components
1. an interpolated table based on a set point

Note that in this case, the zero motor position is no longer necessarily zero, while this does not affect the maths, users will probably want to ensure that in the straight-through case the motor is zero.

The configuration for this is to add an engineering offset object to the IOCDriver as an argument this will do the following:

1. Convert readbacks from the IOC PVWrapper to the uncorrected value 
1. Convert set-point readbacks from the IOC PVWrapper to the uncorrected value
1. Convert set-points from the component to the value that needs setting
1. Convert the initialised set-point from the motor to be the value that needs setting
    1. This is hard because it is the inverse of an nxn matrix potentially.

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

TODO

> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 7


----
<details>
    <summary>Jump To Section</summary>

> 0. [Overview & Setup](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup)
> 1. [The Basics](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-1)
> 1. [Building Up The Beamline Model](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-2)
> 1. [Modes](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-3) 
> 1. [Theta](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-4)
> 1. [Parking Components](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-5)
> 1. [Beamline Parameter Misc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-6)
> 1. [Engineering Corrections](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-7)
> 1. [The Bench](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-8)

</details>

----

# Engineering Corrections

See the [Engineering Corrections Wiki Page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Composite-Driving-Layer#engineering-offset) for more detail.

Engineering corrections are offsets that are added to set points at the Driver level before they are sent off to the underlying motor axes, and subtracted from the readback value before it is propagated up to the component level. These are used to account for inaccuracies in the physical engineering of the beamline. For instance, in the perfect world of the beamline geometry model, all mirrors are perfectly flat and extend into infinite space, whereas in reality, they may be slightly concave or the neutrons hit it off the centre of rotation so that you get slight drift for different mirror angles.

We have different types of engineering corrections, namely:
- `ConstantCorrections` - a static offset
- `UserFunctionCorrection` - a variable offset based on a set of input parameters
- `InterpolatedDataCorrection` - a lookup table of corrections, interpolating values in between discrete points in the matrix
Any of the above can also be made to apply for specific modes only.

### Exercise 7

In this exercise, let's add:
- A constant correction of `0.3` on the detector angle
- A user function correcting the detector height parameter by `0.1 * sm_angle`

A constant correction looks like e.g.
```
constant_correction = ConstantCorrection(1)
```

A user function correction looks like e.g.:
```
def correction_func(corrected_param, input_param):
    return input_param

user_correction = UserFunctionCorrection(correction_function, some_BeamlineParameter)
```

Any correction can be applied like this:
```
add_driver(IocDriver(..., engineering_correction=SomeCorrection))
```


### [< Previous: Beamline Parameter Misc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-6) || [Next: Bench](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-8)>
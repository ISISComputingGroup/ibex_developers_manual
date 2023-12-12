> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 7

# Engineering Corrections

Engineering corrections are offsets that are added to set points at the Driver level before they are sent off to the underlying motor axes, and subtracted from the readback value before it is propagated up to the component level. These are used to account for inaccuracies in the physical engineering of the beamline. For instance, in the perfect world of the beamline geometry model, all mirrors are perfectly flat and extend into infinite space, whereas in reality, they may be slightly concave or the neutrons hit it off the centre of rotation so that you get slight drift for different mirror angles.

### Exercise 7

### [< Previous: Beamline Parameter Misc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-6) || [Next: Bench](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-8)>
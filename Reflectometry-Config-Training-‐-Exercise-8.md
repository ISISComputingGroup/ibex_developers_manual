> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 8

# The Bench

[More detail on the Bench Configuration available here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/reflectometry-bench-configuration).

The bench is a large motion component which moves on an arc around a given pivot point (i.e. the last point where the beam may bounce before the bench). The reason for this is that we want to keep the detector at a constant distance from the sample for all experiments to preserve e.g. Time of Flight regardless of Theta. In case you are wondering how this is handled on beamlines that use a detector driving on a linear height stage, the answer is they do not. However, those instruments (i.e. CRISP and SURF) have an optical lever short enough that they can ignore this factor without sacrificing too much quality. Other devices (such as slits and detectors) can be mounted statically on top of it while the bench handles all the beam tracking. Benches are used for the POLREF secondary beam path (everything after the sample) and for the OFFSPEC primary & secondary beam path.

This component is special compared to the rest of the Reflecometry server as it provides a much more dramatic transformation between motor- and control axes. The control axes provided by the bench component and settable as parameters are
- Height 
- Angle - pivoting around the last point of reflection
- Seesaw - pivoting around the center of rotation of the bench itself - used for alignment only

The physical motor axes are:
- Front Height Jack
- Back Height Jack
- A slide towards/ away from the pivot point (used to maintain a static distance)

The transformation between these two sets of axes happens in the BenchComponent, using math provided to us by the POLREF scientists.

In terms of the configuration, the bench takes a `BenchSetup` object instead of the usual `PositionAndAngle`, which defines the specific geometry of the bench. It is worth noting that all the benches (i.e. Detector bench on POLREF and the Front- and Detector benches on OFFSPEC) are identical regarding their dimensions.

### Exercise 8

In this exercise we will add the bench component to the configuration. You may notice that there aren't any bench related axes in the low motor table for the configuration - this is because the instrument config on the `REFL_TRAINING` branch is based on SURF which does not have a bench. Instead, for the purpose of this training you can repurpose `MTR0401`, `0402` and `0403`, as the bench will replace the tracking detector component in the reflectometry config anyway. If you so wish, you can rename these axes by writing to the `DESC` field of a motor axis:
- `MTR0401.DESC` should be `Bench Front Jack`
- `MTR0402.DESC` should be `Bench Back Jack`
- `MTR0403.DESC` should be `Bench Slide`

You can add the bench component like so (
[Documentation on parameters required for `BenchSetup` can be found here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Configuration#required-1)):

`bench = add_component(BenchComponent("bench", BenchSetup( ... )))`

You then need to add parameters for the Change Axes `POSITION`, `ANGLE` and `SEESAW`, as well as drivers for Change Axes `JACK_FRONT`, `JACK_REAR` and `SLIDE`. 

Remember also that Theta is now calculated by the angle of the bench, rather than the height of the detector component, which needs to be reflected in the configuration with the `theta.add_angle_of` method!

### [< Previous: Engineering Corrections](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-7) 
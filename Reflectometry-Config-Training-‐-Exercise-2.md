> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 2

# Building up the Beamline Model

We have now added a single node of the beamline model to the configuration. Every reflectometry configuration is fundamentally just a series of nodes just like this supermirror, with varying parameters to configure how exactly the transformations between Motor Axes and High-level parameters should work. 

It is worth repeating that the order in which components, parameters and drivers appear in the config matters - items closer to the source of the neutron beam should appear in the file before items closer to the detector. They need to be ordered, because conceptually, we only want a change in the beam model to affect components further downstream, and practically, because these items are linked by listeners so that any change can recursively trigger downstream components to recalculate their relative positions.

In the previous exercise, we created parameters of type `AxisParameter`. These represent positions along one of the possible movement axis for a given component, indicated by the `ChangeAxis` parameter. We have other types of parameter, too. One of those is `DirectParameter` - these bypass the whole Component / IocDriver stack and directly wrap a Motor PV i.e. the reported value will reflect what the Motor PV reports. This type of parameter provides less functionality some of which we will discuss later (e.g. move synchronization or engineering corrections), but they are very easy to set up where that is all we need. The reason we have these in the reflectometry server rather than just interacting with the motor PV directly is so we can make them follow the same convention as all other reflectometry parameters, meaning they look the same on the front panel and they provide the same separation between entering a setpoint and applying it.


In the following exercise, we will add some parameters for Slit gaps & centres (which are a type of DirectParameter), and flesh out the beamline a bit more and solidify what we learned in the last exercise.

## Exercise 2

Add the following items to your configuration:
- Slit 1: Should have VG, VC, HG, HC parameters as well as a linear height offset.
- (from Exercise 1): Supermirror, unchanged
- Slit 2: Equivalent to Slit 1 but using the right axes
- Sample: Should have parameters PHI and SA_OFFSET which drive the angle and height relative to the reflected beam. Should also have PSI and TRANS parameters.

Additional notes:
- Perhaps counterintuitively, we do not want the sample to change the beam path! While the sample reflects the beam in the physical world, in the reflectometry server this is handled via a special parameter "Theta" which we will talk about more later. We do, however, want this component to track the beam in both height and angle.
- Jaws records should already be configured on the `REFL_TRAINING` branch
- You can add slit parameters to your config with a helper method, e.g.:`add_slit_parameters(slit_number=1, include_centres=True)`

### To Test
Once you have added all these components, you should now be able to set the parameters and see the related motor axes move as in the previous exercise. You now also have enough in your beamline model to see beamline parameters react to changes in the beam:
1. Make sure all parameters are at 0 to start with
1. Set an angle SP for `sm_angle`. I recommend 22.5 as this results in a reflection angle of 45 degrees - this produces tracked positions for downstream components that are easy to understand. 
1. When you move `sm_angle` to this setpoints you should now see the RBV of all downstream components change. This is because while the physical axes have not moved, the *beam* has, so their relative positions are now different.
    - `s2_offset` should read equivalent to its distance due to the 45 degree angle i.e. **-10** (negative because it is still centred on the natural beam i.e. below the new reflected beam
    - `sa_offset` similar to `s2_offset` i.e. should be at -20
    - `sa_phi` as still sitting perpendicular to the natural beam, but the reflected beam has been bounced up 45 degrees, i.e. this should now read back -45 
1. If you now click move on any of the downstream parameters, you should see it re-apply its last SP of 0, i.e. move to re-centre itself on the new, reflected beam. The Motor axis should now read back the offset required to move these parameters back into the beam i.e. 10, 20 and 45 respectively.


### [< Previous: The Basics](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-1) || [Next: Modes](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-3)>

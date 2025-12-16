# Exercise 2 - Beamline Model

We have now added a single node of the beamline model to the configuration. Every reflectometry configuration is fundamentally just a series of nodes just like this supermirror, with varying parameters to configure how exactly the transformations between Motor Axes and High-level parameters should work. 

It is worth repeating that the order in which components, parameters and drivers appear in the config matters - items closer to the source of the neutron beam should appear in the file before items closer to the detector. They need to be ordered, because conceptually, we only want a change in the beam model to affect components further downstream, and practically, because these items are linked by listeners so that any change can recursively trigger downstream components to recalculate their relative positions.

In the previous exercise, we created parameters of type `AxisParameter`. These represent positions along one of the possible movement axis for a given component, indicated by the `ChangeAxis` parameter. We have other types of parameter, too. One of those is `DirectParameter` - these bypass the whole Component / IocDriver stack and directly wrap a Motor PV i.e. the reported value will reflect what the Motor PV reports. This type of parameter provides less functionality some of which we will discuss later (e.g. move synchronization or engineering corrections), but they are very easy to set up where that is all we need. The reason we have these in the reflectometry server rather than just interacting with the motor PV directly is so we can make them follow the same convention as all other reflectometry parameters, meaning they look the same on the front panel and they provide the same separation between entering a setpoint and applying it.


In the following exercise, we will add some parameters for Slit gaps & centres (which are a type of DirectParameter), and flesh out the beamline a bit more and solidify what we learned in the last exercise.

## Exercise 2
At the end of this exercise your beamline model should have the following items (in this order):
- Slit 1, with a height
- a supermirror, with a height and an angle (as was set up in exercise 1)
- Slit 2, with a height
- A sample stack, with height, translation, phi, and psi axes.

### 1. Add Slit 1
Slit 1 exists on our imaginary beamline between the source and the supermirror, this means it will have to be added to the beamline model before the supermirror.
The slits have already been set up with the addition of the `jaws.cmd` during the setup.
You will need to add a constant for the distance to these slits, `S1_Z`, which needs to be set to `10.0`.
You can add slit parameters to your config with a helper method, e.g.:`add_slit_parameters(slit_number=1, include_centres=True)`, for this slit set the centres should be included.
As with the supermirror in the previous exercise add a component for the slits, using `0.0`, `S1_Z`, and the `NATURAL_ANGLE` to set the `PositionAndAngle` of the component.
Add another parameter here, but this time the axis paramter is a `POSITION` related to the height of the slit set.
Add the driver for that parameter pointing at `MTR0301`.

### 2. Add Slit 2
Slit 2 exists on our imaginary beamline after the supermirror.
The slits have already been set up with the addition of the `jaws.cmd` during the setup.
You will need to add a constant for the distance to these slits, `S2_Z`, which needs to be set to `S1_Z + 10`. Whilst these distances can be absoute, they are often given as relative to the previous item on the beamline.
Add the slit parameters to your config with the helper method, including the centres and making sure you set the `slit_number` to `2`.
As previously add a component for these slits, using `0.0`, `S2_Z`, and the `NATURAL_ANGLE` to set the `PositionAndAngle` of the component.
Add another parameter here, but this time the axis paramter is a `POSITION` related to the height of the slit set.
Add the driver for that parameter pointing at `MTR0302`.

### 3. Add the Sample stack
The sample is placed after Slits 2.
We added in the axes for this during the setup via the `axes.cmd`.
Again, a distance will be needed, this time it is `SAMPLE_Z` and should be set to `S2_Z + 10.0`.
Add parameters and drvers for the height, translation, phi, and psi. 
The height (or vertical position) is a `POSITION` axis, on motor `MTR0307`, phi (or the pitch) is an `ANGLE` on `MTR0306`, psi (or the roll) is a `PSI` on `MTR0308`, and the translation (or horizontal position) is a `TRANS` on `MTR0305`.
Perhaps counterintuitively, we do not want the sample to change the beam path! While the sample reflects the beam in the physical world, in the reflectometry server this is handled via a special parameter "Theta" which we will talk about more later. We do, however, want this component to track the beam in both height and angle, so it's a `TiltingComponent`.

## To Test
Once you have added all these components, you should now be able to set the parameters and see the related motor axes move as in the previous exercise. You now also have enough in your beamline model to see beamline parameters react to changes in the beam.
1. Go to the table of motors and make sure all are at a `0` position.
1. Restart the IOC to pick up the updated `config.py`.
1. Set an angle SP for `sm_angle`. I recommend 22.5 as this results in a reflection angle of 45 degrees - this produces tracked positions for downstream components that are easy to understand. 
1. When you move `sm_angle` to this setpoint you should now see the RBV of all downstream components change. This is because while the physical axes have not moved, the *beam* has, so their relative positions are now different.
    - `s2_offset` should read equivalent to its distance due to the 45 degree angle i.e. **-10** (negative because it is still centred on the natural beam i.e. below the new reflected beam
    - `sa_offset` similar to `s2_offset` i.e. should be at -20
    - `sa_phi` as still sitting perpendicular to the natural beam, but the reflected beam has been bounced up 45 degrees, i.e. this should now read back -45 
1. If you now click move on any of the downstream parameters, you should see it re-apply its last SP of 0, i.e. move to re-centre itself on the new, reflected beam. The Motor axis should now read back the offset required to move these parameters back into the beam i.e. 10, 20 and 45 respectively.

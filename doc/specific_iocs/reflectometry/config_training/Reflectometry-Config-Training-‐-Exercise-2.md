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
Add another parameter here, but this time the axis parameter is a `POSITION` related to the height of the slit set, which has to be called `S1OFFSET`.
Add the driver for that parameter pointing at `MTR0301`.

### 2. Add Slit 2
Slit 2 exists on our imaginary beamline after the supermirror.
The slits have already been set up with the addition of the `jaws.cmd` during the setup.
You will need to add a constant for the distance to these slits, `S2_Z`, which needs to be set to `S1_Z + 10`. Whilst these distances can be absolute, they are often given as relative to the previous item on the beamline.
Add the slit parameters to your config with the helper method, including the centres and making sure you set the `slit_number` to `2`.
As previously add a component for these slits, using `0.0`, `S2_Z`, and the `NATURAL_ANGLE` to set the `PositionAndAngle` of the component.
Add another parameter here, called `S2OFFSET`, with a `POSITION` axis parameter related to the height of the slit set.
Add the driver for that parameter pointing at `MTR0302`.

### 3. Add the Sample stack
The sample is placed after Slits 2.
We added in the axes for this during the setup via the `axes.cmd`.
Again, a distance will be needed, this time it is `SAMPLE_Z` and should be set to `S2_Z + 10.0`.
Add parameters and drivers for the height, translation, phi, and psi, which should be called `SAMPOFFSET`, `SAMPTRANS`, `SAMPPHI`, and `SAMPPSI`.
The height (or vertical position) is a `POSITION` axis, on motor `MTR0307`, phi (or the pitch) is an `ANGLE` on `MTR0306`, psi (or the roll) is a `PSI` on `MTR0308`, and the translation (or horizontal position) is a `TRANS` on `MTR0305`.
Perhaps counterintuitively, we do not want the sample to change the beam path! While the sample reflects the beam in the physical world, in the reflectometry server this is handled via a special parameter "Theta" which we will talk about more later. We do, however, want this component to track the beam in both height and angle, so it's a `TiltingComponent`.

## To Test
Once you have added all these components, you should now be able to set the parameters and see the related motor axes move as in the previous exercise. You now also have enough in your beamline model to see beamline parameters react to changes in the beam.
1. Go to the table of motors and make sure all are at a `0` position.
2. Restart the IOC to pick up the updated `config.py`.
3. When you look at the `Front Panel` you should now see fewer disconnected items, similarly there should be more values available in the following tabs.
4. If you go to the `Collimation` tab, and set the SP of `SMANGLE` to `22.5` (this results in a reflection angle of 45 degrees - which produces tracked positions for downstream components that are easy to understand), when you click on `Move` you should now see the RBV of all downstream components change. This is because while the physical axes have not moved, the *beam* has, so their relative positions are now different.
    - `S2OFFSET` should read equivalent to its distance due to the 45 degree angle i.e. **-10** (negative because it is still centred on the natural beam i.e. below the new reflected beam
    - `SAMPOFFSET` similar to `S2OFFSET` i.e. should be at -20
    - `SAMPPHI` as still sitting perpendicular to the natural beam, but the reflected beam has been bounced up 45 degrees, i.e. this should now read back -45
5. At this stage, if you look at the table of motors, only the supermirror angle will have moved, everything else is reported according to the relationship to the beam.
6. If you now click move on any of the downstream parameters, you should see it re-apply its last SP of 0, i.e. move to re-centre itself on the new, reflected beam. When the move has finished the `Collimation` tab in the reflectometry perspective should have 0s for everything except `SMANGLE`. The appropriate motor axes on the table of motors should now read back the offset required to move these parameters back into the beam i.e. 10, 20 and 45 respectively, alongside the value of 22.5 for the supermirror angle.

## Solution
<details>
<summary>Should you have trouble the following is what the code could look like</summary>

```pythofrom typing import Dict

from ReflectometryServer.beamline import Beamline
from ReflectometryServer.beamline_constant import BeamlineConstant
from ReflectometryServer.components import (
    Component,
    ReflectingComponent,
    TiltingComponent,
)
from ReflectometryServer.config_helper import (
    add_component,
    add_constant,
    add_driver,
    add_mode,
    add_parameter,
    add_slit_parameters,
    get_configured_beamline,
)
from ReflectometryServer.geometry import ChangeAxis, PositionAndAngle
from ReflectometryServer.ioc_driver import IocDriver
from ReflectometryServer.parameters import AxisParameter
from ReflectometryServer.pv_wrapper import MotorPVWrapper

# Beamline Constants
NATURAL_ANGLE = 90
S1_Z = 10.0
SM_Z = 20.0
S2_Z = SM_Z + 10.0
SAMPLE_Z = S2_Z + 10.0


def get_beamline(macros: Dict[str, str]) -> Beamline:
    #########################
    # FIXED BEAMLINE VALUES #
    #########################

    # Constants
    add_constant(
        BeamlineConstant(
            "NATURAL_ANGLE",
            NATURAL_ANGLE,
            "The difference between the beam and straight through",
        )
    )
    add_constant(BeamlineConstant("S1_Z", S1_Z, "The distance to slits 1"))
    add_constant(BeamlineConstant("SM_Z", SM_Z, "The distance to the supermirror"))
    add_constant(BeamlineConstant("S2_Z", S2_Z, "The distance to slits 2"))

    # Modes
    _nr = add_mode(
        "NR"
    )  # Using underscore to pass pyright as mode has to be created but is not used

    ##############################
    # BEAMLINE MODEL STARTS HERE #
    ##############################

    # Slits 1
    add_slit_parameters(1, include_centres=True)
    s1_comp = add_component(Component("s1", PositionAndAngle(0.0, S1_Z, NATURAL_ANGLE)))
    add_parameter(
        AxisParameter(
            "S1OFFSET",
            s1_comp,
            ChangeAxis.POSITION,
            description="Vertical Position of Slit 1",
        )
    )
    add_driver(IocDriver(s1_comp, ChangeAxis.POSITION, MotorPVWrapper("MOT:MTR0301")))

    # Mirror
    mirror_comp = add_component(
        ReflectingComponent("Mirror", PositionAndAngle(0, SM_Z, NATURAL_ANGLE))
    )
    add_parameter(
        AxisParameter(
            "SMANGLE",
            mirror_comp,
            ChangeAxis.ANGLE,
            description="Angle of the Supermirror",
        )
    )
    add_parameter(
        AxisParameter(
            "SMOFFSET",
            mirror_comp,
            ChangeAxis.POSITION,
            description="Vertical Position of the Supermirror",
        )
    )
    add_driver(IocDriver(mirror_comp, ChangeAxis.ANGLE, MotorPVWrapper("MOT:MTR0207")))
    add_driver(
        IocDriver(mirror_comp, ChangeAxis.POSITION, MotorPVWrapper("MOT:MTR0206"))
    )

    # Slits 2
    add_slit_parameters(2, include_centres=True)
    s2_comp = add_component(Component("s2", PositionAndAngle(0.0, S2_Z, NATURAL_ANGLE)))
    add_parameter(
        AxisParameter(
            "S2OFFSET",
            s2_comp,
            ChangeAxis.POSITION,
            description="Vertical Position of Slit 2",
        )
    )
    add_driver(IocDriver(s2_comp, ChangeAxis.POSITION, MotorPVWrapper("MOT:MTR0302")))

    # SAMPLE
    sample_comp = add_component(
        TiltingComponent("sample", PositionAndAngle(0, SAMPLE_Z, NATURAL_ANGLE))
    )
    add_parameter(
        AxisParameter(
            "SAMPOFFSET",
            sample_comp,
            ChangeAxis.POSITION,
            description="Vertical Position of Sample",
        )
    )
    add_parameter(
        AxisParameter(
            "SAMPPHI",
            sample_comp,
            ChangeAxis.ANGLE,
            description="Phi Angle of Sample (Pitch)",
        )
    )
    add_parameter(
        AxisParameter(
            "SAMPPSI",
            sample_comp,
            ChangeAxis.PSI,
            description="Psi Angle of Sample (Roll)",
        )
    )
    add_parameter(
        AxisParameter(
            "SAMPTRANS",
            sample_comp,
            ChangeAxis.TRANS,
            description="Horizontal Position of Sample",
        )
    )
    add_driver(
        IocDriver(sample_comp, ChangeAxis.POSITION, MotorPVWrapper("MOT:MTR0307"))
    )
    add_driver(IocDriver(sample_comp, ChangeAxis.ANGLE, MotorPVWrapper("MOT:MTR0306")))
    add_driver(IocDriver(sample_comp, ChangeAxis.PSI, MotorPVWrapper("MOT:MTR0308")))
    add_driver(IocDriver(sample_comp, ChangeAxis.TRANS, MotorPVWrapper("MOT:MTR0305")))

    return get_configured_beamline()

```
</details>

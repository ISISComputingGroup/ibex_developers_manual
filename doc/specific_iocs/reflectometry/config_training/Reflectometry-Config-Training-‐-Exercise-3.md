# Exercise 3 - Modes

Next, we will look at modes. Modes are a way to configure the beamline/tracking model for different types of experiment at runtime at the push of a button. Modes achieve this through a number of features:
- You can choose which parameters should automatically track the beam, i.e. they move to stay aligned to the reflected beam when it changes
- You can define a set of default parameter values to apply when you enter the mode (and optionally, to re-apply on every beamline move)
- You can choose for engineering corrections to only apply to certain modes (more on that later)

In the following exercise we will categorize the parameters we have added so far by mode and give them some default values.

## Exercise 3
### 1. Create your modes
So far there has always been a mode `_nr`, without a mode the reflectometry server, but as this variable wasn't used there is an underscore to let Pyright know that it could be ignored.
Start by removing that `_`.
Add another mode called `PNR` in the same way that `NR` is added.
Create a list `all_modes` which includes both `nr` and `pnr`.

### 2. Add modes to parameters
Give each parameter a `modes` argument follwoing on after the `AxisParameter` argument. Note that `modes` has to be a list, so if you are only applying a single mode don't forget to add square brackets.
The slit offsets should track the beam in `all_modes`.
Both of the supermirror parameters should use `pnr` mode.
The sample axes should never track the beam automatically. This is because the scientists don't want this component to move implicitly on beam changes, only when they explicitly tell it to. 

## To Test
1. Don't forget to restart the IOC to pick up the changes to `config.py` you have just made.
2. You'll likely start up in `NR` mode, and if you go to the `Collimation` tab, you should see two green Ms, by each slit offset.
3. Go back to the front panel, and you should be able to switch between the two modes using the buttons next to the status information. If you leave it on `PNR` and go back to collimation then as well as the previous green Ms by the slit offsets there should be ones alongside the supermirror parameters.
4. Assuming nothing has changed after the steps in the previous exercise, everything else should be reading as 0 on the `Collimation` tab, and if you look at the Table of Motors, then the supermirror angle is `22.5`, the slit 2 height at `10`, the sample height at `20`, and the sample phi at `45`.
5. Staying in `PNR` mode, set the `SMANGLE` to `11.25` on the `Collimation` tab.
6. The downstream values on this tab will still change with that value, except the `S2OFFSET` will end up back at 0 as it has moved with the change to the angle. The readback value of `SAMPOFFSET` and `SAMPPHI` will read as `11.716` and `22.5` respectively as these values as this is where these axes are now in relation to the beam. If you look at the Table of Motors, then the supermirror angle is now `11.25`, the slit 2 offset is `4.143`, and the sample height and phi haven't changed and are still at `20` and `45` respectively. So in this mode you can see that the height of slit 2 is moving automatically with changes to the beam.

## Solution
<details>
<summary>Should you have trouble the following is what the code could look like</summary>

```python
from typing import Dict

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
    nr = add_mode("NR")
    pnr = add_mode("PNR")
    all_modes = [nr, pnr]

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
        ),
        modes=all_modes,
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
        ),
        modes=[pnr],
    )
    add_parameter(
        AxisParameter(
            "SMOFFSET",
            mirror_comp,
            ChangeAxis.POSITION,
            description="Vertical Position of the Supermirror",
        ),
        modes=[pnr],
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
        ),
        modes=all_modes,
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

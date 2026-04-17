# Exercise 4 - Theta

Other than the properties of the sample itself, the reflectivity of surfaces and interfaces between media is dependant on the incident angle of the beam at the sample, this primary parameter is also known as Theta. For any given sample, the scientists usually take measurements at 3 or 4 different Theta angles, then stitch the data together to get the complete reflectivity profile. 

> Side note: taking more measurements at finer Theta steps would produce better data. Theoretically, scientists could take measurements at many more discrete angles, stopping and starting data collection in between, however this is impractical due to the added overhead in time and effort required for setting up each measurement. The current approach of measuring a handful of Theta is considered a "good enough" solution. 
>
> In an ideal world, we could sweep scan over the whole Theta range, taking one snapshot of data for the current Theta RBV for every ISIS pulse. Currently this is not possible as our move synchronization is not sophisticated enough to ensure a consistent alignment throughout the sweep. Solving this problem is what we mean when we talk about "Continuous Scanning". 

Setting a Theta angle is similar to setting a super mirror angle in that every component downstream from the `ThetaComponent` in the reflectometry config will be subject to the new beam path. There is an important difference however in that Theta is NOT linked to the physical angle of the sample stack. This is because the scientists do not want this angle to ever be set implicitly as it could have severe consequences if the sample is e.g. a large tank of liquid which could accidentally be angled and spill all over the blockhouse. Instead, Theta only sets the positions of downstream components for a theoretical incident angle. To ensure the actual beam follows this beam path, the sample Phi angle needs to be set to match this theoretical beam path, the Theta parameter and component are however entirely separate entities from the Sample component and angle.

Similarly, the Theta RBV is not derived from the sample Phi axis, but from an axis representing the position of the detector. At ISIS, we have two different types of detectors from a motion point of view:
1. Detectors moving on a linear height stage that can tilt towards the beam (SURF, CRISP)
1. Detectors mounted on another component that moves on an arc around the sample (POLREF, INTER, OFFSPEC)

For the former, Theta is calculated via trigonometry, where the Detector Height is the Adjacent, and the distance between Sample and Detector is the Opposite side of the right angle triangle. For the latter, the component the detector is mounted on (= a bench or vacuum tank) will have a rotation axis that we can use as readback.

From a config point of view, we can provide the `ThetaComponent` with a list of downstream components from which Theta's RBV can be derived. This is a list as some beamlines may use one of several detectors. Theta will look for the next component in the list that is currently active in the beam and derive it's angle from it. 

As an example, let's say our beamline has a structure of `Beam Source - Sample - Point Detector - Linear Detector` where both detectors are driven by linear height stages. If both detectors are in the beam, Theta will derive its value from the Point Detector Height axis. If the point detector is parked out of the beam, Theta will derive its value from the Linear Detector Height axis.

> Side note: The arc detector solution is technically superior as it maintains a constant distance between sample and detector, meaning e.g. Time of Flight is not dependant on Theta. This produces a slight inaccuracy for SURF and CRISP, however due to the optical lever on those beamlines being fairly short the effect is small enough to be ignored.

## Exercise 4
In this exercise, let's add Theta and a detector component from which we can derive its value to our beamline model. For this exercise, we will assume we are using the setup that is found on SURF and CRISP, i.e. a detector that can move up and down on a linear height axis, and tilt towards the beam via a separate rotation axis. (we will look at a bench setup in a later exercise).
At the end of this exercise your bemline should have the following in order:
* Slit 1, with a height (as was set up in exercise 2)
* a supermirror, with a height and an angle (as was set up in exercise 1)
* Slit 2, with a height (as was set up in exercise 2)
* A sample stack, with height, translation, phi, and psi axes (as was set up in exercise 2)
* A theta component
* A detector, with a height and an angle

### 1. Add in the Theta Component and Parameter
Because Theta is related in reality to the sample position, this component should be added next to the sample stack. Because we don't want theta to influence the sample stack, as explained above, it should be put directly after the sample stack if using one. In our imaginary beamline, we are keeping the sample stack in.
Theta has it's own component type, `ThetaComponent`. This component has the added functionality of being able to listen to a different component from which to derive it's values.
The (virtual) Theta component's coordinates need to match the (real) Sample Components coordinates, so you should using `0.0`, `SAMPLE_Z`, and the `NATURAL_ANGLE` to set the PositionAndAngle of the component. 
The `Theta` parameter itself is just a simple Axis Parameter, same as we added for the supermirror in Exercise 1. This parameter is used in `all_modes`.

### 2. Add in the detector component
Start by creating the constant for `DET_Z`, which is the distance to the detector, and for this exercise will be `SAMPLE_Z` + `10.0`. 
The detector is added after Theta, and is another `TiltingComponent`. The `PositionAndAngle` setup should be set to `0.0`, `DET_Z`, and the `NATURAL_ANGLE`.
We also need to add 2 parameters, the angle and the height, which will be referenced to `MTR0201` and `MTR0202` respectedly, and are available in all modes. This is done in the same way as items were added in previous exercises.

At this point you can restart the IOC and you should be able to see the detector height and angle parameters as with everything we have added previously. The angle should be reading `22.5` and the height `-4.142`, whilst on the table of motors both are at `0.0`. Theta should also be there and read `NaN` as we have not yet told it what axis it should derive its value from. Similarly the downstream `RBV` value on the `Collimation` tab will be `NaN`, as they are downstream of something unknown. At this point you can move those axes like the others.

### 3. Linking the detector and Theta
The ThetaComponent provides the methods `add_angle_to(component)` to do this for a linear height axis, or `.add_angle_of(component)` for an arc component.
Add in the detector component created above as a linear axis.

## To Test
1. Go to the table of motors and make sure all are at a `0` position.
2. Restart the IOC to pick up the updated `config.py`.
3. If you go to the Collimation tab and set `Theta` to `22.5` the readbacks there should stay as `0.0` after the move. If you check the table of motors, then the detector angle should now read `45 deg`, and the height will be `10.0`. That height is the difference between Theta and the detector components.

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
    ThetaComponent,
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
DET_Z = SAMPLE_Z + 10.0


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
    add_constant(BeamlineConstant("DET_Z", DET_Z, "The distance to the detector"))

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
    
    # THETA
    theta_comp = add_component(
        ThetaComponent("ThetaComp", PositionAndAngle(0.0, SAMPLE_Z, NATURAL_ANGLE))
    )
    add_parameter(
        AxisParameter(
            "THETA",
            theta_comp,
            ChangeAxis.ANGLE,
            description="Incident Angle at Sample",
        ),
        modes=all_modes,
    )
    
    # DETECTOR
    det_comp = add_component(
        TiltingComponent("Detector", PositionAndAngle(0.0, DET_Z, NATURAL_ANGLE))
    )
    add_parameter(
        AxisParameter(
            "DETANGLE", det_comp, ChangeAxis.ANGLE, description="Angle of Detector"
        ),
        modes=all_modes,
    )
    add_parameter(
        AxisParameter("DETHEIGHT", det_comp, ChangeAxis.POSITION, description="Vertical Position of Detector"),
        modes=all_modes,
    )
    add_driver(IocDriver(det_comp, ChangeAxis.ANGLE, MotorPVWrapper("MOT:MTR0201")))
    add_driver(IocDriver(det_comp, ChangeAxis.POSITION, MotorPVWrapper("MOT:MTR0202")))
    theta_comp.add_angle_to(det_comp)

    return get_configured_beamline()
```

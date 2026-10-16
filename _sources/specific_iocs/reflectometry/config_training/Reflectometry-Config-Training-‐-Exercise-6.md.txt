# Exercise 6 - Optional Features

## `autosave`
With autosave set to `True`, if you change a value when the reflectometry server is not running it should come back with the last SP before IOC restart. Without, it should come back with the current RBV applied as SP. This is usually desired for parameters which are assigned to variables, which is why you will get a warning if you don't add this to the `AxisParameter`.

## `characteristic_value`
Sometimes, scientists want to be able to see a beamline parameter and the low level axis it derives its value from side by side for diagnostics purposes. You can do this by "tagging" a beamline parameter with the relevant axis e.g. `AxisParameter(..., characteristic_value="MOT:MTR0101")`. This will just make the value for the given PV display next to the parameter, there is nothing too clever happening under the hood.

## `DirectParameter`
A type of beamline parameter that forgoes the `Component` and `IocDriver` layers, and directly mirrors the value from a given `PvWrapper` instead. We use this in instances where we want a parameter on the front panel but what the parameter controls is completely independent of the beam path. Slit Gap and Centre parameters are instances of `DirectParameter` for example.

## Exercise 6
### 1. Add a `characteristic_value`
Go to the `AxisParameter` creation for the sample offset, and add in the `chatacteristic_value` parameter after the description, and assign it to `MOT:MTR0307` in our fictitious beamline. 

### 2. Add a `DirectParameter`
Create this somewhere in the config file, call it `MONITORPOS`, give it a `pv_wrapper` value of a `MotorPVWrapper` pointing at `MOT:MTR0208` which in our beamline is the axis controlling the position of the monitor. Don't forget to import `DirectParameter` from `ReflectometryServer.parameters`.

## Testing
1. Go to the table of motors and make sure all are at a 0 position.
2. Restart the IOC to pick up the updated config.py.
3. On the `Collimation Plane Parameters` tab, the `SAMPOFFSET` parameter should now have a label alongside it, reading `0.0`.
4. Set the `SMANGLE` to `22.5`. Whilst the `RDB` for `SAMPOFFSET` should update to `-20.0` the label should remain at `0.0`, that difference is equal to the displacement of the reflected beam.
5. Go now to the `Slit Parameters` page and you should see the direct parameter created above listed in there, in the appropriate place in the list in relation to the slit sets. If you set this parameter, then the appropriate axis on the table of motors should move with it with no differences seen.

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
from ReflectometryServer.out_of_beam import OutOfBeamPosition
from ReflectometryServer.parameters import AxisParameter, DirectParameter, InBeamParameter
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
    
    # Direct Parameters
    add_parameter(
        DirectParameter(
            "MONITORPOS",
            pv_wrapper=MotorPVWrapper("MOT:MTR0208"),
            description="Vertical pos of beam monitor",
        )
    )

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
    add_parameter(
        InBeamParameter("SMIN", mirror_comp, description="Toggle Supermirror In Beam"),
        modes=all_modes,
        mode_inits=[(nr, 0), (pnr, 1)],
    )
    add_driver(
        IocDriver(
            mirror_comp,
            ChangeAxis.ANGLE,
            MotorPVWrapper("MOT:MTR0207"),
            out_of_beam_positions=[OutOfBeamPosition(0.0)],
        )
    )
    add_driver(
        IocDriver(
            mirror_comp,
            ChangeAxis.POSITION,
            MotorPVWrapper("MOT:MTR0206"),
            out_of_beam_positions=[OutOfBeamPosition(-20.0)],
        )
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
            characteristic_value="MOT:MTR0307",
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
    add_parameter(
        InBeamParameter(
            "SAMPIN", 
            sample_comp, 
            description="Toggle Sample In Beam",
        )
    )
    add_driver(
        IocDriver(sample_comp, ChangeAxis.POSITION, MotorPVWrapper("MOT:MTR0307"))
    )
    add_driver(IocDriver(sample_comp, ChangeAxis.ANGLE, MotorPVWrapper("MOT:MTR0306")))
    add_driver(IocDriver(sample_comp, ChangeAxis.PSI, MotorPVWrapper("MOT:MTR0308")))
    add_driver(
        IocDriver(
            sample_comp, 
            ChangeAxis.TRANS, 
            MotorPVWrapper("MOT:MTR0305"),
            out_of_beam_positions=[OutOfBeamPosition(100.0)],
        )
    )
    
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

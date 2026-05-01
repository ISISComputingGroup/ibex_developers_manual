# Exercise 7 - Engineering Corrections

See the [Engineering Corrections Wiki Page](#reflectometry_engineering_offset) for more detail.

Engineering corrections are offsets that are added to set points at the Driver level before they are sent off to the underlying motor axes, and subtracted from the readback value before it is propagated up to the component level. These are used to account for inaccuracies in the physical engineering of the beamline. For instance, in the perfect world of the beamline geometry model, all mirrors are perfectly flat and extend into infinite space, whereas in reality, they may be slightly concave or the neutrons hit it off the centre of rotation so that you get slight drift for different mirror angles.

We have different types of engineering corrections, namely:
- `ConstantCorrections` - a static offset
- `UserFunctionCorrection` - a variable offset based on a set of input parameters
- `InterpolatedDataCorrection` - a lookup table of corrections, interpolating values in between discrete points in the matrix
Any of the above can also be made to apply for specific modes only.

## Exercise 7
Here we will add corrections to the detector, as we will be considering things against actual motor values do consider adding in charactaristic values to the detector height and angle to save on moving between views.

### 1. Add a constant correction
Create a `constant_correction` variable using the `ConstantCorrection` function with a value of `0.3`
Add this as an `engineering_correction` to the driver for the detector angle.

### 2. Add a user function correction
Create a function in your config file for this training, normally it would probably be cleaner to put these functions in a separate file and import them.
This function should take in a float, and return that float mulitplied by `0.1`
For our example, let's use the supermirror angle as the source for our float, which is already defined as a parameter. However, to use this that parameter will need to be assigned to a variable, so make sure you do that.
It's also a good idea to specify an autosave on any parameter you use like this, that way even if the motor is moved it is easy to see what the setpoint was. If you don't, then there will be a warning displyed.
To use this function create a variable that calls `UserFunctionCorrection`, supplying it with the namce of the function you have just created, and the `BeamlineParameter` to use, in this case use the variable you have just created. Apply this correction to the detector height.

## To Test
1. Before doing anything else, have a look at your collimation panel, if it is in the same state as it was before then `theta` is currently `-45.0`, the detector angle is `90.0` and the detector height is `20.0`. Your supermirror angle should be at `22.5`.
2. Set everything to `0.0` on the collimation panel.
3. Set `theta` to `2.0`. Note that the height and angle for the detector will still read `0.0` (or very close to that value), whilst the motors will read `4.0` for the angle and `0.7` for the height.
4. Go to the table of motors and make sure all are at a 0 position.
5. Restart the IOC to pick up the updated config.py.
6. If you look at the collimation tab in the reflectometry server view you will now see that the detector angle is reading `-0.3`, this is the correction from `0.0` applied by the constant created during this exercise. If you look at the table of motors (or the characteristic value if you set it up) you will see that the motor position is still `0.0`.
7. Set `theta` to `2.0`.
8. At this point, the detector angle and height should still be reading as `-0.3` and `0.0`, but, the motors themselves have moved to `4.0` and `0.7` respectively, to maintain that theta value.
9. Set everything back to `0.0` on the collimation panel tab. All actual motor position should be `0.0`, apart from the detector angle, which will now be `0.3` having had the constant value applied. It may be worth restarting the IOC again for clarity in the next steps.
12. Set the supermirror angle to `22.5`. Looking at the values when the move completes, `theta` is again `-45.0`, the detector angle is instead `44.7`, and the detector height is `-12.25`. All the motor positions shuold be `0.0`.

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
from ReflectometryServer.engineering_corrections import ConstantCorrection, UserFunctionCorrection
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


def correction_function(_: None, param: float) -> float:
    return param * 0.1



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
    SMANGLE = add_parameter(
        AxisParameter(
            "SMANGLE",
            mirror_comp,
            ChangeAxis.ANGLE,
            description="Angle of the Supermirror",
            autosave=True,
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
    constant_correction = ConstantCorrection(0.3)
    function_correction = UserFunctionCorrection(correction_function, SMANGLE)
    
    det_comp = add_component(
        TiltingComponent("Detector", PositionAndAngle(0.0, DET_Z, NATURAL_ANGLE))
    )
    add_parameter(
        AxisParameter(
            "DETANGLE", det_comp, ChangeAxis.ANGLE, description="Angle of Detector", characteristic_value="MOT:MTR0201",
        ),
        modes=all_modes,
    )
    add_parameter(
        AxisParameter("DETHEIGHT", det_comp, ChangeAxis.POSITION, description="Vertical Position of Detector", characteristic_value="MOT:MTR0202",),
        modes=all_modes,
    )
    add_driver(
        IocDriver(
            det_comp, 
            ChangeAxis.ANGLE, 
            MotorPVWrapper("MOT:MTR0201"), 
            engineering_correction=constant_correction,
        )
    )
    add_driver(
        IocDriver(
            det_comp, 
            ChangeAxis.POSITION, 
            MotorPVWrapper("MOT:MTR0202"),
            engineering_correction=function_correction,
        )
    )
    theta_comp.add_angle_to(det_comp)

    return get_configured_beamline()
```

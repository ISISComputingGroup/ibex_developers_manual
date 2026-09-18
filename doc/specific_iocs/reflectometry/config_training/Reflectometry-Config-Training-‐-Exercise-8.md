# Exercise 8 - The Bench

## The Bench

[More detail on the Bench Configuration available here](../reflectometry-bench-configuration).

The bench is a large motion component which moves on an arc around a given pivot point (i.e. the last point where the beam may bounce before the bench). The reason for this is that we want to keep the detector at a constant distance from the sample for all experiments to preserve e.g. Time of Flight regardless of Theta. In case you are wondering how this is handled on beamlines that use a detector driving on a linear height stage, the answer is they do not. However, those instruments (i.e. CRISP and SURF) have an optical lever short enough that they can ignore this factor without sacrificing too much quality. Other devices (such as slits and detectors) can be mounted statically on top of it while the bench handles all the beam tracking. Benches are used for the POLREF secondary beam path (everything after the sample) and for the OFFSPEC primary & secondary beam path.

This component is special compared to the rest of the Reflectometry server as it provides a much more dramatic transformation between motor- and control axes. The control axes provided by the bench component and settable as parameters are
- Height 
- Angle - pivoting around the last point of reflection
- Seesaw - pivoting around the centre of rotation of the bench itself - used for alignment only

The physical motor axes are:
- Front Height Jack
- Back Height Jack
- A slide towards/ away from the pivot point (used to maintain a static distance)

The transformation between these two sets of axes happens in the BenchComponent, using maths provided to us by the POLREF scientists.

In terms of the configuration, the bench takes a `BenchSetup` object instead of the usual `PositionAndAngle`, which defines the specific geometry of the bench. It is worth noting that all the benches (i.e. Detector bench on POLREF and the Front- and Detector benches on OFFSPEC) are identical regarding their dimensions.

## Exercise 8
### 1. Comment out the existing tracking detectors
We shall consider here a post sample bench, which replaces the tracking detector component usually. However, as this is a simulated beamline we can use the appropriate motors set up initially. however, as everything else stays valid, just put the detector part of `config.py` into a block comment.

### 2. Add the bench constants
Add in `BENCH_PIVOT_Z` and set it to `SAMPLE_Z`, as that is the ideal pivot point. Also create `BENCH_FRONT_Z` which is `10.0` from `BENCH_PIVOT_Z`, `BENCH_PIVOT_TO_FRONT` and set it to `10.0`, `BENCH_PIVOT_TO_REAR` and set it to `20.0`, and `BENCH_PIVOT_TO_BEAM` and set it to `5.0`.
We also need to add in the concept of both the `NATURAL_ANGLE` we've been using throughout and the `ANGLE_OF_MOVEMENT`. Rename `NATURAL_ANGLE` to `ANGLE_OF_MOVEMENT` throughout and add in a new `NATURAL_ANGLE` of `0.0`. Update the `ANGLE_OF_MOVEMENT` to be the `NATURAL_ANGLE` + `90.0`.

### 3. Add the bench component
Use the bench component helper method, and the associated setup to create the bench as per: `bench = add_component(BenchComponent("bench", BenchSetup( ... )))`.
Both `BenchComponent` and `BenchSetup` are in `ReflectometryServer.components`.
Give the setup the following arguments: `0.0`, `BENCH_PIVOT_Z`, `ANGLE_OF_MOVEMENT`, `BENCH_PIVOT_TO_FRONT`, `BENCH_PIVOT_TO_REAR`, `NATURAL_ANGLE`, `BENCH_PIVOT_TO_BEAM`, `0.0`, and `10.0`.

### 4. Add parameters and drivers for the bench
We need to add the parameters for the Change Axes `POSITION`, `ANGLE` and `SEESAW`, as well as drivers for Change Axes `JACK_FRONT`, `JACK_REAR` and `SLIDE` which are associated with `MOT:MTR0203`, `MOT:MTR0204`, `MOT:MTR0205` respectively.

### 5. Add the bench to `theta`
This time you are using the `theta.add_angle_of` method, and asking it to use the bench which is a different method to the one used by the detector previously.

## To Test
1. Set everything to `0.0`.
2. Restart the IOC to pick up the updated `config.py`.
3. The collimation panel should now have swapped out the detector entries for the bench angle and offset. The bench seesaw parameter should have been added to the other parameters tab.
4. Set the supermirror angle to `22.5`, and `theta` to `2.0`, use the move all button to set both values at the same time.
5. After the move, everything in the reflectometry server should be reading `0.0`, but the motors will be reading quite different values, as those are maintaining the transformed values to be `0.0`. The bench front should have gone to `29.785`, the back to `41.288`, and the slide to `0.578`.

## Solution
<details>
<summary>Should you have trouble the following is what the code could look like</summary>

```python
from typing import Dict

from ReflectometryServer.beamline import Beamline
from ReflectometryServer.beamline_constant import BeamlineConstant
from ReflectometryServer.components import (
    BenchComponent,
    BenchSetup,
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
NATURAL_ANGLE = 0.0
ANGLE_OF_MOVEMENT = NATURAL_ANGLE + 90.0
S1_Z = 10.0
SM_Z = 20.0
S2_Z = SM_Z + 10.0
SAMPLE_Z = S2_Z + 10.0
DET_Z = SAMPLE_Z + 10.0
BENCH_PIVOT_Z = SAMPLE_Z
BENCH_FRONT_Z = BENCH_PIVOT_Z + 10.0
BENCH_PIVOT_TO_FRONT = 10.0
BENCH_PIVOT_TO_REAR = 20.0
BENCH_PIVOT_TO_BEAM = 5.0


def correction_function(_: None, param: float) -> float:
    return param * 0.1



def get_beamline(macros: Dict[str, str]) -> Beamline:
    #########################
    # FIXED BEAMLINE VALUES #
    #########################

    # Constants
    add_constant(
        BeamlineConstant(
            "ANGLE_OF_MOVEMENT",
            ANGLE_OF_MOVEMENT,
            "The difference between the beam and straight through",
        )
    )
    add_constant(BeamlineConstant("S1_Z", S1_Z, "The distance to slits 1"))
    add_constant(BeamlineConstant("SM_Z", SM_Z, "The distance to the supermirror"))
    add_constant(BeamlineConstant("S2_Z", S2_Z, "The distance to slits 2"))
    add_constant(BeamlineConstant("DET_Z", DET_Z, "The distance to the detector"))
    add_constant(BeamlineConstant("BENCH_PIVOT_Z", BENCH_PIVOT_Z, "The distance to the bench pivot point"))
    add_constant(BeamlineConstant("BENCH_FRONT_Z", BENCH_FRONT_Z, "The distance to the front of the bench"))
    add_constant(BeamlineConstant("BENCH_PIVOT_TO_FRONT", BENCH_PIVOT_TO_FRONT, "The distance from the bench pivot point to the front of the bench"))
    add_constant(BeamlineConstant("BENCH_PIVOT_TO_REAR", BENCH_PIVOT_TO_REAR, "The distance from the bench pivot point to the rear of the bench"))
    add_constant(BeamlineConstant("BENCH_PIVOT_TO_BEAM", BENCH_PIVOT_TO_BEAM, "The distance from the bench pivot point to the beam"))

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
    s1_comp = add_component(Component("s1", PositionAndAngle(0.0, S1_Z, ANGLE_OF_MOVEMENT)))
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
        ReflectingComponent("Mirror", PositionAndAngle(0, SM_Z, ANGLE_OF_MOVEMENT))
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
    s2_comp = add_component(Component("s2", PositionAndAngle(0.0, S2_Z, ANGLE_OF_MOVEMENT)))
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
        TiltingComponent("sample", PositionAndAngle(0, SAMPLE_Z, ANGLE_OF_MOVEMENT))
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
        ThetaComponent("ThetaComp", PositionAndAngle(0.0, SAMPLE_Z, ANGLE_OF_MOVEMENT))
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
 
    """ 
    Comment out for Exercise 8 
    # DETECTOR
    constant_correction = ConstantCorrection(0.3)
    function_correction = UserFunctionCorrection(correction_function, SMANGLE)
    
    det_comp = add_component(
        TiltingComponent("Detector", PositionAndAngle(0.0, DET_Z, ANGLE_OF_MOVEMENT))
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
    """

    # BENCH
    bench = add_component(
        BenchComponent(
            "bench",
            BenchSetup(
                0.0,
                BENCH_PIVOT_Z,
                ANGLE_OF_MOVEMENT,
                BENCH_PIVOT_TO_FRONT,
                BENCH_PIVOT_TO_REAR,
                NATURAL_ANGLE,
                BENCH_PIVOT_TO_BEAM,
                0.0,
                10.0,
            ),
        )
    )
    
    add_parameter(AxisParameter("B_ANGLE", bench, ChangeAxis.ANGLE), modes=all_modes)
    add_parameter(AxisParameter("B_OFFSET", bench, ChangeAxis.POSITION), modes=all_modes)
    add_parameter(AxisParameter("B_SEESAW", bench, ChangeAxis.SEESAW), modes=all_modes)

    add_driver(IocDriver(bench, ChangeAxis.JACK_FRONT, MotorPVWrapper("MOT:MTR0203")))
    add_driver(IocDriver(bench, ChangeAxis.JACK_REAR, MotorPVWrapper("MOT:MTR0204")))
    add_driver(IocDriver(bench, ChangeAxis.SLIDE, MotorPVWrapper("MOT:MTR0205")))

    theta_comp.add_angle_of(bench)
    
    return get_configured_beamline()
```

# Exercise 5 - Parking Components

## Parking Components

As we briefly touched on in a previous section, the beamline occasionally needs be re-configured by moving components in or out of the beam. This could be a polariser when switching between NR and PNR mode, moving the sample out of the beam to record the base neutron flux, moving everything out of the way of the laser (and back in) for alignment, among many more reasons. In order to facilitate this action, the reflectometry server provides `InBeam Parameters`, a toggle parameter type for moving a given component in or out of the beam. This is an abstraction layer for applying one out of a set of pre-defined, named numerical positions. As the `InBeam Parameter` is applied at the component level, this may set those pre-defined positions on multiple axes of that component. 

When you move a component out of the beam, it's offset Setpoints and `SP:RBV`s are preserved but each axis physically moves to its park position (if defined). Once it's parked, a component will not track or change the beam path in the beamline model. You should also see the move button for other parameters on this component being locked on the OPI for this reason.

When you move a component into the beam, each parked axis returns to its SP:RBV and it can become part of the active tracking model again (if all other conditions are met too e.g. its part of the current mode).

## Design Rationale
These parameters function very similarly to [Motion Set Points](/specific_iocs/motor_extensions/Motion-Set-points). There are a few reasons why we integrated these into the reflectometry server as a parameter type rather than just using motion setpoints:
- As for other Parameters, they provide the option to enter a setpoint without applying it
- The in/out of beam status affects the beam tracking model, e.g. `sm_angle` will be ignored for the beam path if the super mirror component is parked
- `InBeam` Parameters allow for [more sophisticated parking behaviour](#reflectometry_parking_sequences), such as 
    - moving through a sequence of positions when parking in special cases where the linear path is physically obstructed on the beamline
    - applying one of several possible parked positions depending on the beam position in cases where we might accidentally obstruct it otherwise. e.g. Park High for low angled beam, Park Low for high angled beam.

## Exercise 5

### 1. Add an in beam parameter to the supermirror
Adding in this kind of parameter is very similar to other parameters, `add_parameter(InBeamParameter("comp_in", some_compon, description=""),modes=[mode], mode_inits=[(mode, value)])`. Whilst it is typically best practice to only include this in appropriate modalities, for now keep this in `all_modes`. To initialise the value of this parameter for specific modes use the `mode_inits` list, at the moment set this to `0` for `nr`, and `1` for `pnr`.
Add the information for the parked position to the existing drivers using the parameter `out_of_beam_positions` setting it to a list containing the appropriate position. In the case of the supermirror the height should be `-20.0` and the angle set to `0.0`

### 2. And an in beam parameter to the sample component
Add an in beam parameter to the sample in just the same way as above. This time however, only the translation needs to be given a position, set it to `100.0`, and the mode items can be omitted, as there will always be a sample point to consider.

In this exercise, we will add parking behaviour to the super mirror and sample components. We want the following:
- An `InBeamParameter` each for the Super Mirror and Sample components, which lets you toggle between in and out of beam for each component
- When the Super Mirror gets parked, move its height to -20 and its angle to 0
- When the Sample gets parked, move its `TRANS` axis to 100
- Think about which parameters are used in which experimental modality and give them appropriate Modes and Mode Inits

## To Test
1. Go to the table of motors and make sure all are at a 0 position.
2. Go to the reflectometry server view and make sure you are in `PNR` mode.
3. Restart the IOC to pick up the updated config.py.
4. If you go to the `Activation Parameters` tab in the reflectometry view you should now see the two parameters created in this exercise listed there, and both should be `IN`.
5. Change the mode to `NR`, go back to the `Activation Parameters` tab, and the `IN|OUT` buttons for the supermirror parameter should be swapped, and highlighted in yellow. Note that the move is saved until other values are changed, but if you hit move at this point, the `RBV` for the supermirror parameter should start moving. When it reads out, if you look on the table of motors then the height axis for the supermirror should be reading `-20`.
6. Go back to the reflectometry front panel, go back to PNR mode, set theta to 22.5, and select `Move`. Theta should start to change, along with the other associated values. However, as things bing in/out are meant to be a specific descision, you will still have to go to the activation parameters tab to trigger the move for the supermirror.

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
from ReflectometryServer.parameters import AxisParameter, InBeamParameter
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

# Overview

The reflectometry configuration describes the geometry of the beamline and is read by the reflectometry IOC on startup. The config file is written in python and lives in `<config area>/refl/config.py`.

This file needs to import relevant classes and methods used for constructing the configuration via the line `from ReflectometryServer import *`

[Jump to Example Configuration]()

# Reference Manual

This section contains an overview of the available building blocks in the form of classes and helper methods, which are used to construct the beamline model.

## Types of Objects

### [Beamline Constants](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Object#beamline-constants)

These are fixed values which are exposed by the IOC as PVs of the form `<PREFIX>:REFL:CONST:<NAME>`, but cannot be changed at runtime. They follow a naming convention so that they can be read automatically by the shared reflectometry scripting library. The default set of constants the configuration has to define consists of:
- `S1_Z`: Z coordinate of Slit 1
- `S2_Z`: Z coordinate of Slit 2
- `S3_Z`: Z coordinate of Slit 3
- `S1_4`: Z coordinate of Slit 4
- `SM_Z`: Z coordinate of the supermirror
- `SAMPLE_Z`: Z coordinate of the sample point
- `PD_Z`: Z coordinate of the point detector
- `S3_MAX`: Maximum vertical gap for S3
- `S4_MAX`: Maximum vertical gap for S4
- `THETA`: Maximum Theta angle
- `NATURAL_ANGLE`: Natural angle of the beam as it enters the blockhouse
- `HAS_HEIGHT2`: Whether the sample stack has a second height stage (`True`/`False` only)

#### Example:

```
BeamlineConstant("MAX_THETA", 1.8, "Maximum Theta value")
```


### [Components](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Geometry-Components)
Components are the central building blocks of the configuration. Each of them represents a node of interaction with the beam on the instrument (either passively tracking or actively affecting it). They are also the connective middle layer element between the user-facing beamline parameters and the composite drivers that talk to low level motors.

All components take the following two arguments:
- `name`: Name of the component
- `setup`: The geometry setup for this component as an object of the form `PositionAndAngle(component_y, component_z, angle_of_linear_displacement_axis)`

#### Types of Component
- `Component`: Most basic type of component with 1 degree of freedom: linear displacement relative to the beam
- `TiltingComponent`: 2 degrees of freedom: linear and angular displacement. This allows the component to stay perpendicular to the beam as well as centred (e.g. point detector on SURF/CRISP). This component does not affect the beam path.
- `ReflectingComponent`: 2 degrees of freedom like `TiltingComponent`, except this component reflects the beam and thus changes its path (e.g. supermirror)
- `ThetaComponent`: like `ReflectingComponent`, except the angle is derived from the height of this component and the height of another component further down the beamline. For this purpose, `ThetaComponent` receives a list of components via an additional argument `angle_to`. It will use the height of the next component along the beam that is currently in beam and in the mode.

#### Example

```
detector = TiltingComponent("detector", setup=PositionAndAngle(0.0, 100.0, 90.0))

ThetaComponent("theta_component", setup=PositionAndAngle(0.0, 50.0, 90.0), angle_to=[detector])
```


### [Beamline Parameters](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Parameters)

These are the top-level parameters exposed as PVs of the form `<PREFIX>:REFL:PARAM:<NAME>:<SUFFIX>`, which the users can set via the reflectometry front panel or scripting. Parameters can take the following arguments:

Required:
- `name`: name of the parameter
- `component`: The component this parameter is for

Optional:
- `description`: A description of this parameter (Default: use parameter `name`)
- `autosave`: Whether the parameter should be [autosaved](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Parameters#parameter-initialisation) to file (meaning that on IOC start up, the last known setpoint is re-applied, rather than inferred from a motor position). If multiple parameters depend on a single motor axis (e.g. `Theta` and `PDOffset` are inferred from  , all but one of them should be autosaved in order to not lose their values (Default: `False`)
- `rbv_to_sp_tolerance`: The maximum difference between parameter readback and setpoint values at which it is still considered by the IOC to have arrived at its setpoint. (Default: `0.002`)

#### Types of parameter

- `TrackingPosition`: A displacement relative to the beam along a linear movement axis (e.g. offset on supermirror height `SMOFFSET`)
- `AngleParameter`: An displacement relative to the beam along an angular movement axis (e.g. angle of the point detector `PDANGLE`)
- `InBeamParameter`: A multi-state parameter which says whether this component is currently in the beam and tracking, or in a parked state
- `DirectParameter`: A non-tracking parameter (i.e. the value is independent of the current beam path). This currently does not require a `Component` but is instead directly passed a `PVWrapper` through which it talks to the motors.
    - `SlitGapParameter`: A specific type of `DirectParameter` describing slit gaps (functionally the same)

#### Example

```
# Parameter relative to the beam path
AngleParameter("SM_angle", supermirror_component)

# Parameter that directly wraps a motor value
DirectParameter("sample_trans", MotorPVWrapper("MOT:MTR0305"))
```

### [Composite Drivers](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Composite-Driving-Layer)

These objects link the middle-layer component model to low-level motors. They take the following arguments:

Required:
- `component`: The source component
- `axis`: The physical motor axis as a `PVWrapper` object (see below)

Optional:
- `synchronised`: Whether this driver should be able to alter axis velocity when multiple axes are being moved (used for synchronised beamline movement) (Default: `True`)
- `engineering_correction`: any [corrections](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Composite-Driving-Layer#engineering-offset) that should be applied to the motor position (Default: `None`)
- `out_of_beam_positions` (`DisplacementDriver` only): A list of possible [parked positions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Composite-Driving-Layer#out-of-beam-positions) for this axis (Default: `None`)

#### Types of Driver

- `DisplacementDriver`: The driver for a single linear displacement axis
- `AngleDriver`: The driver for a single angular displacement axis

#### Example
```
# linear and angular drivers for supermirror with parked position
DisplacementDriver(sm_component, MotorPVWrapper("MOT:MTR0101"))
AngleDriver(sm_component, MotorPVWrapper("MOT:MTR0102"))

# with parked position
sm_out_pos = OutOfBeamPosition(-20)
DisplacementDriver(sm_component, MotorPVWrapper("MOT:MTR0101"), out_of_beam_positions=[sm_out_pos])
```

### PV Wrappers

Wrappers around lower level motors to read, monitor and cache relevant PV values (such as SP/RBV positions, or velocity related fields for synchronising moves). 

Required:
- `base_pv`: The base PV of the axis being driven

Optional:
- `min_velocity_scale_factor`: used to compute a minimum motor velocity in case none is set via `VBAS` on the underlying axis. Having a minimum velocity avoids motor stalling. The minimum velocity will be equal to `VMAX / min_velocity_scale_factor`. (Default: 100 - i.e. default minimum velocity `VMAX`/100)

The following types of PV Wrapper exist:
- `MotorPVWrapper`: Wrapper around a standard motor PV
- `JawsGapPVWrapper`: Wrapper around a Jaws Gap PV
- `JawsCentrePVWrapper`: Wrapper around a Jaws Centre PV. *NOTE:* this can be used for a slit without a height stage

#### Example:
```
# Drive Axis 0101
MotorPVWrapper("MOT:MTR0101")

# Drive Axis JAWS1:HGAP
SlitGapPVWrapper("JAWS1", is_vertical=False)

# Drive Axis JAWS1:VCENT
SlitCentrePVWrapper("JAWS1", is_vertical=True)
```

### [Modes of Operation](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Object)

Modes allow users to switch between different experimental setups more easily. They take the following arguments:
- `name`: The name of the mode (e.g. `NR`, `Liquid`)
- `beamline_parameters_to_calculate`: The list of parameters that should automatically track the beam path when this mode is active
- `sp_inits`: A dictionary of `parameter:value` pairs to be applied when entering this mode (Default: empty)
- `is_disabled`: denotes that this is a special ["disabled" mode](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Object#disabled-mode), which means all beam tracking is disabled. This is useful for aligning individual parameters in isolation. (Default: False) 

#### Example:
```
pnr_params = [...]  # A list of all parameters relevant to PNR mode
pnr_inits = {"SM_inbeam": True}
BeamlineMode("Polarised NR", pnr_params, sp_inits=pnr_inits, is_disabled=False) 
```

### [Footprint Calculator](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-IOC#footprint-calculator)

The footprint calculator provides values for beam footprint and resolution based on the current slit gaps / theta, and exposes them to the front panel and scripting via PVs. It is instantiated by the beamline object if a `FootprintSetup` argument is passed, which defines relevant dimensions on the beamlne.

The footprint setup takes the following arguments:
- `pos_s1`: Z coordinate of slit 1
- `pos_s2`: Z coordinate of slit 2
- `pos_s3`: Z coordinate of slit 3
- `pos_s4`: Z coordinate of slit 4
- `pos_sample`:  Z coordinate of the sample
- `s1vg`: The vertical `SlitGapParameter` for Slit 1
- `s2vg`: The vertical `SlitGapParameter` for Slit 2
- `s3vg`: The vertical `SlitGapParameter` for Slit 3
- `s4vg`: The vertical `SlitGapParameter` for Slit 4
- `theta`: The Theta `AngleParameter`
- `lambda_min`: The minimum lambda for this beamline
- `lambda_max`: The maximum lambda for this beamline

#### Example
```
# All of these arguments should already have been defined elsewhere in the config:
footprint_setup = FootprintSetup(z_s1, z_s2, z_s3, z_s4, z_sample, s1vg, s2vg, s3vg, s4vg, theta, lambda_min, lambda_max)
```

## Helper functions

The reflectometry server provides a set of helper functions to aid writing valid configuration files by automatically adding objects to the correct lists which are eventually passed into the top level `Beamline` object. The following methods are available:

### `add_mode`

### `add_beam_start`

### `add_constant`

### `add_component`

### `add_component_marker`

### `add_parameter`

### `add_parameter_marker`

### `add_driver`

### `add_driver_marker`

### `create_jaws_pv_driver`

### `add_slit_parameters`


## Notes:


# Example Configuration

Following is a simplified example of a typical beamline configuration to illustrate concepts.

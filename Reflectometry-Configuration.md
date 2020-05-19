# Overview

The reflectometry configuration describes the geometry of the beamline and is read by the reflectometry IOC on startup. The config file is written in python and lives in `<config area>/refl/config.py`.

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
- 'ThetaComponent': like `ReflectingComponent`, except the angle is derived from the height of this component and the height of another component further down the beamline. For this purpose, `ThetaComponent` receives a list of components via an additional argument `angle_to`. It will use the height of the next component along the beam that is currently in beam and in the mode.

#### Example

```
detector = TiltingComponent("detector", setup=PositionAndAngle(0.0, 100.0, 90.0))

ThetaComponent("theta_component", setup=PositionAndAngle(0.0, 50.0, 90.0), angle_to=[detector])
```


### [Beamline Parameters](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Parameters)

These are the top-level parameters exposed as PVs, which the users can set via the reflectometry front panel or scripting.
All parameters expect at least 2 arguments for a) parameter name, and b) its base `Component` (see below). Additionally, all parameters can be passed optional arguments for:
- `description`: A description of this parameter
- `autosave`: Whether the parameter should be [autosaved](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Parameters#parameter-initialisation) to file (meaning that on IOC start up, the last known setpoint is re-applied, rather than inferred from a motor position)
- `rbv_to_sp_tolerance`: The maximum difference between parameter readback and setpoint values at which it is still considered by the IOC to have arrived at its setpoint.

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

These objects link the middle-layer component model to the low-level motor axes. They take the following arguments:

Required:
- `component`: The source component
- `axis`: The physical motor axis as a `PVWrapper` object (see below)

Optional:
- `synchronised`: Whether this axis should alter its velocity when moving multiple axes, to move concurrently with the slowest one.
- `engineering_correction`: any corrections (link) that should be applied to the motor position
- `out_of_beam_positions` (`DisplacementDriver` only): A list of possible parked positions (link) for this axis

#### Types of Driver

- `DisplacementDriver`:
- `AngleDriver`:

#### [PV Wrappers]()

### [Modes of Operation](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Object)

### [Footprint Calculator](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-IOC#footprint-calculator)


## Helper functions

## Notes:


# Example Configuration

Following is a simplified example of a typical beamline configuration to illustrate concepts.



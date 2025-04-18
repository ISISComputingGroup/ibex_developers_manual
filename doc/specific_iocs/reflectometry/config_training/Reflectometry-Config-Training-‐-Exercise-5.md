# Exercise 5 - Parking Components

## Parking Components

As we briefly touched on in a previous section, the beamline occasionally needs be re-configured by moving components in or out of the beam. This can be the polariser when switching between NR and PNR mode, moving the sample out of the beam to record the base neutron flux, moving everything out of the way of the laser (and back in) for alignment, among many more reasons. In order to facilitate this action, the reflectometry server provides `InBeam Parameters`, a toggle parameter type for moving a given component in or out of the beam, an abstraction layer for applying one out of a set of pre-defined, named numerical positions. As the `InBeam Parameter` is applied at the component level, this may set those pre-defined positions on multiple axes of that component. 

When you move a component out of the beam, it's offset Setpoints and SP:RBVs are preserved but each axis physically moves to its park position (if defined). Once it's parked, a component will not track or change the beam path in the beamline model. You should also see the move button for other parameters on this component being locked on the OPI for this reason.

When you move a component into the beam, each parked axis returns to its SP:RBV and it can become part of the active tracking model again (if all other conditions are met too e.g. its part of the current mode).

## Design Rationale
These parameters function very similarly to [Motion Set Points](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Motion-Set-points). There are a few reasons why we integrated these into the reflectometry server as a parameter type rather than just using motion setpoints:
- As for other Parameters, they provide the option to enter a setpoint without applying it
- The in/out of beam status affects the beam tracking model, e.g. `sm_angle` will be ignored for the beam path if the super mirror component is parked
- `InBeam` Parameters allow for [more sophisticated parking behaviour](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Composite-Driving-Layer#out-of-beam-positions-and-parking-sequences), such as 
    - moving through a sequence of positions when parking in special cases where the linear path is physically obstructed on the beamline
    - applying one of several possible parked positions depending on the beam position in cases where we might accidentally obstruct it otherwise. e.g. Park High for low angled beam, Park Low for high angled beam.

## Exercise 5

In this exercise, we will add parking behaviour to the super mirror and sample components. We want the following:
- An `InBeamParameter` each for the Super Mirror and Sample components, which lets you toggle between in and out of beam for each component
- When the Super Mirror gets parked, move its height to -20 and its angle to 0
- When the Sample gets parked, move its `TRANS` axis to 100
- Think about which parameters are used in which experimental modality and give them appropriate Modes and Mode Inits

## Tips:

- You can create an `InBeam` parameter like this: 

`add_parameter(InBeamParameter("comp_in", some_compon, description=""),modes=[mode], mode_inits=[(mode, value)])`

- You can add a Park Position on an axis like this:

`add_driver(IocDriver(..., out_of_beam_positions=[OutOfBeamPosition(-10)]))`

- You might get a warning if you do not enable autosave on the `InBeam` parameter. This  does not stop you from running the server but it means that on startup, we cannot differentiate between an offset from a parameter setpoint and an offset from being parked so they might be initialised wrong. More detail can be found here: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Parameters#parameter-initialisation

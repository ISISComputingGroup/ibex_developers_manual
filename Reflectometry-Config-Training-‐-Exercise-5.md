> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 5

# Parking Components

As we briefly touched on in a previous section, the beamline occasionally needs be re-configured by moving components in or out of the beam. This can be the polariser when switching between NR and PNR mode, moving the sample out of the beam to record the base neutron flux, moving everything out of the way of the laser (and back in) for alignment, among many more reasons. In order to facilitate this action, the reflectometry server provides `InBeam Parameters`, a toggle parameter type for moving a given component in or out of the beam. These function very similarly to [Motion Set Points](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Motion-Set-points) in that they create an abstraction layer for pre-defined numerical positions. As the `InBeam Parameter` is applied at the component level, this may set those pre-defined positions on multiple axes of that component. 

There are several reasons we integrated these into the reflectometry server as a parameter type rather than just using motion setpoints:
- As for other Parameters, they provide the option to enter a setpoint without applying it
- The in/out of beam status affects the beam tracking model, e.g. `sm_angle` will be ignored for the beam path if the super mirror component is parked
- `InBeam` Parameters allow more sophisticated parking behaviour, such as moving through a sequence of positions when parking in special cases where the linear path is physically obstructed on the beamline

## Exercise 5

### [< Previous: Theta](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-4) || [Next: Engineering Corrections](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Training-%E2%80%90-Exercise-6)>
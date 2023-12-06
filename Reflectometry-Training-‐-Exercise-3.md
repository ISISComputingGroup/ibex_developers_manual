> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 3


# Modes

Next, we will look at modes. Modes are a way to configure the beamline/tracking model for different types of experiment at runtime at the push of a button. Modes achieve this through a number of features:
- You can choose which parameters should automatically track the beam, i.e. they move to stay aligned to the reflected beam when it changes
- You can define a set of default parameter values to apply when you enter the mode (and optionally, to re-apply on every beamline move)
- You can choose for engineering corrections to only apply to certain modes (more on that later)

In the following exercise we will categorize the parameters we have added so far by mode and give them some default values.

## Exercise 3

Make the following changes to your `config.py`:
- In addition to `NR` mode, add another mode called `PNR` to your config using the `add_mode` helper method.
- Add each parameter to the appropriate modes using the `modes` argument e.g. `add_parameter(AxisParameter(...), modes=[nr])`
    - Slits should track the beam in every mode
    - The Super Mirror should track the beam in `PNR` mode only
    - The sample axes should never track the beam automatically. This is because the scientists don't want this component to move implicitly on beam changes, only when they explicitly tell it to

### To Test
1. Once you have made these changes, restart the `REFL_01` IOC. 
1. You should now be able to switch between `NR` and `PNR` mode via the front panel OPI. 
1. When doing so, you should see a little green "M" appear/disappear next to parameters, indicating whether they are part of the currently selected mode.
1. Try moving `sm_angle`. You should now see `s2_offset` automatically staying aligned to the reflected beam, while `sa_offset` and `sa_phi` are not (as they were prior to this exercise)

### [< Previous: Building Up The Beamline Model](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-2) || [Next: (Placeholder)](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Training-%E2%80%90-Exercise-4)>
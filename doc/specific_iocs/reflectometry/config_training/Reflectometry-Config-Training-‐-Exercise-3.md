# Exercise 3 - Modes

Next, we will look at modes. Modes are a way to configure the beamline/tracking model for different types of experiment at runtime at the push of a button. Modes achieve this through a number of features:
- You can choose which parameters should automatically track the beam, i.e. they move to stay aligned to the reflected beam when it changes
- You can define a set of default parameter values to apply when you enter the mode (and optionally, to re-apply on every beamline move)
- You can choose for engineering corrections to only apply to certain modes (more on that later)

In the following exercise we will categorize the parameters we have added so far by mode and give them some default values.

## Exercise 3
### 1. Create your modes
So far there has always been a mode `_nr`, without a mode the reflectometry server, but as this variable wasn't used there is an underscore to let Pyright know that it could be ignored.
Start by removing that `_`.
Add another mode called `PNR` in the same way that `NR` is added.
Create a list `all_modes` which includes both `nr` and `pnr`.

### 2. Add modes to parameters
Give each parameter a `modes` argument follwoing on after the `AxisParameter` argument. Note that `modes` has to be a list, so if you are only applying a single mode don't forget to add square brackets.
The slit offsets should track the beam in `all_modes`.
Both of the supermirror parameters should use `pnr` mode.
The sample axes should never track the beam automatically. This is because the scientists don't want this component to move implicitly on beam changes, only when they explicitly tell it to. 

## To Test
1. Don't forget to restart the IOC to pick up the changes to `config.py` you have just made.
2. You'll likely start up in `NR` mode, and if you go to the `Collimation` tab, you should see two green Ms, by each slit offset.
3. Go back to the front panel, and you should be able to switch between the two modes using the buttons next to the status information. If you leave it on `PNR` and go back to collimation then as well as the previous green Ms by the slit offsets there should be ones alongside the supermirror parameters.
4. Assuming nothing has changed after the steps in the previous exercise, everything else should be reading as 0 on the `Collimation` tab, and if you look at the Table of Motors, then the supermirror angle is `22.5`, the slit 2 height at `10`, the sample height at `20`, and the sample phi at `45`.
5. Staying in `PNR` mode, set the `SMANGLE` to `11.25` on the `Collimation` tab.
6. The downstream values on this tab will still change with that value, except the `S2OFFSET` will end up back at 0 as it has moved with the change to the angle. The readback value of `SAMPOFFSET` and `SAMPPHI` will read as `11.716` and `22.5` respectively as these values as this is where these axes are now in relation to the beam. If you look at the Table of Motors, then the supermirror angle is now `11.25`, the slit 2 offset is `4.143`, and the sample height and phi haven't changed and are still at `20` and `45` respectively. So in this mode you can see that the height of slit 2 is moving automatically with changes to the beam.

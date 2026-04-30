# Exercise 6 - Optional Features

## `autosave`
Should you see this it is related to the ability to swap between multiple control software types, and as only IBEX and this server is now in use is informally deprecated, and as such will not be covered in detail, merely mentioned that with autosave, if you change a value when the reflectometry server is not running it should come back with the last SP before IOC restart. Without, it should come back with the current RBV applied as SP

## `characteristic_value`
Sometimes, scientists want to be able to see a beamline parameter and the low level axis it derives its value from side by side for diagnostics purposes. You can do this by "tagging" a beamline parameter with the relevant axis e.g. `AxisParameter(..., characteristic_value="MOT:MTR0101")`. This will just make the value for the given PV display next to the parameter, there is nothing too clever happening under the hood.

## `DirectParameter`
A type of beamline parameter that forgoes the `Component` and `IocDriver` layers, and directly mirrors the value from a given `PvWrapper` instead. We use this in instances where we want a parameter on the front panel but what the parameter controls is completely independent of the beam path. Slit Gap and Centre parameters are instances of `DirectParameter` for example.

## Exercise 6
### 1. Add a `characteristic_value`
Go to the `AxisParameter` creation for the sample offset, and add in the `chatacteristic_value` parameter after the description, and assign it to `MOT:MTR0307` in our fictitous beamline. 

### 2. Add a `DirectParameter`
Create this somewhere in the config file, call it `MONITORPOS`, give it a `pv_wrapper` value of a `MotorPVWrapper` pointing at `MOT:MTR0208` which in our beamline is the axis controlling the position of the monitor.

## Testing
1. Go to the table of motors and make sure all are at a 0 position.
2. Restart the IOC to pick up the updated config.py.
3. On the `Collimation Plane Parameters` tab, the `SAMPOFFSET` parameter should now have a label alongside it, reading `0.0`.
4. Set the `SMANGLE` to `22.5`. Whilst the `RDB` for `SAMPOFFSET` should update to `-20.0` the label should remain at `0.0`, that difference is equal to the displacement of the reflected beam.
5. Go now to the `Slit Parameters` page and you should see the direct parameter created above listed in there, in the appropriate place in the list in relation to the slit sets. If you set this parameter, then the appropriate axis on the table of motors should move with it with no differences seen.

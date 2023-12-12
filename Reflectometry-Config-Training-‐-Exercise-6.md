> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 6


# Beamline Parameters Misc

In this short section, I just want to briefly highlight some other optional functionality Beamline Parameters can provide:

#### `autosave`
Parameters have an optional `autosave` flag which determines how SPs for those parameters get initialised on start-up. At this point in time **we probably just want to autosave every parameter by default** - read below for rationale
- If `True`, they are read from a file in `/Instrument/var/refl/`. SPs get autosaved whenever a parameter is moved i.e. a new SP is applied as SP:RBV. 
- If `False`, parameters are initialised to their current RBV. This option was implemented as a way for the reflectometry server to account for positions being changed outside of IBEX when swapping between SECI and IBEX for testing. This option is deprecated as not autosaving positions can lead to some ambiguity when initialising setpoints, and the workflow it supported is outdated as reflectometers are not going back to SECI anymore.

#### `characteristic_value`
Sometimes, scientists want to be able to see a beamline parameter and the low level axis it derives its value from side by side for diagnostics purposes. You can do this by "tagging" a beamline parameter with the relevant axis e.g. `AxisParameter(..., characteristic_value="MOT:MTR0101")`. This will just make the value for the given PV display next to the parameter, there is nothing too clever happening under the hood.

#### `custom_function`
Run a custom function whenever a given parameter is being "moved". This is potentially quite powerful as this can be arbitrary code, however this should be used sparingly and cautiously, as it is not subject to reviews, automated tests etc. We have used this in the past e.g. to load appropriate wiring tables when moving Point / Linear detectors in or out of the beam.

#### `DirectParameter`
A type of beamline parameter that forgoes the `Component` and `IocDriver` layers, and directly mirrors the value from a given `PvWrapper` instead. We use this in instances where we want a parameter on the front panel but what the parameter controls is completely independent of the beam path. Slit Gap and Centre parameters are instances of `DirectParameter` for example.

### Exercise 6

- Try adding the sample height axis as a `characteristic value` of the `sa_offset` parameter. This should add a readback label of the motor value next to the beamline parameter in the `Collimation Plane` tab. When using the super mirror with a non-zero angle, you should be able to see a difference between the parameter and motor values equal to the displacement of the reflected beam.
- Add a `DirectParameter` called `monitor_pos` which drives the appropriate motor axis (should be 0408). It does not matter where in the config file this parameter appears. Confirm that setting the parameter moves the associated motor axis.
- Try setting `autosave` for `monitor_pos` to `False`. To see the difference, try killing the IOC, moving the motor axis via the low motor table, and restarting it. With autosave, it should come back with the last SP before IOC restart. Without, it should come back with the current RBV applied as SP

### [< Previous: Parking Components](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-5) || [Next: Engineering Corrections](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-7)>
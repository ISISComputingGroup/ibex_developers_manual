# Purpose

The purpose of autosave is to capture tunable parameters in a config-independent way. Examples of things we autosave are things like motor settings (resolutions, speeds, etc.).

# Snapshots

In the future, we may use an autosave-like mechanism to apply snapshots of motor settings at a particular time to an IOC again. However this is not currently implemented nor required on any beamline that we support.

# Dangers

Mixing autosave with IOCs that load a dynamic number of axes/sensors can be dangerous. If the IOC is accidentally started with a macro that makes the IOC load no axes, autosave will save a file containing no values. When the IOC is subsequently restarted with the correct macros, it will read the autosave file (which has no values in it). This causes the IOC to "lose" its previously saved values. This was seen in https://github.com/ISISComputingGroup/IBEX/issues/2180.

# How to Add

To add autosave to a field see [autosave PVs in finishing touches](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/IOC-Finishing-Touches#4-autosave-pvs).

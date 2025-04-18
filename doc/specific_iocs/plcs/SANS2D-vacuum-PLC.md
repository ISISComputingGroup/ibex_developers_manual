# SANS2D Vacuum PLC

## Vacuum Status

Currently, we get a tank vacuum status from the PLC. This was not available in SECI. There are 4 different states, ATMOSPHERE, AT VACUUM, VAC DOWN, VENTING, but if we cannot get a state the PV goes into major alarm and has the string ERROR: STATUS UNKNOWN. This is displayed on the OPI in both the regular and advanced tab.

## Front beamstop inhibit

Done as part of motorExtensions. See https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/SANS2D-Front-Beam-Stop-inhibit-movement
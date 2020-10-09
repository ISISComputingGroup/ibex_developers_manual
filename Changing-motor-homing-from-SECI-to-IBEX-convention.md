> [Wiki](Home) > [Galils Under SECI](galils-under-seci) > [Changing motor homing from SECI to IBEX convention](Changing-motor-homing-from-SECI-to-IBEX-convention)

The convention for home values and offsets differs between IBEX and SECI. On many instruments, this difference doesn't matter as the switch between the two control systems happens only infrequently, so the motors can be homed as required.

On the instruments which do expect to switch between the two control systems more often, we have decided to change the home position and offset convention in the SECI config files to the IBEX convention, where the motor home position is defined as zero.

In a nutshell, this migration shifts the home position to zero, and applies the SECI home position as an offset. If no soft limits have been set, this only has the effect of changing how the user axis (the value shown to the user) maps to the drive axis (how far along the actual axis you are).

If soft limits have been set, these need to be adjusted to make sure the distance each axis can travel remains the same as before. The new soft limit = old soft limit - old home position + old offsets:

![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/seci_to_ibex_home_scheme.png)

The tool to perform this is held in the [ibex utils](https://github.com/ISISComputingGroup/ibex_utils) repository under `galil_ini_parser`. Note that this script does not change any user limits.

To perform the migration:
1. Take a backup of the original Galil configuration file
1. Copy the Galil configuration file from the instrument to somewhere you can run the script (usually your developer machine)
1. Run the script in ibex_utils on this configuration file
1. Sanity check the output of the script and copy it to the instrument machine
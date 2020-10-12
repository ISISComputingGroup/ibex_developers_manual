> [Wiki](Home) > [Galils Under SECI](galils-under-seci) > [Changing motor homing from SECI to IBEX convention](Changing-motor-homing-from-SECI-to-IBEX-convention)

The convention for home values and offsets differs between IBEX and SECI. On many instruments, this difference doesn't matter as the switch between the two control systems happens only infrequently, so the motors can be homed as required.

On the instruments which do expect to switch between the two control systems more often, we have decided to change the home position and offset convention in the SECI config files to the IBEX convention, where the motor home position is defined as zero.

There are three rules which must be followed to change from SECI to the IBEX configuration:

1. When we are on a home switch this always translates to the same position in user space (both before and after migration and on switching IBEX/SECI)
1. The home position must be zero, in SECI this translates to `home_val-offset = 0` as the offset is subtracted from the home_val when a home is done
1. The distance between the physical home position and the limits must stay the same (both before and after migration and on switching IBEX/SECI). In SECI the limits are defined in drive space and so as we're changing the offset, which moves drive space, we must then change the limits

These rules are illustrated here:

![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/seci_to_ibex_home_scheme.png)

The tool to perform this is held in the [ibex utils](https://github.com/ISISComputingGroup/ibex_utils) repository under `galil_ini_parser`. Note that this script does not change any user limits.

To perform the migration:
1. Take a backup of the original Galil configuration file
1. Copy the Galil configuration file from the instrument to somewhere you can run the script (usually your developer machine)
1. Run the script in ibex_utils on this configuration file
1. Sanity check the output of the script and copy it to the instrument machine
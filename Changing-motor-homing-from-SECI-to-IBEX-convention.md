The convention for home values and offsets differs between IBEX and SECI. On many instruments, this difference doesn't matter as the switch between the two control systems happens only infrequently, so the motors can be homed as required.

On the instruments which do expect to switch between the two control systems more often, we have decided to change the home position and offset convention in the SECI config files to the IBEX convention, where the motor home position is defined as zero.

In a nutshell, this migration shifts the home position to zero, and applies the SECI home position as an offset. To make sure the distance each axis can travel remains is the same as before, the soft limits need to be shifted by the difference between the (old home position + any old applied offsets) and the new home position, which is equal to the old offsets:
![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/seci_to_ibex_home_scheme.png)

The tool to perform this is held in the [ibex utils](https://github.com/ISISComputingGroup/ibex_utils) repository under `galil_ini_parser`. Note that this script does not change any user limits.

To perform the migration:
1. Take a backup of the original Galil configuration file
1. Copy the Galil configuration file from the instrument to somewhere you can run the script (usually your developer machine)
1. Run the script in ibex_utils on this configuration file
1. Sanity check the output of the script and copy it to the instrument machine
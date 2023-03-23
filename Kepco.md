> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Kepco](Kepco)

Summary of use is now in the [user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Kepco-Power-Supply).

## Remote connection details

See [HTS magnet](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/HTS-Magnet#kepco-power-supplies) for information.

## Remote Command

Most of the KEPCOs at ISIS which are BOPs (Bipolar Operational Power) do not have the REM command to switch the PSU to remote mode, only the more recent digital display ones, and possibly some of the dial display ones that were bought more recently (hence there being a manual labelled "firmware not in use").

## Calibrating Current to a Field

The KEPCO can also use a calibration file to set and readback a field instead of a current. This is currently only used for the [HTS magnet](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/HTS-Magnet). It looks in `Setting\config\common\magnets` for this file.

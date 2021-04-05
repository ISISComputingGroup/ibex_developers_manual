> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Kepco](Kepco)

Summary of use is now in the [user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Kepco-Power-Supply).

## Remote Command

Most of the KEPCOs at ISIS which are BOPs do not have the REM command to switch the Kepco to remote mode, only the more recent digital display ones, and possibly some of the dial display ones that were bought more recently (hence there being a manual labelled "firmware not in use")

## Calibrating Current to a Field
The Kepco can also use a calibration file to set and readback a field instead of a current. This is currently only used for the HTS magnet. It looks in `Setting\config\common\magnets` for this calibration.

## HTS Smart Monitor
The HTS smart monitor is a device that shows the current status of a KEPCO for use with the HTS magnet system. It is capable of showing safe operating limits, hard limits and the current voltages and temperatures of the connected KEPCO. Currently it sits on a static IP which is set by the device, and on POLREF it is connected to the private network. 

The device can be configured with its webserver which should be at `<static ip>:8080`; this can be used to configure a different static IP address or to enable DHCP. 
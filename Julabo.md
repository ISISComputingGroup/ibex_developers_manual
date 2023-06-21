> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Julabo](Julabo)

Julabo is a temperature control unit. There are many different versions. The commands for each model are slightly different. When migrating an instrument, care must be taken to check exactly which command set it is using under SECI and to configure an equivalent command set in IBEX. A spreadsheet of labview settings against command set is in [this spreadsheet](backend_system/IOCs/julabo_commands.xlsx).

The IOC copes with these variations in commands by making 4 commands configurable via macros:
- `READ_POWER_CMD_NUMBER` configures the command used to read power. This macro should be the 2-digit number at the end of the read power command in the spreadsheet above (for the relevant model of julabo).
- `READ_EXT_TEMP_CMD_NUMBER` - syntax as above but for reading external temperature
- `READ_HIGH_LIM_CMD_NUMBER` - syntax as above but for reading the high limit from the julabo
- `READ_LOW_LIM_CMD_NUMBER` - syntax as above but for reading the low limit from the julabo
- `OEOS` - the output terminator. Needs slashes escaping, so set to `\\r\\n` for a CR LF terminator.
- `IEOS` - the input terminator. Needs slashes escaping, so set to `\\r\\n` for a CR LF terminator.

Note - if the commands are wrong they may still reply, but report the wrong numbers! For example `IN_PV_02` can mean "read external temperature" or "read heater power" depending on the model of Julabo used. Do not assume that because there are numbers coming back they are necessarily the right numbers!

In general they control the temperature by pumping a fluid from a temperature controller bath to the sample and back. It is possible to connect an external sensor to the unit and have it control the temperature from this sensor or have it control itself from the internal bath temperature.

# Setpoints

The Julabo device only has one setpoint. To enable `cset` to be used with blocks pointing at either internal or external temperature, there are aliases from `EXTTEMP:SP` to `TEMP:SP`. This does mean as a user I can set the setpoint for the wrong item I am controlling (e.g. mode is external control but the user set the temperature on temp) but this is better than:

1. Having an alarm on the pv when the wrong setpoint is used because it relies on the the control mode read back value being up-to-date
1. Setting the setpoint depends on the control mode because it relies on the control mode being up-to-date or on change sending a temperature change to the device; on startup this could be 0
1. Having a unique setpoint PV because then user can not have a single block which is their sample temperature and legacy scripts already use the setpoint block.

# P, I and D

The Julabo has PID setting for temperature control and both the internal and external sensors (6 parameters in total). On at least one model (He) setting these using the remote interface, e.g. from IBEX, does not cause the unit to store these values. This means that on a power cycle it resets the values it had to the ones that were last set using the interface on the device. Furthermore from ticket [3104](https://github.com/ISISComputingGroup/IBEX/issues/3104) these values can not be set on startup using either autosave or default PVs in a config.

# Communication

null modem: depends on Julabo If none of the settings above allow you to connect to a unit try installing a null modem.

# Troubleshooting

The julabo hardware supports having several different setpoints and can control on any of them, ibex always uses setpoint 1. If the julabo hardware is set to e.g. use setpoint 2 then ibex will think all is fine and send/read the setpoint 1 ok, but the julabo hardware will how a different setpoint value (setpoint 2) on its screen. A technician will need to go into the configuration menu on the device and change it to use setpoint 1  
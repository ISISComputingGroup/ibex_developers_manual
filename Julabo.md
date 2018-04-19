> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Julabo](Julabo)

Julabo is a temperature control unit. There are many different versions. The commands are slightly different I have made a record in [this spreadsheet](backend_system/IOCs/julabo_commands.xlsx).

In general they control the temperature by pumping a fluid from a temperature controller bath to the sample and back. It is possible to connect an external sensor to the unit and have it control the temperature from this sensor or have it control itself from the internal bath temperature.

# Setpoints

The Julabo device only has one setpoint. To enable `cset` to be used with blocks pointing at either internal or external temperature, there are aliases from `EXTTEMP:SP` to `TEMP:SP`.

# P, I and D

The Julabo has PID setting for temperature control and both the internal and external sesnors (6 parameters in total). On at least one model (He) setting these using the remote interface, e.g. from IBEX, does not cause the unit to store these values. This means that on a power cycle it resets the values it had to the ones that were last set using the interface on the device.

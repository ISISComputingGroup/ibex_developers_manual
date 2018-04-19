> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Julabo](Julabo)

Julabo is a temperature control unit. There are many different versions. The commands are slightly different I have made a record in [this spreadsheet](backend_system/IOCs/julabo_commands.xlsx).

# Setpoints

The Julabo device only has one setpoint. To enable `cset` to be used with blocks pointing at either internal or external temperature, there are aliases from `EXTTEMP:SP` to `TEMP:SP`.
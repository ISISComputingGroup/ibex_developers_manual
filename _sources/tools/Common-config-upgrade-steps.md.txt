# Common config upgrade steps

## Changing macros

The classes for changing macro names and values use the `Macro` structure, which lets you specify the name of the IOC which is to be changed (e.g. `AMINT2L`), as well the value. There is a common interface to change macros in a globals.txt file, as well as the XML files in an instrument configuration.

When changing macros, you need to supply the name of the IOC and two `Macro` objects. The first Macro defines the _current_ name of the macro to be found. If a value is supplied here (optional), only macros which match on the IOC name, macro name and value will be changed.

The second `Macro` object defines what the macro should look like _after_ the upgrade step. You can keep the macro name the same as the first macro object but add a new/different value. The macro name can be different, which would change the name of the macro (the moxa e12xx upgrade step does this), no value needs to be supplied for this. Or you can change both the macro name and the value, which would change both.

### Examples:

```
macros_to_change = [
    (Macro("IP_ADDR"), Macro("ADDR")),
]
change_xml_macros.change_macros("MOXA12XX", macros_to_change)
```
This is taken from the moxa 12XX upgrade step. It finds all existing MOXA12XX IOCs in configurations, and changes the name of the `IP_ADDR` macro to `ADDR`. The macro value is not changed.

```
macros_to_change = [
    (Macro("ADDR"), Macro("ADDR", "127.0.0.1")),
]
change_xml_macros.change_macros("MOXA12XX", macros_to_change)
```
This sets the value of all `ADDR` macros on MOXA12XX IOCs to 127.0.0.1. This is because no macro value has been specified in the first macro, so it updates the value regardless of what the current value of the macro is.

```
macros_to_change = [
    (Macro("ADDR", "8.8.8.8"), Macro("ADDR", "127.0.0.1")),
    (Macro("BAUDRATE"), Macro("BAUD", "9600")),

]
change_xml_macros.change_macros("MOXA12XX", macros_to_change)
```
Multiple macros can be passed through in the list. Here, the same operation as above is performed except only `ADDR` macros currently set to 8.8.8.8 will be changed. Also, MOXA12XX IOCs with a `BAUDRATE` macros defined get renamed to `BAUD`, with their value set to 9600.
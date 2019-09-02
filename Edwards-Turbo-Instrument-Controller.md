> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > [Edwards TIC](Edwards-Turbo-Instrument-Controller)
# Device notes

The Edwards turbo instrument controller (TIC) is a relatively straightforward turbo pump controller. In addition to the turbo pump controls, it also has three measurement gauges which can be read back into the OPI. Each gauge can be disabled via macros to prevent disconnected errors appearing.

This driver was given to us by the Daresbury lab. This was added to the IBEX codebase with a few changes to adhere to IBEX coding standards.
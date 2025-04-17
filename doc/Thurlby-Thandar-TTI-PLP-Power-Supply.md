> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Thurlby Thandar TTI-PLP](Thurlby-Thandar-TTI-PLP-Power-Supply)

The Thurlby Thandar TTI PLP series are simple generic bench power supplies.

Items that can be set include :

1. Output voltage.
1. Output current.
1. Output On/Off.
1. Voltage limit.
1. Current limit.

* There are two switches on the rear of the unit to control whether the two modes, constant voltage and constant current, are controlled locally or 
remotely.  Set these switches according to the experiment requirements.

* The serial connection is made using a standard MOXA 9-pin cable.

* The device has an address based on whether there are 1 or 2 independent power supplies in the same unit (c.f. Eurotherm). This is mirrored in the IOC with an ADDRESS macro. Currently, ISIS only has single power supply units.

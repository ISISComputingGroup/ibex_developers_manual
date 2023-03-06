> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Razorbill RP100](Razorbill-RP100-Strain-Cell-PSU)

## Razorbill RP100 Strain Cell PSU

This is a small power supply (±200V, ±6mA) used to drive a piezoelectric strain cell.  It has a USB interface which connects to an AnywhereUSB USB<->Ethernet adapter on the beamline, or a local PC for testing/setup.

WISH are the primary users of this device and previously have had to borrow one from SE Electronics Group, but now have their own unit.

### IOC

The PSU has a short list of remote commands as it's a very simple device to control.  The IOC implements most of these:
- ID String
- Read & write voltage
- Read & write voltage slew rate (ramp rate)
- Read & write output (On / Off state)

It is also possible to read the voltage and current present at the front panel, but this was not required for the initial creation of the IOC.
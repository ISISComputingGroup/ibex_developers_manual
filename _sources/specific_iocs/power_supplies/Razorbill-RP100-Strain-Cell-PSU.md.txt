# Razorbill RP100 Strain Cell PSU

This is a small power supply (±200V, ±6mA) used to drive a piezoelectric strain cell.  It has a USB interface which connects to an [AnywhereUSB](/specific_iocs/other/AnywhereUSB) USB<->Ethernet adapter on the beamline, or a local PC for testing/setup.

[When connecting via an AnywhereUSB adapter or directly to a PC](/specific_iocs/other/AnywhereUSB), an additional COM port will appear.  Usually it's the next available, although it's not possible to predict which number it will be.  The Windows Device Manager can be used to find out (view only under normal user privileges), where it will show a `USB Serial Device (COMn)` under `Ports (COM & LPT)`.  This value can then be used for an IOC macro in the usual way.

WISH are the primary users of this device and previously have had to borrow one from SE Electronics Group, but now have their own unit.  Usually their experiments using the Razorbill PSU also involve the [Keysight E4980AL LCR Meter](https://github.com/ISISComputingGroup/IBEX/issues/7663).

## IOC (based on functionality of the original VIs)

The VI sent a "Clear Status" command on startup (`*CLS`) but this contravenes IBEX code not to alter a device's state on starting an IOC, therefore the command was not implemented.  However, it would be very simple to add this should the need arise.

The PSU has a short list of remote commands as it's a very simple device to control.  The IOC implements most of these, specifically:
- Read ID String
- Read & write voltage (V)
- Read & write voltage slew rate (ramp rate, V/s)
- Read & write output (On / Off state)

It is also possible to read the instantaneous voltage and current present at the front panel terminals, but this was not required for the initial creation of the IOC.

## OPI

A simple OPI exists to interact with the IOC.

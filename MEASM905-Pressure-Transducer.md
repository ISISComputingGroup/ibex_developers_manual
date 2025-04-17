This device is used on PEARL as a read-only pressure monitor, as part of the larger pressure control rig. 

In its current implementation, the device uses ASCII protocol to receive a simple command for a pressure reading. A bespoke db25 to Moxa cable has been created, as it uses a different protocol from RS232.

The PEARL handbook specifies that this device can use three different protocols: It currently uses the "M905 Protocol 1" to talk to the device.

## update

there are a set of standalone units created for other beamlines, ioc works well, just requires a male DB9 moxa cable

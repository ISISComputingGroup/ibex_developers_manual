> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Lakeshore 336

The Lakeshore 336 is a temperature controller that has four input temperature readings and two heater outputs. The user can configure which heater output is paired up with which input.

## IOC Setup
When connecting to the real device, the IOC requires its IP address, but the software installed on the device has a bug and does not return the correct IP address. Its network name, however, is correct.
To use the device, set the IPADDR macro in globals.txt to be the device network name, e.g. `LKSH336_01__IPADDR=ls336-1`.


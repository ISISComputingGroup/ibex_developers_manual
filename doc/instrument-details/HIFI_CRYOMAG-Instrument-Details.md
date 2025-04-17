# HIFI-CRYOMAG

This page contains information pertinent to the conversion of the HIFI_CRYOMAG control system from LabVIEW to EPICS.

## Background & Timeline ##
A control system was supplied on a separate PC for use with the HIFI cryomagnet. In order to utilise this system more completely and to update the code it should be migrated to use EPICS. At present the interaction between HIFI and the cryomagnet is undertaken via Channel Access, the LabVIEW VI which provides this access can be slowly replaced using IOCs rather than the current drivers.

## Control System ##
The control will be undertaken via EPICS and the IOCs. Some GUI interaction is likely to be required using IBEX for local control of the system, and via LabVIEW for the control from the instrument,

## Equipment ##
Note that the order listed below is the most logical order for replacing the code within the system. Some items are required for multiple devices, e.g. the simple PSU controller is needed for X, Y and Z magnets.

| Manufacturer | Model | Type | Connection | Driver | Notes |
| --- | --- | --- | --- | --- | --- |
| Lakeshore | LS460 | Gaussmeter | | | |
| Keithley | 2700 | Temperature Scanner | | | |
| [Cryomech](http://www.cryomech.com/) | | Compressor | | | This uses a specific protocol, so will not be an asyn driver |
| [Cryogenic](http://www.cryogenic.co.uk/) | SMS | PSU | | | There is need for a driver which includes the control of required cryogenic components |
| [Cryogenic](http://www.cryogenic.co.uk/) | SMS | PSU | | | There is need for a driver without the cryogenic components |
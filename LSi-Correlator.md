> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > LSi Correlator

The LSi correlator is a device used as part of the DLS system on LOQ. It can be controlled either with the vendor-supplied software, or using the Python, Labview or Matlab APIs.

## The vendor software
### Connecting the software to the correlator

The software struggles to find the correlator's IP address on our network. Instead, the IP address can be entered manually in the settings file in

`<LSI Software root>\LSI Correlator Acquisition Software\LSI Correlator Acquisition Software Settings.ini`

In this file, change the default setting of the correlator's IP address to the actual device IP then reboot the software.

## The Vendor Python API

The python 'API' is little more than a reference implementation of a websocket client. It is installed with the vendor software. This code has been placed in a private repository as we have not got permission from LSI to publicly distribute it.

The LSI python API has two dependencies in Python 3+:
1. `autobahn`
    - This is their module used to create websockets
1. `twisted`
    - This is a common python library used by autobahn to control low-level TCP connections

The vendor-supplied example script, `ExampleMainCorrelator.py`, was modified to produce the `take_data` function in the EPICS IOC.

**Note:** The second argument of the `LSICorrelator` object is the firmware revision on the device. This can be found from the LSi correlator vendor software.
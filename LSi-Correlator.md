> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > LSi Correlator

The LSi correlator is a device used as part of the DLS system on LOQ. It can be controlled either with the vendor-supplied software, or using the Python, Labview or Matlab APIs.

## The vendor software
### Connecting the software to the correlator

The software struggles to find the correlator's IP address on our network. Instead, the IP address can be entered manually in the settings file in

`<LSI Software root>\LSI Correlator Acquisition Software\LSI Correlator Acquisition Software Settings.ini`

In this file, change the default setting of the correlator's IP address to the actual device IP then reboot the software.

## The Python API

The python 'API' is little more than a reference implementation of a websocket client. It is installed with the vendor software, and is found in `<LSI Software root>\LSI Python API`.

The LSI python API has three dependencies:
1. `ipaddress`
    - This provides a standardised IP address object back-ported from python 3
1. `autobahn`
    - This is their module used to create websockets
1. `twisted`
    - This is a common python library used by autobahn to control low-level TCP connections


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

**Notes:**
 - The second argument of the `LSICorrelator` object is the firmware revision on the device. This can be found from the LSi correlator vendor software.

## The EPICS IOC
The EPICS IOC is based on PCASpy to create and interact with PVs over channel access. A major function of the IOC is to convert the values taken in from channel access into values/objects which the LSI python API can interpret. This IOC is only compatible with Python 3+.

The PCASpy/EPICS driver has a dictionary of 'internal' values. These have have been converted from the PVs to they can be directly passed through to the drivers. The PVConfig structure standardises where these conversions to and from the LSI vendor API and channel access PVs take place.

All communications to the physical device are handled by the LSI python API. The `take_data` function was developed from the example script supplied with this API.

### Issues/gotchas
 - Currently there are no IOC macros for this device. To change the IP address or the saved filepath this must be performed on the instrument in the PCASpy IOC code
 - This device is not polled, and so it is difficult to truly know whether the connection to the device has been dropped. Currently the device will read disconnected after a correlator run is started and no data is returned.
   - It might be possible to do something with websockets which would provide more immediate feedback whether the device connection is still alive, which is what most devices do.
 - Once the device connection has be severed, the IOC must be restarted. There is no logic in place to drop the `LSICorrelator` object and attempt a reconnection by spawning a new object.
 - Two of the output values from the device, `TraceChA` and `TraceChB` have a length which is proportional to the measurement duration requested. Because PCASpy PV lengths are specified at IOC boot time, these arrays may have to be truncated to publish them as PVs. Currently they are not published, but are saved to file.
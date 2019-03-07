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

There is also a vendor-supplied example script to use with the API, `ExampleMainCorrelator.py`. This can be used, although it is recommended to remove the plotting from this script as it seems to be quite buggy. The ip address in the script will have to be changed to match that of the device

**Note:** The second argument of the `LSICorrelator` object is the firmware value of the device. This is shown in the LSi correlator vendor software.

## LSI correlator communication investigation
[Ticket 4021](https://github.com/ISISComputingGroup/IBEX/issues/4021) was an investigation into how the LSi correlator can be integrated into Ibex. The points are addressed here.

1. I can open a connection to the LSi Correlator.

    - Using the steps above, both the vendor software and the Python API can be used to connect to the device.

1. I can configure the LSi Correlator (to the extent permitted by the API).

    - The vendor-provided example script runs without errors, which includes configuring various options. The `measurementDuration` and `TransferRate` were changed and affected the output of the device.

1. I can close a connection to the LSi Correlator.

    - There is a bug in the python API which causes a script to hang on terminating the connection with the device. This will need to be fixed before it can be used.

1. I can run a Python script demonstrating the collection & plotting (e.g. with matplotlib) of data from the LSi Correlator. Also demonstrate how to start a (neutron) run and how to generate a suitable run title.

    - The LSi-provided script can run and return some data (all zeroes as the correlator was not connected to a laser box).
    - This data can be plotted with matplotlib, but it's not clear whether the raw data from the correlator is useful to plot on its own. Are the actual values of interest obtained after the vendor's software has done some analysis?
    - The script was run within genie python, which suggests that it is possible to have the LSi correlator API called from a normal instrument script (after the dependencies have been added to genie python).
    - The run title cannot be changed from within the python API. The API and the vendor software are largely independent.
    - The python API can not be used to start a run which was set up in the vendor software

1. I have created appropriate documentation explaining how to use the LSi Correlator API.
    - See above for description on how to run the vendor-supplied API
1. I have produced written recommendations for how we should support this device in IBEX.
    - See conclusions

### Conclusions
1. It is possible to use the Python API to get unprocessed data off the device.
   - We can add this to Ibex this by either calling the API from instrument scripts, or by using `pydevsup` or `PCASpy` to make an IOC-like device.
1. It is **not** possible to use python to start a run which has been set up in the vendor software (LSi Correlator Acquisition Software)
    - This is an issue, as the vendor software performs analysis on the raw data
1. In order to use the vendor's analysis tools, we would have to reverse engineer the XML save format used
1. We need to understand if we want to use the vendor's analysis tools in the vendor software or not.
   - If we want to use the vendor's analysis tools, we should ask the vendor for the XML specification
   - If we do not need to use the vendor's analysis tools, we will need to get a specification for the data analysis required on the data from the device

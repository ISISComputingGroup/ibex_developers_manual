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

### Adding a new record (PV)
The correlator PCASpy IOC adds a new interface (see [here](https://github.com/ISISComputingGroup/EPICS-LSICorrelator/blob/master/record.py)) which brings together methods typically required of a record/PV. `VAL`, `SEVR` and `STAT` fields are automatically created for all records.

A basic `Record` object holds the name of PV and a dictionary containing information about the fields of the record as specified in the [PCASpy documentation](https://pcaspy.readthedocs.io/en/latest/api.html#database-field-definition). For example, a simple PV to publish a temperature could look like:

```
temperature = Record("TEMPERATURE", {"VAL": float})
```


For enum records, the class attributes `convert_from_pv` and `convert_to_pv` lets you define a function which converts between the value of the PV and a more useful object. This is important for enums where the actual value of the PV is an integer, so a conversion between the integer and what that value represents is necessary.
Example, a basic binary PV:
```
SIM = Record("SIM",
             {'type': 'enum', 'enums': ["NO", "YES"]},
             convert_from_pv=bool
            )
```
Here, the value of the PV is 1 or 0, and the `bool()` built-in takes the current value of the PV as its argument and returns a boolean. The [PV database](https://github.com/ISISComputingGroup/EPICS-LSICorrelator/blob/master/pvdb.py) of the correlator uses this to convert between enum values and the objects they represent in python.

To create a setpoint PV which mimics the current Record type, set `has_setpoint = True` as an argument when instantiating the class. For example:
```
temperature = Record("TEMPERATURE", {"VAL": float}, has_setpoint=True)
```
will create `TEMPERATURE` and `TEMPERATURE:SP`, as well as the expected `VAL`, `SEVR` and `STAT` fields for the setpoint PV. These are all added to the `database_entries` for the object `temperature`. 

To add the PVs created in the Record `temperature` to the static PV database (including all `:SP` PVs) so they can be loaded into the PCASpy server:
```
STATIC_PV_DATABASE = {}
STATIC_PV_DATABASE.update(temperature.database_entries)
```

A `device_setter` is a function which takes in the current value of the PV and will perform some action on it, such as writing the PV value on to the device. In the LSI correlator, the settings for the correlator are written to the device through the vendor API using `device_setter`s.

### Issues/gotchas
 - This device is not polled, and so it is difficult to truly know whether the connection to the device has been dropped. Currently the device will read disconnected after a correlator run is started and no data is returned.
   - It might be possible to do something with websockets which would provide more immediate feedback whether the device connection is still alive, which is what most devices do.
 - Once the device connection has be severed, the IOC must be restarted. There is no logic in place to drop the `LSICorrelator` object and attempt a reconnection by spawning a new object.
 - Two of the output values from the device, `TraceChA` and `TraceChB` have a length which is proportional to the measurement duration requested. Because PCASpy PV lengths are specified at IOC boot time, these arrays may have to be truncated to publish them as PVs. Currently they are not published, but are saved to file.
 - The time series for the taken data labelled in the file as `Count Rate History (KHz)  CR CHA / CR CHB` is generated by using a constant called `DELTA_T` the value is from the example API documentation that comes with the device driver.
 - There is some test data which can be loaded into the analysis software in the manuals directory in testing. There is also the mock data used to generate that file which was used in testing the saving ticket.
 - Because this is not a traditional IOC with a `st.cmd` for starting, macro values are not explicitly shown before starting. If incorrect the IOC may fall over and start trying to parse blank strings etc. which will lead to exceptions like `RuntimeError: No file path specified to save data to: 'FILEPATH'`
 - If the correlation does not output in the file due to the `correlation_data` being equal to a blank array (`[]`), check that the default sampling time (minimum time lag) variable is set to an appropriate value. Common pre-sets used by IS are as follows: `12.5, 200, 400, 800, 1600, 3200`nano seconds.

### Saving the data
Ideally the data would be saved into a nexus file, and the subsequent data analysis would be performed in mantid. However, because this data analysis is not yet available in mantid, the data must be processed by the vendor's software. Therefore we need to recreate a data format which can be imported by the vendor software in order to do this data analysis. The format of these data files is a tab-separated variable format with the extension `.dat`, examples of which can be found on the share.

The IOC saves the file in two locations, once in `C:\Data` with a filename which allows it to get saved into the archive. The other file gets saved in a location specified by the user in a macro.

After a brief look, it appears that the vendor software may be using the `CONTIN` library to perform fitting of the correlation function.

## Testing with Hardware
To test with the LSi Correlator hardware, the laser will need to be run onto a sample so that the correlation function can be populated. This means that the DLS would need to be installed where safe to operate and the correlator plugged into the network on an instrument. IBEX can then be run (as distinct from the vendor program).
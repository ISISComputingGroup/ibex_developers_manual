> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [CAEN](CAEN)

A high voltage power supply normally used for detector electronics.

They are communicated with using Ethernet using an IOC originally developed at the Canadian Lightsource.

### Communicating with multiple CAENs
A single IOC can communicate with up to 8 CAEN crates, this appears to be a limit in the CAEN library as it defines MAX_CRATES as 8 in the library header and has a "too many connections" error code listed in its potential error codes. 

To do this the crates must be added into the `st.cmd` as so:

```
CAENx527ConfigureCreate "hv0", "_IP_ADDR1_"
CAENx527ConfigureCreate "hv1", "_IP_ADDR2_"
```

When `CAENx527DbLoadRecords` is called it will then create PVs of the form `hv0:_SLOT_:_CHANNEL_`
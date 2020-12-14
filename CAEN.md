> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [CAEN](CAEN)

A high voltage power supply normally used for detector electronics.

There are now two IOCs devoted to the CAEN. An older one from the Canadian light source (HVCAEN) and a newer one from SLAC (HVCAENA). They are communicated with over Ethernet. HVCAEN is used widely and HVCAENA is to be used on DETMON to test it. HVCAENA has more information available including board and crate parameters. Both IOCs have a read-only mode which can be set via macros.

### Communicating with multiple CAENs (Older IOC)
A single IOC can communicate with up to 8 CAEN crates, this appears to be a limit in the CAEN library as it defines MAX_CRATES as 8 in the library header and has a "too many connections" error code listed in its potential error codes. 

To do this the crates must be added into the `st.cmd` as so:

```
CAENx527ConfigureCreate "hv0", "_IP_ADDR1_"
CAENx527ConfigureCreate "hv1", "_IP_ADDR2_"
```

When `CAENx527DbLoadRecords` is called it will then create PVs of the form `hv0:_SLOT_:_CHANNEL_`

### Troubleshooting
If you run `dbl` and get mainly standard support IOC PVs check that comms have been established to the given IP address

If you log in to the console and cannot get an EPICS prompt, the whole console/procserv must be restarted, as typically the `Ctrl-X` option does not work in this situation either

If you can ping and telnet to the crate, but the EPICS driver cannot connect, the crate may need a (physical) power cycle. This is best done by detector group.

### HVCAENA (Newer IOC)

Currently can communicate with 4 CAEN crates at a time. Set up by defining macros IP_ADDRESS_X and SYS_TYPE_X for X from 0 to 3. Another macro READ_ONLY defines whether we can write to the CAEN crate with 1 for readonly and 0 for read and write.

A crate is loaded in the st.cmd with:

```
CAENHVAsynSetEpicsPrefix("$(MYPVPREFIX)$(IOCNAME):HV0:")
CAENHVAsynConfig("HV0",$(SYS_TYPE_0),"$(IP_ADDRESS_0)","username","password")
```

CAENHVAsynSetEpicsPrefix simply sets the pv prefix in the driver.
CAENHVAsynConfig creates a new CAENHVAsyn object, which loads dbs and creates pvs for system properties, board parameters and channel parameters. 

Read/write is set in the st.cmd with:

`CAENHVAsynReadOnly($(READ_ONLY=0))`


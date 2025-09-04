# Record simulation

EPICS supports the concept of running IOC records in "simulation mode" - here rather than reading input/output from devices 
according to the INP/OUT fields the record will bypass hardware and use an alternative value. We should only need to add this support to records that access hardware, other records should be able to work as normal on these supplied simulated values.

Simulated values can either be a constant, or can be read/written to another PV location. The principle we will use here is to create a set of dummy records named $(P)SIM:* to which we will read and write values, hence allowing us to join a set and a read together. Initially these dummy records will be "Soft Channel" analogue/binary records which will be joined so that readback and set are connected, in future these records could be pointed at a dummy ioc mechanism to e.g. smoothly ramp. 

Though a simulated motor exists, it is probably still worth doing record simulation for e.g. jaws as it provides a convenient way to test GUIs without having to start additional IOCs

The EPICS record has to initialise first before simulation mode is enabled internally, and this is where problems can occur. Some drivers will try to read a value from the hardware at record initialisation, and if this fails they leave the record in an error state that stops simulation mode working. If you see PACT is stuck at 1 this is typical of a failed record initialisation. You will either need to fix the device driver, or avoid this record when using recsim. 
  
There are several cases where recsim doesn't work properly (or not without significant extra work):
- Records with `PINI="YES"` - initialisation runs before channel access is active which causes issues.
- For I/O interrupt records there will be no hardware to trigger, but you can use the SSCN (simulation scan mode)
- Records that get pushed to from a protocol file, as the protocol file will not be run. 
- MBBI/MBBO records with Soft channel device support. Soft channel doesn't populate `RVAL`, it is possible to work around this in some simple cases but often the benefit of adding recsim to these records is not worth the time to get it to work.

There is a [script to help](Add-sim-records-script).
First add the following record that will be used to indicate if simulation mode is being used (this will have been done for you if you used the [device generator script](../creation/IOC-Generator)):

```
record(bo, "$(P)SIM") 
{
    field(SCAN, "Passive")
    field(DTYP, "Soft Channel")
    field(ZNAM, "NO")
    field(ONAM, "YES")
    field(VAL, "$(RECSIM=0)")
}
```

Add to the IOC in the db load (this will have been done for you if you used the [device generator script](../creation/IOC-Generator)):

```
RECSIM=$(RECSIM=0)
```


next you need to modify any records that talk to real hardware (i.e. those where DTYP is not "Soft Channel" or "Raw Soft Channel"). You add the SIML field (to tell the record whether it should run in simulation mode) and the SIOL fields (to tell it where to read/write values when in simulation mode). For example:
 
```
record(ai, "$(P)CURRENT") 
{
    field(SCAN, "1 second")
    field(DTYP, "stream")
    field(INP,  "@kepco.proto readActualCurrent $(PORT)")
    field(PREC, "3")
    field(EGU,  "A")
    field(SIML, "$(P)SIM")
    field(SIOL, "$(P)SIM:CURRENT")
}

record(ao, "$(P)CURRENT:SP") 
{
    field(SCAN, "Passive")
    field(DTYP, "stream")
    field(OUT,  "@kepco.proto writeCurrent $(PORT)")
    field(EGU, "A")
    field(PREC, "3")
    field(SIML, "$(P)SIM")
    field(SIOL, "$(P)SIM:CURRENT:SP PP")
}

record(ai, "$(P)CURRENT:SP:RBV") 
{
    field(SCAN, "1 second")
    field(DTYP, "stream")
    field(INP,  "@kepco.proto readSetpointCurrent $(PORT)")
    field(PREC, "3")
    field(EGU,  "A")
    field(SIML, "$(P)SIM")
    field(SIOL, "$(P)SIM:CURRENT:SP:RBV")
}
```



We now need to add, and join if necessary, the relevant $(P)SIM dummy records. For the moment we will just do a simple join of the records by creating an alias - however by using an alias rather than pointing at a single PV we allow a future option of using a soft IOC to e.g. ramp values smoothly. 

```
record(ao, "$(P)SIM:CURRENT") 
{
    field(SCAN, "Passive")
    field(DTYP, "Soft Channel")
}

alias("$(P)SIM:CURRENT","$(P)SIM:CURRENT:SP")

alias("$(P)SIM:CURRENT","$(P)SIM:CURRENT:SP:RBV")
```

To link the simulation to a record that is passively scanning you should add `field(FLNK, "<SOFT_CHANNEL_RECORD>")` to the simulation record.

For more information on fields in simulation records see [here](https://epics.anl.gov/base/R7-0/6-docs/dbCommonInput.html) for input records, or [here](https://epics.anl.gov/base/R7-0/6-docs/dbCommonOutput.html) for output records.

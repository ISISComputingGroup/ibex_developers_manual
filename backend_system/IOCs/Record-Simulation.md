> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Record simulation

EPICS supports the concept of running IOC records in "simulation mode" - here rather than reading input/output from devices 
according to the INP/OUT fields the record will bypass hardware and use an alternative value. We should only need to add this support to records that access hardware, other records should be able to work as normal on these supplied simulated values.

Simulated values can either be a constant, or can be read/written to another PV location. The principle we will use here is to create a set of dummy records named $(P)SIM:* to which we will read and write values, hence allowing us to join a set and a read together. Initially these dummy records will be "Soft Channel" analogue/binary records which will be joined so that readback and set are connected, in future these records could be pointed at a dummy ioc mechanism to e.g. smoothly ramp. 

Though a simulated motor exists, it is probably still worth doing record simulation for e.g. jaws as it provides a convenient way to test GUIs without having to start additional IOCs

There are several cases where recsim doesn't work properly (or not without significant extra work):
- Records with `PINI="YES"` - initialisation runs before channel access is active which causes issues.
- I/O interrupt records.
- Records that get pushed to from a protocol file.
- Records that get their values pushed from another DB record.
- MBBI/MBBO records - Soft channel device support doesn't populate `RVAL`, it is possible to work around this in some simple cases but often the benefit of adding recsim to these records is not worth the time to get it to work.
- Records with an AsynInt/AsynFloat datatype. See for example the AG3631A current pv.

There is a [script to help](Add-sim-records-script).
First add the following record that will be used to indicate if simulation mode is being used

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

Add to the IOC in the db load:

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
    field(SIOL, "$(P)SIM:CURRENT:SP")
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

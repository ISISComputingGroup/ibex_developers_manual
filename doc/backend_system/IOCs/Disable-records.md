> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Disable records

It would be convenient to be able to turn an IOC on/off by accessing a PV. We should allow this in IOCs that we write, but cannot guarantee that it will be always be possible. This could allow us to start all IOC's up in "disabled" mode, and then enable/disable by PV as per user choice, but for the moment the code below will start an IOC with comms enabled. The IBEX backend provide a macro setting the disable value this is `DISABLE` this need passed in dbload records. There is a helper script that will do this for you, as well as add `RECSIM`, see [here](Add-sim-records-script).

The work required is similar to that for adding RecordSimulation - we add an '''SDIS''' field to any records that access hardware (i.e. that are not "soft channel" records) and point this at a PV to control the mode 
   
```
record(ai, "$(P)CURRENT") 
{
    field(SCAN, "1 second")
    field(DTYP, "stream")
    field(INP,  "@kepco.proto readActualCurrent $(PORT)")
    field(PREC, "3")
    field(EGU,  "A")
    field(SDIS, "$(P)DISABLE")
}
``` 

```
record(bo, "$(P)DISABLE") 
{
  field(DESC, "Disable comms")
  field(PINI, "YES")
  field(VAL, "$(DISABLE=0)")
  field(OMSL, "supervisory")
  field(ZNAM, "COMMS ENABLED")
  field(ONAM, "COMMS DISABLED")
}
```

Add to the IOC in the db load:

```
DISABLE=$(DISABLE=0)
```
# Motors

If you are looking to disable motors from display in the motors view you need to set `MTRXXXX_able.VAL 1` or 0 if you want to enable them.
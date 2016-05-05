It would be convenient to be able to turn an IOC on/off by accessing a PV. We should allow this in IOCs that we write, but cannot guarantee that it will be always be possible. This could allow us to start all IOC's up in "disabled" mode, and then enable/disable by PV as per user choice, but for the moment the code below will start an IOC with comms enabled.

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
  field(VAL, "0")
  field(OMSL, "supervisory")
  field(ZNAM, "COMMS ENABLED")
  field(ONAM, "COMMS DISABLED")
}
```
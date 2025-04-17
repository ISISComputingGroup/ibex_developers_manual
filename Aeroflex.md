Previous logic of the ioc had this logic for sending mode params:

This logic is probably in connection with changing from PULSE to none PULSE versions of the MODE setpoint. The calculation part
*probably* takes care of switching to the right mode with respect to the specified order of modes in the mbbo in record MODE:SP

### Model 2023A

In db file at `aeroflexSup\aeroflex_2023A.db`
```
record(calcout, "$(P)SEND_MODE_PARAMS")
{
    field(DESC, "Set modulation button")
    field(SCAN, "Passive")
	field(INPA, "$(P)MODE:SP_NO_ACTION")
	field(INPB, "$(P)PULSE_CHECK:SP")
	field(CALC, "(B = 0) ? ((2 * A) + 1) : (2 * A)")
	field(OUT, "$(P)MODE:SP PP")
}
```

### Model 2030

In db file at `aeroflexSup\aeroflex_2030.db`
```
record(calcout, "$(P)SEND_MODE_PARAMS")
{
    field(DESC, "Set modulation button")
    field(SCAN, "Passive")
	field(INPA, "$(P)MODE:SP_NO_ACTION")
	field(INPB, "$(P)PULSE_CHECK:SP")
	field(CALC, "((B=1)&&(A>2))?(A-3):(A+2)")
	field(OUT, "$(P)MODE:SP PP")
}
```

These are now removed.
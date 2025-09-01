# Run Control

Run control is implemented purely in EPICS, by [the `RUNCTRL` ioc](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/RUNCTRL),
which uses [the `runcontrol` support module](https://github.com/isiscomputinggroup/epics-runcontrol).

The run control PVs are in the form:
```
IN:INSTNAME:CS:SB:block_name:RC:LOW         # Run-control low limit
IN:INSTNAME:CS:SB:block_name:RC:HIGH        # Run-control high limit
IN:INSTNAME:CS:SB:block_name:RC:ENABLE      # Whether run-control is enabled
IN:INSTNAME:CS:SB:block_name:RC:INRANGE     # Whether the block is currently in range
```

When a value is out of range, it will push this information into variables managed by the RUNCTRL ioc,
which will ultimately pause/resume data collection. Feedback can be obtained via the following PVs:

```
IN:INSTNAME:CS:RC:OUT:CNT      # number of items out of range
IN:INSTNAME:CS:RC:OUT:LIST     # names of PVs out of range (space separated in char waveform)
```

Channel access monitors can be posted on either `CNT` or `LIST`, `CNT` is guaranteed to see all transitions,
`LIST` will be up to date but may not see all transitions.

The blockserver is responsible for configuring the `RUNCTRL` ioc with the current list of blocks; it does
this by writing to the file
```
C:\Instrument\Settings\config\<machine>\configurations\rc_settings.cmd
```
which contains a set of `dbLoadRecords` instructions, which are picked up on a subsequent restart of the
`RUNCTRL` ioc, which the blockserver also performs.

The system is implemented by a set of db files in `support/RunControl` called `gencontrol.db` and `gencontrolMgr.db`.
These define logic for calling an action when values go in and out of range, as well as adding case insensitive
aliases. In the `RUNCTRL` ioc, these are loaded twice to create:
* `:RC:` (run control) PVs which trigger a DAE waiting state when out of range
* `:AC:` (alert control) PVs which trigger sending a message when out of range

On LOQ, a separate `:DC:` instance is also created, this calls a procedure to put in the aperture when the
detector count rate exceeds a limit.

## Troubleshooting

If the system gets stuck in a WAITING state with no blocks being outside runcontrol limits, 
then you can force a resync of the system with
```
caput %MYPVPREFIX%CS:RC:SYNC:SP 1
```

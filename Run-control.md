> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [Run Control](Run-control)

Run control is implemented purely in EPICS. A DB file support/RunControl/runcontrol.db can be loaded into any IOC and given the name of each PV that needs this feature. It defines a few PVs for this:

```
$(PV):RC:LOW
$(PV):RC:HIGH
$(PV):RC:ENABLE
$(PV):RC:INRANGE
```

When a values is out of range, it will push this information into variables managed by INSTETC which will ultimately pause/resume data collection. Feedback can be obtained via:

```
$(P):CS:RC:OUT:CNT      number of items out of range
$(P):CS:RC:OUT:LIST     names of PVs out of range (space separated in char waveform)
```

CA monitors can be posted on either `CNT` or `LIST`, `CNT` is guaranteed to see all transitions, `LIST` will be up to date but may not see all transitions

(`LIST` is actually a set which can be added to/removed from via PVs; it is called generically via aSub records so provides a general mechanism for keeping a more readable list of things if we need it).

Run `testRunControl` from `iocBoot` for an example. You need to start `INSTETC` first if you wish to use the above CS variables.

To do run control on SECI blocks a separate IOC ioc/RUNCTRL will be used. This will need to be restarted by the blockserver as appropriate and the blockserver will also need to (re)write a startup file for it containing lines like:

The system is implemented by a set of db files in `support/RunControl` called `gencontrol.db` and `gencontrolMgr.db`. These define logic for calling an action when values go in and out of range, as well as adding case insensitive aliases. In the ioc/RUNCONTROL these are loaded twice to create:
* :RC: (run control) PVs who allow setting limits and triggering WAITING on out of range
* :AC: (alert control) PVs who allow setting limits and triggering sending a message on out of range

On LOQ a separate :DC: instance is also created, this calls a procedure to put in the aperture when the detector count rate exceeds a limit

If the system gets stuck in a WAITING state with no blocks being outside of runcontrol limits, then you can force a resync of the system with e.g. for OFFSPEC `caput IN:OFFSPEC:CS:RC:SYNC:SP 1`

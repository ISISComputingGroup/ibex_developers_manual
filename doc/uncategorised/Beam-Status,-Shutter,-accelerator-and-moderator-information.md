> [Wiki](Home) > Accelerator Information

Information about the beam current and instrument shutter status is stored in the main accelerator control computer system, though a shutter is local to an instrument it is part of a safety system and we do not have direct access to it ourselves. Also the accelerator computer system can only read main shutter status - opening/closing a main shutter can only be performed using a physical button in the cabin. 

This information is fed from an IOC running on a machine on the accelerator network (merckx.isis.rl.ac.uk). This is a [Open VMS](https://en.wikipedia.org/wiki/OpenVMS) machine with the EPICS distribution from [here](https://github.com/ISISComputingGroup/EPICS-VMS/). The IOC is set to run on boot time and is auto-restarted if it is not present, it will also auto-restart if it receives too many errors, but some failures can cause it to hang.

**If the system restarts itself, then there will be a brief loss of PVs for beam current/shutters/moderator temp to instruments, some will go into a WAITING state when this happens if run control is enabled on the block**

if you need to contact the accelerator controls team, look for "ISIS Controls (Support)" in outlook
 
You can see the current error counts in nagios for the merckx system or via
```
camonitor ICS:IB:ERRCNT ICS:IB:CHANERRCNT
```
You can log onto this machine using details on usual access page (you will need to use ssh via something like PuTTY, or git bash with `-oHostKeyAlgorithms=+ssh-dss` as an argument)


The most likely cause of a problem is that the local database has stopped updating, thus giving an unchanging value. You can can check the server log file with: 
```
cd beamlogdir
type isisbeam.log
```
And see if there are errors about parameters not updating. Probably easiest thing to do is to kill the service and let it restart, then see if errors continue in the log. First type:
```
pipe sh sys | sea sys$input isisbeam
```
you will see a line like
```
26E12DAA ISISBEAM        LEF      6   132040   0 00:00:01.40       284    241
26F991FC ISISBEAM_1      HIB      4  2416385   0 00:08:24.20      9589   3173 MS
```
[_ISISBEAM_1_ is a sub-process of ISISBEAM and will die when you kill _ISISBEAM_]
The first number is the process id, in this case type
```
stop /id=26E12DAA
```
to kill it, then wait for it to restart (may take up to 30 seconds). Use the above `pipe` command to see then it has restarted, and then check isisbeam.log again. Look for messages after the `Starting iocInit` line in the file  

## more complicated details

The asyn parameters that are served by the IOC are mapped to VISTA parameters (this is the accelerator control system). You can see the mapping with:  
```
type params.txt
```
a line like
```
beam_ions        float    t  0    IDTOR::IRT1:CURRENT
```
means asyn parameter `beam_ions` (in the IOC Db files) is mapped to VISTA parameter `IDTOR::IRT1:CURRENT`. The other columns are related to data type and how the programs tries to check for stale (non updating) values. If the `isisbeam.log` indicated a huge number of errors for a particular parameter, then this could affect reading other parameters - after a certain number of errors the program restarts, but if it starts restarting too frequently this can cause PVs never to reconnect properly. In that case you _may need to temporarily remove a line_, but seek advice first. 

You can read the VISTA parameter directly on MERECKX if you think the issue is with the IOC e.g.
```
db_access IDTOR::IRT1:CURRENT
db_access t1shut::n1_overview:sta
```
you can search for errors about a particular parameter by e.g.
```
sea isisbeam.log IDTOR::IRT1:CURRENT
```
If you killed the `ISISBEAM` process above it has restarted, then the `isisbeam.log` file will only contain values since that restart. you can look at the previous log file by adding `;-1` to the file name
```
sea isisbeam.log;-1 IDTOR::IRT1:CURRENT
```
To see all log file versions type `dir isisbeam.log`

If something does appear to have gone wrong with this service (e.g. values are not updating) you should get in touch with the _accelerator controls group_. The easiest way to do this is to call the MCR and find out who is on call.

## Beam current block shows 0

A "Beam current" block may not be showing the accelerator beam current, it may be showing the effective beam current from the DAE. Blocks read from the accelerator will all be referring to global PV names starting AC: and TG: so if the block refers to an IN: it will be something on the local instrument. The DAE:BEAMCURRENT value is the effective DAE beam current, but if the dae is not counting (SETUP, WAITING, PAUSED) then this value will be zero. If the DAE is vetoing this value will vary between 0 and something else depending on what % of frames are being vetoed. If the chopper is being run at a lower frequency, the value will be lower too as the DAE is seeing less pulses and hence a lower effective beam current.    

## Value shows zero in IBEX/SECI but non-zero with `db_access` on MERECKX

If the third column in `params.txt` contains a `z` (e.g. `tz`) then this means that the parameter will be monitored for a stale (non updating) state and if this is detected it will send 0 as the value to IBEX/SECI. At time of writing this had only been requested for the decoupled methane, sending 0 when the value is uncertain means they will go into a WAITING state as they run control on methane temperature and it is important that they are not collecting data when a methane charge-change happens. In future the value could be EPICS alarmed, but for SECI instruments we need to send 0

You may be able to confirm a value is not updating by running `db_access` on it a few times with a reasonable time delay in-between, but some values are quite stable or fluctuate only a bit so this may be difficult to determine. You can view the typical value and variation in an accelerator parameter by following the links on values at [http://beamlog.nd.rl.ac.uk/status.xml](http://beamlog.nd.rl.ac.uk/status.xml) 

**If this is after a shutdown**, check the `st.cmd` and see if `epicsEnvSet("SIM_ISISBEAM", "1")` has been uncommented to stop out of cycle errors, if so comment it out and then kill the ISISBEAM process so it can restart

## Checking channel access on MERCKX
if you type
```
dir [--.db]
```
you will see all the db files used by the program, you can display one to screen using e.g.
```
type/page [--.db]isisbeam.db
```
On MERCKX `$(P)` is "" so there is no prefix to PVs you see listed. To use `caget` you first need to set an epics address list as broadcasts do not work (they require privileges). So type
```
def EPICS_CA_ADDR_LIST merckx
```
and then you can use `caget` or `camonitor` on values e.g.
```
camonitor TG:TS2:DMOD:METH:TEMP
```
You can [browse the Db file source on the web](https://github.com/FreddieAkeroyd/EPICS-VMS/tree/master/ioc/ISISBEAM/isisbeamApp/Db)
  
## intermittent dropouts

The program will restart after too many errors are detected. If you run:
```
camonitor ICS:IB:ERRCNT ICS:IB:CHANERRCNT
```
`ERRCNT` is the total number of channel reads errors since last successful read, `CHANERRCNT` is the number of channels currently in error. When `ERRCNT` passes a threshold, the program restarts and you will see these PVs as well as other beam PVs briefly become disconnected. Note that `CHANERRCNT` may be non-zero while `ERRCNT` remains 0, this means that there isn't an actual read error on the channel, but it is considered in error for another reason. You would typically need to look at `isisbeam.log` to tell. This usually means the program thinks the channel is `stale`. Each channel, even if it does not change value, should have its timestamp updated by the accelerator control system. Also things like beam current are flagged as suspicious if their value (when non-zero) is exactly the same value for a long period of time.       

## nothing working

check `isisbeam.log` but could be a scaled up version of intermittent dropouts leading to extremely frequent restarts and so no time for PVS to get connected. In bad cases you may need to remove lines from the `params.txt` file described above to stop the erroring reads being attempted.

## things not updating

`db_access LOCAL::BEAM:TARGET2`

on merckx will show the local database TS2 beam, if this seems unusually stable then the accelerator controls vista system may have frozen.

## server or services unavailable (nagios)

Check for `merckx` in nagios, put it in the quick search box on the nagios top page. The `TS2 Beam Current Updating` check should reflect similar to the `db_access LOCAL::BEAM:TARGET2`

If nagios shows `merckx` is down:
* during office hours email "ISIS Controls (support)" in the outlook address book and tell them that "The VMS MERCKX server is unreachable and instruments cannot access beam and moderator information that is important for running"
* out of hours contact the MCR and ask them to contact the on call ISIS accelerator controls computing person


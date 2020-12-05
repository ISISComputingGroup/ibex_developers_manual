> [Wiki](Home) > Accelerator Information

Information about the beam current and instrument shutter status is stored in the main accelerator control computer system, though a shutter is local to an instrument it is part of a safety system and we do not have direct access to it ourselves. Also the accelerator computer system can only read main shutter status - opening/closing a main shutter can only be performed using a physical button in the cabin. 

This information is fed from an IOC running on a machine on the accelerator network (merckx.isis.rl.ac.uk). This is a [Open VMS](https://en.wikipedia.org/wiki/OpenVMS) machine with the EPICS distribution from [here](https://github.com/FreddieAkeroyd/EPICS-VMS). The IOC is set to run on boot time and is auto-restarted if it is not present, it will also auto-restart if it receives too many errors, but some failures can cause it to hang.

You can log onto this machine using details on usual access page (you will need to use ssh via something like PuTTY)

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
231601FE ISISBEAM        HIB      6   346363   0 00:01:10.27      3907   2860 M
```
[_ISISBEAM_1_ is a sub-process of ISISBEAM and will die when you kill _ISISBEAM_]
The first number is the process id, in this case type
```
stop /id=231601FE
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
means asyn parameter `beam_ions` (in the IOC Db files) is mapped to VISTA parameter `IDTOR::IRT1:CURRENT`. The other columns are related to data type and how the programs tries to check for state values. If the `isisbeam.log` indicated a huge number of errors for a particular parameter, then this could affect reading other parameters - after a certain number of errors the program restarts, but if it starts restarting too frequently this can cause PVs never to reconnect properly. In that case you may need to temporarily remove a line, but seek advice first. 

You can read the VISTA parameter directly on MERECKX if you think the issue is with the IOC e.g.
```
db_access IDTOR::IRT1:CURRENT
db_access t1shut::n1_overview:sta
```

If something does appear to have gone wrong with this service you should get in touch with the accelerator controls group. The easiest way to do this is to call the MCR.

## Value shows zero in IBEX/SECI but non-zero with `db_access`

If the third column in `params.txt` is `tz` then this means that the parameter will be monitored for a stale (non updating) state and if this is detected it will send 0 as the value to IBEX/SECI. At time of writing this had only been requested for the decoupled methane, sending 0 when the value is uncertain means they will go into a WAITING state as they run control on methane temperature and it is important that they are not collecting data when a methane charge-change happens. In future the value could be alarmed, but for SECI we need to send 0     
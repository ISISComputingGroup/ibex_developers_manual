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
The first number is the process id, in this case type
```
stop /id=231601FE
```
to kill it, then wait for it to restart (may take up to 30 seconds). Use the above `pipe` command to see then it has restarted, and then check isisbeam.log again. Look for messages after the `Starting iocInit` line in the file  

The asyn parameters that are served are mapped to VISTA parameters  
```
type params.txt
```
you can read the VISTA parameter directly on MERECKX e.g.
```
db_access t1shut::n1_overview:sta
```

If something does appear to have gone wrong with this service you should get in touch with the accelerator controls group. The easiest way to do this is to call the MCR.
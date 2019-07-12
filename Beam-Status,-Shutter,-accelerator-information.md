> [Wiki](Home) > Accelerator Information

This information is fed from an IOC running on a machine on the accelerator network (merckx.isis.rl.ac.uk). The IOC is set to run on boot time and is auto-restarted if it is not present, it will also auto-restart if it receives too many errors.

You can log onto this machine using details on usual access page

The most likely cause of a problem is that the local database has stopped updating, thus giving an unchanging value. You can can check the server log file with: 
```
cd beamlogdir
type isisbeam.log
```
The asyn parameters that are served are mapped to VISTA parameters  
```
type params.txt
```
you can read the VISTA parameter directly on MERECKX e.g.
```
db_access t1shut::n1_overview:sta
```

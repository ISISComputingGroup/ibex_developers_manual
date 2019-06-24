> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [GUI](GUI-Troubleshooting)

This page contains information on how to troubleshoot some common issues with the GUI. These are issues that occur once the GUI has started, not issues in starting the GUI. A good place to start are the log files, they are stored in `...\Instrument\Apps\Client\workspace\logs`.

## IOC Start/Stop list is not Populated

If the IOC Start/Stop list is blank when the instrument is running then there is a problem with the PV serving this. The PV serving it comes from the DBSRV ioc and ultimately comes from the MySQL database. Console to the BD server:

`console -M localhost DBSVR`

should not be producing errors (pressing return creates blank lines)

Next check that the [database is up](Database-Troubleshooting).

## Target Platform Errors

In some cases when you recieve a `Resolving Target Definition` error, this can relate to some cached files that need to be refreshed and repeatedly performing the loop of `Clean project > Set as Target Platform > Reload` between 3-10 times can fix this issue. Set as Target Platform and Reload are located on the target view, located at `uk.ac.stfc.isis.ibex.targetplatform.target`.

## Other issues

[Memory "leaks"](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Debugging-memory-leaks-in-the-IBEX-GUI)

[PV Manager and Observers](PV-Manager-and-Observers-Logging)
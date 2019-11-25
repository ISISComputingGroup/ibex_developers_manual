> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [GUI](GUI-Troubleshooting)

This page contains information on how to troubleshoot some common issues with the GUI. These are issues that occur once the GUI has started, not issues in starting the GUI. A good place to start are the log files, they are stored in `...\Instrument\Apps\Client\workspace\logs`.

## IOC Start/Stop list is not Populated

If the IOC Start/Stop list is blank when the instrument is running then there is a problem with the PV serving this. The PV serving it comes from the DBSRV ioc and ultimately comes from the MySQL database. Console to the BD server:

`console -M localhost DBSVR`

should not be producing errors (pressing return creates blank lines)

Next check that the [database is up](Database-Troubleshooting).

## Target Platform Errors

In some cases when you receive a `Resolving Target Definition` error, this can relate to some cached files that need to be refreshed and repeatedly performing the loop of `Clean project > Set as Target Platform > Reload` between 3-10 times can fix this issue. Set as Target Platform and Reload are located on the target view, located at `uk.ac.stfc.isis.ibex.targetplatform.target`.

## JAXB dependency issues

We have seen some cases of JAXB causing issues with the GUI building. Since Eclipse builds in parallel a race condition can arise between building CSS (which expects some XML classes in the standard library) and the rest of the GUI (which has XML outside of the standard library due to using Java 11). If you have a load of JAXB issues, try the following:

1. In the project explorer delete all the plugins (Do not delete the files from disk)
1. Select "Import Existing Projects" and select the GUI base folder
1. Open the `uk.ac.stfc.isis.ibex.targetplatform` file
1. After the project has been imported click "Set Target Platform" in the top right

This seems to be the best way to resolve this. If you have persistent issues with JAXB and this method not working, please inform the team as we would like to investigate.

## Delete dotfiles

If Eclipse gets very confused with the project build, you might want to completely wipe clean all files/folders used in the project. You can create a new workspace but there are still several additional folders worth deleting if needed. In your user folder, there should be hidden "dot" folders called:

- .m2 (contains downloaded dependencies)
- .p2

## Other issues

[Memory "leaks"](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Debugging-memory-leaks-in-the-IBEX-GUI)

[PV Manager and Observers](PV-Manager-and-Observers-Logging)
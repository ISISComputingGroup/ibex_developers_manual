> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [DAE](DAE-Trouble-Shooting)

### No log files are produced in `c:\data` even though blocks are set to log.
The reason may be because cp hasn't been set to look for epics. In `C:\LabVIEW Modules\dae\isisicp.properties` set `isisicp.epicsdb.use = true` to log the epic's blocks

### DAE doesn't seem to be conected/I want to run without a DAE connected
The DA can be set to run in simulation mode, this must be unset before data will be collected. To set the mode edit the xml file in `C:\LabVIEW Modules\dae\icp_config.xml` set the simulate property to 1 to simulate 0 to use hardware.


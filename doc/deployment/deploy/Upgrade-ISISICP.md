# ISISICP

## DAE type remaining the same

1. Check `isisicp` and `isisdatasvr` processes are not running. You cannot kill them if ISISDAE-IOC-01 is running so you need to stop this separately (and stop procserv restarting them) or run stop_ibex_server  
1. Backup existing installation: copy the following to `c:\data\old\isisdae_backup_YYY_MM_DD`:
    - `c:\LabVIEW Modules\dae`
    - `c:\data\recovery.run`
    - `c:\data\selog.*` (`.sq3` `.sq3-shm` and `.sh3-wal` files)

1. Confirm the type of DAE hardware you have - look in `c:\labview modules\dae\icp_config.xml`, if DAEType in this file is 1 or 2 you have DAE2 hardware (1 means it runs in neutron mode, 2 in muon mode), if it is 3 you have a DAE3 hardware. So if DAEType is 1 or 2 use the **DAE2** folder on the share below to install from, if DAEType is 3 use the **DAE3** folder to install from. If you install the wrong type, it will just fail to start and complain in the ICP log file about wrong dae type; you would just need to reinstall the right one.
1. Go to `\\isis\inst$\Kits$\CompGroup\ICP\ISISICP` and into the directory for the DAE hardware you determined was installed (DAE2 or DAE3)
1. Go into the latest build number directory (also in `LATEST_BUILD.txt`) and double click on `update_inst.cmd`
   This can take a while (several minutes). You will get various messages. The following are OK:
    * If it can't replace the file `isisicp_extMC.dll` as it is open
1. As printed to screen at the end of script, open a command terminal as administrator (gamekeeper) and run
   ```
   cd "c:\labview modules\dae"
   register_programs.cmd
   ```
1. Now delete `c:\data\selog.*` (`.sq3` `.sq3-shm` and `.sh3-wal` files), `c:\data\current.run*` and `c:\data\data.run*`
```
del /q c:\data\selog.*
del /q c:\data\current.run*
del /q c:\data\data.run*
```

This completes the ISISICP installation.

***

At this point is it useful to install/update the JournalParser. This utility is not part of the ISISICP
but parses the XML journal files generated by the ISISICP in `c:\data` at run end and updates entries in the MqSQL database
 used by the IBEX journal viewer. The journal parser executable program is ran by the isisicp at each run end 
via end_of_run.bat to add a new entry  

1. To install/update journal parser, navigate to  `<public share>\journalparser_static_new`
   - *Either* run `install.bat` to install it an migrate all old journal files (new ibex instrument)
   - *or* run `install_no_migrate.bat` to install it without copying old journal files (existing ibex instrument)

If this install fails for some reason, it will not affect an instrument operating - it will just mean that new run entries will not 
be visible in the ibex journal viewer (which looks at MySQL). It will not affect the actual creation of the XML reference files by the ISISICP,
so a full re=import can be done at a later date when any issues are resolved.


### A log from register_programs.cmd
```

C:\Windows\system32>cd "c:\labview modules\dae"
c:\LabVIEW Modules\dae>register_programs.cmd
ERROR: The process "LabVIEW.exe" not found.
ERROR: The process "SeciUserInterface.exe" not found.
ERROR: The process "SECIStartup.exe" not found.
ERROR: The process "mkscript3.exe" not found.
ERROR: The process "muonscript.exe" not found.
ERROR: The process "makescript.exe" not found.
ERROR: The process "PlotScan.exe" not found.
ERROR: The process "vs7jit.exe" not found.
ERROR: The process "mari_script.exe" not found.
ERROR: The process "tkgenie32.exe" not found.

INFO: No tasks running with the specified criteria.
ERROR: The process "isisdatasvr.exe" not found.
ERROR: The process "isisicp.exe" not found.
ERROR: The process "cwdss.exe" not found.
ERROR: The process "runapp.exe" not found.
The process cannot access the file because it is being used by another process.
Registering Release images
Registering in x64\Release
Press any key to continue . . .

c:\LabVIEW Modules\dae>
```

## Changing DAE type (DAE2 -> DAE3)

1. If DAE3 is new to this computer, it may not have the "Microsoft Visual C++ 2015 redistributable" installed. Check in the installed program list, if it is missing run `vc_redist.x64.exe` in `\\isis\inst$\Kits$\CompGroup\ICP\ISISICP\VS2015`   
1. install the new DAE software as above
1. edit icp_config.xml and change DAEType from 1 to 3
1. Before you run DAE3 for first time you will need to run `set_dae3_arp.bat` in `labview modules\dae` as an administrator
1. You will also need to add `set_dae3_arp.bat` to be run as administrator at system startup. To do this run the task scheduler as administrator and then import the `DAE3_arp_boot_task.xml` boot task file.
1. Also check firewall settings 

## Developer installation

The ISISICP on a developer machine is ran from the `ICP_Binaries` directory, this will get automatically updated when `create_icp_binaries.bat` is run. If you get simulated DAE issues, you may need to re-register the ISISICP by running `EPICS\ICP_Binaries\isisdae\register_programs.cmd` as an admin account  

> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) > [Upgrade ISISICP](Upgrade-ISISICP)

# To upgrade on a computer when the DAE type is remaining the same

1. Check `isisicp` and `isisdatasvr` processes are not running. You cannot kill them if ISISDAE-IOC-01 is running so you need to stop this separately (and stop procserv restarting them) or run stop_ibex_server  
1. Backup existing installation: copy the following to `c:\data\old\isisdae_backup_YYY_MM_DD`:
    - `c:\LabVIEW Modules\dae`
    - `c:\data\recovery.run`
    - `c:\data\selog.*` (.sq3 .sq3-shm and .sh3-wal files)

1. Confirm the type of DAE you have - look in c:\labview modues\dae\icp_config.xml, if DAEType is 1 you have a DAE2, if it is 3 you have a DAE3. If you install the wrong type, it will just fail to start and complain in the ICP log file.
1. Go to \\isis\inst$\Kits$\CompGroup\ICP\ISISICP and into the directory for the DAE type you have
1 . Go into the latest build directory and double click on update_inst.cmd
   This can take a while (several minutes). You will get various messages. The following are OK:
    * If it can't replace the file `isisicp_extMC.dll` as it is open
1. As printed to screen at the end of script, open a command terminal as administrator (gamekeeper) and run
   ```
   cd "c:\labview modules\dae"
   register_programs.cmd
   ```
1. Now delete `c:\data\selog.*` (.sq3 .sq3-shm and .sh3-wal files)
1. Finally run journal parser installation, found at `<public share>\journalparser_static_new`
   - *Either* run `install.bat` to install it an migrate all old journal files
   - *or* run `install_no_migrate.bat` to install it without copying old journal files

and a log from register_programs.cmd
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

# changing DAE type (DAE2 -> DAE3)

1. install the new DAE software as above
1. edit icp_config.xml and change C DAEType from 1 to 3
 
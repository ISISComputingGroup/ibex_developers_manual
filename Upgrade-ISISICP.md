> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) > [Upgrade ISISICP](Upgrade-ISISICP)

1. Check isisicp and isisdatasvr processes are not running. You cannot kill them if ISISDAE-IOC-01 is running so you need to stop this separately (and stop procserv restarting) or run stop_ibex_server  
1. Backup existing installation: copy to `c:\data\old\isisdae_backup_YYY_MM_DD`
    - `c:\LabVIEW Modules\dae`
    - `c:\data\recovery.run`
    - c:\data\selog.* (.sq3 .sq3-shm and .sh3-wal files)

1. Open a command window
1. Run:
   ```
      cd c:\LabVIEW Modules\dae
      update_inst.cmd
   ```
This can take a while. You will get various messages. The following are OK:
1. access denied messages for `ss.ini`
1. If it can't replace the file isisicp_extMC.dll as it is open
1. messages about establishing working folders for projects

1. Run again from the same directory (you need to do `cd ..` to get back to the dae directory)
1. Should be quicker this time
1. As printed to screen at endf of script, Open a command terminal as administrator
1. Run
   ```
   cd "c:\labview modules\dae"
   register_programs.cmd
   ```

Now delete c:\data\selog.* (.sq3 .sq3-shm and .sh3-wal files)

The following is a log from update_inst going OK
```
C:\LabVIEW Modules\dae>update_inst.cmd
Current project is $/Labview/Ray Of Light LabVIEW Modules/dae
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\dae has been established as the working folder for project
$/Labview/Ray Of Light LabVIEW Modules/dae.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
Running update_inst_main.cmd $LastChangedRevision: 1550 $, $LastChangedDate: 2013-06-24 15:54:15 +0100 (Mon, 24 Jun 2013) $
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
** Updating Labview project dae (recursive) **
A subdirectory or file c:\labview modules\dae already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/dae
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\dae has been established as the working folder for project
$/Labview/Ray Of Light LabVIEW Modules/dae.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
** Updating Labview project beam logger (recursive) **
A subdirectory or file c:\labview modules\beam logger already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/beam logger
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\beam logger has been established as the working folder for
project $/Labview/Ray Of Light LabVIEW Modules/beam logger.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
** Updating Labview project Common/User Details (recursive) **
A subdirectory or file c:\labview modules\Common\User Details already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/Common/User Details
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\Common\User Details has been established as the working
folder for project $/Labview/Ray Of Light LabVIEW Modules/Common/User Details.Access to file "\\isis\inst$\safe$\users\spudulik\ss.
ni" denied
** Updating Labview project Common/Version Control (recursive) **
A subdirectory or file c:\labview modules\Common\Version Control already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/Common/Version
Control
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\Common\Version Control has been established as the working
folder for project $/Labview/Ray Of Light LabVIEW Modules/Common/Version
Control.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
** Updating Labview project Common/External Interface (recursive) **
A subdirectory or file c:\labview modules\Common\External Interface already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/Common/External
Interface
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\Common\External Interface has been established as the
working folder for project $/Labview/Ray Of Light LabVIEW
Modules/Common/External Interface.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
** Updating Labview project Common/Experiment Parameters (recursive) **
A subdirectory or file c:\labview modules\Common\Experiment Parameters already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/Common/Experiment
Parameters
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\Common\Experiment Parameters has been established as the
working folder for project $/Labview/Ray Of Light LabVIEW
Modules/Common/Experiment Parameters.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
** Updating Labview file save xml to file.vi in project Common **
A subdirectory or file c:\labview modules\Common already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/Common
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\Common has been established as the working folder for
project $/Labview/Ray Of Light LabVIEW Modules/Common.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
** Updating Labview file load xml from file.vi in project Common **
A subdirectory or file c:\labview modules\Common already exists.
Current project is $/Labview/Ray Of Light LabVIEW Modules/Common
Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
c:\labview modules\Common has been established as the working folder for
project $/Labview/Ray Of Light LabVIEW Modules/Common.Access to file "\\isis\inst$\safe$\users\spudulik\ss.ini" denied
C:journal_main.html
1 File(s) copied
C:journal.xsl
1 File(s) copied
C:journal_help.html
1 File(s) copied
Could Not Find c:\LabVIEW Modules\dae\service\isis*.*
Could Not Find c:\LabVIEW Modules\dae\service\SELOG*.*
Could Not Find c:\LabVIEW Modules\dae\service\Microsoft.*
ECHO is off.
*******************************************************************************************
** YOU NOW NEED TO RUN  "c:\labview modules\dae\register_programs.cmd"  AS  "gamekeeper" **
*******************************************************************************************
```
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
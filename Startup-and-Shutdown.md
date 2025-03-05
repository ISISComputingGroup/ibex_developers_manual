> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [Startup and Shutdown](Startup-and-Shutdown)

This page shows the behaviour expected for IBEX or starting and stopping. There are two different modes in which IBEX can run:

1. Full: As the instrument control, which archiving, configurations, logging etc
2. MiniInst: As a provider of IOCs which are used by SECI

In addition to this it can be on an instrument but switched off because SECI is running.

The system will provide IOCs for SECI (2) if a file called `startup.txt` is in the ICP Config Root. ICP Config Root defaults to `C:/Instrument/Settings/config/<COMPUTERNAME>/configurations` but may be overridden in `icpconfighost.txt` in `C:/Instrument/Settings/config`.

On a system reboot IBEX should start but only if it was running when the machine was shut down. Whether IBEX was running is recorded by the contents of a file (<add file path>) - this will be done as part of ticket [#1950](https://github.com/ISISComputingGroup/IBEX/issues/1950). The reboot behaviour is achieved by placing start_ibex_server script in the startup directory.

Start behaviour:
* If IBEX is running and IBEX is requested to start then IBEX should restart itself (this should have minimal data loss).
* If SECI is running and IBEX is requested to start then IBEX should kill it on start and remove the file which claims it is the only running control software.
* If full IBEX is running and SECI starts it will kill IBEX using the stop IBEX server script - this ticket [#1951](https://github.com/ISISComputingGroup/IBEX/issues/1951).

## Process on Start (not definitive see actual scripts)

There is a startup script `ibex_system_boot.bat`, this can be installed as a startup program, if IBEX server was previously started it restarts it otherwise it does nothing. It is detected by the presence of `c:\instrument\var\tmp\ibex_running.txt`.

Start is initiated from `C:\Instrument\Apps\EPICS\start_ibex_server.bat`. It:

1. Stop the ibex server (see below)
1. Put start file in place [#1950](https://github.com/ISISComputingGroup/IBEX/issues/1950)
1. Runs ca repeater bat
    1. Kills old carepeater tasks
    1. Starts a new task in procserve
1. Runs conserver bat
    1. Stops conserver
    1. Starts a new conserver
1. If startup.txt exists in config runs start_ibex_server_mini else runs start_ibex_server_full.bat
1. [full only] update iocs db
1. [full only] start ioc log server (if logs cannot be loaded, you may not have permission to view the files, this can happen if you accidentally started the server in admin mode in the past. This can be fixed by either changing the folder's permissions or deleting its configs)
1. [full only] start the alarm server
1. start the gateways
1. start the procserver for the iocs (call `iocstartup\procserv.bat`)
1. starts proc server control (PSCTRL IOC)
1. Reload conserver
1. [full only] start the block server
1. [full only] start the database server
1. [full only] start the script server (if not on an instrument)
1. [mini only] Start and enable auto start on IOC in startup.txt list

## Process on Stop (not definitive see actual scripts)

Initiated from start or `C:\Instrument\Apps\EPICS\stop_ibex_server.bat`. It stops the following

1. Remove start file [#1950](https://github.com/ISISComputingGroup/IBEX/issues/1950)
1. IOCs in `startup.txt`
1. Conserver
1. IOC Log Server
1. Alarm server
1. Gateway
1. Blockserver
1. Database Server
1. Script Server
1. IOCs with PID files
1. All procserve processes
1. All exes in ioc startups
1. Gateway exe
1. `Conserver.exe`
1. `Console.exe`
1. `PSCTRL`
1. Archive engine
1. MK3 Chopper
1. [instrument only] `css.exe`
1. [instrument only] `javaw`
1. [instrument only] `java`
1. [instrument only] `pythonw`
1. [instrument only] `ibex-client`
1. [without startup.txt] `python`
1. [without startup.txt] `SeciUserInterface`
1. [without startup.txt] `SeciStartup`
1. [without startup.txt] `LabView`
1. [without startup.txt] `mkscript3`
1. [without startup.txt] `muonscript`
1. [without startup.txt] `PlotScan.exe`
1. [without startup.txt] `vs7jit.exe`
1. [without startup.txt] `mari_script.exe`
1. [without startup.txt] `tkgenie32.exe`
1. [without startup.txt] `dllhost.exe`
1. [without startup.txt] `isisdatasvr.exe`
1. [without startup.txt] `isisicp.exe`
1. [without startup.txt] `cwdss.exe`
1. `camonitor`
1. `caRepeater`

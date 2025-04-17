> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [Other](Other-Troubleshooting)

## Can not rename/delete/move a file/folder

This happens when windows locks a file for you. The lock can either be because of a local process or because of a file is shared from another computer. 
### Local Process
Close items that might be using the file, especially command line consoles in that directory. If you still can't find it load "Process Explorer" (sysinternels some of the machines have this in the start menu). Thn click `Menu` -> `Find` -> `Find File or Handle ...` type the path and this will give you the process id that is holding the lock. 

### Share
If it is through a share the file lock will not appear in here. In this case look at the share information <update where that is here> then kill the share. It may reconnect so just do the operation quickly.

## Instrument state keeps 'Processing' but always goes back to 'Unknown'

Check to see if you have any errors similar to the following:

```
[2016-11-07 16:04:49] CoCreateInstanceEx (ISISICP) : Class not registered
```

If so, you haven't registered your `isisicp.exe` program with the registry. Follow the steps to [Configure DAE for simulation mode on developer's computer](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/First-time-installing-and-building-(Windows)#configure-dae-for-simulation-mode-on-developers-computer)

If you have done this it may be that the isisicp.exe program is too old. Older versions do not contain a function which is needed by IBEX. Check the file   svn_revision.txt   in c:\labview modules\dae - it needs to be 1633 or higher. If it needs updating, ask a SECI specialist to update the program.

## Instrument Page not Working on Web Dashboard

Several causes

1. Check that the instrument is in the list of Instruments in https://github.com/ISISComputingGroup/JSON_bourne/blob/master/webserver.py and that the version on web server is up-to-date.

1. Issues with MySQL in the moment the IBEX server was started (this seems to affect the archiver start up). Check logs of the MySQL service in the `var` area, fix any issues so that MySQL is running correctly again, then restart the IBEX server.

1. If it works in your browser but not he users they may have a old cached copy (this shouldn't happen but we have seen it in Safari). Clear their browser cache and reload.

1. Try restarting `ARINST` on the instrument. It can happen that the archiver does not pick up all PVs to be archived on server startup. A symptom of this is that the configuration file under `EPICS\CSS\master\ArchiveEngine\inst_config.xml` is very short compared to other machines.

## `cmake error: could not load cache` seen during build

Try deleting any `CMakeCache.txt` files in the appropriate directory

# Unable to communicate with MOXA ports

We encountered this issue in August 2017 on HRPD. Neither SECI nor IBEX could communicate with the MOXA. We solved the problem on the fly by remapping the ports from COM blocks 5-20 to 21-36. NPort Administrator had several ports in the former block marked as in use in spite of no devices being active. The ultimate fix was to clear out the offending registry value:

1. Click start → Run → type regedit and click OK button
1. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\COM Name Arbiter`
1. Now on the right panel, you can see the key `ComDB`. Right-click it and click modify
1. In value Data section select all and delete reset to zero
1. Restart the machine if needed (to do this remotely use the command `shutdown -r -t 0`

A similar (but I think unrelated) problem was found in June 2018 on ZOOM. Some ports in a MOXA were found to not communicate with a Julabo. According to both the lights on the MOXA and the MOXA's web interface there was data being transmitted both to and from the device. However, when transmitting to the device (either via hyperterminal or IOC) no actual data was received. Restarting the MOXA had no affect. The problem was ultimately not resolved, the julabos were moved to different ports.

# Can't build any IOCS

When trying to use Make to build IOCs you might encounter an Error 2. The failing Make will look something like this:
```
process_begin: CreateProcess(NULL, echo Generating runIOC.bat, ...) failed.
make (e=2): The system cannot find the file specified.
```
This can be a result of having an environment path for git that points to `git/bin`. If it is, then make will think you are on linux and then the build will fail. You must change this to be `git/cmd` to point at the Windows binaries.

See also [Ticket 4201](https://github.com/ISISComputingGroup/IBEX/issues/4201) for a potential fix.

# Beam Logger details not updating

If PVs are visible in R3 then probably the gateway on the control service machine need to be updated.

# User says they can not see their nexus data files on external machine

See [DAE-Trouble-Shooting](DAE-Trouble-Shooting#user-says-they-can-not-see-their-nexus-data-files-on-external-machine)

# Value logs from IOC not produced/ARACCESS not creating log files/ENGINX Stress Rig not writing log files

See [ioc trouble shooting](IOC-And-Device-Trouble-Shooting#value-logs-from-ioc-not-producedaraccess-not-creating-log-filesenginx-stress-rig-not-writing-log-files)


# Remote desktop client keep freezing/hanging

Try the following as administrator on the machine that you are running remote desktop client on:
```
* Run gpedit.msc
* Navigate to Computer Configuration > Administration Templates > Windows Components > Remote Desktop Services > Remote Desktop Connection Client. 
* Set the "Turn Off UDP On Client" setting to Enabled.
```


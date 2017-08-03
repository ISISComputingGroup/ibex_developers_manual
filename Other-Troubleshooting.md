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

Check that the instrument is in the list of Instruments in https://github.com/ISISComputingGroup/JSON_bourne/blob/master/webserver.py and that the version on NDAEXTWEB1 is up-to-date.

## `cmake error: could not load cache` seen during build

Try deleting any `CMakeCache.txt` files in the appropriate directory

# Unable to communicate with MOXA ports

We encountered this issue in August 2017 on HRPD. Neither SECI nor IBEX could communicate with the MOXA. We solved the problem on the fly by remapping the ports from COM blocks 5-20 to 21-36. NPort Administrator had several ports in the former block marked as in use in spite of no devices being active. The ultimate fix was to clear out the offending registry value:

1. Click start → Run → type regedit and click OK button
1. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\COM Name Arbiter`
1. Now on the right panel, you can see the key `ComDB`. Right-click it and click modify
1. In value Data section select all and delete reset to zero
1. Restart the machine if needed (to do this remotely use the command `shutdown -r -t 0`

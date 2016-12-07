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

If so, you haven't registered your `isisicp.dae` program with the registry. Follow the steps to [Configure DAE for simulation mode on developer's computer](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/First-time-installing-and-building-(Windows)#configure-dae-for-simulation-mode-on-developer's-computer)
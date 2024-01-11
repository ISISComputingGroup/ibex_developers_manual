> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [genie_python](genie_python-Troubleshooting)

## Logging

### Where are the logs?

Genie_python writes its logs to `...\Instrument\var\logs\genie_python`.

### What does `ERROR: CAException` mean when it is in the log?

The following is written to the log when a virtual circuit disconnects from the IOC side:

```
    2018-05-21T15:21:31	(CA)	(15712)	ERROR: CAException: type=-1 state=192 op=5 file=..\cac.cpp lineNo=1223
    2018-05-21T15:21:31	(CA)	(15712)	ERROR: CAException: type=6 state=192 op=0 file=..\getCopy.cpp lineNo=92
```

The time stamp on these are for the first `get_pv` call or equivalent after a disconnect.

## Command problems

### Can not set or get a block reports disconnected

There can be multiple problems, check:

1. Block exists
1. Block is spelt correctly, use `b.` and autocomplete
1. Try getting the underlying PV `g.get_pv("IN:<instrument>:CS:SB:<Block name?")`
1. Restart the GUI genie_python console

## Import problems

### Problems importing a dependency that should be in `genie_python`

Have you pulled and [rebuilt](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-and-installing-genie_python) the latest version of the repository under `\Apps\Python3` ?

### Genie_python crashes on start, Underlying python works but fails on `import numpy`

If `genie_python` crashes on start with a windows error but the underlying Python appears to start ok try importing `numpy`. We have a problem with the latest CPUs (`skylakex`) running under the hypervisor which means that the `OPENBLAS` library has an unknown instruction in it. The current fix is to set the environment variable so it appears it is running a different core type. Do this with:

    OPENBLAS_CORETYPE=Haswell

This is set within the system environment on the PC; currently, this fix is only needed on `RIKENFE` and `MUONFE`.

### Can't find Python 3

If you get an error message similar to

```
*** Cannot find GENIE-PYTHON 3 - some things are not likely to work ***
```
on running `config_env.bat`, you need to ensure you have Python 3 available on your system.

## Error patching CaChannel
When running `dev_build_python.bat`, you may get an error when Windows tries to apply a patch to the `CaChannel.py` file. E.g. 
```
can't find file to patch at input line XXX
Perhaps you should have used the -p or --strip option?
```
This seems to be caused by using patch from strawberry perl patch and not from git.

If this happens, comment out the `patch` command in `common_build_python.bat`, then run the script again. Once it's finished, open a Git Bash window, `cd` to `/c/Instrument/Apps/Python3/package_builder` and run the same `patch` command you commented out, changing the Windows paths to UNIX paths (`\` -> `/` and `C:` -> `/c`). Then, check the `CaChannel.py` file to ensure it was patched properly.

## Other Issues

### Can not set change users

Users seems not to get set properly using g.change_users, see ticket [5812](https://github.com/ISISComputingGroup/IBEX/issues/5812). Look into this it is more than a one off.

### Repeated error messages in console while waiting

If you get repeated errors of the form:

```
2020-11-11T17:20:48	(CMD)	(17808)	2020-11-11 17:20:48.374781: Exception in waitfor loop: UnableToConnectToPVException: Unable to connect to PV IN:LARMOR:DAE:GOODUAH: does not exist
2020-11-11T17:20:48	(CMD)	(17808)	2020-11-11 17:20:48.512496: Exception cleared
```
You may need to restart the genie_python session. The root cause of this issue is currently unknown. See ticket [5893](https://github.com/ISISComputingGroup/IBEX/issues/5893) for details, including a script which can scan all instruments for occurrences of this issue. If this issue is seen again, please create a new ticket to investigate further and also link it here.

### can read local PVs from instrument but not e.g. `CS:INSTLIST` or accelerator ones like beam current

In one case this was due to the firewall rule for `A:\python3\python.exe` had been disabled - a process firewall exception is needed to allow it to receive the UDP name query reply 

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

### Can not set or get a block reports diconnected

There can be multiple problems, check:

1. Block exists
1. Block is spelt correctly, use `b.` and autocomplete
1. Try getting the underlying pv `g.get_pv("IN:<instrument>:CS:SB:<Block name?")
1. Restart the GUI genie_python console

## Import problems

### Problems importing a dependency that should be in `genie_python`

Have you pulled and [rebuilt](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-and-installing-genie_python) the latest version of the repository under `\Apps\Python` ?

### Genie_python crashes on start, Underlying python works but fails on `import numpy`

If `genie_python` crashes on start with a windows error but the underlying Python appears to start ok try importing `numpy`. We have a problem with the latest CPUs (`skylakex`) running under the hypervisor which means that the `OPENBLAS` library has an unknown instruction in it. The current fix is to set the environment variable so it appears it is running a different core type. Do this with:

    OPENBLAS_CORETYPE=Haswell

This is set within the system environment on the PC; currently, this fix is only needed on `RIKENFE` and `MUONFE`.

### Can't find Python 3

If you get an error message similar to

```
*** Cannot find GENIE-PYTHON 3 - some things are not likely to work ***
```
on running `config_env.bat`, you need to ensure you have **both** python 2 and python 3 available on your system.

## Error patching CaChannel
When running `dev_build_python.bat`, you may get an error when Windows tries to apply a patch to the `CaChannel.py` file.

If this happens, comment out the `patch` command in `common_build_python.bat`, then run the script again. Once it's finished, open a Git Bash window, `cd` to `/c/Instrument/Apps/Python/package_builder` and run the same `patch` command you commented out, changing the Windows paths to UNIX paths (`\` -> `/` and `C:` -> `/c`). Then, check the `CaChannel.py` file to ensure it was patched properly.
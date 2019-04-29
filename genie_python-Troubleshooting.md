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

## Problems importing a dependency that should be in `genie_python`

Have you pulled and [rebuilt](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-and-installing-genie_python) the latest version of the repository under `\Apps\Python` ?

### Genie_python rashes on start, Underlying python works but fails on `import numpy`

If `genie_python` crashes on start with a windows error but the underlying Python appears to start ok try importing `numpy`. We have a problem with the latest CPUs (`skylakex`) running under the hypervisor which means that the `OPENBLAS` library has an unknown instruction in it. The current fix is to set the environment variable so it appears it is running a different core type. Do this with:

    OPENBLAS_CORETYPE=Haswell

This is set within the system environment on the PC; currently, this fix is only needed on `RIKENFE` and `MUONFE`.

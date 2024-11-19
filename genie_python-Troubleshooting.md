> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [genie_python](genie_python-Troubleshooting)

## Logging

### Where are the logs?

Genie_python writes its logs to `C:\Instrument\var\logs\genie_python`.

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

Have you pulled and [rebuilt](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-and-installing-uktena) the latest version of the repository under `\Apps\Python3` ?

### Can't find Python 3

If you get an error message similar to

```
*** Cannot find GENIE-PYTHON 3 - some things are not likely to work ***
```
on running `config_env.bat`, you need to ensure you have Python 3 available on your system.

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

### Can't import channel-access modules

If you get an error of the form:

```
Traceback (most recent call last):
  File "c:\Jenkins\workspace\System_Tests\test_genie_python_common_imports.py", line 33, in _attempt_to_import_module_by_name
    mod = importlib.import_module(module_name)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Instrument\Apps\Python3\Lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Instrument\Apps\Python3\Lib\site-packages\setuptools_dso\__init__.py", line 10, in <module>
    from .dsocmd import DSO, Extension, install, build, build_dso, build_ext, bdist_egg
  File "C:\Instrument\Apps\Python3\Lib\site-packages\setuptools_dso\dsocmd.py", line 729, in <module>
    _needs_builddso(_build, right_before='build_clib')
  File "C:\Instrument\Apps\Python3\Lib\site-packages\setuptools_dso\dsocmd.py", line 715, in _needs_builddso
    assert issubclass(command, Command)
```

When trying to import channel access libraries (`CaChannel`, `pcaspy`, `aioca`, `p4p` etc), this may be because `import pip` has previously been run in the same python session. See https://github.com/pypa/pip/issues/8761 for some details/links. `import pip` is not generally supported/recommended by python and is a bad idea - if wanting to install packages dynamically, use `subprocess` instead to explicitly spawn a new process which calls pip.

It's also technically possible to replace `import pip` with:

```
import _distutils_hack
_distutils_hack.remove_shim()
import pip
```

But this is not recommended for obvious reasons.

# `genie_python` Troubleshooting

## Logging

### Where are the logs?

`genie_python` writes its logs to `C:\Instrument\var\logs\genie_python`.

### What does `ERROR: CAException` mean when it is in the log?

The following is written to the log when a virtual circuit disconnects from the IOC side:

```
    2018-05-21T15:21:31	(CA)	(15712)	ERROR: CAException: type=-1 state=192 op=5 file=..\cac.cpp lineNo=1223
    2018-05-21T15:21:31	(CA)	(15712)	ERROR: CAException: type=6 state=192 op=0 file=..\getCopy.cpp lineNo=92
```

The time stamp on these are for the first {external+genie_python:py:obj}`get_pv <genie.get_pv>` call or equivalent after a disconnect.

## Command problems

### Can not set or get a block; reports disconnected

There can be multiple problems, check:

1. Block exists
1. Block is spelt correctly, use `b.` and autocomplete
1. Try getting the underlying PV `g.get_pv("IN:<instrument>:CS:SB:<Block name>")`
1. Restart the GUI Python console

## Problems finding a python interpreter

### Can't find the Uktena Python distribution

If you get an error message similar to

```
*** Cannot find GENIE-PYTHON 3 - some things are not likely to work ***
```
on running `config_env.bat`, you need to ensure you have the {doc}`/system_components/Python` installed on your system.
You may need to follow the {doc}`/system_components/python/Building-and-installing-uktena` instructions.

```{note}
As of October 2025, many processes in the IBEX backend depend on the Uktena python distribution. However, we are
gradually migrating these to use {doc}`python virtual environments </system_components/python/Python-venvs>`; the eventual goal is that Uktena will not be required
for the IBEX server backend.
```

### No appropriate `venv` has been created for a backend process

We are gradually migrating our server-side processes to use {doc}`uv python environments </system_components/python/Python-venvs>`.

These virtual environments are created on instruments [by the IBEX deployment script](https://github.com/ISISComputingGroup/ibex_utils/blob/b5998462ddd4d5aa4123e30104166043151cefea/installation_and_upgrade/ibex_install_utils/tasks/system_tasks.py#L146). If that step has previously been missed or failed during a deployment, it will need to be re-run.

If you need to do this manually for one specific module, you may run:
```
rmdir /s /q .venv
uv venv .venv
uv pip sync requirements-frozen.txt
```
at the top-level of the relevant module. Modules using this approach will have a `requirements-frozen.txt`.

On a developer machine, the virtual environments are created by the [developer update script](https://github.com/ISISComputingGroup/ibex_utils/blob/master/installation_and_upgrade/developer_update.bat); if you are missing virtual environments on your developer machine, you will need to re-run that script.

## Other Issues

### Repeated error messages in console while waiting

If you get repeated errors of the form:

```
2020-11-11T17:20:48	(CMD)	(17808)	2020-11-11 17:20:48.374781: Exception in waitfor loop: UnableToConnectToPVException: Unable to connect to PV IN:LARMOR:DAE:GOODUAH: does not exist
2020-11-11T17:20:48	(CMD)	(17808)	2020-11-11 17:20:48.512496: Exception cleared
```
You may need to restart the genie_python session. The root cause of this issue is currently unknown. See ticket [5893](https://github.com/ISISComputingGroup/IBEX/issues/5893) for details, including a script which can scan all instruments for occurrences of this issue. If this issue is seen again, please create a new ticket to investigate further and also link it here.

### Can read local PVs but not central PVs

Central PVs could include:
- `CS:INSTLIST` (the instrument list)
- Accelerator PVs, for example beam current

In one case, this was due to the firewall rule for `A:\python3\python.exe` which had been disabled - a process firewall exception is needed to allow it to receive the UDP name query reply.

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

```python
import _distutils_hack
_distutils_hack.remove_shim()
import pip
```

But this is not recommended for obvious reasons.

### Pyright completely fails to run

Pyright keeps a cache directory in `c:\Users\<user>\.cache\pyright-python`, this can get corrupted, if it does get corrupted pyright will entirely fail to execute. This cache directory can be deleted (at the cost of the next script-check operation being much slower).

Error from {external+genie_python:py:obj}`g.load_script <genie.load_script>` will be a `json.decoder.JSONDecodeError` as pyright does not return JSON in this case (but rather, returns some non-JSON error message).

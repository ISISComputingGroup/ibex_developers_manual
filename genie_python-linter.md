> [Wiki](Home) > [genie_python](genie_python) > [linter information](genie_python-linter)

On `g.load_script` genie_python now runs pylint on the scripts. This help the user see errors before the script is run. However sometimes this causes its own issues. There is a [page in the user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Error-Checking-Troubleshooting) describing what the user should do.

Here are some more tips that we don't necessarily want to encourage. 

Warnings can be removed from a line by adding a comment

`<line> # pylint disable=<warning name>`

e.g. `from IMAT_library import *  # pylint: disable=wildcard-import, unused-wildcard-import`


### Linting dynamically defined variables
Python allows programmers to set attributes dynamically using expressions like `locals()['foo'] = 1`, which creates a local variable called `foo` with value `1`. Pylint doesn't support dynamic assignment, so if `foo` was subsequently referenced in the code it would be counted as an undefined variable.

In cases where we need to lint scripts containing dynamic assignments, we can write a Pylint [transform plugin](http://pylint.pycqa.org/en/latest/how_tos/transform_plugins.html) to let Pylint know that the dynamically assigned variables are OK and should not be counted as undefined. This has been done [here](https://github.com/ISISComputingGroup/genie_python/blob/0a5f5093486e85e550b8168810e3d5cd762e34ff/Lib/site-packages/genie_python/scanning_instrument_pylint_plugin.py) to support dynamic assignments in the [SCANS library](https://github.com/ISISComputingGroup/IBEX/issues/5214), where some scripts were dynamically adding all methods of classes derived from `ScanningInstrument` to the local module.



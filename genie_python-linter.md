> [Wiki](Home) > [genie_python](genie_python) > [linter information](genie_python-linter)

On `g.load_script` genie_python now runs pylint on the scripts. This help the user see errors before the script is run. However sometimes this causes its own issues. There is a [page in the user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Error-Checking-Troubleshooting) describing what the user should do.

Here are some more tips that we don't necessarily want to encourage. 

Warnings can be removed from a line by adding a comment

`<line> # pylint disable=<warning name>`

e.g. `from IMAT_library import *  # pylint: disable=wildcard-import, unused-wildcard-import`


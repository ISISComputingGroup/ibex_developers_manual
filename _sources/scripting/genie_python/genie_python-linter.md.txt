# `genie_python` script checking (linting)

On {external+genie_python:py:obj}`g.load_script <genie.load_script>` genie_python now runs pylint on the scripts. This help the user see errors before the script is run. However sometimes this causes its own issues. There is a {external+ibex_user_manual:doc}`page in the user manual <scripting/Error-Checking-Troubleshooting>` describing what the user should do.

If a warning cannot be fixed, and you are sure the code is otherwise correct, warnings can be ignored from a line by adding a comment:

```python
some_code()  # pylint disable=<warning name>
```

For example:
```python
from IMAT_library import *  # pylint: disable=wildcard-import, unused-wildcard-import
```

If the error is a pyright (typing) error, as opposed to a pylint error, then the comment syntax is:

```python
some_code()  # pyright: ignore
```

### Linting dynamically defined variables

Python allows programmers to set attributes dynamically using expressions like `locals()['foo'] = 1`, which creates a local variable called `foo` with value `1`. Pylint doesn't support dynamic assignment, so if `foo` was subsequently referenced in the code it would be counted as an undefined variable.

In cases where we need to lint scripts containing dynamic assignments, we can write a Pylint [transform plugin](http://pylint.pycqa.org/en/latest/how_tos/transform_plugins.html) to let Pylint know that the dynamically assigned variables are OK and should not be counted as undefined. This has been done [here](https://github.com/ISISComputingGroup/genie/blob/19cdfeedaf5ec9107f0328a69204b621858c859a/src/genie_python/scanning_instrument_pylint_plugin.py#L14) to support dynamic assignments in the [SCANS library](https://github.com/ISISComputingGroup/IBEX/issues/5214), where some scripts were dynamically adding all methods of classes derived from `ScanningInstrument` to the local module.



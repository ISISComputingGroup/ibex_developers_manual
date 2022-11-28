# Importing

### Current mechanism

Currently the instrument scripts area has a custom import mechanism which essentially tries to replicate:

```
from * import *
import *
```

This has caused a number of issues with modules overwriting functions, everything being put in the global namespace, and module ordering conditions. It was decided at a meeting to phase out this method of importing instrument scripts.

### Future (new) mechanism

Instrument script imports should use standard python imports everywhere, including in the instrument scripts `__init__` file. This new mechanism will be phased in for new instruments and instruments that run into an issue with the old mechanism. When Python 3 comes along, we should go through the remaining instruments and also convert those to using standard python imports.

An example of a "standard" python import is:
```
from module.file import function
```

For example, on an instrument which defines a `set_temperature` method inside `inst\eurotherms.py`, the import would be:
```
from inst.eurotherms import set_temperature
```

For simple instruments, we may be able to put all of the instrument scripts in one file (`inst.py`) rather than a module. In that case we would just have:

```
from inst import set_temperature
```

It was decided not to try to bulk-change all existing instrument scripts, as this is too risky in terms of potentially breaking scripts.

See also the issues linked to https://github.com/ISISComputingGroup/IBEX/issues/3496

### General Instrument Scripts
The general instrument scripts are in this [repository](https://github.com/ISISNeutronMuon/InstrumentScripts) and include scripts like `do_sans` and `do_trans`, as well as the scans library.
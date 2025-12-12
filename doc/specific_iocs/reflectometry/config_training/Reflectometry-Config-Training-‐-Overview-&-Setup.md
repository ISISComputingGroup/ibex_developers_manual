# Reflectometry Config Training: Overview & Setup

This training unit presents a series of exercises which take you through the creation of a reflectometry config. The aim of this is to become more confident in working with the python configuration itself as well as to hopefully learn something about how the reflectometry IOC works internally. 

**NB:** Whilst care has been taken so that the examples in the exercises produce a beamline model that resembles those of real instruments, it will be simplified in many ways for the sake of clarity. 

## Useful Resources:

- {external+ibex_user_manual:doc}`Reflectometry View User Manual <gui/Reflectometry-View>`
- [Reflectometry Config Documentation & Reference Manual](../Reflectometry-Configuration)
- [Reflectometry Glossary](../Reflectometry-Glossary)

## Setup Instrument Configuration & Dev Environment:

1. Open up the IBEX GUI.
2. Create a new configuration called `REFL_TRAINING` or something similar.
3. Add the `GALIL_01` IOC to the configuration, give it a `Sim. Level` of `RECSIM`, and assign `01` to the `MTRCTRL` macro, everything else can stay as the default values.
4. Add the `GALIL_02` IOC to the configuration, give it a `Sim. Level` of `RECSIM`, and assign `02` to the `MTRCTRL` macro, everything else can stay as the default values.
5. Add the `GALIL_03` IOC to the configuration, give it a `Sim. Level` of `RECSIM`, and assign `03` to the `MTRCTRL` macro, everything else can stay as the default values.
6. Add the `REFL_01` IOC to the configuration, everything stays as the default values.
7. Load your configuration.
8. Make sure the Reflectomery perspective is available to you, if it isn't you can make it visible via the `Preferences` menu.
9. At this point if you open the Relectometry perspective the `Server Status` should indicate an `ERROR` as it can't find the configuration.
10. In the configurations folder for the computer you are using create a folder called `refl`, and in `refl` create `config.py`.
11. If you restart the `REFL_01` IOC at this point, the server will still be in error, but the error text should have changed to being unable to read the file rather than being unable to find it.
12. Open `config.py` in the editor of your choice, and copy in this code, which is the most reflectometry configuration you have that will load.

```Python
from typing import Dict

from ReflectometryServer.beamline import Beamline
from ReflectometryServer.config_helper import (
    add_mode,
    get_configured_beamline,
)


def get_beamline(macros: Dict[str, str]) -> Beamline:
    #########################
    # FIXED BEAMLINE VALUES #
    #########################

    # Modes
    _nr = add_mode("NR") # The underscore is to ensure this passes for pyright because the mode is needed for getting the configured beamline, but is unused locally

    ##############################
    # BEAMLINE MODEL STARTS HERE #
    ##############################

    return get_configured_beamline()
    
```

13. At this point you should be able to edit `config.py` in the following pages and build up your example system.


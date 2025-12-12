# Reflectometry Config Training: Overview & Setup

This training unit presents a series of exercises which take you through the creation of a reflectometry config. The aim of this is to become more confident in working with the python configuration itself as well as to hopefully learn something about how the reflectometry IOC works internally. 

**NB:** Whilst care has been taken so that the examples in the exercises produce a beamline model that resembles those of real instruments, it will be simplified in many ways for the sake of clarity. 

## Useful Resources:

- {external+ibex_user_manual:doc}`Reflectometry View User Manual <gui/Reflectometry-View>`
- [Reflectometry Config Documentation & Reference Manual](../Reflectometry-Configuration)
- [Reflectometry Glossary](../Reflectometry-Glossary)

## Setup Instrument Configuration & Dev Environment:

1. Navigate to `...\Apps\EPICS\support\motorExtensions\master\settings\<computer name>\galil`
2. Create a `jaws.cmd` with the following contents, so that the appropriate jaws are available later.

```
$(IFIOC_GALIL_01) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS1:,mXN=MTR0101,mXS=MTR0102,mXW=MTR0104,mXE=MTR0103")
$(IFIOC_GALIL_01) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS2:,mXN=MTR0105,mXS=MTR0106,mXW=MTR0108,mXE=MTR0107")
```

3. In the same folder create an `axes.cmd` with the following, these aliases are useful later.

```
$(IFIOC_GALIL_03) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:TRANS,mAXIS=MTR0305")
$(IFIOC_GALIL_03) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:HEIGHT,mAXIS=MTR0307")
$(IFIOC_GALIL_03) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:PHI,mAXIS=MTR0306")
$(IFIOC_GALIL_03) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:PSI,mAXIS=MTR0308")
$(IFIOC_GALIL_02) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=MONITOR,mAXIS=MTR0208")
```

4. Open up the IBEX GUI.
5. Create a new configuration called `REFL_TRAINING` or something similar.
6. Add the `GALIL_01` IOC to the configuration, give it a `Sim. Level` of `RECSIM`, and assign `01` to the `MTRCTRL` macro, everything else can stay as the default values.
7. Add the `GALIL_02` IOC to the configuration, give it a `Sim. Level` of `RECSIM`, and assign `02` to the `MTRCTRL` macro, everything else can stay as the default values.
8. Add the `GALIL_03` IOC to the configuration, give it a `Sim. Level` of `RECSIM`, and assign `03` to the `MTRCTRL` macro, everything else can stay as the default values.
9. Add the `REFL_01` IOC to the configuration, everything stays as the default values.
10. Load your configuration.
11. It may make things clearer if you update the motor descriptions as per the following table:

| Axis | Galil 01 | Galil 02 | Galil 03 |
| -- | -- | -- | -- |
| 01 | Jaws 1, North | Detector Angle | Slit 1 Offset |
| 02 | Jaws 1, South | Detector Position | Slit 2 Offset |
| 03 | Jaws 1, East | Bench Front | |
| 04 | Jaws 1, West | Bench Back | |
| 05 | Jaws 2, North | Bench Slide | Sample Stack Translation |
| 06 | Jaws 2, South | Supermirror Position | Sample Stack Phi | 
| 07 | Jaws 2, East | Sumpermirror Angle | Sample Stack Height/Offset |
| 08 | Jaws 2, West | Monitor | Sample Stack Psi |

12. Make sure the Reflectometry perspective is available to you, if it isn't you can make it visible via the `Preferences` menu.
13. At this point if you open the Reflectometry perspective the `Server Status` should indicate an `ERROR` as it can't find the configuration.
14. In the configurations folder for the computer you are using create a folder called `refl`, and in `refl` create `config.py`.
15. If you restart the `REFL_01` IOC at this point, the server will still be in error, but the error text should have changed to being unable to read the file rather than being unable to find it.
16. Open `config.py` in the editor of your choice, and copy in this code, which is the most reflectometry configuration you have that will load.

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

17. At this point you should be able to edit `config.py` in the following pages and build up your example system.


The calibration files are anything that are equipment specific but not how to drive it, they are settings which are common to all instruments. The test for whether a file belong in this repository is imagine changing a file on an instrument the change should be able to be reflected to the other instruments thus improving their results. There will be some grey areas for instance the barn doors on Muon Front end. It is unlikely these calibration setting will be used elsewhere but they could be and if they were changed it wouldn't effect anything else so this is a good place to put them.

A prime example of this are the temperature sensors which have a calibration of current to temperature. If a mistake is found in the calibration it should be corrected and pushed to other instruments.

These files live in a separate repository at:

    http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git

This repo should be clones with:

    git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git C:\Instrument\Settings\config\common

The reason these files are in a separate repository is that they have a different release cycle to the ibex backend (they can be updated mid experiment where we wouldn't want to release a whole new experiment backend). It might be possible to place them in the configuration branch for instruments but merging them across instruments would be tricky. They need to be shared because equipment is shared between experiments.

## Calibration Data within the Repo

1. `temp_sensors` - temperature sensor calibration files
1. `magnets` - calibration for magnets (mostly Danfysik)
1. `barndoors` - calibration for motors on barndoors
1. `ramps` - shared ramp files (mostly for a eurotherm)

Items **NOT** within the repostiory

1. `motion set points` - calibration for motion set points e.g. sample changes. These probably do not belong in the repository (after debate) because they will be changed on an instrument but if this is pushed to another instrument the offsets do not make any sense. Some motion set points might be applicable we shall wait and see.


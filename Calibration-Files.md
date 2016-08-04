The calibration files are anything that are equipment specific but not how to drive it, they are settings. A prime example of this are the temperature sensors which have a calibration of current to temperature. These files live in a separate repository:

    TODO create repo

This repo should be clones with:

    git clone <address> C:\Instrument\Settings\config\calib

The reason these files are in a separate repository is that they have a different release cycle to the ibex backend (they can be updated mid experiment where we wouldn't want to release a whole new experiment backend). It might be possible to place them in the configuration branch for instruments but merging them across instruments would be tricky. They need to be shared because equipment is shared between experiments.

## Calibration Data within the Repo

This section should be retired if it gets out of date too quickly.

1. `temp_sensors` - temperature sensor calibration files
1. `magnets` - calibration for magnets (mostly Danfysik)
1. `motion set points` - calibration for motion set points e.g. sample changes, the offsets for these change on a regular basis




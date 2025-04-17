# Central archiver appliance

Note: this page describes the work-in-progress implementation of the _central_ inst archiver based on the [archive appliance](https://epicsarchiver.readthedocs.io/en/latest/). For information about the older, existing inst archiver, see [CSS archiver](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/CSS-Archive-Engine).

## Architecture

Based on decisions taken in [issue 8469](https://github.com/ISISComputingGroup/IBEX/issues/8489), the proposed architecture is:

- Run a single, central, archive appliance cluster for the inst archiver
  * (the word "cluster" is archive appliance terminology, this may actually just be one machine depending on performance metrics etc)
- Initially for a short period this may be in parallel with the existing inst archivers on the instruments
  * As we gain confidence with the new archiver, we then may choose to start automatically removing old rows from the "old" archiver (without backup) periodically, and then eventually remove it once we've gained enough confidence.
- Various options for where exactly the central archiver will get deployed.
  * Our own central windows machine that we control / administer
  * Our own central linux machine that we control / administer
  * SCD cloud (probably linux?)
  * FIT cloud (probably windows?)
- Use containers so that the solution is agnostic to where it actually ends up running.
  * Needs a reasonable amount of disk space. Based on historic archiving data something on the order of a TB or two will likely be sufficient to keep a cycles' worth of data at full granularity, and then decimated data longer-term.
        We can adjust our archive appliance policies here to fine-tune the exact balance between space usage and data granularity
- Don't move the block archiver (at least initially)
  * This means isisicp doesn't need to change initially - if/when we move the block archiver we'll also need to change isisicp.
  * This also means that we can gain experience/confidence with the inst archiver running centrally, and then can make a decision about what we want to do with the block archiver later, based on the experience we've gained and reliability metrics etc etc.
  * inst archiver likely takes the bulk of the space for archived data on most instruments.

## Implementation

Archive appliance configuration files are in [isis-aa-config](https://github.com/isiscomputinggroup/isis-aa-config) and our build of the archive appliance is at [`epicsarchiverap`](https://github.com/isiscomputinggroup/epicsarchiverap).

The archiver appliance is run using containers, so you will need to install rancher desktop to do any development on this system.

Some key commands are:

Run the archive appliance (run from within `isis-aa-config` repo):
```
nerdctl compose -f docker-compose.yaml up
```

Stop, rebuild & restart container (without cached images, e.g. if you have changed `Containerfile`):
```
nerdctl compose -f docker-compose.yaml down && nerdctl compose -f docker-compose.yaml build --no-cache && nerdctl compose -f docker-compose.yaml up
```

To run a bash session inside the running container:
```
nerdctl exec -it my_aa /bin/bash
```

When running, the archive appliance UI is available at http://localhost:17665/mgmt/ui/index.html


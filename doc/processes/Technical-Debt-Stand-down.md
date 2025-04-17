# Technical Debt Stand-down

A technical debt stand-down day is a day devoted to fixing technical debt in the system. The format is:

1. Choose a day where most people are free
1. Choose a topic (See table below)
1. On the day, people pick up tickets when they get in, often working in pairs. There is an extra standup at 4pm to discuss what has been done. This is the moment to choose to either:
    - stop working on a ticket (commit everything to a branch and add it to the ticket to be picked up later)
    - move it into the current sprint
    - ensure a ticket is reviewed

Try to make sure all tickets by the end of the day are in a good state.

### Ideas for Topics


- Fix script generator errors: https://github.com/ISISComputingGroup/IBEX/issues/5500
- Emulator for the compressors
- Improve genie python unit tests coverage. It is lacking in several complicated pieces of code, such as the genie_change_cache module.
- Add to IOC numbers so that all IOCs have at least 2
- Alarming
   * Web does the same GUI
   * Remove invalid alarm
   * All IOCs should have an beast alarm
- Squish tests [#3707](https://github.com/ISISComputingGroup/IBEX/issues/3707)
- Eclipse/CSS interaction
- Tech debt tickets
- Block server exception handling
- Deployment/release process
    - Automatically add release numbers based on the name of the release branch
    - On install if only one component is release then fall back to later components e.g. if only 4.4.1 GUI is available install 4.4.0 server and genie_python
    - Automate some manual steps
- Bugs
- Emulator/IOC tests
- Excess logging
- Dataweb/dashboard improvements
- Server submodule clean
    - Add readmes to submodules in the server 
    - Remove unneeded submodules.
    - Create automated dependency map
    - Put all tools in one place (See [duplicated code](Code-Duplication))
    - Think about moving ISIS things to support
- EPICS Make clean uninstall can be successfully performed if old git files exist
- Fix IOC generator
- `genie_python` unit test coverage
- `dbchecker` vs `dbunitchecker` vs `dbchanges`
- Python 3 Compatibility
- User manual updates e.g. https://github.com/ISISComputingGroup/IBEX/issues/2763 and https://github.com/ISISComputingGroup/IBEX/issues/3814
- Update the specific device IOC pages see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Retrospective-notes-2020.05.28#specific-device-ioc-pages-on-wiki)
- Tidy up code, remove unneeded parts
    - Discuss what to do with pv sets
- Fix epics unit tests (https://github.com/ISISComputingGroup/IBEX/issues/5539)

### Missing Documentation

Section to document missing documentation.

- Area detector [#4362](https://github.com/ISISComputingGroup/IBEX/issues/4362)


# Creating new submodules in EPICS

You will want to make sure you have run [IOC Generator](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/IOC-Generator) first, if this is for a new device's IOC. 

This script will create the IOC, OPI, support (including lewis emulator and system tests), and Makefiles for these various folders as well.

## Write the IOC, OPI, emulator, system tests, etc. 

Consult the device's manual, as well as any documentation the instrument scientists may have on their needs/wants. More info can be found here:
* [Creating an ISIS StreamDevice IOC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-an-ISIS-StreamDevice-IOC)
* [OPI Creation](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/OPI-Creation)
* [Emulating Devices](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Emulating-Devices)
* [Test naming](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Test-naming)
* [IOC Test Framework Documentation](https://github.com/ISISComputingGroup/EPICS-IOC_Test_Framework/blob/master/README.md)

## Final Push to EPICS top

Once everything is written, and final commits and pull requests have been created in the `EPICS-<device-name>` and `EPICS-ioc` repositories, navigate to the top of EPICS, from the branch created by `device_generator.py` (Ticket_XXXX_Add_IOC_<DEVICENAME>) add, commit, and push the newly added submodule
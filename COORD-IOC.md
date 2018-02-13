# Purpose

The COORD IOC should be home for any inter-IOC interactions. Currently it is being used for mode change sequences on RIKEN (https://github.com/ISISComputingGroup/IBEX/issues/2813).

It contains:
- SNL programs specific to the co-ordination task(s) in a particular setup. These are state machines.
- DBs which the SNL use to communicate with outside records (if intermediate DBs are required)

# Testing

The IOC test framework is now capable of spawning multiple IOCs together. Therefore, it is possible to test a full stack of interactions from one IOC to another via the COORD IOC. For documentation on the IOC test framework see https://github.com/ISISComputingGroup/EPICS-IOC_Test_Framework .
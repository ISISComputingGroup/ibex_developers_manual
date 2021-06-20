> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [IOC Testing framework](IOC-Testing-Framework)

See documentation at [https://github.com/ISISComputingGroup/EPICS-IOC_Test_Framework/blob/master/README.md](https://github.com/ISISComputingGroup/EPICS-IOC_Test_Framework/blob/master/README.md)

As of [6555](https://github.com/ISISComputingGroup/IBEX/issues/6555) IOC system tests are being moved from a single location to being next to the device they test. The tests next to the device can be run using `run_tests.bat` in `support/device/master/system_tests`. This bat file will pass through any command line arguments to the IOC_Test_Framework and so arguments documented above can still be used. You can also run `make ioctests` in the `support/device/master` to run the tests but this will not let you pass through command line arguments and will not display output until the whole test is finished.

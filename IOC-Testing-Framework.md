The aim of the IOC Testing Framework is to allow the creation of automated tests for testing the behaviour of the IOCs. These tests are designed to be run on a nightly basis via Jenkins to provide some reassurance that there have been no breaking changes applied to the IOCs.

The testing is limited to a certain extent because it won't be testing the IOCs with the real hardware, but Lewis can be used to provide a good approximation.

It is also possible to use the framework to test the IOC in record simulation mode if a Lewis emulator is not available, but is should be noted that provides a less complete simulation.

Instructions for running the tests, adding new tests etc. are provided in the README file for the repository.





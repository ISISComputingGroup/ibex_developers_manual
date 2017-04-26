> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [IOC Testing framework](IOC-Testing-Framework)

The aim of the IOC Testing Framework is to allow the creation of automated tests for testing the behaviour of the IOCs. These tests are designed to be run on a nightly basis via Jenkins to provide some reassurance that there have been no breaking changes applied to the IOCs.

The testing is limited to a certain extent because it won't be testing the IOCs with the real hardware, but Lewis can be used to provide a good approximation.

It is also possible to use the framework to test the IOC in record simulation mode if a Lewis emulator is not available, but is should be noted that provides a less complete simulation.

Instructions for running the tests, adding new tests etc. are provided in the README file for the repository.

# The IOCs
The IOCs need to have their st.cmd or st-common.cmd editing to enable them to work with the testing framework.
Here is an example st-common.cmd from the Julabo:

```
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(JULABO)/julaboApp/protocol"

cd ${TOP}

##ISIS## Run IOC initialisation
< $(IOCSTARTUP)/init.cmd

## For testing framework only:
$(TESTDEVSIM) epicsEnvSet "IFDEVSIM" " "
$(TESTDEVSIM) epicsEnvSet "IFNOTDEVSIM" "#" 
$(TESTDEVSIM) epicsEnvSet "RECSIM" "0"
$(TESTRECSIM) epicsEnvSet "IFDEVSIM" "#"
$(TESTRECSIM) epicsEnvSet "IFNOTDEVSIM" " " 
$(TESTRECSIM) epicsEnvSet "RECSIM" "1"

## For emulator use:
$(IFDEVSIM) epicsEnvShow("EMULATOR_PORT") 
$(IFDEVSIM) drvAsynIPPortConfigure("L0", "localhost:$(EMULATOR_PORT)")

## For real device use:
$(IFNOTDEVSIM) drvAsynSerialPortConfigure("L0", "$(PORT)", 0, 0, 0, 0)
$(IFNOTDEVSIM) asynSetOption("L0", -1, "baud", "4800")
$(IFNOTDEVSIM) asynSetOption("L0", -1, "bits", "7")
$(IFNOTDEVSIM) asynSetOption("L0", -1, "parity", "even")
$(IFNOTDEVSIM) asynSetOption("L0", -1, "stop", "1")

## Load record instances

##ISIS## Load common DB records 
< $(IOCSTARTUP)/dbload.cmd

## Load our record instances
dbLoadRecords("$(DB_FILE)","P=$(MYPVPREFIX)$(IOCNAME):, PORT=L0, RECSIM=$(RECSIM=0), DISABLE=$(DISABLE=0)")

##ISIS## Stuff that needs to be done after all records are loaded but before iocInit is called 
< $(IOCSTARTUP)/preiocinit.cmd

cd ${TOP}/iocBoot/${IOC}
iocInit

## Start any sequence programs

##ISIS## Stuff that needs to be done after iocInit is called e.g. sequence programs 
< $(IOCSTARTUP)/postiocinit.cmd
```
The section labelled `For testing framework only` uses the `$(TESTDEVSIM)` macro to enable the IOC to be run in the correct mode for testing. The macro specifying the port number to use is generated within the testing framework, it will be a random free port number.
The '$(TESTDEVSIM)' macro shouldn't appear for configuration in the IBEX GUI.




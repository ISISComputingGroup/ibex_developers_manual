> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [IOC Testing framework](IOC-Testing-Framework)

The aim of the IOC Testing Framework is to allow the creation of automated tests for testing the behaviour of the IOCs. These tests are designed to be run on a nightly basis via Jenkins to provide some reassurance that there have been no breaking changes applied to the IOCs.

The testing is limited to a certain extent because it won't be testing the IOCs with the real hardware, but Lewis can be used to provide a good approximation.

It is also possible to use the framework to test the IOC in record simulation mode if a Lewis emulator is not available, but is should be noted that provides a less complete simulation.

Instructions for running the tests, adding new tests etc. are provided in the README file for the repository.

# The IOCs
The IOCs need to have their st.cmd or st-common.cmd editing to enable them to work with the testing framework.
Here is an example st-common.cmd from the AMINT2L:

```
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(AMINT2L)/data"

##ISIS## Run IOC initialisation 
< $(IOCSTARTUP)/init.cmd

# For dev sim devices
$(IFDEVSIM) drvAsynIPPortConfigure("L0", "localhost:$(EMULATOR_PORT=)")

## For real device use:
$(IFNOTDEVSIM) $(IFNOTRECSIM) drvAsynSerialPortConfigure("L0", "$(PORT=NO_PORT_MACRO)", 0, 0, 0, 0)
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "baud", "$(BAUD=9600)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "bits", "$(BITS=8)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "parity", "$(PARITY=none)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "stop", "$(STOP=1)")

##ISIS## Load common DB records 
< $(IOCSTARTUP)/dbload.cmd

############################
## Load our record instances
############################

dbLoadRecords("$(AMINT2L)/db/amint2l.db","P=$(MYPVPREFIX)$(IOCNAME):, PORT=L0, RECSIM=$(RECSIM=0), DISABLE=$(DISABLE=0), ADDR=$(ADDR)")

##ISIS## Stuff that needs to be done after all records are loaded but before iocInit is called 
< $(IOCSTARTUP)/preiocinit.cmd

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=hgv27692Host"

##ISIS## Stuff that needs to be done after iocInit is called e.g. sequence programs 
< $(IOCSTARTUP)/postiocinit.cmd
```

The IOC testing framework will set the EMULATOR_PORT; it will also set the macros `IFTESTDEVSIM` and `IFNOTTESTDEVSIM` (as of beam stop merge). The code for this is in `EPICS\iocstartup\ioctesting.cmd`. This file sets these macros and also loads the file $(ICPVARDIR)/tmp/test_config.txt which the testing frame work will add extra macros to.

# Notes for update

Run epics terminal `cd support\IocTestFramework\master`:

```
python run_tests.py -pf %MYPVPREFIX%  -d amint2l -p C:\Instrument\Apps\EPICS\ioc\master\AMINT2L\iocBoot\iocAMINT2L-IOC-01 -e C:\Instrument\Apps\Python\Scripts\lewis.exe -pf %MYPVPREFIX% -ea C:\Instrument\Apps\EPICS\support\DeviceEmulator\master -ek lewis_emulators -ic
```


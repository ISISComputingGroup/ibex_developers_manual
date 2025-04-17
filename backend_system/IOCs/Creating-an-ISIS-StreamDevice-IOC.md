> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Creating an ISIS StreamDevice IOC

## Before you begin

Is the a support module already available? Check https://epics.anl.gov/modules/manufacturer.php. If it's not listed there, email tech talk https://epics.anl.gov/tech-talk/.

## First step

The easiest way to create a StreamDevice is to use the script [here](https://github.com/ISISComputingGroup/IBEX_device_generator) but if for some reason you want to create it manually the instructions are as follows:

> [!WARNING]
> The IOC creating script is improving but still under testing. Git operations should be happening correctly.
> Tickets related to the issues:
> - https://github.com/ISISComputingGroup/IBEX/issues/3431
> - https://github.com/ISISComputingGroup/IBEX/issues/3588
> - https://github.com/ISISComputingGroup/IBEX/issues/4659
> - https://github.com/ISISComputingGroup/IBEX/issues/8249

## Create a StreamDevice support module

Note: The support module is put in the `EPICS\support` directory, but the actual IOC(s) are put in the `EPICS\ioc\master` directory

First, set up the Support Module (Using the Hameg 8123 as an example.):

Make the main directory:

```
cd ...EPICS\support
mkdir Hameg_8123
cd Hameg_8123
```

Get an admin to [create a git repository](Adding-new-modules-via-Git).

Create a stream support module:

```
cd ...EPICS\support\Hameg_8123\master
makeSupport.pl -t streamSCPI Hameg_8123
```

Edit the protocol file in `Hameg_8123Sup`, so it reads like:

```
Terminator = '\r\n';
ReplyTimeout = 2000;

getIDN {
    out "*IDN?";
    #Read no more than 39 chars (EPICS limit)
    in "%/(.{0,39})/";
    ExtraInput = Ignore;
}

getTriggerLevel {
    out "LV\$1?";
    in "%s";
    ExtraInput = Ignore;
}

setTriggerLevel {
    out "LV\$1%s?";
}

resetCounts {
    out "RES";
}
```


Note: I have only included a very small section of the command set for this device for brevity.



Now add the directory name to the support make file (`C:\Instrument\Apps\EPICS\support\Makefile`), ie to DIRS at the top. Also add dependencies if needed.

Next the db file needs to created. The db file should now be stored with the proto file in `hameg8123Sup` to aid portability. For the Hameg the part of the db file looks like this:
```
record(ai, "$(P)CHAN_A:TRIG_LVL")
{
    field(SCAN, "1 second")
    field(DTYP, "stream")
    field(INP,  "@Hameg_8123.proto getTriggerLevel(A) $(PORT)")
    field(PREC, "3")
    field(EGU,  "V")
}

record(ao, "$(P)CHAN_A:TRIG_LVL:SP")
{
    field(DTYP, "stream")
    field(OUT,  "@Hameg_8123.proto setTriggerLevel(A) $(PORT)")
    field(PREC, "3")
    field(EGU, "V")
}
```

`Hameg_8123.proto` is the name of the protocol file for the Hameg created here.

Note that the db file should conform to the naming standards detailed in [PV-Naming](PV-Naming), and that ANY value which might be read and set as a block must have a `:SP` as well as a non post-fixed name entry.

Also note that ALL streamdevice PVs must have the field `DTYP` set to `"stream"`, otherwise they will not correctly communicate.


Modify the Makefile in the same directory as the protocol and db files to have lines like:

```
DB += <db_file_name>.db
DATA += <protocol_file_name>
```

If the Makefile has a line that reads `DATA += $(patsubst ../%, %, $(wildcard ../*.proto))`, delete it.


## Creating the IOC

All IOCs used at ISIS reside in the `EPICS\ioc\master` directory.

For this example we are using the Hameg 8123.

Please take note of the [IOC naming conventions](IOC-Naming). The same name (with the same casing) should be used both for the top-level IOC directory under `EPICS\ioc\master` and in the `makeBaseApp` command, as in the example below.

First create the necessary directory structure and IOC boilerplate, starting from the `EPICS\ioc` directory (we're going to create at least two IOCs):
```
mkdir HAMEG8123
cd HAMEG8123
makeBaseApp.pl -t ioc HAMEG8123-IOC-01
makeBaseApp.pl -t ioc HAMEG8123-IOC-02
makeBaseApp.pl -i -t ioc HAMEG8123-IOC-01
<Press return>
makeBaseApp.pl -i -t ioc HAMEG8123-IOC-02
<Press return>
```

The next step is to adjust the Makefile in `HAMEG8123-IOC-02App\src:`
```
cd HAMEG8123-IOC-02App\src
del build.mak
notepad Makefile
```

In notepad, adjust the Makefile as outlined in the in-line comments, namely change the line:
`include $(TOP)/HAMEG8123-IOC-02App/src/build.mak` to `include $(TOP)/HAMEG8123-IOC-01App/src/build.mak`.
Don't forget to save it!

Now it is time to edit the `build.mak` file in `HAMEG8123-IOC-01App\src` - this is the master build file for all the HAMEG8123 IOCs. In notepad (or similar) add any require DBD files and LIBS to the respective listings. For example, for the Hameg it is necessary to add the DBDs for stream, asyn and the communication protocols:
```
...
## ISIS standard dbd ##
$(APPNAME)_DBD += devSequencer.dbd
$(APPNAME)_DBD += icpconfig.dbd
$(APPNAME)_DBD += pvdump.dbd
$(APPNAME)_DBD += asSupport.dbd
$(APPNAME)_DBD += devIocStats.dbd
$(APPNAME)_DBD += caPutLog.dbd
$(APPNAME)_DBD += utilities.dbd
## add other dbd here ##
$(APPNAME)_DBD += stream.dbd
$(APPNAME)_DBD += asyn.dbd
$(APPNAME)_DBD += drvAsynSerialPort.dbd
$(APPNAME)_DBD += drvAsynIPPort.dbd
...
```

Likewise, the LIBs need to be added too:
```
## ISIS standard libraries ##
$(APPNAME)_LIBS += seq pv
$(APPNAME)_LIBS += devIocStats
$(APPNAME)_LIBS += pvdump easySQLite sqlite
$(APPNAME)_LIBS += caPutLog
$(APPNAME)_LIBS += icpconfig
$(APPNAME)_LIBS += autosave
$(APPNAME)_LIBS += utilities
## Add other libraries here ##
$(APPNAME)_LIBS += stream
$(APPNAME)_LIBS += pcre
$(APPNAME)_LIBS += asyn
$(APPNAME)_LIBS += calc
```

The final step is to rationalise the st.cmd files for each IOC. There will be a default `st.cmd` for each IOC which will call a common file in the 01 directory. The top files for IOC-YY should look like the following (XXXX is the name of the IOC):

```
#!../../bin/windows-x64/XXXX-IOC-YY

## You may have to change XXXX to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/XXXX-IOC-YY.dbd"
XXXX_IOC_YY_registerRecordDeviceDriver pdbbase

## calling common command file in ioc 01 boot dir
< ${TOP}/iocBoot/iocXXXX-IOC-01/st-common.cmd

```

The a common file, `st-common.cmd` should look like (NOTE: the support files location is a macro defined in the `<IOC_DIR>\configure\RELEASE` file):

```
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(AMINT2L)/data"

##ISIS## Run IOC initialisation 
< $(IOCSTARTUP)/init.cmd

## For recsim:
$(IFRECSIM) drvAsynSerialPortConfigure("L0", "$(PORT=NUL)", 0, 1, 0, 0)

# For dev sim devices
$(IFDEVSIM) drvAsynIPPortConfigure("L0", "localhost:$(EMULATOR_PORT=57677)")

## For real device use:
$(IFNOTDEVSIM) $(IFNOTRECSIM) drvAsynSerialPortConfigure("L0", "$(PORT=NO_PORT_MACRO)", 0, 0, 0, 0)
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "baud", "$(BAUD=9600)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "bits", "$(BITS=7)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "parity", "$(PARITY=even)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "stop", "$(STOP=1)")
## Hardware flow control off
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", 0, "clocal", "Y")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"crtscts","N")
## Software flow control off
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"ixon","N")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"ixoff","N")

##ISIS## Load common DB records 
< $(IOCSTARTUP)/dbload.cmd

## Load our record instances
dbLoadRecords("[support_module_path]/db/devAMINT2L.db","P=$(MYPVPREFIX)$(IOCNAME):, PORT=L0, RECSIM=$(RECSIM=0), DISABLE=$(DISABLE=0)")

##ISIS## Stuff that needs to be done after all records are loaded but before iocInit is called 
< $(IOCSTARTUP)/preiocinit.cmd

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=hgv27692Host"

##ISIS## Stuff that needs to be done after iocInit is called e.g. sequence programs 
< $(IOCSTARTUP)/postiocinit.cmd

```

Now is a good time to add everything into Git. Once that is done it is time to build it and run it:

```
cd c:\Instrument\Apps\EPICS\ioc\master\HAMEG8123
make
cd iocBoot\iocHAMEG8123-IOC-01
runIOC.bat st.cmd
```

Hopefully, the IOC will start and the `dbl` command will list all the PVs.

Now it builds add a reference to the IOC make file in `C:\Instrument\Apps\EPICS\ioc\master\Makefile` add the directory name to `IOCDIRS`. If this gets to long split with `IOCDIR +=`

Before the IOC is complete you will need to finish all the [relevant workflow steps](IOCs#creating-an-ioc)

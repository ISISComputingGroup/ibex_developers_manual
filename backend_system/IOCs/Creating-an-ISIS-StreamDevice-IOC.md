> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Creating an ISIS StreamDevice IOC

## Create a StreamDevice support module

Note: The support module is put in the `EPICS\support` directory, but the actual IOC(s) are put in the `EPICS\ioc\master` directory

First, set up the Support Module (Using the Hameg 8123 as an example.):

Make the main directory:

```
cd ...EPICS\support
mkdir Hameg_8123
cd Hameg_8123
```

Get an admin to [create a git repository](Adding%20new%20modules).

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
    #Read no more that 39 chars (EPICS limit)
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

Delete the db file in `Hameg_8123Sup` and modify the Makefile so it not longer refers to it.

Modify the Makefile in the same directory as the protocol file to have a line like:

```
DATA += <protocol_file_name>
```

If the Makefile has a line that reads `DATA += $(patsubst ../%, %, $(wildcard ../*.proto))`, delete it.

Now add the directory name to the support make file (`C:\Instrument\Apps\EPICS\support\Makefile`), ie to DIRS at the top. Also add dependencies if needed.

### Helpful hints from previous developers

To create the support module, in an epics terminal.

```
C:\Instrument\Apps\EPICS\support\mercury_ict\master>makeSupport.pl -A ..\..\asyn
\master -B ..\..\..\base\master -t streamSCPI  mercury_ict
```

Add macro to group macros `C:\Instrument\Apps\EPICS\configure\MASTER_RELEASE`

You can also define macros in the file `globals.txt` at:

```
C:\Instrument\Settings\config\NDW1695\configurations\globals.txt
```

Each macro is separated on a new line and has the format `[IOC name]__[macro name]=[macro value]`. For example `LINKAM95_01__PORT=COM1`. Each time you add a new macro to this file, don't forget to recompile the IOC! (In general you need to recompile your IOC any time you make changes that affect the build files, e.g. the db files or Makefiles, but you don't need to recompile e.g. when changes affect only the protocol or st.cmd file)


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
$(APPNAME)_LIBS += seqDev seq pv
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
```

Next the db file needs to created. For the Hameg (and most devices) the db only need to be stored in `HAMEG8123-IOC-01App\Db`. For the Hameg the part of the db file looks like this:
```
record(ai, "$(P)CHAN_A:TRIG_LVL")
{
    field(SCAN, "1 second")
    field(DTYP, "stream")
    field(INP,  "@devHameg_8123.proto getTriggerLevel(A) $(PORT)")
    field(PREC, "3")
    field(EGU,  "V")
}

record(ao, "$(P)CHAN_A:TRIG_LVL:SP")
{
    field(DTYP, "stream")
    field(OUT,  "@devHameg_8123.proto setTriggerLevel(A) $(PORT)")
    field(PREC, "3")
    field(EGU, "V")
}
```

`devHameg_8123.proto` is the name of the protocol file for the Hameg created here.

The newly created db file needs to be added to the `Makefile` file in `HAMEG8123-IOC-01App\Db`:
```
#DB += xxx.db
DB += <db_file_name>.db
```

The final step is to rationalise the st.cmd files for each IOC. There will be a default `st.cmd` for each IOC beneath the `iocBoot` directory, but it will require information adding such as information about the db files, protocol files, hardware connection etc. The final Hameg `st.cmd` looks like this (the bits added have been highlighted) (NOTE: the macro `$(HAMEG8123)` is the same as defined in the `EPICS\configure\MASTER_RELEASE` file) :

```
#!../../bin/windows-x64-debug/HAMEG8123-IOC-01

## You may have to change HAMEG8123-IOC-01 to something else
## everywhere it appears in this file

# Increase this if you get <<TRUNCATED>> or discarded messages warnings in your errlog output
errlogInit2(65536, 256)

< envPaths

epicsEnvSet "STREAM_PROTOCOL_PATH" "$(HAMEG8123)/data"                          #Added
epicsEnvSet "TTY" "$(TTY=\\\\\\\\.\\\\COM19)"                                   #Added

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/HAMEG8123-IOC-01.dbd"
HAMEG8123_IOC_01_registerRecordDeviceDriver pdbbase

##ISIS## Run IOC initialisation
< $(IOCSTARTUP)/init.cmd

drvAsynSerialPortConfigure("L0", "$(TTY)", 0, 0, 0, 0)                          #Added
asynSetOption("L0", -1, "baud", "9600")                                         #Added
asynSetOption("L0", -1, "bits", "8")                                            #Added
asynSetOption("L0", -1, "parity", "none")                                       #Added
asynSetOption("L0", -1, "stop", "1")                                            #Added
asynOctetSetInputEos("L0", -1, "\r")                                            #Added
asynOctetSetOutputEos("L0", -1, "\r")                                           #Added

## Load record instances

##ISIS## Load common DB records
< $(IOCSTARTUP)/dbload.cmd

## Load our record instances
dbLoadRecords("db/devHameg_8123.db","P=$(MYPVPREFIX)$(IOCNAME):, PORT=L0")      #Added

##ISIS## Stuff that needs to be done after all records are loaded but before iocInit is called
< $(IOCSTARTUP)/preiocinit.cmd

cd ${TOP}/iocBoot/${IOC}
iocInit

## Start any sequence programs
#seq sncxxx,"user=Host"

##ISIS## Stuff that needs to be done after iocInit is called e.g. sequence programs
< $(IOCSTARTUP)/postiocinit.cmd
```

Now is a good time to add everything into Git. Once that is done it is time to build it and run it:

```
cd c:\Instrument\Apps\EPICS\ioc\HAMEG8123
make
cd iocBoot\iocHAMEG8123-IOC-01
runIOC.bat st.cmd
```

Hopefully, the IOC will start and the `dbl` command will list all the PVs.

Now it builds add a reference to the IOC make file in `C:\Instrument\Apps\EPICS\ioc\master\Makefile` add the directory name to `IOCDIRS`. If this gets to long split with `IOCDIR +=`

Before the IOC is complete you will need to finish the workflow to include:

1. PVs of note are designated as interesting [PVs, are archive and have units. All Macros are documented.](IOC-Finishing-Touches)
1. Record level simulation is provided (see [Record simulation](Record-Simulation))
1. The IOC has a disable record (see [Disable records](Disable-records))

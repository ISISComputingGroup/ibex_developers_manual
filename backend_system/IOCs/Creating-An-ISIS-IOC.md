Note: if you are creating a StreamDevice start [here](Creating-an-ISIS-StreamDevice-IOC).

All IOCs used at ISIS reside in the EPICS\\ioc directory.

For this example we are using the Hameg 8123.

First create the necessary directory structure and IOC boilerplate, starting from the EPICS\\ioc directory::

    mkdir HAMEG8123
    cd HAMEG8123
    makeBaseApp.pl -t ioc HAMEG8123-IOC-01
    makeBaseApp.pl -t ioc HAMEG8123-IOC-02
    makeBaseApp.pl -i -t ioc HAMEG8123-IOC-01
    <Press return>
    makeBaseApp.pl -i -t ioc HAMEG8123-IOC-02
    <Press return>

The next step is to adjust the Makefile in HAMEG8123-IOC-02App\\src::

    cd HAMEG8123-IOC-02App\src
    del build.mak
    notepad Makefile

In notepad, adjust the Makefile as outlined in the in-line comments, namely change the line::

    include $(TOP)/HAMEG8123-IOC-02App/src/build.mak

to::

    include $(TOP)/HAMEG8123-IOC-01App/src/build.mak

Don't forgot to save it!

Now it is time to edit the build.mak file in HAMEG8123-IOC-01App\\src - this is the master build file for all the HAMEG8123 IOCs.
In notepad (or similar) add any require DBD files and LIBS to the respective listings. For example, for the Hameg it is necessary to add the DBDs for stream, asyn and the communication protocols::

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

Likewise, the LIBs need to be added too::

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

Now the configure\\RELEASE file need to be edited to include these extra support modules, for the Hameg the asyn, stream and PCRE modules need to be added::

    ## ISIS standard modules ##
    ICPCONFIG=$(SUPPORT)/icpconfig
    PVDUMP=$(SUPPORT)/pvdump
    DEVIOCSTATS=$(SUPPORT)/devIocStats/3-1-11
    AUTOSAVE=$(SUPPORT)/autosave/R5_0
    SNCSEQ=$(SUPPORT)/seq/2-1-11
    CAPUTLOG=$(SUPPORT)/caPutLog/3-3-3
    SQLITE=$(SUPPORT)/sqlite
    UTILITIES=$(SUPPORT)/utilities
    ZLIB=$(SUPPORT)/zlib/1-2-8

    ## add other modules here ##
    ASYN=$(SUPPORT)/asyn/4-22
    STREAMDEVICE=$(SUPPORT)/StreamDevice
    PCRE=$(SUPPORT)/pcre
    ONRPC=$(SUPPORT)/oncrpc/2

Next the db file needs to created. For the Hameg (and most devices) the db only need to be stored in HAMEG8123-IOC-01App\\Db. For the Hameg the part of the db file looks like this::

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

devHameg_8123.proto is the name of the protocol file for the Hameg created [here](Writing-An-ISIS-Stream-Device).

The final step is to rationalise the st.cmd files for each IOC. There will be a default st.cmd for each IOC beneath the iocBoot directory, but it will require information adding such as information about the db files, protocol files, hardware connection etc.
The final Hameg st.cmd looks like this (the bits added have been highlighted)::

    #!../../bin/windows-x64-debug/HAMEG8123-IOC-01

    ## You may have to change HAMEG8123-IOC-01 to something else
    ## everywhere it appears in this file

    # Increase this if you get <<TRUNCATED>> or discarded messages warnings in your errlog output
    errlogInit2(65536, 256)

    < envPaths

    epicsEnvSet "STREAM_PROTOCOL_PATH" "$(SUPPORT)/Hameg_8123/1-0/Hameg_8123Sup"    #Added
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
 

Now is a good time to add everything into SVN. Once that is done it is time to build it and run it::

    cd c:\Instrument\Apps\EPICS\ioc\HAMEG8123
    make
    cd iocBoot\iocHAMEG8123-IOC-01
    runIOC.bat st.cmd
    
Hopefully, the IOC will start and the 'dbl' command will list all the PVs.


Finally, before checking the this all into SVN, you will need to do the following:

* Mark any interesting PVs in the db file and make sure they have unit fields (EGU) and a description (DESC)

* Add [simulation records](Record-Simulation) and [disable records](Disable-records)
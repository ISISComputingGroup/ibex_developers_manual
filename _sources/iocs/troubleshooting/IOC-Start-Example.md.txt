# IOC Startup Example

The following gives an example of a normal start of SIMPLE IOC running in proc serve with the instrument running. The following splits out all the bits:

```
[2017-08-16 13:53:52] @@@ Restarting child "SIMPLE"
[2017-08-16 13:53:52] @@@    (as C:\windows\system32\cmd.exe)
[2017-08-16 13:53:52] @@@ The PID of new child "SIMPLE" is: 7280
[2017-08-16 13:53:52] @@@ @@@ @@@ @@@ @@@
```
header which shows what has started

```
[2017-08-16 13:53:54] #!../../bin/windows-x64/simple
[2017-08-16 13:53:54] ## You may have to change simple to something else
[2017-08-16 13:53:54] ## everywhere it appears in this file
[2017-08-16 13:53:54] < envPaths
```
start of st.cmd file

```
[2017-08-16 13:53:54] epicsEnvSet("IOC","iocsimple")
[2017-08-16 13:53:54] epicsEnvSet("TOP","C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master")
[2017-08-16 13:53:54] epicsEnvSet("ACCESSSECURITY","C:/Instrument/Apps/EPICS/support/AccessSecurity/master")
...<snip> ...
[2017-08-16 13:53:54] epicsEnvSet("IOCSTARTUP","C:/Instrument/Apps/EPICS/iocstartup")
[2017-08-16 13:53:54] epicsEnvSet("ICPBINARYDIR","C:/Instrument/Apps/EPICS/ICP_Binaries")
```

macros which are defined in `EPICS\configure\MASTER_RELEASE` and point to support modules that may be used by the IOC

```
[2017-08-16 13:53:54] cd C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master
[2017-08-16 13:53:54] ## Register all support components
[2017-08-16 13:53:54] dbLoadDatabase "dbd/simple.dbd"
[2017-08-16 13:53:54] simple_registerRecordDeviceDriver pdbbase
[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/init.cmd
```
More st.cmd and then load initial init which sets up configuration info:

```
[2017-08-16 13:53:54] icpconfigLoad
[2017-08-16 13:53:54] icpconfigLoad: ioc "SIMPLE" group "SIMPLE" options 0x0 host "NDW1798"
[2017-08-16 13:53:54] icpconfigLoad: config base (ICPCONFIGBASE) is "C:/Instrument/Settings/config"
[2017-08-16 13:53:54] icpconfigLoad: config root (ICPCONFIGROOT) is "C:/Instrument/Settings/config/NDW1798/configurations"
[2017-08-16 13:53:54] icpconfigLoad: * $(SIMULATE)="0" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFSIM)="#" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTSIM)=" " ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(SIMSFX)="" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(DISABLE)="0" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFDISABLE)="#" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTDISABLE)=" " ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(DEVSIM)="0" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFDEVSIM)="#" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTDEVSIM)=" " ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(RECSIM)="0" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFRECSIM)="#" ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTRECSIM)=" " ({initial default})
[2017-08-16 13:53:54] icpconfigLoad: * $(ICPCONFIGDIR)="C:/Instrument/Settings/config/NDW1798/configurations/configurations/Instron" ({initial default})
```
defaults
```
[2017-08-16 13:53:54] icpconfigLoad: last configuration was "Instron" (C:/Instrument/Settings/config/NDW1798/configurations/configurations/Instron)
[2017-08-16 13:53:54] icpconfigLoad: configuration "Instron"
[2017-08-16 13:53:54] icpconfigLoad: loading 0 component(s) for "/configurations/Instron"
[2017-08-16 13:53:54] icpconfigLoad: Loading default macros for "/configurations/Instron"
[2017-08-16 13:53:54] icpconfigLoad: Loading IOC sim level "/configurations/Instron"
[2017-08-16 13:53:54] icpconfigLoad: Loading IOC macros for "/configurations/Instron"
[2017-08-16 13:53:54] icpconfigLoad: Loading IOC PVs for "/configurations/Instron"
[2017-08-16 13:53:54] icpconfigLoad: Loading IOC PV sets for "/configurations/Instron"
[2017-08-16 13:53:54] Cannot open directory: C:/Instrument/Settings/config/NDW1798/configurations/configurations/Instron/files
[2017-08-16 13:53:54] icpconfigLoad: Found 0 files for "/configurations/Instron"
```
Last configuration loaded
```
[2017-08-16 13:53:54] icpconfigLoad: loading old macro file "C:/Instrument/Settings/config/NDW1798/configurations/globals.txt"
[2017-08-16 13:53:54] icpconfigLoad: * $(GALILNUMCRATES)="1" 
```
`globals.txt` macros.

```
[2017-08-16 13:53:54] # define a macro with the same name as the IOC name and a blank value. This means we can use a line like
[2017-08-16 13:53:54] #  $(IFIOC_GALIL_01=#) to have something that is only executed in GALIL_01 IOC

[2017-08-16 13:53:54] # and you can pass to db file via A=1,$(IFIOC)= ,A=2

[2017-08-16 13:53:54] # used when loading motorUtils and motors moving

[2017-08-16 13:53:54] epicsEnvSet("IFIOC", "IFIOC_SIMPLE")

[2017-08-16 13:53:54] epicsEnvSet("IFIOC_SIMPLE", " ")

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/asyn.cmd

[2017-08-16 13:53:54] ## defaults for asyn drivers

[2017-08-16 13:53:54] ## Global default is to trace only errors

[2017-08-16 13:53:54] ## 0=none,0x1=err,0x2=IO_device,0x4=IO_filter,0x8=IO_driver,0x10=flow,0x20=warning

[2017-08-16 13:53:54] asynSetTraceMask("", -1, 0x1)

[2017-08-16 13:53:54] asyn.cmd line 5: Command asynSetTraceMask not found.

[2017-08-16 13:53:54] ## Global default to send trace output to errlog (missing 3rd arg passes NULL as that parameter)

[2017-08-16 13:53:54] asynSetTraceFile("", -1)

[2017-08-16 13:53:54] asyn.cmd line 8: Command asynSetTraceFile not found.

[2017-08-16 13:53:54] ## Global default is to print escaped ascii for any IO_* trace specified above

[2017-08-16 13:53:54] ## 0=none,1=ascii,2=esc,4=hex

[2017-08-16 13:53:54] asynSetTraceIOMask("", -1, 0x2)

[2017-08-16 13:53:54] asyn.cmd line 12: Command asynSetTraceIOMask not found.
```
async defaults

```
[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/ioctesting.cmd

[2017-08-16 13:53:54] # If in test dev sim mode set up values

[2017-08-16 13:53:54] epicsEnvSet TESTDEVSIM "#"

[2017-08-16 13:53:54] # epicsEnvSet "DEVSIM" "1"

[2017-08-16 13:53:54] # epicsEnvSet "RECSIM" "0"

[2017-08-16 13:53:54] # stringiftest("DEVSIM", "yes", 2)

[2017-08-16 13:53:54] # stringiftest("RECSIM", "", 2)

[2017-08-16 13:53:54] # < C:/Instrument/Var/tmp/test_config.txt

[2017-08-16 13:53:54] # If in test rec sim mode

[2017-08-16 13:53:54] epicsEnvSet TESTRECSIM "#"

[2017-08-16 13:53:54] # epicsEnvSet "DEVSIM" "0"

[2017-08-16 13:53:54] # epicsEnvSet "RECSIM" "1"

[2017-08-16 13:53:54] # stringiftest("DEVSIM", "", 2)

[2017-08-16 13:53:54] # stringiftest("RECSIM", "yes", 2)

[2017-08-16 13:53:54] # < C:/Instrument/Var/tmp/test_config.txt

[2017-08-16 13:53:54] ## Create the emulator port macro and set it to either the one given or a spare port:

[2017-08-16 13:53:54] # freeIPPort(SPARE_PORT)

[2017-08-16 13:53:54] # epicsEnvSet "EMULATOR_PORT" 

[2017-08-16 13:53:54] # epicsEnvShow("EMULATOR_PORT") 
```
Set up macros for ioc test framework (including loading macros from the temp file if needed)

```
[2017-08-16 13:53:54] ## Load record instances

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/dbload.cmd

[2017-08-16 13:53:54] #dbLoadRecords("$(TIMESTAMPRECORD)/db/timestamp.db","P=$(MYPVPREFIX)$(IOCNAME):")

[2017-08-16 13:53:54] dbLoadRecords("C:/Instrument/Apps/EPICS/support/devIocStats/master/db/iocAdminSoft.db","IOC=TE:NDW1798:CS:IOC:SIMPLE:DEVIOS")

[2017-08-16 13:53:54] #dbLoadRecords("$(ASUBFUNCTIONS)/db/iocExit.db","P=$(MYPVPREFIX),Q=CS:IOC:$(IOCNAME):,IOCNAME=$(IOCNAME)")

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/autosave.cmd

[2017-08-16 13:53:54] ## start autosave.cmd

[2017-08-16 13:53:54] save_restoreSet_Debug(0)

[2017-08-16 13:53:54] # status-PV prefix, so save_restore can find its status PV's.

[2017-08-16 13:53:54] #epicsEnvSet("ASPREFIX","$(MYPVPREFIX)CS:IOC:$(IOCNAME):AS:")

[2017-08-16 13:53:54] epicsEnvSet("ASPREFIX","TE:NDW1798:AS:SIMPLE:")

[2017-08-16 13:53:54] save_restoreSet_status_prefix("TE:NDW1798:AS:SIMPLE:")

[2017-08-16 13:53:54] # Ok to save/restore save sets with missing values (no CA connection to PV)?  

[2017-08-16 13:53:54] save_restoreSet_IncompleteSetsOk(1)

[2017-08-16 13:53:54] # Save dated backup files?

[2017-08-16 13:53:54] save_restoreSet_DatedBackupFiles(1)

[2017-08-16 13:53:54] # Number of sequenced backup files to write

[2017-08-16 13:53:54] save_restoreSet_NumSeqFiles(1)

[2017-08-16 13:53:54] # Time interval between sequenced backups

[2017-08-16 13:53:54] save_restoreSet_SeqPeriodInSeconds(300)

[2017-08-16 13:53:54] # specify where save files should be - use a different directory if in simulation mode

[2017-08-16 13:53:54] mkdir("C:/Instrument/Var/autosave/SIMPLE") 

[2017-08-16 13:53:54] set_savefile_path("C:/Instrument/Var/autosave", "SIMPLE")

[2017-08-16 13:53:54] ## specify what save files should be restored.  Note these files must be

[2017-08-16 13:53:54] ## in the directory specified in set_savefile_path(), or, if that function

[2017-08-16 13:53:54] ## has not been called, from the directory current when iocInit is invoked

[2017-08-16 13:53:54] ## example: set_pass0_restoreFile("autosave_geiger.sav")

[2017-08-16 13:53:54] ## restore positions at pass 0 so not passed to hardware

[2017-08-16 13:53:54] ##

[2017-08-16 13:53:54] ## Use     epicsEnvSet("AUTOSAVEREQ","#")   if you do not have any req files to load

[2017-08-16 13:53:54]  set_pass0_restoreFile("SIMPLE_positions.sav")

[2017-08-16 13:53:54]  set_pass0_restoreFile("SIMPLE_settings.sav")

[2017-08-16 13:53:54] # restore settings at pass 1 so passed to hardware

[2017-08-16 13:53:54]  set_pass1_restoreFile("SIMPLE_settings.sav")

[2017-08-16 13:53:54] # these values are obtained from info fields in DB files via makeAutosaveFiles() / makeAutosaveFileFromDbInfo()

[2017-08-16 13:53:54] set_pass0_restoreFile("SIMPLE_info_positions.sav")

[2017-08-16 13:53:54] set_pass0_restoreFile("SIMPLE_info_settings.sav")

[2017-08-16 13:53:54] set_pass1_restoreFile("SIMPLE_info_settings.sav")

[2017-08-16 13:53:54] #save_restoreSet_CAReconnect(1)

[2017-08-16 13:53:54] # specify directories in which to to search for included request files

[2017-08-16 13:53:54] set_requestfile_path("C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master/iocBoot/iocsimple", "")

[2017-08-16 13:53:54] # Autosave status PVs - P must be same as used in save_restoreSet_status_prefix() above

[2017-08-16 13:53:54] dbLoadRecords("C:/Instrument/Apps/EPICS/support/autosave/master/asApp/Db/save_restoreStatus.db", "P=TE:NDW1798:AS:SIMPLE:")

[2017-08-16 13:53:54] ## end autosave.cmd
```
setup autosave.

```
[2017-08-16 13:53:54] dbLoadRecords("db/simple.db","P=TE:NDW1798:SIMPLE:")
```
IOC db load of records

```
[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/preiocinit.cmd

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] # write process variable and IOC startup information to database 

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] pvdump

[2017-08-16 13:53:54] pvdump: ioc name is "SIMPLE" pid 11856

[2017-08-16 13:53:54] pvdump: MySQL write of 129 PVs with 33 info entries, plus 307 macros took 0.092 seconds

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] # set up IOC access security

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] asSetFilename("C:/Instrument/Apps/EPICS/support/AccessSecurity/master/default.acf")

[2017-08-16 13:53:54] asSetSubstitutions("P=TE:NDW1798:,ACF_IH1=localhost,ACF_IH2=localhost,ACF_IH3=localhost,ACF_IH4=localhost")

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] # log to server address EPICS_IOC_LOG_INET listening on port EPICS_IOC_LOG_PORT 

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] epicsEnvSet("EPICS_IOC_LOG_INET", "localhost")

[2017-08-16 13:53:54] iocLogInit()

[2017-08-16 13:53:54] log client: connected to log server at "127.0.0.1:7004"

[2017-08-16 13:53:54] cd C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master/iocBoot/iocsimple

[2017-08-16 13:53:54] iocInit

[2017-08-16 13:53:54] sevr=info Starting iocInit

[2017-08-16 13:53:54] ############################################################################

[2017-08-16 13:53:54] ## EPICS R3.15.5

[2017-08-16 13:53:54] ## EPICS Base built Jul 10 2017

[2017-08-16 13:53:54] ############################################################################

[2017-08-16 13:53:54] sevr=info reboot_restore: entry for file 'SIMPLE_positions.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_positions.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.savB'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.savB'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't figure out which seq file is most recent,

[2017-08-16 13:53:54] sevr=info save_restore: so I'm just going to start with 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't find a file to restore from...sevr=info save_restore: ...last tried 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'. I give up.

[2017-08-16 13:53:54] save_restore: **********************************

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info save_restore: Can't open save file.sevr=info reboot_restore: entry for file 'SIMPLE_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't figure out which seq file is most recent,

[2017-08-16 13:53:54] sevr=info save_restore: so I'm just going to start with 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't find a file to restore from...sevr=info save_restore: ...last tried 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'. I give up.

[2017-08-16 13:53:54] save_restore: **********************************

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info save_restore: Can't open save file.sevr=info reboot_restore: entry for file 'SIMPLE_info_positions.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_info_positions.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_info_positions.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info reboot_restore: done with file 'SIMPLE_info_positions.sav'

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info reboot_restore: entry for file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_info_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_info_settings.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info reboot_restore: done with file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info reboot_restore: entry for file 'SIMPLE_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav' at initHookState 7 (after record/device init) ***

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't figure out which seq file is most recent,

[2017-08-16 13:53:54] sevr=info save_restore: so I'm just going to start with 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't find a file to restore from...sevr=info save_restore: ...last tried 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'. I give up.

[2017-08-16 13:53:54] save_restore: **********************************

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info save_restore: Can't open save file.sevr=info reboot_restore: entry for file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_info_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_info_settings.sav' at initHookState 7 (after record/device init) ***

[2017-08-16 13:53:54] sevr=info reboot_restore: done with file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] icpconfigLoad: setPVValuesStatic setting 0 pvs (pre iocInit)

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:55] cas warning: Configured TCP port was unavailable.

[2017-08-16 13:53:55] cas warning: Using dynamically assigned TCP port 60745,

[2017-08-16 13:53:55] cas warning: but now two or more servers share the same UDP port.

[2017-08-16 13:53:55] cas warning: Depending on your IP kernel this server may not be

[2017-08-16 13:53:55] cas warning: reachable with UDP unicast (a host's IP in EPICS_CA_ADDR_LIST)

[2017-08-16 13:53:55] sevr=info iocRun: All initialization complete

[2017-08-16 13:53:55] icpconfigLoad: setPVValues setting 0 pvs (post iocInit)

[2017-08-16 13:53:55] < C:/Instrument/Apps/EPICS/iocstartup/postiocinit.cmd

[2017-08-16 13:53:55] # enable caPutLog to logger on localhost

[2017-08-16 13:53:55] # pass 0 to log value changes, pass 1 to log all puts, 2 logs all puts with no filtering on same PV

[2017-08-16 13:53:55] caPutLogInit "localhost" "1"

[2017-08-16 13:53:55] log client: connected to log server at "127.0.0.1:7011"

[2017-08-16 13:53:55] sevr=info caPutLog: successfully initialized

[2017-08-16 13:53:55] # Handle autosave 'commands' contained in loaded databases.

[2017-08-16 13:53:55] # file naming needs to agree with autosave.cmd

[2017-08-16 13:53:55] makeAutosaveFileFromDbInfo("SIMPLE_info_settings","autosaveFields")

[2017-08-16 13:53:55] makeAutosaveFileFromDbInfo("SIMPLE_info_positions","autosaveFields_pass0")

[2017-08-16 13:53:55] create_monitor_set("SIMPLE_info_positions.req", 5, "")

[2017-08-16 13:53:55] create_monitor_set("SIMPLE_info_settings.req", 30, "")

[2017-08-16 13:53:55] sevr=info SIMPLE_info_positions.sav: 63 of 63 PV's connected

[2017-08-16 13:53:55] sevr=info 

[2017-08-16 13:53:56] sevr=info SIMPLE_info_settings.sav: 1 of 1 PV's connected

[2017-08-16 13:53:56] sevr=info 
```

Initialise and run

# Full Log
```
[2017-08-16 13:53:52] @@@ Restarting child "SIMPLE"
[2017-08-16 13:53:52] @@@    (as C:\windows\system32\cmd.exe)
[2017-08-16 13:53:52] @@@ The PID of new child "SIMPLE" is: 7280
[2017-08-16 13:53:52] @@@ @@@ @@@ @@@ @@@
[2017-08-16 13:53:54] #!../../bin/windows-x64/simple

[2017-08-16 13:53:54] ## You may have to change simple to something else

[2017-08-16 13:53:54] ## everywhere it appears in this file

[2017-08-16 13:53:54] < envPaths

[2017-08-16 13:53:54] epicsEnvSet("IOC","iocsimple")

[2017-08-16 13:53:54] epicsEnvSet("TOP","C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master")

[2017-08-16 13:53:54] epicsEnvSet("ACCESSSECURITY","C:/Instrument/Apps/EPICS/support/AccessSecurity/master")

[2017-08-16 13:53:54] epicsEnvSet("AGILENT33220A","C:/Instrument/Apps/EPICS/support/agilent33220A/master")

[2017-08-16 13:53:54] epicsEnvSet("AGILENT3631A","C:/Instrument/Apps/EPICS/support/agilent3631A/master")

[2017-08-16 13:53:54] epicsEnvSet("AMINT2L","C:/Instrument/Apps/EPICS/support/amint2l/master")

[2017-08-16 13:53:54] epicsEnvSet("AREA_DETECTOR","C:/Instrument/Apps/EPICS/support/areaDetector/master")

[2017-08-16 13:53:54] epicsEnvSet("ASUBFUNCTIONS","C:/Instrument/Apps/EPICS/support/asubFunctions/master")

[2017-08-16 13:53:54] epicsEnvSet("ASYN","C:/Instrument/Apps/EPICS/support/asyn/master")

[2017-08-16 13:53:54] epicsEnvSet("AUTOSAVE","C:/Instrument/Apps/EPICS/support/autosave/master")

[2017-08-16 13:53:54] epicsEnvSet("AXIS","C:/Instrument/Apps/EPICS/support/axis/master")

[2017-08-16 13:53:54] epicsEnvSet("BARNDOORS","C:/Instrument/Apps/EPICS/support/barndoors/master")

[2017-08-16 13:53:54] epicsEnvSet("BOOST","C:/Instrument/Apps/EPICS/libraries/master/boost")

[2017-08-16 13:53:54] epicsEnvSet("BUSY","C:/Instrument/Apps/EPICS/support/busy/master")

[2017-08-16 13:53:54] epicsEnvSet("CALC","C:/Instrument/Apps/EPICS/support/calc/master")

[2017-08-16 13:53:54] epicsEnvSet("CAPUTLOG","C:/Instrument/Apps/EPICS/support/caPutLog/master")

[2017-08-16 13:53:54] epicsEnvSet("CCD100","C:/Instrument/Apps/EPICS/support/CCD100/master")

[2017-08-16 13:53:54] epicsEnvSet("COMMON","C:/Instrument/Apps/EPICS/ISIS/Common/master")

[2017-08-16 13:53:54] epicsEnvSet("CRYVALVE","C:/Instrument/Apps/EPICS/support/cryValve/master")

[2017-08-16 13:53:54] epicsEnvSet("CSM","C:/Instrument/Apps/EPICS/support/csm/master")

[2017-08-16 13:53:54] epicsEnvSet("CURL","C:/Instrument/Apps/EPICS/support/curl/master")

[2017-08-16 13:53:54] epicsEnvSet("DANFYSIK8000","C:/Instrument/Apps/EPICS/support/danfysikMps8000")

[2017-08-16 13:53:54] epicsEnvSet("DAQMXBASE","C:/Instrument/Apps/EPICS/support/DAQmxBase/master")

[2017-08-16 13:53:54] epicsEnvSet("DEVIOCSTATS","C:/Instrument/Apps/EPICS/support/devIocStats/master")

[2017-08-16 13:53:54] epicsEnvSet("ECLAB","C:/Instrument/Apps/EPICS/support/ECLab/master")

[2017-08-16 13:53:54] epicsEnvSet("EEMCU","C:/Instrument/Apps/EPICS/support/MCAG_Base_Project/master/epics/epicsIOC")

[2017-08-16 13:53:54] epicsEnvSet("EFSW","C:/Instrument/Apps/EPICS/support/efsw/master")

[2017-08-16 13:53:54] epicsEnvSet("EUROTHERM2K","C:/Instrument/Apps/EPICS/support/eurotherm2k/master")

[2017-08-16 13:53:54] epicsEnvSet("FILELIST","C:/Instrument/Apps/EPICS/support/FileList/master")

[2017-08-16 13:53:54] epicsEnvSet("FILESERVER","C:/Instrument/Apps/EPICS/support/FileServer/master")

[2017-08-16 13:53:54] epicsEnvSet("FINS","C:/Instrument/Apps/EPICS/support/FINS/master")

[2017-08-16 13:53:54] epicsEnvSet("FLATBUFFERS","C:/Instrument/Apps/EPICS/support/flatbuffers/master")

[2017-08-16 13:53:54] epicsEnvSet("GALIL","C:/Instrument/Apps/EPICS/support/galil/master")

[2017-08-16 13:53:54] epicsEnvSet("HAMEG8123","C:/Instrument/Apps/EPICS/ISIS/Hameg_8123/master")

[2017-08-16 13:53:54] epicsEnvSet("HIDEWINDOW","C:/Instrument/Apps/EPICS/support/HideWindow/master")

[2017-08-16 13:53:54] epicsEnvSet("HTMLTIDY","C:/Instrument/Apps/EPICS/support/htmltidy/master")

[2017-08-16 13:53:54] epicsEnvSet("HVCAEN","C:/Instrument/Apps/EPICS/support/HVCAENx527/master")

[2017-08-16 13:53:54] epicsEnvSet("ICPCONFIG","C:/Instrument/Apps/EPICS/support/icpconfig/master")

[2017-08-16 13:53:54] epicsEnvSet("INSTRON","C:/Instrument/Apps/EPICS/support/instron/master")

[2017-08-16 13:53:54] epicsEnvSet("IP","C:/Instrument/Apps/EPICS/support/ip/master")

[2017-08-16 13:53:54] epicsEnvSet("IPAC","C:/Instrument/Apps/EPICS/support/ipac/master")

[2017-08-16 13:53:54] epicsEnvSet("ISISDAE","C:/Instrument/Apps/EPICS/support/isisdae/master")

[2017-08-16 13:53:54] epicsEnvSet("JAWS","C:/Instrument/Apps/EPICS/support/jaws/master")

[2017-08-16 13:53:54] epicsEnvSet("JULABO","C:/Instrument/Apps/EPICS/support/julabo/master")

[2017-08-16 13:53:54] epicsEnvSet("KHLY2400","C:/Instrument/Apps/EPICS/support/Keithley_2400/master")

[2017-08-16 13:53:54] epicsEnvSet("KEPCO","C:/Instrument/Apps/EPICS/support/kepco/master")

[2017-08-16 13:53:54] epicsEnvSet("LKSH336","C:/Instrument/Apps/EPICS/support/lakeshore/master/lakeshore336")

[2017-08-16 13:53:54] epicsEnvSet("LIBICONV","C:/Instrument/Apps/EPICS/support/libiconv/master")

[2017-08-16 13:53:54] epicsEnvSet("LIBJSON","C:/Instrument/Apps/EPICS/support/libjson/master")

[2017-08-16 13:53:54] epicsEnvSet("LIBRDKAFKA","C:/Instrument/Apps/EPICS/support/librdkafka/master")

[2017-08-16 13:53:54] epicsEnvSet("LIBXML2","C:/Instrument/Apps/EPICS/support/libxml2/master")

[2017-08-16 13:53:54] epicsEnvSet("LIBXSLT","C:/Instrument/Apps/EPICS/support/libxslt/master")

[2017-08-16 13:53:54] epicsEnvSet("LINKAM95","C:/Instrument/Apps/EPICS/support/linkam95/master")

[2017-08-16 13:53:54] epicsEnvSet("LVDCOM","C:/Instrument/Apps/EPICS/ISIS/lvDCOM/master")

[2017-08-16 13:53:54] epicsEnvSet("MCA","C:/Instrument/Apps/EPICS/support/mca/master")

[2017-08-16 13:53:54] epicsEnvSet("MAGNET3D","C:/Instrument/Apps/EPICS/ISIS/magnet3D/master")

[2017-08-16 13:53:54] epicsEnvSet("MERCURY_ITC","C:/Instrument/Apps/EPICS/ISIS/MercuryiTC/master")

[2017-08-16 13:53:54] epicsEnvSet("MK2CHOPR","C:/Instrument/Apps/EPICS/support/mk2chopper/master")

[2017-08-16 13:53:54] epicsEnvSet("MODBUS","C:/Instrument/Apps/EPICS/support/modbus/master")

[2017-08-16 13:53:54] epicsEnvSet("MOTIONSETPOINTS","C:/Instrument/Apps/EPICS/support/motionSetPoints/master")

[2017-08-16 13:53:54] epicsEnvSet("MOTOR","C:/Instrument/Apps/EPICS/support/motor/master")

[2017-08-16 13:53:54] epicsEnvSet("MYSQL","C:/Instrument/Apps/EPICS/support/MySQL/master")

[2017-08-16 13:53:54] epicsEnvSet("NEOCERA","C:/Instrument/Apps/EPICS/support/neocera/master")

[2017-08-16 13:53:54] epicsEnvSet("NETSHRVAR","C:/Instrument/Apps/EPICS/support/NetShrVar/master")

[2017-08-16 13:53:54] epicsEnvSet("NANODAC","C:/Instrument/Apps/EPICS/support/nanodac/master")

[2017-08-16 13:53:54] epicsEnvSet("NULLHTTPD","C:/Instrument/Apps/EPICS/support/nullhttpd/master")

[2017-08-16 13:53:54] epicsEnvSet("OPENSSL","C:/Instrument/Apps/EPICS/support/OpenSSL/master")

[2017-08-16 13:53:54] epicsEnvSet("OPTICS","C:/Instrument/Apps/EPICS/support/optics/master")

[2017-08-16 13:53:54] epicsEnvSet("PCRE","C:/Instrument/Apps/EPICS/support/pcre/master")

[2017-08-16 13:53:54] epicsEnvSet("PDR2000","C:/Instrument/Apps/EPICS/support/pdr2000/master")

[2017-08-16 13:53:54] epicsEnvSet("PIXELMAN","C:/Instrument/Apps/EPICS/support/pixelman/master")

[2017-08-16 13:53:54] epicsEnvSet("PROCSERVCONTROL","C:/Instrument/Apps/EPICS/support/procServControl/master")

[2017-08-16 13:53:54] epicsEnvSet("PUGIXML","C:/Instrument/Apps/EPICS/support/pugixml/master")

[2017-08-16 13:53:54] epicsEnvSet("PVCOMPLETE","C:/Instrument/Apps/EPICS/support/pvcomplete/master")

[2017-08-16 13:53:54] epicsEnvSet("PVDUMP","C:/Instrument/Apps/EPICS/support/pvdump/master")

[2017-08-16 13:53:54] epicsEnvSet("READASCII","C:/Instrument/Apps/EPICS/support/ReadASCII/master")

[2017-08-16 13:53:54] epicsEnvSet("ROTSC","C:/Instrument/Apps/EPICS/support/rotating_sample_changer/master")

[2017-08-16 13:53:54] epicsEnvSet("RUNCONTROL","C:/Instrument/Apps/EPICS/support/RunControl/master")

[2017-08-16 13:53:54] epicsEnvSet("RANDOM","C:/Instrument/Apps/EPICS/support/random/master")

[2017-08-16 13:53:54] epicsEnvSet("SAMPLECHANGER","C:/Instrument/Apps/EPICS/support/sampleChanger/master")

[2017-08-16 13:53:54] epicsEnvSet("SLACKING","C:/Instrument/Apps/EPICS/libraries/master/slacking")

[2017-08-16 13:53:54] epicsEnvSet("SNCSEQ","C:/Instrument/Apps/EPICS/support/seq/master")

[2017-08-16 13:53:54] epicsEnvSet("SKFCHOPPER","C:/Instrument/Apps/EPICS/support/SKFChopper/master")

[2017-08-16 13:53:54] epicsEnvSet("SPRLG","C:/Instrument/Apps/EPICS/support/superlogics/master")

[2017-08-16 13:53:54] epicsEnvSet("SQLITE","C:/Instrument/Apps/EPICS/support/sqlite/master")

[2017-08-16 13:53:54] epicsEnvSet("SSCAN","C:/Instrument/Apps/EPICS/support/sscan/master")

[2017-08-16 13:53:54] epicsEnvSet("STD","C:/Instrument/Apps/EPICS/support/std/master")

[2017-08-16 13:53:54] epicsEnvSet("STPS350","C:/Instrument/Apps/EPICS/ISIS/Stanford_PS350/master")

[2017-08-16 13:53:54] epicsEnvSet("STSR400","C:/Instrument/Apps/EPICS/ISIS/Stanford_SR400/master")

[2017-08-16 13:53:54] epicsEnvSet("STREAMDEVICE","C:/Instrument/Apps/EPICS/support/StreamDevice/master")

[2017-08-16 13:53:54] epicsEnvSet("TDKLAMBDAGENESYS","C:/Instrument/Apps/EPICS/support/TDKLambdaGenesys/master")

[2017-08-16 13:53:54] epicsEnvSet("TEKDMM40X0","C:/Instrument/Apps/EPICS/support/Tektronix_DMM_40X0/master")

[2017-08-16 13:53:54] epicsEnvSet("TEKAFG3XXX","C:/Instrument/Apps/EPICS/support/Tektronix_AFG3XXX/master")

[2017-08-16 13:53:54] epicsEnvSet("TEKMSO4104B","C:/Instrument/Apps/EPICS/support/Tektronix_MSO_4104B/master")

[2017-08-16 13:53:54] epicsEnvSet("TINYXML","C:/Instrument/Apps/EPICS/support/TinyXML/master")

[2017-08-16 13:53:54] epicsEnvSet("TPG300","C:/Instrument/Apps/EPICS/support/TPG/master")

[2017-08-16 13:53:54] epicsEnvSet("TPG","C:/Instrument/Apps/EPICS/support/TPG/master")

[2017-08-16 13:53:54] epicsEnvSet("TTIEX355P","C:/Instrument/Apps/EPICS/support/ttiEX355P/master")

[2017-08-16 13:53:54] epicsEnvSet("UTILITIES","C:/Instrument/Apps/EPICS/support/utilities/master")

[2017-08-16 13:53:54] epicsEnvSet("VISADRV","C:/Instrument/Apps/EPICS/support/VISAdrv/master")

[2017-08-16 13:53:54] epicsEnvSet("WEBGET","C:/Instrument/Apps/EPICS/support/webget/master")

[2017-08-16 13:53:54] epicsEnvSet("ZLIB","C:/Instrument/Apps/EPICS/support/zlib/master")

[2017-08-16 13:53:54] epicsEnvSet("EV4_BASE","C:/Instrument/Apps/EPICS/support/EPICS_V4/master")

[2017-08-16 13:53:54] epicsEnvSet("PVDATABASE","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/pvDatabaseCPP")

[2017-08-16 13:53:54] epicsEnvSet("PVASRV","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/pvaSrv")

[2017-08-16 13:53:54] epicsEnvSet("PVACLIENT","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/pvaClientCPP")

[2017-08-16 13:53:54] epicsEnvSet("PVACCESS","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/pvAccessCPP")

[2017-08-16 13:53:54] epicsEnvSet("NORMATIVETYPES","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/normativeTypesCPP")

[2017-08-16 13:53:54] epicsEnvSet("PVDATA","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/pvDataCPP")

[2017-08-16 13:53:54] epicsEnvSet("PVCOMMON","C:/Instrument/Apps/EPICS/support/EPICS_V4/master/pvCommonCPP")

[2017-08-16 13:53:54] epicsEnvSet("MK3CHOPPER","C:/Instrument/Apps/EPICS/support/mk3chopper/master")

[2017-08-16 13:53:54] epicsEnvSet("ONCRPC","C:/Instrument/Apps/EPICS/support/oncrpc/master")

[2017-08-16 13:53:54] epicsEnvSet("EPICS_BASE","C:/Instrument/Apps/EPICS/base/master")

[2017-08-16 13:53:54] epicsEnvSet("EPICS_ROOT","C:/Instrument/Apps/EPICS")

[2017-08-16 13:53:54] epicsEnvSet("SUPPORT","C:/Instrument/Apps/EPICS/support")

[2017-08-16 13:53:54] epicsEnvSet("ISISSUPPORT","C:/Instrument/Apps/EPICS/ISIS")

[2017-08-16 13:53:54] epicsEnvSet("IOCSTARTUP","C:/Instrument/Apps/EPICS/iocstartup")

[2017-08-16 13:53:54] epicsEnvSet("ICPBINARYDIR","C:/Instrument/Apps/EPICS/ICP_Binaries")

[2017-08-16 13:53:54] cd C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master

[2017-08-16 13:53:54] ## Register all support components

[2017-08-16 13:53:54] dbLoadDatabase "dbd/simple.dbd"

[2017-08-16 13:53:54] simple_registerRecordDeviceDriver pdbbase

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/init.cmd

[2017-08-16 13:53:54] icpconfigLoad

[2017-08-16 13:53:54] icpconfigLoad: ioc "SIMPLE" group "SIMPLE" options 0x0 host "NDW1798"

[2017-08-16 13:53:54] icpconfigLoad: config base (ICPCONFIGBASE) is "C:/Instrument/Settings/config"

[2017-08-16 13:53:54] icpconfigLoad: config root (ICPCONFIGROOT) is "C:/Instrument/Settings/config/NDW1798/configurations"

[2017-08-16 13:53:54] icpconfigLoad: * $(SIMULATE)="0" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFSIM)="#" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTSIM)=" " ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(SIMSFX)="" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(DISABLE)="0" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFDISABLE)="#" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTDISABLE)=" " ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(DEVSIM)="0" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFDEVSIM)="#" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTDEVSIM)=" " ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(RECSIM)="0" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFRECSIM)="#" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(IFNOTRECSIM)=" " ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: * $(ICPCONFIGDIR)="C:/Instrument/Settings/config/NDW1798/configurations/configurations/Instron" ({initial default})

[2017-08-16 13:53:54] icpconfigLoad: last configuration was "Instron" (C:/Instrument/Settings/config/NDW1798/configurations/configurations/Instron)

[2017-08-16 13:53:54] icpconfigLoad: configuration "Instron"

[2017-08-16 13:53:54] icpconfigLoad: loading 0 component(s) for "/configurations/Instron"

[2017-08-16 13:53:54] icpconfigLoad: Loading default macros for "/configurations/Instron"

[2017-08-16 13:53:54] icpconfigLoad: Loading IOC sim level "/configurations/Instron"

[2017-08-16 13:53:54] icpconfigLoad: Loading IOC macros for "/configurations/Instron"

[2017-08-16 13:53:54] icpconfigLoad: Loading IOC PVs for "/configurations/Instron"

[2017-08-16 13:53:54] icpconfigLoad: Loading IOC PV sets for "/configurations/Instron"

[2017-08-16 13:53:54] Cannot open directory: C:/Instrument/Settings/config/NDW1798/configurations/configurations/Instron/files

[2017-08-16 13:53:54] icpconfigLoad: Found 0 files for "/configurations/Instron"

[2017-08-16 13:53:54] icpconfigLoad: loading old macro file "C:/Instrument/Settings/config/NDW1798/configurations/globals.txt"

[2017-08-16 13:53:54] icpconfigLoad: * $(GALILNUMCRATES)="1" (C:/Instrument/Settings/config/NDW1798/configurations/globals.txt)

[2017-08-16 13:53:54] icpconfigLoad: * $(GALIL_01__GALILADDR01)="130.246.51.169" (C:/Instrument/Settings/config/NDW1798/configurations/globals.txt)

[2017-08-16 13:53:54] icpconfigLoad: * $(GALIL_02__GALILADDR02)="None" (C:/Instrument/Settings/config/NDW1798/configurations/globals.txt)

[2017-08-16 13:53:54] icpconfigLoad: * $(GALIL_03__GALILADDR03)="None" (C:/Instrument/Settings/config/NDW1798/configurations/globals.txt)

[2017-08-16 13:53:54] icpconfigLoad: loaded 4 macros from old macro file "C:/Instrument/Settings/config/NDW1798/configurations/globals.txt" (0 ioc, 0 group)

[2017-08-16 13:53:54] # define a macro with the same name as the IOC name and a blank value. This means we can use a line like

[2017-08-16 13:53:54] #  $(IFIOC_GALIL_01=#) to have something that is only executed in GALIL_01 IOC

[2017-08-16 13:53:54] # and you can pass to db file via A=1,$(IFIOC)= ,A=2

[2017-08-16 13:53:54] # used when loading motorUtils and motors moving

[2017-08-16 13:53:54] epicsEnvSet("IFIOC", "IFIOC_SIMPLE")

[2017-08-16 13:53:54] epicsEnvSet("IFIOC_SIMPLE", " ")

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/asyn.cmd

[2017-08-16 13:53:54] ## defaults for asyn drivers

[2017-08-16 13:53:54] ## Global default is to trace only errors

[2017-08-16 13:53:54] ## 0=none,0x1=err,0x2=IO_device,0x4=IO_filter,0x8=IO_driver,0x10=flow,0x20=warning

[2017-08-16 13:53:54] asynSetTraceMask("", -1, 0x1)

[2017-08-16 13:53:54] asyn.cmd line 5: Command asynSetTraceMask not found.

[2017-08-16 13:53:54] ## Global default to send trace output to errlog (missing 3rd arg passes NULL as that parameter)

[2017-08-16 13:53:54] asynSetTraceFile("", -1)

[2017-08-16 13:53:54] asyn.cmd line 8: Command asynSetTraceFile not found.

[2017-08-16 13:53:54] ## Global default is to print escaped ascii for any IO_* trace specified above

[2017-08-16 13:53:54] ## 0=none,1=ascii,2=esc,4=hex

[2017-08-16 13:53:54] asynSetTraceIOMask("", -1, 0x2)

[2017-08-16 13:53:54] asyn.cmd line 12: Command asynSetTraceIOMask not found.

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/ioctesting.cmd

[2017-08-16 13:53:54] # If in test dev sim mode set up values

[2017-08-16 13:53:54] epicsEnvSet TESTDEVSIM "#"

[2017-08-16 13:53:54] # epicsEnvSet "DEVSIM" "1"

[2017-08-16 13:53:54] # epicsEnvSet "RECSIM" "0"

[2017-08-16 13:53:54] # stringiftest("DEVSIM", "yes", 2)

[2017-08-16 13:53:54] # stringiftest("RECSIM", "", 2)

[2017-08-16 13:53:54] # < C:/Instrument/Var/tmp/test_config.txt

[2017-08-16 13:53:54] # If in test rec sim mode

[2017-08-16 13:53:54] epicsEnvSet TESTRECSIM "#"

[2017-08-16 13:53:54] # epicsEnvSet "DEVSIM" "0"

[2017-08-16 13:53:54] # epicsEnvSet "RECSIM" "1"

[2017-08-16 13:53:54] # stringiftest("DEVSIM", "", 2)

[2017-08-16 13:53:54] # stringiftest("RECSIM", "yes", 2)

[2017-08-16 13:53:54] # < C:/Instrument/Var/tmp/test_config.txt

[2017-08-16 13:53:54] ## Create the emulator port macro and set it to either the one given or a spare port:

[2017-08-16 13:53:54] # freeIPPort(SPARE_PORT)

[2017-08-16 13:53:54] # epicsEnvSet "EMULATOR_PORT" 

[2017-08-16 13:53:54] # epicsEnvShow("EMULATOR_PORT") 

[2017-08-16 13:53:54] ## Load record instances

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/dbload.cmd

[2017-08-16 13:53:54] #dbLoadRecords("$(TIMESTAMPRECORD)/db/timestamp.db","P=$(MYPVPREFIX)$(IOCNAME):")

[2017-08-16 13:53:54] dbLoadRecords("C:/Instrument/Apps/EPICS/support/devIocStats/master/db/iocAdminSoft.db","IOC=TE:NDW1798:CS:IOC:SIMPLE:DEVIOS")

[2017-08-16 13:53:54] #dbLoadRecords("$(ASUBFUNCTIONS)/db/iocExit.db","P=$(MYPVPREFIX),Q=CS:IOC:$(IOCNAME):,IOCNAME=$(IOCNAME)")

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/autosave.cmd

[2017-08-16 13:53:54] ## start autosave.cmd

[2017-08-16 13:53:54] save_restoreSet_Debug(0)

[2017-08-16 13:53:54] # status-PV prefix, so save_restore can find its status PV's.

[2017-08-16 13:53:54] #epicsEnvSet("ASPREFIX","$(MYPVPREFIX)CS:IOC:$(IOCNAME):AS:")

[2017-08-16 13:53:54] epicsEnvSet("ASPREFIX","TE:NDW1798:AS:SIMPLE:")

[2017-08-16 13:53:54] save_restoreSet_status_prefix("TE:NDW1798:AS:SIMPLE:")

[2017-08-16 13:53:54] # Ok to save/restore save sets with missing values (no CA connection to PV)?  

[2017-08-16 13:53:54] save_restoreSet_IncompleteSetsOk(1)

[2017-08-16 13:53:54] # Save dated backup files?

[2017-08-16 13:53:54] save_restoreSet_DatedBackupFiles(1)

[2017-08-16 13:53:54] # Number of sequenced backup files to write

[2017-08-16 13:53:54] save_restoreSet_NumSeqFiles(1)

[2017-08-16 13:53:54] # Time interval between sequenced backups

[2017-08-16 13:53:54] save_restoreSet_SeqPeriodInSeconds(300)

[2017-08-16 13:53:54] # specify where save files should be - use a different directory if in simulation mode

[2017-08-16 13:53:54] mkdir("C:/Instrument/Var/autosave/SIMPLE") 

[2017-08-16 13:53:54] set_savefile_path("C:/Instrument/Var/autosave", "SIMPLE")

[2017-08-16 13:53:54] ## specify what save files should be restored.  Note these files must be

[2017-08-16 13:53:54] ## in the directory specified in set_savefile_path(), or, if that function

[2017-08-16 13:53:54] ## has not been called, from the directory current when iocInit is invoked

[2017-08-16 13:53:54] ## example: set_pass0_restoreFile("autosave_geiger.sav")

[2017-08-16 13:53:54] ## restore positions at pass 0 so not passed to hardware

[2017-08-16 13:53:54] ##

[2017-08-16 13:53:54] ## Use     epicsEnvSet("AUTOSAVEREQ","#")   if you do not have any req files to load

[2017-08-16 13:53:54]  set_pass0_restoreFile("SIMPLE_positions.sav")

[2017-08-16 13:53:54]  set_pass0_restoreFile("SIMPLE_settings.sav")

[2017-08-16 13:53:54] # restore settings at pass 1 so passed to hardware

[2017-08-16 13:53:54]  set_pass1_restoreFile("SIMPLE_settings.sav")

[2017-08-16 13:53:54] # these values are obtained from info fields in DB files via makeAutosaveFiles() / makeAutosaveFileFromDbInfo()

[2017-08-16 13:53:54] set_pass0_restoreFile("SIMPLE_info_positions.sav")

[2017-08-16 13:53:54] set_pass0_restoreFile("SIMPLE_info_settings.sav")

[2017-08-16 13:53:54] set_pass1_restoreFile("SIMPLE_info_settings.sav")

[2017-08-16 13:53:54] #save_restoreSet_CAReconnect(1)

[2017-08-16 13:53:54] # specify directories in which to to search for included request files

[2017-08-16 13:53:54] set_requestfile_path("C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master/iocBoot/iocsimple", "")

[2017-08-16 13:53:54] # Autosave status PVs - P must be same as used in save_restoreSet_status_prefix() above

[2017-08-16 13:53:54] dbLoadRecords("C:/Instrument/Apps/EPICS/support/autosave/master/asApp/Db/save_restoreStatus.db", "P=TE:NDW1798:AS:SIMPLE:")

[2017-08-16 13:53:54] ## end autosave.cmd

[2017-08-16 13:53:54] dbLoadRecords("db/simple.db","P=TE:NDW1798:SIMPLE:")

[2017-08-16 13:53:54] < C:/Instrument/Apps/EPICS/iocstartup/preiocinit.cmd

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] # write process variable and IOC startup information to database 

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] pvdump

[2017-08-16 13:53:54] pvdump: ioc name is "SIMPLE" pid 11856

[2017-08-16 13:53:54] pvdump: MySQL write of 129 PVs with 33 info entries, plus 307 macros took 0.092 seconds

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] # set up IOC access security

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] asSetFilename("C:/Instrument/Apps/EPICS/support/AccessSecurity/master/default.acf")

[2017-08-16 13:53:54] asSetSubstitutions("P=TE:NDW1798:,ACF_IH1=localhost,ACF_IH2=localhost,ACF_IH3=localhost,ACF_IH4=localhost")

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] # log to server address EPICS_IOC_LOG_INET listening on port EPICS_IOC_LOG_PORT 

[2017-08-16 13:53:54] #

[2017-08-16 13:53:54] epicsEnvSet("EPICS_IOC_LOG_INET", "localhost")

[2017-08-16 13:53:54] iocLogInit()

[2017-08-16 13:53:54] log client: connected to log server at "127.0.0.1:7004"

[2017-08-16 13:53:54] cd C:/Instrument/Apps/EPICS/ISIS/SimpleIoc/master/iocBoot/iocsimple

[2017-08-16 13:53:54] iocInit

[2017-08-16 13:53:54] sevr=info Starting iocInit

[2017-08-16 13:53:54] ############################################################################

[2017-08-16 13:53:54] ## EPICS R3.15.5

[2017-08-16 13:53:54] ## EPICS Base built Jul 10 2017

[2017-08-16 13:53:54] ############################################################################

[2017-08-16 13:53:54] sevr=info reboot_restore: entry for file 'SIMPLE_positions.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_positions.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.savB'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.savB'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't figure out which seq file is most recent,

[2017-08-16 13:53:54] sevr=info save_restore: so I'm just going to start with 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't find a file to restore from...sevr=info save_restore: ...last tried 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_positions.sav0'. I give up.

[2017-08-16 13:53:54] save_restore: **********************************

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info save_restore: Can't open save file.sevr=info reboot_restore: entry for file 'SIMPLE_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't figure out which seq file is most recent,

[2017-08-16 13:53:54] sevr=info save_restore: so I'm just going to start with 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't find a file to restore from...sevr=info save_restore: ...last tried 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'. I give up.

[2017-08-16 13:53:54] save_restore: **********************************

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info save_restore: Can't open save file.sevr=info reboot_restore: entry for file 'SIMPLE_info_positions.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_info_positions.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_info_positions.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info reboot_restore: done with file 'SIMPLE_info_positions.sav'

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info reboot_restore: entry for file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_info_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_info_settings.sav' at initHookState 6 (before record/device init) ***

[2017-08-16 13:53:54] sevr=info reboot_restore: done with file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info reboot_restore: entry for file 'SIMPLE_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav' at initHookState 7 (after record/device init) ***

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.savB'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't figure out which seq file is most recent,

[2017-08-16 13:53:54] sevr=info save_restore: so I'm just going to start with 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Trying backup file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'

[2017-08-16 13:53:54] sevr=info save_restore: Can't open file 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'.

[2017-08-16 13:53:54] sevr=info save_restore: Can't find a file to restore from...sevr=info save_restore: ...last tried 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_settings.sav0'. I give up.

[2017-08-16 13:53:54] save_restore: **********************************

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] sevr=info save_restore: Can't open save file.sevr=info reboot_restore: entry for file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] sevr=info reboot_restore: Found filename 'SIMPLE_info_settings.sav' in restoreFileList.

[2017-08-16 13:53:54] sevr=info *** restoring from 'C:/Instrument/Var/autosave/SIMPLE/SIMPLE_info_settings.sav' at initHookState 7 (after record/device init) ***

[2017-08-16 13:53:54] sevr=info reboot_restore: done with file 'SIMPLE_info_settings.sav'

[2017-08-16 13:53:54] 

[2017-08-16 13:53:54] icpconfigLoad: setPVValuesStatic setting 0 pvs (pre iocInit)

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:54] sevr=info Duplicated host 'localhost' in HAG 'instmachine'

[2017-08-16 13:53:55] cas warning: Configured TCP port was unavailable.

[2017-08-16 13:53:55] cas warning: Using dynamically assigned TCP port 60745,

[2017-08-16 13:53:55] cas warning: but now two or more servers share the same UDP port.

[2017-08-16 13:53:55] cas warning: Depending on your IP kernel this server may not be

[2017-08-16 13:53:55] cas warning: reachable with UDP unicast (a host's IP in EPICS_CA_ADDR_LIST)

[2017-08-16 13:53:55] sevr=info iocRun: All initialization complete

[2017-08-16 13:53:55] icpconfigLoad: setPVValues setting 0 pvs (post iocInit)

[2017-08-16 13:53:55] < C:/Instrument/Apps/EPICS/iocstartup/postiocinit.cmd

[2017-08-16 13:53:55] # enable caPutLog to logger on localhost

[2017-08-16 13:53:55] # pass 0 to log value changes, pass 1 to log all puts, 2 logs all puts with no filtering on same PV

[2017-08-16 13:53:55] caPutLogInit "localhost" "1"

[2017-08-16 13:53:55] log client: connected to log server at "127.0.0.1:7011"

[2017-08-16 13:53:55] sevr=info caPutLog: successfully initialized

[2017-08-16 13:53:55] # Handle autosave 'commands' contained in loaded databases.

[2017-08-16 13:53:55] # file naming needs to agree with autosave.cmd

[2017-08-16 13:53:55] makeAutosaveFileFromDbInfo("SIMPLE_info_settings","autosaveFields")

[2017-08-16 13:53:55] makeAutosaveFileFromDbInfo("SIMPLE_info_positions","autosaveFields_pass0")

[2017-08-16 13:53:55] create_monitor_set("SIMPLE_info_positions.req", 5, "")

[2017-08-16 13:53:55] create_monitor_set("SIMPLE_info_settings.req", 30, "")

[2017-08-16 13:53:55] sevr=info SIMPLE_info_positions.sav: 63 of 63 PV's connected

[2017-08-16 13:53:55] sevr=info 

[2017-08-16 13:53:56] sevr=info SIMPLE_info_settings.sav: 1 of 1 PV's connected

[2017-08-16 13:53:56] sevr=info 
```
> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [DAE](DAE-Trouble-Shooting)

### DAE switches from processing to Unknown and never goes into SetUp

See [Other Troubleshooting -> instrument page not working on web dashboard](Other-Troubleshooting#instrument-page-not-working-on-web-dashboard)

Also once observed on LARMOR, accompanied by the following error messages continuously being logged to `C:\data\log\icp-<date>.log`:

```
2017-04-13 20:52:14  NIVISA: Error "Could not perform operation because of I/O error." (code 0xbfff003e) returned from "viMoveIn32"  while transferring 1001 items at VME address 0x18000fa4
2017-04-13 20:52:15  NIVISA: Error "Could not perform operation because of I/O error." (code 0xbfff003e) returned from "viMoveIn32"  while transferring 1001 items at VME address 0x18000fa4
2017-04-13 20:52:16  NIVISA: Error "Could not perform operation because of I/O error." (code 0xbfff003e) returned from "viMoveIn32"  while transferring 1001 items at VME address 0x18000fa4
2017-04-13 20:52:17  (0) NIVisa: [Warning] (NIVisa::retryBlock) retryBlock: 1001 items from address 0x18000fa4
2017-04-13 20:52:17  (0) NIVisa: [Information] (NIVisa::reinit) Calling NIVisa::reinit()
2017-04-13 20:52:17  Calling NIVisa::reinit()
2017-04-13 20:52:17  Endian workaround DISABLED, blocks transfers DISABLED
2017-04-13 20:52:17  This is a VXI DAE
```

This was resolved by powercycling the DAE followed by stopping the visa server and running `resman`. (Ask Freddy or Gareth to find out more)

### No log files are produced in `c:\data` even though blocks are set to log.
The reason may be because cp hasn't been set to look for epics. In `C:\LabVIEW Modules\dae\isisicp.properties` set `isisicp.epicsdb.use = true` to log the epic's blocks

### DAE doesn't seem to be connected/I want to run without a DAE connected
The DAE can be set to run in simulation mode, this must be unset before data will be collected. To set the mode edit the xml file in `C:\LabVIEW Modules\dae\icp_config.xml` set the simulate property to 1 to simulate 0 to use hardware.

### Log file for labview modules DA

The log file for real icpisis program is written to `C:\Data\Export only\logs\icp\log\icp-<date>log` and should read something like:

```
2017-04-20T10:47:54 ################################################################################

2017-04-20T10:47:54 ISIS ICP Starting from c:\labview modules\dae\service\x64\Release at 2017-04-20T10:47:54

2017-04-20T10:47:54 SVN revision 842 (2010/06/11 11:37:02, Modified)

2017-04-20T10:49:42 SELOGGER with ISISDB schema rev 37 using SQLITE 3.6.22

2017-04-20T10:49:42 There is        81 percent of memory in use.
2017-04-20T10:49:42 There are  4193848 total Kbytes of physical memory.
2017-04-20T10:49:42 There are   795580 free Kbytes of physical memory.
2017-04-20T10:49:42 There are  8590636 total Kbytes of paging file.
2017-04-20T10:49:42 There are  2411068 free Kbytes of paging file.
2017-04-20T10:49:42 There are 8589934464 total Kbytes of virtual memory.
2017-04-20T10:49:42 There are 8589814888 free Kbytes of virtual memory.
2017-04-20T10:49:42 There are        0 free Kbytes of extended memory
2017-04-20T10:49:42 Setting DAE type to NEUTRON on NDXHRPD
2017-04-20T10:49:42 XML key "UseFullInstNameForFiles" not found
2017-04-20T10:49:42 Run digits = 5
2017-04-20T10:49:42 Opening connection to VISA resource ISISDAE0

2017-04-20T10:49:42 Calling NIVisa::reinit()
2017-04-20T10:49:42 ScanBus skipped - set ISISVME_SCANBUS environment variable to enable
2017-04-20T10:49:42 Endian workaround DISABLED, blocks transfers DISABLED
2017-04-20T10:49:42 This is a VXI DAE
2017-04-20T10:49:42 This Card Supports Fast (Fermi) Chopper Vetos
--- DAE2 card with address/position/number = 0 ---
Firmware register: 0x41030403
Hardware type: ENVIRONMENT CARD (Configured from detector card)
Firmware sub version = 3
Firmware minor version = 4
Firmware hardware version = 3

This is an ENVIRONMENT card
RC register value = 0x110008
Status: Stopped
Frame Sync: External
Delayed start: disabled
Frame sync delay: 29996
FIFO Veto is ENABLED (vetoed 0) frames
SMP (chopper) Veto is ENABLED (vetoed 0) frames
Fermi Chopper Veto is DISABLED (counted 0) frames
TS2 Pulse Veto is DISABLED (counted 0) frames
ISIS 50 Hz Veto is DISABLED (counted 0) frames
External Veto 0 is ENABLED (vetoed 0) frames
External Veto 1 is DISABLED (counted 0) frames
External Veto 2 is ENABLED (vetoed 0) frames
External Veto 3 is DISABLED (counted 0) frames
GOOD/RAW frames: 0/0
GOOD/RAW uamph: 0/0
Period Type: Software

2017-04-20T10:49:42 Highest DAE2 spectrum: 2
Number of position: 2
MPOS: 0 to 0
MODN: 0 to 1

2017-04-20T10:49:42 Recreated DAE1 specmap with DAE1 spec range 1 to 2

2017-04-20T10:49:43 Unable to determine card memory size; assuming 128Mb
2017-04-20T10:49:43 This Card Supports HARDWARE periods
This Card Supports VETO logging
This Card supports delayed frame sync
--- DAE2 card with address/position/number = 1 ---
Firmware register: 0x82060105
Hardware type: DETECTOR CARD (Neutron, 16 DIM)
Firmware sub version = 5
Firmware minor version = 1
Firmware hardware version = 6

This is a DECTECTOR card with 128 MB memory
Highest DAE2 spectrum used = 2
14661 time channels
SOFTWARE periods: number of periods = 1
Total counts register = 0
Veto for Dim0 is ENABLED, CLEAR
Veto for Dim1 is ENABLED, CLEAR
Veto for Dim2 is ENABLED, CLEAR
Veto for Dim3 is ENABLED, CLEAR
Veto for Dim4 is ENABLED, CLEAR
Veto for Dim5 is ENABLED, CLEAR
Veto for Dim6 is ENABLED, CLEAR
Veto for Dim7 is ENABLED, CLEAR
Veto for Dim8 is ENABLED, CLEAR
Veto for Dim9 is ENABLED, CLEAR
Veto for Dim10 is ENABLED, CLEAR
Veto for Dim11 is ENABLED, CLEAR
Veto for Dim12 is ENABLED, CLEAR
Veto for Dim13 is ENABLED, CLEAR
Veto for Dim14 is ENABLED, CLEAR
Veto for Dim15 is ENABLED, CLEAR
Delayed Frame synch  = 0
POSLUT checksum = 817e75953d48998d20aebc226ce44c8

2017-04-20T10:49:43 Highest DAE2 spectrum: 191
Number of position: 976
MPOS: 0 to 376
MODN: 5 to 11

2017-04-20T10:49:43 Recreated DAE1 specmap with DAE1 spec range 1 to 191

2017-04-20T10:49:44 Unable to determine card memory size; assuming 128Mb
2017-04-20T10:49:44 This Card Supports HARDWARE periods
This Card Supports VETO logging
This Card supports delayed frame sync
--- DAE2 card with address/position/number = 2 ---
Firmware register: 0x82060105
Hardware type: DETECTOR CARD (Neutron, 16 DIM)
Firmware sub version = 5
Firmware minor version = 1
Firmware hardware version = 6

This is a DECTECTOR card with 128 MB memory
Highest DAE2 spectrum used = 191
14661 time channels
SOFTWARE periods: number of periods = 1
Total counts register = 0
Veto for Dim0 is ENABLED, CLEAR
Veto for Dim1 is ENABLED, CLEAR
Veto for Dim2 is ENABLED, CLEAR
Veto for Dim3 is ENABLED, CLEAR
Veto for Dim4 is ENABLED, CLEAR
Veto for Dim5 is ENABLED, CLEAR
Veto for Dim6 is ENABLED, CLEAR
Veto for Dim7 is ENABLED, CLEAR
Veto for Dim8 is ENABLED, CLEAR
Veto for Dim9 is ENABLED, CLEAR
Veto for Dim10 is ENABLED, CLEAR
Veto for Dim11 is ENABLED, CLEAR
Veto for Dim12 is ENABLED, CLEAR
Veto for Dim13 is ENABLED, CLEAR
Veto for Dim14 is ENABLED, CLEAR
Veto for Dim15 is ENABLED, CLEAR
Delayed Frame synch  = 0
POSLUT checksum = 6a385651302654f3d7429d1656ce8ed0

2017-04-20T10:49:44 Highest DAE2 spectrum: 256
Number of position: 1536
MPOS: 0 to 255
MODN: 0 to 5

2017-04-20T10:49:44 Recreated DAE1 specmap with DAE1 spec range 1 to 256

2017-04-20T10:49:45 Unable to determine card memory size; assuming 128Mb
2017-04-20T10:49:45 This Card Supports HARDWARE periods
This Card Supports VETO logging
This Card supports delayed frame sync
--- DAE2 card with address/position/number = 3 ---
Firmware register: 0x82060105
Hardware type: DETECTOR CARD (Neutron, 16 DIM)
Firmware sub version = 5
Firmware minor version = 1
Firmware hardware version = 6

This is a DECTECTOR card with 128 MB memory
Highest DAE2 spectrum used = 256
14661 time channels
HARDWARE periods: number of DAQ periods = 1
Current DAQ period number = 0
Current DAQ period size (words) = 0
Total counts register = 0
Veto for Dim0 is ENABLED, CLEAR
Veto for Dim1 is ENABLED, CLEAR
Veto for Dim2 is ENABLED, CLEAR
Veto for Dim3 is ENABLED, CLEAR
Veto for Dim4 is ENABLED, CLEAR
Veto for Dim5 is ENABLED, CLEAR
Veto for Dim6 is ENABLED, CLEAR
Veto for Dim7 is ENABLED, CLEAR
Veto for Dim8 is ENABLED, CLEAR
Veto for Dim9 is ENABLED, CLEAR
Veto for Dim10 is ENABLED, CLEAR
Veto for Dim11 is ENABLED, CLEAR
Veto for Dim12 is ENABLED, CLEAR
Veto for Dim13 is ENABLED, CLEAR
Veto for Dim14 is ENABLED, CLEAR
Veto for Dim15 is ENABLED, CLEAR
Delayed Frame synch  = 0
POSLUT checksum = 8bc9ea7e4e6221c9f8844dcc39d5fc

2017-04-20T10:49:45 Highest DAE2 spectrum: 24
Number of position: 72
MPOS: 0 to 15
MODN: 0 to 7

2017-04-20T10:49:45 Recreated DAE1 specmap with DAE1 spec range 1 to 24

2017-04-20T10:49:45 Unable to determine card memory size; assuming 128Mb
2017-04-20T10:49:45 This Card Supports HARDWARE periods
This Card Supports VETO logging
This Card supports delayed frame sync
--- DAE2 card with address/position/number = 4 ---
Firmware register: 0x82060105
Hardware type: DETECTOR CARD (Neutron, 16 DIM)
Firmware sub version = 5
Firmware minor version = 1
Firmware hardware version = 6

This is a DECTECTOR card with 128 MB memory
Highest DAE2 spectrum used = 24
14661 time channels
HARDWARE periods: number of DAQ periods = 1
Current DAQ period number = 0
Current DAQ period size (words) = 0
Total counts register = 0
Veto for Dim0 is ENABLED, CLEAR
Veto for Dim1 is ENABLED, CLEAR
Veto for Dim2 is ENABLED, CLEAR
Veto for Dim3 is ENABLED, CLEAR
Veto for Dim4 is ENABLED, CLEAR
Veto for Dim5 is ENABLED, CLEAR
Veto for Dim6 is ENABLED, CLEAR
Veto for Dim7 is ENABLED, CLEAR
Veto for Dim8 is ENABLED, CLEAR
Veto for Dim9 is ENABLED, CLEAR
Veto for Dim10 is ENABLED, CLEAR
Veto for Dim11 is ENABLED, CLEAR
Veto for Dim12 is ENABLED, CLEAR
Veto for Dim13 is ENABLED, CLEAR
Veto for Dim14 is ENABLED, CLEAR
Veto for Dim15 is ENABLED, CLEAR
Delayed Frame synch  = 0
POSLUT checksum = 43557b38a98c1d6b91c2f490c3b9421d

2017-04-20T10:49:45 Card 0 is present on dae 0 (ISISDAE0)(Environment card)
Card 1 is present on dae 0 (ISISDAE0)(Neutron Detector card)
Card 2 is present on dae 0 (ISISDAE0)(Neutron Detector card)
Card 3 is present on dae 0 (ISISDAE0)(Neutron Detector card)
Card 4 is present on dae 0 (ISISDAE0)(Neutron Detector card)

2017-04-20T10:49:45 XML key "DAEDevice1" not found
2017-04-20T10:49:45 CRPT "c:\data\current.run" size 65414 KB
2017-04-20T10:49:45 CRPT version 2 ($Revision: 827 $)
2017-04-20T10:49:45 CRPT data "c:\data\data.run" size 781250 KB
2017-04-20T10:49:46 XML key "AlertEmail" not found
2017-04-20T10:49:46 XML key "UAmpScale" not found
2017-04-20T10:49:46 XML key "CompressionLevel" not found
2017-04-20T10:49:46 XML key "CompressionBlockSize" not found
2017-04-20T10:49:46 Setting up DAE
2017-04-20T10:49:46 Highest dae, detector card, crate number used = 0, 4, 4
2017-04-20T10:49:46 Number of time regimes = 1
2017-04-20T10:49:46 DAE memory used = 19 Mb
2017-04-20T10:49:46 Number of periods (daq, total) = (1, 1)
2017-04-20T10:49:46 Resetting DAE - ignore veto counter values as not yet cleared
2017-04-20T10:49:46 SMP vetoed frames = 0
Externally vetoed frames = 0
FIFO vetoed frames = 0
TS2 pulse vetoed frames = 0
ISIS not at 50Hz vetoed frames = 0
Fermi chopper vetoed frames = 0
TOTAL VETOED FRAMES from all sources = 0

2017-04-20T10:49:46 RELOAD TABLES ONLY requested - DAE memory not zeroed
2017-04-20T10:49:46 Programming Time channels
2017-04-20T10:49:46 Global Frame sync delay = 29996 us
2017-04-20T10:49:46 Electronics delay = 7 clock pulses
2017-04-20T10:49:46 Setting 14661 time channels from 3.781250 to 100003.781250 us
2017-04-20T10:49:46 Setting FS delay on DC 1 to 0 us
2017-04-20T10:49:46 Setting FS delay on DC 2 to 0 us
2017-04-20T10:49:46 Setting FS delay on DC 3 to 0 us
2017-04-20T10:49:46 Setting FS delay on DC 4 to 0 us
2017-04-20T10:49:46 Programming POSLUT
2017-04-20T10:49:46 Card: 1 DAE2 Highest: 2 DAE1 low: 64 DAE1 high: 65 NPOS: 2
MPOS: 0 to 0
MODN: 0 to 1

2017-04-20T10:49:46 
2017-04-20T10:49:46 There is a gap of total size 3 in the DAE1 spectra on the card
Card: 2 DAE2 Highest: 191 DAE1 low: 0 DAE1 high: 193 NPOS: 1280
MPOS: 0 to 383
MODN: 4 to 11

2017-04-20T10:49:46 
2017-04-20T10:49:46 Card: 3 DAE2 Highest: 256 DAE1 low: 66 DAE1 high: 321 NPOS: 1536
MPOS: 0 to 255
MODN: 0 to 5

2017-04-20T10:49:46 
2017-04-20T10:49:46 Card: 4 DAE2 Highest: 24 DAE1 low: 322 DAE1 high: 345 NPOS: 72
MPOS: 0 to 15
MODN: 0 to 7

2017-04-20T10:49:46 
2017-04-20T10:49:46 Software periods enabled
2017-04-20T10:49:46 (setting period card, if present, to 1 hardware period of 15000 frames)
2017-04-20T10:49:46 No period card present
2017-04-20T10:49:46 Setting vetos
2017-04-20T10:49:46 Enabling FIFO veto
2017-04-20T10:49:46 Enabling SMP veto
2017-04-20T10:49:46 Enabling EXTERNAL veto 0
2017-04-20T10:49:46 Disabling EXTERNAL veto 1
2017-04-20T10:49:46 Enabling EXTERNAL veto 2
2017-04-20T10:49:46 Disabling EXTERNAL veto 3
2017-04-20T10:49:46 Disabling Fermi Chopper veto
2017-04-20T10:49:46 Disabling TS2 Pulse veto
2017-04-20T10:49:46 Disabling ISIS 50Hz veto
2017-04-20T10:49:46 ***
*** ISIS ICP STARTUP COMPLETE 2017-04-20T10:49:46
***
```

### Error pop up: `*** ICP failed to start - your DAE may be switched OFF or is missing cards ***`
The DAE unit may be switched off. This is particularly likely during shut down. Change the DAE into simulation mode as described above.

If the DAE is on then it is likely that it has been power cycled.
Two possible ways to fix it are:
 
1) Restarting the DAE rack server
 
1) Via NI MAX, using the following steps:
    a) Connect to the DAE rack server via Remote Desktop from the NDX machine (the machine should be listed in the Remote Desktop dialog)
    b) Run NI MAX on the DAE rack server
    c) Under Software->NI-VISA X.X.X,  select VISA Server and click "Stop server now"
    d) Under "Devices and Interfaces", select "VXI System" and click "Run the VXI Resources Manager.
    e) Finally, repeat b) but click "Start server now"

### Blocks not being added to Nexus file
This should not occur but has when a database was missing our extra column in the archive. If the sample table in the archive is missing a sample_id, run the following. Note that it can take a while on a database with a large number of rows in that table.
``` "c:\programs files\wherever...\Mysql.exe" -u root -p  --execute="ALTER TABLE sample ADD COLUMN sample_id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Sample id'" archive```

### Not enough CRPT memory

CRPT (Current Run Parameter Table) memory is a large in-memory structure used to store information about the run, including histogrammed data. Data is read from the DAE into CRPT memory and then written to file, in event mode CRPT memory is where events are histogrammed on the fly during collecting to provide real-time spectra. If you get a CRPT size error, it means the product of (number of periods) * (number of spectra) * (number of time channels) is too big. If you are in histogram mode you either need to reduce one of these variables or get the CRPT size increased (icp_config.xml) but remember this is real memory that the ICP will claim at startup. If you are in event mode and get a CRPT error, it may mean you have misconfigured the time regime you plan to use for the on-the-fly rebinning e.g. you are trying to rebin events at event mode resolution not at a coarser resolution. The event mode / histogram mode choice and which time regime to use is governed by the wiring tables.

### End of run script not working

See https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Experimental-Runs#experimental-files-not-being-archived-and-so-not-appearing-in-the-journal

### No frames/beam current registered by the DAE

Try switching the timing source to "Internal test clock" and starting a run. If counts are received in this state, it means that the DAE isn't receiving timing pulses from the central source. If that's the case, it needs attention from the electronics group (e.g. Simon Moorby).  Note, this may occur on more than one beam line so keep an ear open for any other reports.

Don't forget to switch the timing source back when you're done!

Other things to to check in this state are:

- [ ] Visit the beamline - (possibly with electronics is suspecting a hardware problem).
   Software usually doesn't just stop normally when other things are working  - right? :smile: 
- [ ] Most importantly, ask the scientists if anything happened around the time of the problem, in a recent case they mentioned someone had moved a cable on an ADC (although this was not the problem!).
- [ ] Look at the lights on the ADC or detector input module cards on the DAE. If no lights flickering, there is no data coming in and this is a good indicator that the HT might be off (a few lights might mean shutter closed or beam off).
- [ ] data/transfer lights on a DAEII, flickering & transfer lights inactive not a good sign.  Could be the link to the PC if transfer lights are not showing activity.
- [ ] If frame/raw counts are not showing up, a good diagnostic is to put the DAE into "Internal Test Clock".  If this works and frames appear, it is likely that there may be a problem with a Time of Flight signal (this often affects more than one beamline.

## Simulation mode DAE complains about missing cards

From an issue in Ticket https://github.com/ISISComputingGroup/IBEX/issues/3099 - example traceback:

```
[2018-04-09 15:26:49] sevr=major  setDCEventMode: Unknown detector card 3

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 3

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 4

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 4

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 5

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 5

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 6

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 6

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 7

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 7

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 8

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 8

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 9

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 9

[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 10

[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 10

[2018-04-09 15:26:49]  Cannot find card for crate 3

[2018-04-09 15:26:49]  Unknown detector card 3

[2018-04-09 15:26:49]  Cannot find card for crate 4

[2018-04-09 15:26:49]  Unknown detector card 4

[2018-04-09 15:26:49]  Cannot find card for crate 5

[2018-04-09 15:26:49]  Unknown detector card 5

[2018-04-09 15:26:49]  Cannot find card for crate 6

[2018-04-09 15:26:49]  Unknown detector card 6

[2018-04-09 15:26:49]  Cannot find card for crate 7

[2018-04-09 15:26:49]  Unknown detector card 7

[2018-04-09 15:26:49]  Cannot find card for crate 8

[2018-04-09 15:26:49]  Unknown detector card 8

[2018-04-09 15:26:49]  Cannot find card for crate 9

[2018-04-09 15:26:49]  Unknown detector card 9

[2018-04-09 15:26:49]  Cannot find card for crate 10

[2018-04-09 15:26:49]  Unknown detector card 10

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 3

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 4

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 5

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 6

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 7

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 8

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 9

[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 10

[2018-04-09 15:26:49] : Exception occurred.
```

The issue here is that the default simulated DAE has 2 detector cards in it, but the real DAE has more cards. To fix edit `isisicp.properties` in Labview modules to create more cards. Note this is not an ibex issue - it will also affect DAE simulation mode under SECI. The number of cards on each crate is given by the maximum missing card for the crate (see log), more crates can be added as well as cards. An example from wish with 3 crates, 10, 10 and 12 card per crate is:

```
isisicp.simulation.detcards.crate0.number = 10
isisicp.simulation.detcards.crate1.number = 10
isisicp.simulation.detcards.crate2.number = 12
```

If you have defined   isisisp.datadae.use = true     in isisicp.properties   then you need to make sure the setector card referred to in data_dae.xml  is created by above. If this is a pure setup/test machine rather than a real instrument, you may just want to set     isisisp.datadae.use = false  
 
## DAE3 does not start 

DAE3 is new ethernet based acquisition electronics on ZOOM and MARI, it used ISISICP and looks like DAE2 for most purposes. If everything remains in processing, it may be that the `arp` network entries did not get created - these should be done as a system time boot task. Do `arp -a` and see if there is an entry for 192.168.1.101 etc.  If not, run `set_dae3_arp.bat` in `c:\labview modules\dae` as as administrator

## Error code 112

If there is an error code 112 reported in the log it means that the disk (data volume) is full and it can not start the isisicp program.

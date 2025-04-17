> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [DAE](DAE-Trouble-Shooting) > [DAE Normal Log](DAE-Normal-Log)

# Standard startup log

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

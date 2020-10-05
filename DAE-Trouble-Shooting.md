> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [DAE](DAE-Trouble-Shooting)

### Restarting the DAE in IBEX

This IOC does not appear in the normal IOC restart list in the IBEX client, first open an EPICS terminal

`...\EPICS\epicsterm.bat`

then run

`console -M localhost ISISDAE_01`

and when connected press `Ctrl-x` once, you should see some restart messages from the IOC. Quit the EPICS term.

### invalid tcb start

It is likely that you are in a muon configuration for the DAE but using a neutron tcb file or vice versa.

Either change the [tcb file](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/DAE-and-the-ICP#configuring-the-daeicp) you are using or do the following steps to change the DAE type:

1. Change the DAE type of your icp_config.xml (in EPICS/ICP_Binaries) to the correct value (1 for DAE2 neutron, 2 for DAE2 muon, 3 for DAE3 neutron, 4 for DAE3 muon).
2. In the same directory edit the isisicp.properties file to use either neutron or muon for `isisicp.simulation.detcards.type`
3. Restart the ISISDAE using console in an EPICS terminal and end the isisicp task in the task manager (the ISISDAE should autorestart it)

### DAE switches from processing to Unknown and never goes into SetUp / Run can not be ended

See [Other Troubleshooting -> instrument page not working on web dashboard](Other-Troubleshooting#instrument-page-not-working-on-web-dashboard)

*DAE2*

This issue has been observed on LARMOR and TOSCA, accompanied by the following error messages continuously being logged to `C:\data\log\icp-<date>.log`:

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
This was resolved by powercycling the DAE followed by stopping the visa server and running `resman`. Instructions how to reset the DAE can be found in [these slides](https://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ISISICP%20and%20DAE.pptx). Ask Freddy to find out more

*DAE3*

On a DAE3 machine a vendor network library is used rather than NI Visa and the equivalent sorts of errors will have `Qx` or `Quixtream` prefixes. Access from the ISISICP is via the network, so there is no intermediate service/server to restart. Usually the ISISICP will retry failed connections, but check with electronics if there are repeated failures. You can try restarting ISISICP in case the vendor library needs a reload itself. An example of the error message is:

```
2020-02-27T09:55:41  Qxtrm_channel::RDMARead failed rdma2 address 0x40010 nbytes 4(Quixtream: The timeout period on this channel expired before the transfer commenced. Channel status: Transfer failed. Data packet not received before timeout. )
```

In general if you see an error like this or starting with `NIVISA` you should restart the DAE, then [contact electronics](https://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Contact%20details%20for%20other%20groups.docx).

### No log files are produced in `c:\data` even though blocks are set to log.
The reason may be because cp hasn't been set to look for epics. In `C:\LabVIEW Modules\dae\isisicp.properties` set `isisicp.epicsdb.use = true` to log the epic's blocks. You will need to restart the `isisicp` process for this to take effect. To do this, just end the `isisicp` process in task manager.

### DAE doesn't seem to be connected/I want to run without a DAE connected
The DAE can be set to run in simulation mode, this must be unset before data will be collected. To set the mode run `g.set_dae_simulation_mode(True)` or `g.set_dae_simulation_mode(False)` to unset.

To change the simulation mode manually, in `icp_config.xml` change the simulate property to 1 (or 0 if turning off simulation mode). `icp_config.xml` can be found in either the "LabVIEW modules" or "ICP Binaries" directory. Stop the DAE IOC from the console, then kill the ISISICP process. Finally, restart the DAE IOC from the console.

### Log file for labview modules DA

The log file for real icpisis program is written to `C:\Data\Export only\logs\icp\log\icp-<date>log`. There is an [example DAE log in this wiki](DAE-Normal-Log).


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

CRPT (Current Run Parameter Table) memory is a large in-memory structure used to store information about the run, including histogrammed data. Data is read from the DAE into CRPT memory and then written to file, in event mode CRPT memory is where events are histogrammed on the fly during collecting to provide real-time spectra. If you get a CRPT size error, it means the product of (number of periods) * (number of spectra) * (number of time channels) is too big. If you are in histogram mode you either need to reduce one of these variables or get the CRPT size increased (icp_config.xml) but remember this is real memory that the ICP will claim at startup. If you are in event mode and get a CRPT error, it may mean you have misconfigured the time regime you plan to use for the on-the-fly rebinning e.g. you are trying to rebin events at event mode resolution not at a coarser resolution. The event mode / histogram mode choice and which time regime to use is governed by the [wiring tables](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/DAE-and-the-ICP#configuring-the-daeicp).

### End of run script not working or data not being copied to the archive

There is a known bug where starting a run at the same time as the previous run is being saved can be cause the nexus file not to be marked read-only and so not copied to the archive. A `NEXUS ERROR: ERROR:` message will appear in the log. See https://github.com/ISISComputingGroup/IBEX/issues/4977

To fix this and other errors see https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Experimental-Runs#experimental-files-not-being-archived-and-so-not-appearing-in-the-journal

### No frames/beam current registered by the DAE

Try switching the timing source to "Internal test clock" (found in experiment setup tab of DAE) and starting a run. If counts are received in this state, it means that the DAE isn't receiving timing pulses from the central source. If that's the case, it needs attention from the electronics group (e.g. Simon Moorby).  Note, this may occur on more than one beam line so keep an ear open for any other reports.

Don't forget to switch the timing source back when you're done!

Other things to to check in this state are:

- [ ] Visit the beamline - (possibly with electronics is suspecting a hardware problem).
   Software usually doesn't just stop normally when other things are working  - right? :smile: 
- [ ] Most importantly, ask the scientists if anything happened around the time of the problem, in a recent case they mentioned someone had moved a cable on an ADC (although this was not the problem!).
- [ ] Look at the lights on the ADC or detector input module cards on the DAE. If no lights flickering, there is no data coming in and this is a good indicator that the HT might be off (a few lights might mean shutter closed or beam off).
- [ ] data/transfer lights on a DAEII, flickering & transfer lights inactive not a good sign.  Could be the link to the PC if transfer lights are not showing activity.
- [ ] If frame/raw counts are not showing up, a good diagnostic is to put the DAE into "Internal Test Clock".  If this works and frames appear, it is likely that there may be a problem with a Time of Flight signal (this often affects more than one beamline.

### My total counts are low
Make sure that the timing is appropriate (e.g. a DAE Timing Source of `ISIS (first TS1)` will only count the first pulse not all 4)

### Simulation mode DAE complains about missing cards

From an issue in Ticket https://github.com/ISISComputingGroup/IBEX/issues/3099 - example traceback:

```
[2018-04-09 15:26:49] sevr=major  setDCEventMode: Unknown detector card 3
[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 3
[2018-04-09 15:26:49]  setDCEventMode: Unknown detector card 4
[2018-04-09 15:26:49]  setDCCardMode: Unknown detector card 4
[2018-04-09 15:26:49]  Cannot find card for crate 3
[2018-04-09 15:26:49]  Unknown detector card 3
[2018-04-09 15:26:49]  Cannot find card for crate 4
[2018-04-09 15:26:49]  Unknown detector card 4
[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 3
[2018-04-09 15:26:49]  Attempt to use missing detector card/crate 4
[2018-04-09 15:26:49] : Exception occurred.
```

The issue here is that the default simulated DAE has 2 detector cards in it, but the real DAE has more cards. To fix edit `isisicp.properties` in Labview modules to create more cards. Note this is not an ibex issue - it will also affect DAE simulation mode under SECI. The number of cards on each crate is given by the maximum missing card for the crate (see log), more crates can be added as well as cards. An example from wish with 3 crates, 10, 10 and 12 card per crate is:

```
isisicp.simulation.detcards.crate0.number = 10
isisicp.simulation.detcards.crate1.number = 10
isisicp.simulation.detcards.crate2.number = 12
```

If you have defined `isisisp.datadae.use = true` in `isisicp.properties` then you need to make sure the detector card referred to in data_dae.xml  is created by above. If this is a pure setup/test machine rather than a real instrument, you may just want to set `isisisp.datadae.use = false`

### Real DAE complains about missing cards
If you see messages like
```
setDCEventMode: Unknown detector card 1
setDCCardMode: Unknown detector card 1
Attempt to use missing detector card/crate 1
Unknown detector card 
```
when trying to BEGIN on a real DAE, then there are two likely causes:
- you are loading a wiring table that is specifying cards that do no exist, you need to correct the wiring table
- The ICP has not detected all the cards you believe are present in the DAE, hence they appear to be "missing" or "unknown"

If the wiring table is correct, try a restart of the ISISICP - the DAE is only scanned at program startup, it might be the DAE hardware was not feeling very responsive first time around. If this doesn't help, then it may be the detector card has failed, or it could be the hardware is in a strange state and needs a reset. Electronics group have programs that can do this.  

### DAE exception messages

If you get an error in you IOC log like:

```
[2018-10-26 17:33:37] sevr=major Win32StructuredException code 0xc0000005 pExpCode 0xc0000005 pExpAddress 0000000000000000
[2018-10-26 17:33:37] 2018/10/26 17:33:36.741 IN:DEMO:DAE:AD1:INTG:TMIN:SP devAsynFloat64 pPvt->result.status=3, process error isisdaeDriver:writeFloat64: status=0, function=184, name=INTG_TMIN, value=0.000000, error=Win32StructuredException code 0xc0000005 pExpCode 0xc0000005 pExpAddr
```
 
One cause would be the IOC is trying to call a function in the ISISICP that it can't find. If the ISISICP has been updated, but   /RegServer  has not been run, then new functions added there will not be visible. See [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/First-time-installing-and-building-(Windows)#configure-dae-for-simulation-mode-on-developers-computer--register-isisicp).
  
### DAE3 does not start 

DAE3 is new ethernet based acquisition electronics on ZOOM and MARI, it used `ISISICP` and looks like DAE2 for most purposes. If everything remains in processing, it may be that the `arp` network entries did not get created - these should be done as a system time boot task. Do `arp -a` and see if there is an entry for 192.168.1.101 etc.  If not, run `set_dae3_arp.bat` in `c:\labview modules\dae` as as administrator

### Error code 112

If there is an error code 112 reported in the log it means that the disk (data volume) is full and it can not start the `isisicp` program.

### DAE Type mismatch error

If you get an error from ISISICP `*** ISISICP STARTUP FAILED (DAE type mistmatch)***` it means you are running `isisicp` program with the wrong sort of dae ie 2 when you have 3. You need to source the correct version of the code for your type of DAE.

### isisicp.exe keeps allocating 4GB of memory and then releasing it

It may be https://github.com/ISISComputingGroup/IBEX/issues/3701 - you just need to change the archive array table type to MEDIUMBLOB.  Due to a bug in the C++/MySQL connector, each time the database is read, a LONGBLOB's worth of memory (4GB) is allocated and then released.  By changing to MEDIUMBLOB (16MB), a much smaller amount is used.

In `C:\Instrument\Apps\MySQL\bin>`, run `mysql.exe -u root -p` and enter the MySQL root password when prompted.

Then run these commands to modify the DB in place:

```
USE archive;
ALTER TABLE sample MODIFY COLUMN array_val MEDIUMBLOB;
```

### Instrument stuck in `WAITING` state

We have observed on a couple of occasions that the DAE got stuck in `WAITING` despite no blocks being outside of runcontrol limits. The cause is yet unclear but in the meantime a restart of the `RUNCTRL_01` IOC seems to fix the issue.

### ISISDAE reports `time regimes 1 and 2 are incompatible`

[Time regimes](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/DAE-and-the-ICP#configuring-the-daeicp) are incompatible when their starts differ by a non-integer number of microseconds, but sometimes rounding errors may lead to this happening in other circumstances. This check is actually no longer required and has been removed in ISISICP SVN revisions 2010 and above. 

### ISISICP writes a corrupted journal file

The symptom is that `C:\data\journal_<cycle_number>.xml` will not be valid xml, it will be truncated at some point. We believe this happens when there are too many blocks set to log into the journal in a particular configuration.

After switching back to a configuration with fewer blocks, the journal file can be (carefully!) manually edited to remove the corrupt entry. Once this is done, runs should go back into the journal as normal (however, runs done while in the configuration with too many blocks will be lost from the journal).

Freddie may also have a patched version of the isisicp that fixes this issue.

### My blocks aren't being written to a run title properly

See the documentation in the [user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Add-blocks-to-run-title)

### Exception in ICP log

If the ICP is showing an error in the form of `NeXusEventCallback: [Warning] (NeXusEventCallback<class DAE2DetCardPolicy>::allFrameCallback) Invalid DAE time value` this indicates a hardware problem. Newer versions of the ISISICP will estimate and then correct the time information based on good data either side of the corrupt data, if these messages are appearing frequently you should get in touch with the electronics group.

### A `measurement.nxs` file is being written to the `C:\data` area

This file is written by the ISISICP on some instruments if they have defined a non-zero "measurement ID". It is intended to be used for correlating runs. The presence of the file itself is nothing to worry about.

### Gap in time in journal file for run start and end (so may think No Data has been written)

If the instrument is in a WAITING state for the entire run, then the end_time as written in the nexus file/journal will be the same as the start time. The ICP interprets end time as end of neutron data collection, so if this never starts it remains the same as the start time and run duration is 0. All sample environment data will be collected OK in a WAITING state.

### Simulated DAE does into VETOING after a PAUSE/RESUME

The symptom is that, when you do a begin the instrument will go into running and look happy, but after you do a pause/resume it will permanently be in vetoing (until the run is ended and the next run is started).

This is a bug in the ISISICP as it does not simulate hardware period properly.

Resolution:
- Ensure period mode is not "hardware" (use software)
- Kill and restart `isisicp.exe` (need to do this as the simulated isisicp can't change period modes correctly without restarting)

### Control program unable to read from DAE3

If there are lots of read timeouts, but writes work, then this could be a firewall issue. Try disabling the firewall on the DAE private (192.168.*) network (this is the network that is not the "domain" network on an instrument, often it is called "public"). There should be firewall rules to allow programs access, but something may have gone wrong with them
   
### Beam current in Dashboard oscillating

The beam current in the dashboard is not read from the accelerator, but is calculated from the DAE which records the total amount of proton charge received so far. The software reads the DAE charge value, then reads again after a certain amount of time, and then the difference between these plus the time gap allow an effective beam current to be calculated. By effective I mean it will include running at a slow chopper speed as well as vetos, so with a 25Hz chopper on TS1 you will expect to see roughly half the TS1 accelerator delivered value.

If the DAE beam current is oscillating but the accelerator is constant, then this can be due to issues with the time or charge component of the calculation. If it is oscillating rapidly, it may be due to some reads taking longer and meaning the "time" value used in the calculation does not correspond to the charges used. Look for DAE read timeouts, or sometimes if a lot of spectra are being displayed in the GUI this can slow down DAE proton reads. If there are a lot of DAE timeouts in the log, contact electronics group. 

If the DAE beam current is incorrect for a period of time rather than rapid oscillations, this is more likely to be due to either vetos or the DAE syncing to the wrong accelerator pulse. HRPD run at 10Hz and were seeing a DAE beam current going to zero for a period of time and then returning to normal. TS1 runs at 50Hz, but 1 pulse in 5 (10Hz) goes to TS2 so if a  10Hz chopper syncs to the missing pulse you will not see any data. It looked like on HRPD this syncing was shifting and occasionally latching onto the empty pulse for a period of time (several minutes). This syncing could be a chopper or DAE issue, probably start with DAE first .

### Add Single Run Entry into the Journal

It is possible to add a single run into the journal database if it was not included for some reason simply run:

```
"c:\labview modules\dae\JournalParser.exe" <INSTRUMENT> <9 DIGIT run number> cycle_<cycle number, e.g. 19_3> "c:\data\export only" <INSTRUMENT MACHINE HOST NAME>
```
e.g. `"c:\labview modules\dae\JournalParser.exe" LOQ 00108032 cycle_19_3 "c:\data\export only" NDXLOQ`

###  CRPT is not initialised - please set experiment parameters

Ensure you have loaded the correct Time Channels and Data Acquisition tables in the Experiment setup tab of the DAE perspective. Reloading them causes initialisation.

### User Says they Can Not see their Nexus Data files on external machine

After a run the data files should be copied to an external archive so that the users can do more processing. If the user can not get these then there can be multiple causes and it depends exactly where they are looking. The first thing to check is that the machine is copying the files correctly in the post 
end run script. The log for this is stored at `C:\Data\log\post_command_<day>.log`. If there is a problem rectify the problem, possible causes are:

- mapped drive (`d:`) is not connected properly: often double clicking on the drive is enough to get it remapped
- something else: fix and document here

After fixing the issues the files will be copied after the next run is finished. So start and end a run (with a test like title), you may also want to put it in simulation mode if the DAE is switched off. Finally check the files have appeared in `<isis instrument folder>\<machine name>\Instrument\data\cycle_<cycle number>`.

### DAE Server restart doen't work message when clicking start "Cannot start server on port XXX"

If you need to restart the NI visa server on the host machine and clicking start on the server says can not start server, it may be that the via driver has started in the admin account instead of the user account. Log onto the host machine and quit the NI VXI Resource manager application. This should allow the user accounts server to start.


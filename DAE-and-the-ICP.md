> [Wiki](Home) > [The Backend System](The-Backend-System) > [System Components](System-components) > [DAE and the ICP](DAE-and-the-ICP)

# The DAE and the ICP

The Data Acquisition Electronics (DAE) is the physical hardware that reads the neutron events out of the detectors. IBEX communicates with this hardware via the Instrument Control Program (ICP). This program is also responsible for combining the neutron and sample environment data into the NeXus file.
Additional links:

- [Sharepoint Slides with more info on the DAE & ICP](https://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ISISICP%20and%20DAE.pptx)
- [Troubleshooting the DAE](DAE-Trouble-Shooting).
- Details on [dae spectra updating problem](Dae-Spectra-Updating-Problem)

## Running the DAE in Parallel

In some cases you may want your DAE to mimic the state of a DAE on another machine. This is particularly useful when testing the DAE3 hardware as it will give comparable data files to the ones created by a DAE2.

To do this you must:
* Switch to the dae3_pull_dae2_data [branch](https://github.com/ISISComputingGroup/EPICS-isisdae/tree/dae3_pull_dae2_data)
* Add `dbLoadRecords("$(ISISDAE)/db/dae3_pull.db","P=$(MYPVPREFIX),Q=DAE:,O=XXX")` to the st.cmd of your DAE, where XXX is the prefix of the instrument which you wish to mimic.
* Copy across the wiring, detector and spectra tables from the other instrument.
* Set your DAE with the same tables and the same general settings.
* Wait until the other instrument is in SETUP
* Start your DAE

The DAE will mimic the run state, title and period of the DAE it is point to.

## Event and Histogram Mode
The DAE/ICP has two main 'modes' of operation, event mode and histogram mode. In event mode the position and timestamp of every single neutron that the detector finds is passed through the DAE to the ICP and saved into the NeXus file. In histogram mode the DAE will intercept these events and put them into bins based on when they hit the detector. Due to the binning of events histograms lead to some lost information however historically histogrammed data was the only option due to limited data rates. Instruments in general are moving more towards event data but it still has the disadvantage that it will lead to large and unwieldy NeXus files and in some cases offers little benefit as histogramming would be the first step of data analysis anyway.

In reality this mode of operation is actually set per detector card rather than over the whole DAE. However instruments will tend to run with a majority one way or the other and so scientists tend to think of them as distinct modes. The exception to this is monitors where instruments will nearly always histogram them. This is for two reasons:

* They have higher flux than other detectors so will dramatically increase file size if put as events
* They're used mainly for normalisation and diagnostics so loss of precision is not that much of a big deal

## Configuring the DAE/ICP
There are two settings files inside `EPICS/ICP_Binaries` that are used to configure the ICP at start up, these are `icp_config.xml` and `isisicp.properties`. They contain information that is usually quite fixed for an instrument such as whether to start up in simulation mode, how much memory to use etc. **NOTE:** on in instrument these files live in a different location `c:\labview modules\dae`. The `isisicp.properties` file is used to override settings in `isisicp.default.properties`. 

There are three main files that can be set at runtime to change the behaviour of the DAE or used for later analysis, they are collectively known as tables and need to be selected from the "Experiment Setup/Data Acquisition" tab in the GUI:
* *Detector Table*: Files containing the word detector specifying the physical location of each detector. The second line contains the number of entries followed by the number of user parameters. The table consists of a detector id, it's offset, it's L2 (distance from the sample), an id code and then as many user specified parameters as specified in the second line.
* *Spectra Table*: Files containing the word spectra specifying how detector id (which has little meaning to an instrument scientist) maps to spectrum number (which the scientists use for analysis). The second line contains the number of detectors.
* *Wiring Table*: Files containing the word wiring and specifying how the detectors are connected to the DAE. The second line specifies how many detectors there are and how many of those are monitors. The table contains an index, detector id, time regime (see time channels below), physical crate, module and position numbers, the monitor that the detector corresponds to (0 for none) and the monitor prescale. 
These files are picked up from `Instrument/Settings/config/inst/configurations/tables`, have the *.dat suffix and are all human readable. They can be edited by hand but must be done carefully to ensure that there are no logic errors within them. For example if a detector is listed in one file but not in another. 

### Time Channel Binning - setting to event/histogram mode

The way that data is binned by the DAE is set by changing the time channel boundaries (TCB). Scientists generally want different amounts of detail depending on when the neutron hit the detector, which they can do by setting a smaller bin in the time range that they care more about. They can do this through the GUI manually or by creating a tcb file that is loaded into the ICP/ibex GUI. It may be that scientists would like different levels of binning for different banks of detectors they can do this by setting up a number of different `time regimes` and then specifying the regime they would like the detector to go into in the wiring table.

Time regimes defined in the GUI are assigned an integer from 1 to 99. There is a special convention for the time regime number in a wiring table file. If the integer 1-99 is used, this means collect in histogram mode using binning created from that time regime. Specifying a time regime number of > 100 in a wiring table file is a convention for event mode - specifying YYXX will collect events using regime XX regime but create 'on the fly' histograms in YY time regime for quick spectra view. Normally you will see `1` for histogram mode and `102` for event mode in a wiring file, this mean histograms will use time regime 1 and event mode will use time regime 2 for collecting the data at high resolution but create histograms based on time regime 1 resolution for quick spectrum views         

By default data will head into one or two spectra, if you want to see data across all backs e.g. for an areaDetector simulation then look for the following lines in `isisicp.properties` mentioned above in `Configuring the DAE/ICP`
```
isisicp.simulation.neventssim = 50
isisicp.simulation.spreadsimevents = false
```
change `spreadsimevents` to `true`, you probably don't need to increase `neventssim` unless you had loaded a custom larger wiring table and spectra aren't accumulating data fast enough for you.
 
## Performing arbitrary actions on run start/run end

The ISISDAE ioc can be configured to process PVs just after starting and ending runs. It is easiest to configure this in `globals.txt` like the following example for the SANS2D fast shutter:

```
ISISDAE_01__POST_BEGIN_1=TE:NDW1799:FINS_VAC:SHUTTER:OPEN_IF_AUTO.PROC CA PP
ISISDAE_01__POST_RESUME_1=TE:NDW1799:FINS_VAC:SHUTTER:OPEN_IF_AUTO.PROC CA PP
ISISDAE_01__POST_END_1=TE:NDW1799:FINS_VAC:SHUTTER:CLOSE_IF_AUTO.PROC CA PP
ISISDAE_01__POST_ABORT_1=TE:NDW1799:FINS_VAC:SHUTTER:CLOSE_IF_AUTO.PROC CA PP
ISISDAE_01__POST_PAUSE_1=TE:NDW1799:FINS_VAC:SHUTTER:CLOSE_IF_AUTO.PROC CA PP
```

There are currently 4 macros available for each of `POST_BEGIN_x`, `POST_END_x`, `POST_ABORT_x`, `POST_PAUSE_x` and `POST_RESUME_x`.

Note that if the PV you want to process is not in the ISISDAE ioc, you will need to specify the `.PROC` field explicitly for the link to work.

## ISISDAE environment variables

These were added for https://github.com/ISISComputingGroup/IBEX/issues/6560 but testing proved inconclusive, so may need to be revisited:

* `ISISDAE_TIMER_PRIORITY` controls if the spectra read timer queue thread is same (0), higher (1) or lower (-1) priority than other scan threads, defaults to higher 
* `ISISDAE_TIMER_SLEEP` how long to sleep after a spectra read to allow a thread yield (default: 1ms)

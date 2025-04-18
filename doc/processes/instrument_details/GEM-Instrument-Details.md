# GEM

This page collects information that will be useful for the implementation of the IBEX control system on GEM.
## Background & Timeline ##
GEM is a diffractometer instrument at ISIS, on TS1. The [GEM](http://www.isis.stfc.ac.uk/instruments/gem/gem2467.html) web page describes the background to the instrument.

## Control System ##
GEM will migrate from the SECI control system to the IBEX control system in summer 2017.  During the summer 2017 shutdown, new jaws will be installed on GEM.

## GEM Equipment ##
The equipment listed below is used on GEM. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#gem_noteDAE)
ISIS | Mk2 Chopper | Chopper | RS-232 | see [#2130](https://github.com/ISISComputingGroup/IBEX/issues/2130) | [see Chopper note](#gem_noteChopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
??? |  | 5 x 4-blade jaws |  |  | [see Jaws note](#gem_noteJaws)
??? |  | 1 x 4-blade jaws |  |  | "Beamscraper" Jaws [see Jaws note](#gem_noteJaws)
ISIS | Collimator | Oscillating Radial |  |   | [see Collimator note](#gem_noteCollimator)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#gem_noteVacuum)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#gem_noteEurotherm)
Oxford Instruments | Orange Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#gem_noteOxfordInstruments)
Oxford Instruments | Blue Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#gem_noteOxfordInstruments)
Oxford Instruments | Dilution Fridge (Kelvinox) | Cryogenic System |   |  | [see Oxford Instruments note](#gem_noteOxfordInstruments)
   |   | Closed Cycle Refrigerator | | | | [see CCR note](#gem_noteCCR)
ISIS | GEM-Furnace | Furnace |   |  | [see ISIS Furnaces note](#gem_noteISISFurnaces)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#gem_noteMcLennan)
ISIS | GEM Sample Changer | Sample Changer | RS-232 | | Same as POLARIS sample changer. See [#2173](https://github.com/ISISComputingGroup/IBEX/issues/2173)
MKS | PDR2000 | Pressure Transducer | RS-232 | | see [#1406](https://github.com/ISISComputingGroup/IBEX/issues/1406) and [#1620](https://github.com/ISISComputingGroup/IBEX/issues/1620)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | see [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)


From time-to-time, GEM has also used magnets, gas handling and high-pressure systems, but not frequently.

{#gem_noteDAE}
##### Note: DAE #####
Main Detector banks + fixed monitors.

{#gem_noteChopper}
##### Note: Choppers #####
3 choppers: 2 double-disk and one T0 chopper.<br>
Choppers are ISIS Mk2 choppers.  Mk2 choppers have a serial interface (not Ethernet like Mk3).

{#gem_noteCollimator}
##### Note: Oscillating Radial Collimator #####
The oscillating radial collimator is currently driven by a McLennan system, controlled via a custom controller at present. At some point this controller is going to be replaced by a Galil system, but this will not be done by September 2017.

There have been instances where the collimator stops responding (see: https://github.com/ISISComputingGroup/IBEX/issues/3167). These cases present as the device responding to status requests, but not acting on requests to reinitialise or start the oscillator. In this case, the device has to be power-cycled. To do this, it must first be switched off via the front panel, then the power cable must be removed. Leave the device for several seconds before reconnecting and switching back on. If successful, the number of cycles should reset to zero.

{#gem_noteJaws}
##### Note: Jaws #####
GEM has 5 four-blade jaws and one bespoke set of jaws (called the "beam-scraper").<br>
For the "beam-scraper" jaws - see #[2138](https://github.com/ISISComputingGroup/IBEX/issues/2138)<br>
The 5 four-blade jaws were due to be replaced with Galil driven units during summer 2017.  However, as of May 2017, the upgrade has been postponed:<br>
`
From Ivan da Silva:
Finally, due to other instrument works’ priorities, the GEM works for replacing the jaws will not be carried out during the next summer shutdown, but during winter 2017/2018.
Then, for 2017/02 cycle we will be still using the same jaws sets as for now. In principle, we will start using the new jaws on cycle 2017/04 (Feb-Apr 2018).
`<br>
Therefore, all jaws on GEM will continue to be controlled by LinMot controllers until, at least, cycle 2017/04.
Confirmed by Nick Webb (04-07-2017): new GEM jaws, controlled by Galil, will be installed in November 2017.

{#gem_noteVacuum}
##### Note: Vacuum System #####
GEM does not need to control the vacuum system, but it does need to be able to view and log vacuum gauge readings.

{#gem_noteEurotherm}
##### Note: Eurotherm #####
Used to control temperature Orange Cryostat, CCR and Furnace devices.

{#gem_noteOxfordInstruments}
##### Note: Oxford Instruments #####

1. Orange Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.  Orange cryostats are controlled via a temperature controller (e.g. Eurotherm), so nothing on the cryostat itself for IBEX to control.
1. Blue Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.
   1. Are these the Heliox and ITC devices?
   1. The Heliox device has a sorption insert (is that relevant to the control system?)
1. Dilution fridge: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/dilution-refrigerators8825.html) to be determined.
   1. [Kelvinox dilution fridge](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/kelvinox-dilution-fridge/kelvinox-dilution-fridge13981.html)

{#gem_noteCCR}
##### Note: Closed Cycle Refrigerators #####
[CCRs](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/ccrs/closed-cycle-refrigerators-ccrs8446.html). Not directly computer-controlled  - controlled via Eurotherm.

{#gem_noteISISFurnaces}
##### Note: ISIS Furnaces #####
More information on [IRIS Furnaces](http://www.isis.stfc.ac.uk/sample-environment/high-temperature/standard-furnaces/standard-furnaces13745.html).  GEM uses:

1. GEM Furnace
1. RAL 4 Furnace
1. Low temperature furnace

Furnaces are controlled via a temperature controller (e.g. Eurotherm), so nothing on the furnace itself for IBEX to control.

{#gem_noteMcLennan}
##### Note: McLennan #####
[see Collimator note](#gem_noteCollimator)

## GEM SECI Configs ##
Document information about GEM SECI configs here.

Configuration Name                                        | Sub-Configurations                                             | Last Accessed | Required |
----------------------------------------------------------|----------------------------------------------------------------|---------------|----------|
gem_heliox.conf                                           | -                                                              | 14/11/2016    | -
gem_sample_changer_matt.conf                              | Choppers                                                       | 20/05/2016    | -
gem_ccr_matt.conf                                         | Choppers                                                       | 28/04/2016    | -
gem_sample_changer_Alex.conf                              | Choppers                                                       | 24/02/2016    | -
gem_lowT_furnace_matt.conf                                | Choppers                                                       | 04/12/2015    | -
gem_kelvinox_matt.conf                                    | -                                                              | 01/10/2015    | -
GEM_CRYOSTAT.conf                                         | Choppers                                                       | 24/07/2015    | -
gem_furnace_matt.conf                                     | Choppers, Furnace Pressure                                     | 15/06/2015    | -
gem_polaris_sample_changer_matt.conf                      | Choppers                                                       | 26/04/2015    | -
gem_furnace_ramp.conf                                     | Furnace Pressure                                               | 03/04/2015    | -
gem_furnace.conf                                          | Furnace Pressure                                               | 02/04/2015    | -
gem_3eurotherms.conf                                      | -                                                              | 20/03/2015    | -
gem_sample_changer.conf                                   | Choppers                                                       | 18/03/2015    | -
GEM_CRYOSTAT_matt.conf                                    | -                                                              | 02/06/2014    | -
gem_ccr.conf                                              | Choppers                                                       | 02/04/2014    | -
gem_8t cryo.conf                                          | GEM_Base, Choppers                                             | 18/12/2013    | -
5 Axis.conf                                               | -                                                              | 20/07/2013    | -
gem_sample_changer_+_3_Eurotherms.conf                    | 3_Eurotherms                                                   | 18/03/2013    | -
gem_tizrcell_matt.conf                                    | -                                                              | 16/10/2012    | -
gem_3eurotherms_pressure.conf                             | -                                                              | 12/10/2012    | -
gem_ambient.conf                                          | -                                                              | 04/10/2011    | -
gem_3eurotherms_baritron.conf                             | -                                                              | 16/04/2011    | -
gem_express.conf                                          | -                                                              | 23/02/2011    | -
gem_gazcell.conf                                          | -                                                              | 16/02/2011    | -
gem_cryo + eurotherm.conf                                 | -                                                              | 15/02/2011    | -
gem_7t cryomagnet.conf                                    | -                                                              | 15/02/2011    | -
Dave.conf                                                 | -                                                              | 15/02/2011    | -
gem_kelvinox.conf                                         | -                                                              | 27/01/2011    | -
gem_cryo + ilm.conf                                       | -                                                              | 27/01/2011    | -
gem_cryo + ilm + SC.conf                                  | -                                                              | 27/01/2011    | -
gem_cryo + heliox.conf                                    | -                                                              | 27/01/2011    | -
gem_8t cryo + rotation.conf                               | -                                                              | 27/01/2011    | -
gem_8t cryo + kelvinox.conf                               | -                                                              | 27/01/2011    | -
gem_10t cryomagnet.conf                                   | -                                                              | 27/01/2011    | -

## GEM Genie Scripts ##
Similarly, Document information about GEM SECI Genie scripts here.

## GEM Notes ##
Add any notes about special items of equipment, setup or conditions on GEM that might impact the deployment and configuration of IBEX.

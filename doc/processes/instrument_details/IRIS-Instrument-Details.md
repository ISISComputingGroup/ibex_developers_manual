# IRIS

This page collects information that will be useful for the implementation of the new control system on IRIS.

## Online info

* [Instrument Scientists](https://www.isis.stfc.ac.uk/Pages/Instrument-Scientists.aspx) IRIS row
* https://www.isis.stfc.ac.uk/Pages/iris.aspx
* [Beam Line Manual](https://www.isis.stfc.ac.uk/Pages/irisman.pdf)

## Background & Timeline ##
IRIS is a long established instrument at ISIS, on TS1. The [IRIS](http://www.isis.stfc.ac.uk/instruments/iris/iris4691.html) web page describes the background to the instrument.  A schematic layout of IRIS is shown in ​[this diagram](http://www.isis.stfc.ac.uk/images/instruments/iris-/iris-schematic4923.jpg).<br>
IRIS shares a port with [OSIRIS](http://www.isis.stfc.ac.uk/instruments/osiris/osiris4667.html). We may need to have a way of sharing information between the IRIS and OSIRIS control systems. It might also be worth migrating IRIS and ​OSIRIS to IBEX at the same time. 

## Control System ##
IRIS will migrate from the SECI control system to the IBEX control system.

## IRIS Equipment ##
The equipment listed below is used on IRIS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#iris_noteDAE)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
[Pfeiffer](https://www.pfeiffer-vacuum.com/en/products/) | TPG 26x | ISIS Vacuum System | RS232 | | [see Pfeiffer note](#iris_notePfeiffer)
[Pfeiffer](https://www.pfeiffer-vacuum.com/en/products/) | TPG 300 | ISIS Vacuum System | RS232 | #216 | [see Pfeiffer note](#iris_notePfeiffer)
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | #169 | 
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#iris_noteMcLennan)
ISIS| | Sample Changer | via McLennan | | [see Sample Changer note](#iris_noteSampleChanger)
Leybold | 1040 100mm TL GM | Top-Loading Closed Cycle Refrigerator | | | [see Leybold note](#iris_noteLeybold)
Sumitomo | 4K 100mm TL GM | Top-Loading Closed Cycle Refrigerator | | | [see Sumitomo note](#iris_noteSumitomo)
Oxford Instruments | Dilution Fridge | Cryogenic System | RS-232 | | [see Oxford Instruments note](#iris_noteOxfordInstruments)
Oxford Instruments | Blue Cryostat| Cryogenic System | RS-232 | | [see Oxford Instruments note](#iris_noteOxfordInstruments)
ILL?| Orange Cryostat | Cryogenic System | RS-232 | | [see Orange Cryostat note](#iris_noteOrangeCryostat)
ISIS | Furnace | High temperature furnace | RS-232 | | [see Furnace note](#iris_noteFurnace)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#iris_noteEurotherm)
LakeShore | 218 | | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore)| [see LakeShore note](#iris_noteLakeshore )
LakeShore | 336| | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#iris_noteLakeshore )
LakeShore | 340 | | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#iris_noteLakeshore )
MKS | PDR2000 | Pressure Transducer | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#MKS) | [see MKS  note](#iris_noteMKS )
ISIS | Helium 3 Controller | All models at ISIS | RS-232 | | [see He3 Controller note](#iris_noteHe3Controller)
ISIS | Helium Level Gauge | All models at ISIS | RS-232 | | [see He Level Gauge  note](#iris_noteHeLevelGauge)
ISIS | Exchange Gas Controller | All models at ISIS | RS-232 | | [see Exchange Gas Controller note](#iris_noteExchangeGas)
ISIS | CryoValve Controller | All models at ISIS | RS-232 | | [see CryoValve Controller note](#iris_noteCryovalve)

{#iris_noteDAE}
##### Note: DAE #####
Main Detector banks + 2-3 monitors.

{#iris_notePfeiffer}
##### Note: Pfeiffer #####

1. [Model TPG 26x](https://www.pfeiffer-vacuum.com/en/products/measurement/activeline/controllers/?detailPdoId=5724)
2. [Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407)

{#iris_noteMcLennan}
##### Note: McLennan #####
1. One McLennan will eventually be used to control the rotating centre-stick, McLennan-Newport Rotation Stage
2. One McLennan is used to control the Sample Changer, currently set on port 1
3. One McLennan has been used to control a stretching rig, currently set on port 2

The homing behaviour for the McLennans is currently under review. The McLennan IOC startup scripts have been partially customised for Iris based on observed behaviour for each device. This behaviour is subject to review by the development team.

{#iris_noteSampleChanger}
##### Note: Sample Changer #####
The Sample Changer is driven by the McLennan motor (i.e. it raises/lowers sample cans attached to the sample changer).  There is a photograph of the [Sample Changer](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IRIS/IRIS_Sample_Changer.jpg), which shows the sample cans attached to the bottom of the sample changer.  There is also a [diagram](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IRIS/IRIS_Sample_Changer_Diagram(log%20book).JPG) showing the dimensions of the Sample Changer (the diagram is taken from the instrument scientist's notebook - it is a sketch, not an engineering drawing (just to set your expectations :-) ).

{#iris_noteLeybold}
##### Note: Leybold #####
[CCR-11](https://www.isis.stfc.ac.uk/Pages/Top-Loading-CCRs.aspx). Not directly computer-controlled - controlled via Eurotherm.

{#iris_noteSumitomo}
##### Note: Sumitomo #####
[CCR-64](https://www.isis.stfc.ac.uk/Pages/Top-Loading-CCRs.aspx). Not directly computer-controlled  - controlled via Eurotherm.

{#iris_noteOxfordInstruments}
##### Note: Oxford Instruments #####

1. Dilution fridge: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/dilution-refrigerators8825.html) to be determined.
2. Blue Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.

{#iris_noteOrangeCryostat}
##### Note: Orange Cryostat #####
Orange Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.  Eurotherm controlled.

{#iris_noteEurotherm}
##### Note: Eurotherm #####
Used to control temperature of top-loading CCRs, Be Filter, Furnace, Orange Cryostat devices.
There are at least 6 Eurotherm devices on IRIS, arranged in two crates of 3, as illustrated in the photograph of the [Eurotherm Crate](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IRIS/IRIS_Eurotherm_Triple_Crate.jpg).

{#iris_noteLakeshore}
##### Note: LakeShore #####

1. [Model 218](http://www.lakeshore.com/products/Cryogenic-Temperature-Monitors/Model-218/Pages/Overview.aspx): Monitors temperature of Analyser Banks
2. [Model 336](http://www.lakeshore.com/products/cryogenic-temperature-controllers/model-336/Pages/Overview.aspx):
3. [Model 340](http://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-340/Pages/Overview.aspx): this model is now obsolete, having been replaced by the 336 and 350 models.

There are [EPICS drivers](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) for a variety of Lakeshore temperature controllers.

The Lakeshore 336 on IRIS is shown in the linked [photograph](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IRIS/IRIS_Lakeshore_336.jpg).

Documentation on the Lakeshore 336 IOC setup can be found [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Lakeshore336).

{#iris_noteFurnace}
##### Note: ISIS High temperature furnace #####
Controlled via Eurotherm.

{#iris_noteMKS}
##### Note: MKS PDR2000 Pressure Transducer #####
The [MKS PDR2000A](http://www.mksinst.com/product/Product.aspx?ProductID=175) provides power and readout up to two (2) Baratron® pressure transducers.

There are [EPICS drivers](http://www.aps.anl.gov/epics/modules/manufacturer.php#MKS%20Instruments) for a variety of MKS devices (although there is a driver for a PDR4000 pressure transducer, there does not appear to be one for a PDR2000).

{#iris_noteHe3Controller}
##### Note: He3 Controller #####
Consists of ACM1000 Gauge controller, ACT200H Pump Controller, Neocera LTC-21 Temperature Controller

{#iris_noteHeLevelGauge}
##### Note: He Level Gauge #####
_no comment (as yet)_

{#iris_noteExchangeGas}
##### Note: Exchange Gas Controller #####
_no comment (as yet)_

{#iris_noteCryovalve}
##### Note: CryoValve Controller #####
Due to be superseded by the Exchange Gas Controller.

## IRIS SECI Configs ##
Over the years, IRIS has built up a significant collection of SECI configs. Not all of them are current (some may no longer be used, or used only infrequently). We will need to investigate how to convert them to IBEX configs.  The current list of IRIS configs is listed on [trac](https://trac.isis.rl.ac.uk/ICP/wiki/IRIS).
The config files are located in the folder `SECI\Configurations\` on the control server and have the extension `.conf`.  Sub-configuration files have the extension `.comp` (component).  The files with numbers as extensions (`.1`, `.2`, `.3`,etc.) are backups of the configuration and sub-configuration files.

## IRIS Genie Scripts ##
Similarly, IRIS has built up a significant collection of genie scripts over the years. Again, many scripts are old and may no longer be used regularly. Most runs on IRIS are controlled via scripts. There will be a need to convert some of these scripts to genie-python, but probably not all.

The current list of IRIS genie scripts is listed on [trac](https://trac.isis.rl.ac.uk/ICP/wiki/IRIS).

## Tested IOCs ##

| What | When | Notes |
| ---- | ---- | ----- |
| Eurotherm 1 | 15/09/2016 | Temps 1-3 com 6 |
| Eurotherm 2 | 15/09/2016 | Temps 4-6 com 14 |
| Eurotherm 3 | 15/09/2016 | single reading com 8 |
| Lakeshore 218 | 15/09/2016 | com 20 |
| Lakeshore 336 | 15/09/2016 | ip ls336-1 |
| MK3 Choppers | 15/09/2016 |  |
| CryoValve | 15/09/2016 | com 13 |
| TPG300 | 15/09/2016 |  |
| TPG268 | 15/09/2016 | com11 |


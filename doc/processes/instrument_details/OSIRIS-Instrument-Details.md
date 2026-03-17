# OSIRIS

```{include} migration_notes_warning.mdinc
```

This page collects information that will be useful for the implementation of the new control system on OSIRIS.
## Background & Timeline ##
OSIRIS is a long established instrument at ISIS, on TS1. The [OSIRIS](https://www.isis.stfc.ac.uk/Pages/osiris.aspx) web page describes the background to the instrument.  A schematic layout of OSIRIS is shown in ​[this diagram](https://www.isis.stfc.ac.uk/Gallery/OSIRIS_3D_BW_Labelled.JPG).<br>
OSIRIS shares a port with [IRIS](https://www.isis.stfc.ac.uk/Pages/iris.aspx). We may need to have a way of sharing information between the IRIS and OSIRIS control systems. It might also be worth migrating IRIS and ​OSIRIS to IBEX at the same time. 

## OSIRIS Equipment ##
The equipment listed below is used on OSIRIS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | #169 | 
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Motion note](#motion-control) | 
[McLennan](http://www.mclennan.co.uk/) | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#note-mclennan)
[Pfeiffer](https://www.pfeiffer-vacuum.com/en/products/) | TPG 300 | ISIS Vacuum System | RS232 | #216 | [see Pfeiffer note](#note-pfeiffer)
Oxford Instruments | Triton | Cryogen-Free Dilution Fridge | Ethernet | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | 7.5T Magnet | Superconducting Magnet | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Variox | (Blue) Cryostat | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
[LakeShore](http://www.lakeshore.com/Pages/Home.aspx) | 218 | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#note-lakeshore)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#note-neocera)
ISIS | CryoValve Controller | All models at ISIS | RS-232 | | [see CryoValve Controller note](#note-cryovalve-controller)

##### Note: DAE #####
Main Detector banks + 2-3 monitors.

##### Note: Pfeiffer #####
Two controllers each with four active channels.
1. [Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407)
1. TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

##### Note: McLennan #####
1. Controls Rotating centre-stick, McLennan-Newport Rotation Stage
1. Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.

##### Note: Oxford Instruments #####
1. Dilution fridge: Triton.
   * See [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
1. 7.5T [Cryomagnet](https://www.isis.stfc.ac.uk/Pages/75T-Magnet.aspx) (aka the Teslatron)
   * See [#2593](https://github.com/ISISComputingGroup/IBEX/issues/2593)
1. [Variox Cryostat](https://www.isis.stfc.ac.uk/Pages/Oxford-Variox-Cryostats.aspx) (OXF-08)
   * See [#1389](https://github.com/ISISComputingGroup/IBEX/issues/1389), [#1390](https://github.com/ISISComputingGroup/IBEX/issues/1390), [#1391](https://github.com/ISISComputingGroup/IBEX/issues/1391)

##### Note: Eurotherm #####
Used to control temperature of top-loading CCRs, Furnace, Orange Cryostat devices.
OSIRIS has 3 Eurotherm devices, arranged in a single crate, as illustrated in the photograph of the [Eurotherm Crate](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/OSIRIS/OSIRIS_3x_Eurotherm.jpg).

##### Note: LakeShore #####
Three model 218 temperature controllers in total, each with 8 active channels.  Two monitor the temperature of the Analyser and one the beryllium filter.
1. [Model 218](http://www.lakeshore.com/products/Cryogenic-Temperature-Monitors/Model-218/Pages/Overview.aspx).  The [3 LakeShore devices](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/OSIRIS/OSIRIS_3x_LakeShore_218.jpg), are mounted in the OSIRIS rack.

##### Note: Neocera #####
1. [Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)
1. See also [#1828](https://github.com/ISISComputingGroup/IBEX/issues/1828)

##### Note: CryoValve Controller #####
1. Implemented on IRIS - see [#1405](https://github.com/ISISComputingGroup/IBEX/issues/1405).  The [CryoValve Controller](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/OSIRIS/OSIRIS_CryoValve.jpg) sits on the OSIRIS rack.

## OSIRIS Notes ##
#### Specialist Panels/Systems ####
OSIRIS has the following specialist panels/systems:
1. IRIS CryoValve
   * see [CryoValve Controller note](#note-cryovalve-controller)

#### Motion Control ####
OSIRIS has the following devices under motion control:
1. Jaws
   * 2-axis, North and South blades only.  I.e. only vertical gap and centre can be controlled.
1. Beryllium Filter
   * single axis, "IN/OUT" device moving between two setpoints.
1. Sample Changer
   * **N.B.**  For the avoidance of doubt: OSIRIS does not currently (September 2018) have a sample changer.  There have been discussions about building one but, for the foreseeable future, there is no sample changer.

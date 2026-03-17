# TOSCA

```{include} migration_notes_warning.mdinc
```

This page collects information that will be useful for the implementation of the IBEX control system on TOSCA.
## Background & Timeline ##
TOSCA is an indirect geometry spectrometer, on TS1. The [TOSCA](https://www.isis.stfc.ac.uk/Pages/TOSCA.aspx) web page describes the background to the instrument.

## TOSCA Equipment ##
The equipment listed below is used on TOSCA. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#tosca_noteDAE)
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | [#169](https://github.com/ISISComputingGroup/IBEX/issues/169) | [see Mk3 Chopper note](#tosca_noteMk3Chopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#tosca_noteMcLennan)
ISIS| | Sample Positioner | via McLennan | | [see Sample Positioner note](#tosca_noteSamplePositioner)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#tosca_noteVacuum)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#tosca_noteVacuum)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#tosca_noteEurotherm)
MKS | PDR2000 | Pressure Transducer | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#MKS) | 
LakeShore | 218 | Temperature Monitor | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore)| [see LakeShore note](#tosca_noteLakeshore )
ISIS | TOSCA | Helium Gauge |  |  |[see Helium Gauge note](#tosca_noteHeliumGauge)

{#tosca_noteDAE}
##### Note: DAE #####
See multi-detector and single-detector below.

{#tosca_noteMk3Chopper}
##### Note: ISIS Mk3 Choppers #####
TOSCA has an ISIS Mk3 double-disk chopper.

{#tosca_noteMcLennan}
##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets. 

As of 2018-11-15, TOSCA uses only one McLennan motor, which is for the sample changer. The other motors were used for a rotating centre stick and for a rotating stage - both of these were used once a long time ago. The McLennan which drove the rotating centre stick was configured during the migration and then removed after migrating as the scientists do not use it. If it is needed in the future, look at the standard configuration before 2018-11-14 to see details of the motor configuration for the rotating centre stick.

{#tosca_noteSamplePositioner}
##### Note: Sample Positioner #####
The Sample Positioner is driven by a McLennan motor (i.e. it raises/lowers sample plates attached to a chain drive, driven by the McLennan).  Here are 3 photograph of the Sample Positioner: [One](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/TOSCA/TOSCA_Sample_Changer_1.jpg), [Two](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/TOSCA/TOSCA_Sample_Changer_2.jpg), [Three](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/TOSCA/TOSCA_Sample_Changer_3.jpg).

{#tosca_noteJaws}
##### Note: Jaws #####
There are no jaws on TOSCA.

{#tosca_noteVacuum}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063). The vacuum system is currently operated separately.

{#tosca_noteEurotherm}
##### Note: Eurotherm #####
Eurotherms are used to control temperature Orange Cryostat, CCR and Furnace devices.

{#tosca_noteLakeshore}
##### Note: LakeShore #####

TOSCA uses four Lakeshore 218s - not all of the channels are enabled on each of these.

1. [Model 218](http://www.lakeshore.com/products/Cryogenic-Temperature-Monitors/Model-218/Pages/Overview.aspx)
   * See also [#1097](https://github.com/ISISComputingGroup/IBEX/issues/1097), [#1098](https://github.com/ISISComputingGroup/IBEX/issues/1098) & [#3223](https://github.com/ISISComputingGroup/IBEX/issues/3223).

There are [EPICS drivers](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) for a variety of Lakeshore temperature controllers.

{#tosca_noteHeliumGauge}
##### Note: Helium Gauge #####
1. The Helium Gauge is no longer used on TOSCA.

## TOSCA Notes ##
TOSCA has the following specialist panels/systems:
1. ~MAPS CCR (PM600)~
    * See [McLennan note](#tosca_noteMcLennan).
1. ~TOSCA Helium Level Gauge~
   * See [Helium Gauge](#tosca_noteHeliumGauge) note
1. TOSCA New Sample Changer (PM600)
1. ~Rotating Centre Stick (PM600)~
    * See [McLennan note](#tosca_noteMcLennan).

TOSCA has the following devices under motion control:
1. XY beam scanner (2 axis GALIL motor - this GALIL moves about and is not permanently on TOSCA).

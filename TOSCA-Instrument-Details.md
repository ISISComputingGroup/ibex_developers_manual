This page collects information that will be useful for the implementation of the IBEX control system on TOSCA.
## Background & Timeline ##
TOSCA is an indirect geometry spectrometer, on TS1. The [TOSCA](https://www.isis.stfc.ac.uk/Pages/TOSCA.aspx) web page describes the background to the instrument.

## Control System ##
TOSCA will migrate from the SECI control system to the IBEX control system in late October 2018 (prior to Cycle 2018/03).

## TOSCA Equipment ##
The equipment listed below is used on TOSCA. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | [#169](https://github.com/ISISComputingGroup/IBEX/issues/169) | [see Mk3 Chopper note](#noteMk3Chopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#noteMcLennan)
ISIS| | Sample Positioner | via McLennan | | [see Sample Positioner note](#noteSamplePositioner)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#noteVacuum)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#noteVacuum)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
MKS | PDR2000 | Pressure Transducer | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#MKS) | [see MKS  note](#noteMKS )
LakeShore | 218 | Temperature Monitor | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore)| [see LakeShore note](#noteLakeshore )
ISIS | TOSCA | Helium Gauge |  |  |[see Helium Gauge note](#noteHeliumGauge)

<a name="noteDAE"></a>
##### Note: DAE #####
See multi-detector and single-detector below.

<a name="noteMk3Chopper"></a>
##### Note: ISIS Mk3 Choppers #####
TOSCA has an ISIS Mk3 double-disk chopper.

<a name="noteMcLennan"></a>
##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets. 

As of 2018-11-15, TOSCA uses only one McLennan motor, which is for the sample changer. The other motors were used for a rotating centre stick and for a rotating stage - both of these were used once a long time ago. The McLennan which drove the rotating centre stick was configured during the migration and then removed after migrating as the scientists do not use it. If it is needed in the future, look at the standard configuration before 2018-11-14 to see details of the motor configuration for the rotating centre stick.

<a name="noteSamplePositioner"></a>
##### Note: Sample Positioner #####
The Sample Positioner is driven by a McLennan motor (i.e. it raises/lowers sample plates attached to a chain drive, driven by the McLennan).  Here are 3 photograph of the Sample Positioner: [One](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/TOSCA/TOSCA_Sample_Changer_1.jpg), [Two](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/TOSCA/TOSCA_Sample_Changer_2.jpg), [Three](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/TOSCA/TOSCA_Sample_Changer_3.jpg).

<a name="noteJaws"></a>
##### Note: Jaws #####
There are no jaws on TOSCA.

<a name="noteVacuum"></a>
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063). The vacuum system is currently operated separately.

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/TOSCA/TOSCA_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

<a name="noteLakeshore"></a>
##### Note: LakeShore #####

TOSCA uses four Lakeshore 218s - not all of the channels are enabled on each of these.

1. [Model 218](http://www.lakeshore.com/products/Cryogenic-Temperature-Monitors/Model-218/Pages/Overview.aspx)
   * See also [#1097](https://github.com/ISISComputingGroup/IBEX/issues/1097), [#1098](https://github.com/ISISComputingGroup/IBEX/issues/1098) & [#3223](https://github.com/ISISComputingGroup/IBEX/issues/3223).

There are [EPICS drivers](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) for a variety of Lakeshore temperature controllers.

<a name="noteHeliumGauge"></a>
##### Note: Helium Gauge #####
1. The Helium Gauge is no longer used on TOSCA.

## TOSCA Notes ##
TOSCA has the following specialist panels/systems:
1. ~MAPS CCR (PM600)~
    * See [McLennan note](#noteMcLennan).
1. ~TOSCA Helium Level Gauge~
   * See [Helium Gauge](#noteHeliumGauge) note
1. TOSCA New Sample Changer (PM600)
1. ~Rotating Centre Stick (PM600)~
    * See [McLennan note](#noteMcLennan).

TOSCA has the following devices under motion control:
1. XY beam scanner (2 axis GALIL motor - this GALIL moves about and is not permanently on TOSCA).

## TOSCA SECI Configs ##
Document information about TOSCA SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
Standard + Rotation Stage.conf               | -                                                  | 25/10/2018    | -        |

## TOSCA Genie Scripts ##
Similarly, Document information about TOSCA SECI Genie scripts here.

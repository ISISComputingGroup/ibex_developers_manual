# WISH

This page collects information that will be useful for the implementation of the IBEX control system on WISH.
## Background & Timeline ##
WISH is a long-wavelength diffractometer, on TS2. The [WISH](https://www.isis.stfc.ac.uk/Pages/WISH.aspx) web page describes the background to the instrument.

## Control System ##
WISH has migrated to IBEX from SECI

## WISH Equipment ##
The equipment listed below is used on WISH. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#wish_note-dAE)
ISIS | MK3 | Disk Chopper | Ethernet | EPICS | [see Disk Chopper note](#wish_note-disk-chopper) |
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#wish_note-mclennan)
??? |  | 4-blade jaws |  |  | [see Jaws note](#wish_note-jaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#wish_note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#wish_note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#wish_note-eurotherm)
LakeShore | 340 | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#wish_note-lakeshore)
LakeShore | 350 | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore)| [see LakeShore note](#wish_note-lakeshore)
LakeShore | 370 | Resistance Bridge | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore)| [see LakeShore note](#wish_note-lakeshore)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#wish_note-neocera)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#wish_note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#wish_note-oxford-instruments)
Oxford Instruments |  | Cryogenic Equipment | RS-232 | | [see Oxford Instruments note](#wish_note-oxford-instruments)
Oxford Instruments | Teslatron |  | RS-232 | | [see Oxford Instruments note](#wish_note-oxford-instruments)
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#wish_note-thurlby)
[Stanford RS](http://www.thinksrs.com/) | SR850 | Amplifier |  |  | [see Stanford RS note](#wish_note-stanfordrs)
Tektronix | AFG 3021B | Function Generator | Ethernet | #237 |[see Tektronix note](#wish_note-tektronix)
Keithley | 6517B | Electrometer | RS-232 | | [see Keithley note](#wish_note-keithley)
Razorbill | RP100 | Power Supply | RS-232 | |  [see Razorbill note](#wish_note-razorbill)

{#wish_note-dAE}
##### Note: DAE #####
See multi-detector and single-detector below.

{#wish_note-disk-chopper}
##### Note: WISH Disk Chopper #####
Disk Chopper is an ISIS MK3 chopper.

{#wish_note-mclennan}
##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.

##### Note: LinMot #####
[LinMot User Manual](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf)

{#wish_note-jaws}
##### Note: Jaws #####
Provide information about WISH jaws.

{#wish_note-vacuum-system}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

{#wish_note-eurotherm}
##### Note: Eurotherm #####
Eurotherms are used to control temperature Orange Cryostat, CCR and Furnace devices.

{#wish_note-lakeshore}
##### Note: LakeShore #####
1. [Model 340](http://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-340/Pages/Overview.aspx): this model is now obsolete, having been replaced by the 336 and 350 models.
1. [Model 350](http://www.lakeshore.com/products/Cryogenic-Temperature-Monitors/Model-350/Pages/Overview.aspx):
1. [Model 370](https://www.lakeshore.com/products/AC-Resistance-Bridges/Model-370/Pages/Overview.aspx): this model is now obsolete, having been replaced by the 372 model.

There are [EPICS drivers](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) for a variety of Lakeshore temperature controllers.

{#wish_note-neocera}
##### Note: Neocera #####
1. [Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)
1. See also [#1828](https://github.com/ISISComputingGroup/IBEX/issues/1828)

{#wish_note-oxford-instruments}
##### Note: Oxford Instruments #####
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
   * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
1. Blue Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Oxford-Variox-Cryostats.aspx) to be determined.
1. 7.5T [Cryomagnet](https://www.isis.stfc.ac.uk/Pages/75T-Magnet.aspx) (aka the Teslatron)
   * See [#2593](https://github.com/ISISComputingGroup/IBEX/issues/2593)
   * Can also be 9T (see LET) or 14T magnets.

{#wish_note-thurlby}
##### Note: Thurlby #####
[Thurlby Thandar Instruments](https://www.aimtti.com/)
1. [Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)
   * see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).

{#wish_note-tektronix}
##### Note: Tektronix #####
1. Tektronix Function Generator: [AFG 3021B](https://www.tek.com/datasheet/afg3000-series)
   * See also [#237](https://github.com/ISISComputingGroup/IBEX/issues/237)

{#wish_note-stanfordrs}
##### Note: Stanford RS #####
1. [SR850 lock-in amplifier](http://www.thinksrs.com/products/sr850.html)
1. There are existing [EPICS drivers](https://epics.anl.gov/modules/manufacturer.php#Stanford%20Research) for Stanford devices.

{#wish_note-keithley}
##### Note: Keithley #####
1. [Keithley 6500 Series Electrometers](https://uk.tek.com/keithley-low-level-sensitive-and-specialty-instruments/keithley-high-resistance-low-current-electrom).
   * [Keithley 6517B DataSheet](https://uk.tek.com/datasheet/high-resistance-low-current-electrometers-series-6500-6430/model-6517b-electrometer-high-r)
   * See also [Keithley 6517B Reference Manual](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?FolderCTID=0x0120005C4AD37BB338BE469E2247B9E5E1C301&id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FKeithley)
1. There are existing [EPICS drivers](https://epics-controls.org/resources-and-support/modules/hardware-support/) for similar Keithley devices (but not for model 6517B).

{#wish_note-razorbill}
##### Note: Razorbill #####
1. This is a small power supply controlling the WISH strain cell. 
   * [RP100 Manual](https://razorbillinstruments.com/wp-content/uploads/2018/10/RP100-Manual-v6.1-1.pdf)

## WISH Notes ##
WISH has the following specialist panels/systems:
1. Rotating CCR (PM600)
   * See `C:\LabVIEW Modules\Rotating CCR\Rotating CCR - Front Panel.vi`
1. GEM Beamline Jaws (PM341)
   * check existing VI on WISH (GEM has been upgraded since original system was written)
   * PM341 is a McLennan model
   * Instrument scientist is not sure why GEM VIs are installed on WISH (they may not actually be used).
1. GEM Jaws (Linmot)
   * check existing VI on WISH (GEM has been upgraded since original system was written)
   * Instrument scientist is not sure why GEM VIs are installed on WISH (they may not actually be used).
1. GEM ORC
   * check existing VI on WISH (GEM has been upgraded since original system was written)
   * See also [#2409](https://github.com/ISISComputingGroup/IBEX/issues/2409) and [#2808](https://github.com/ISISComputingGroup/IBEX/issues/2808)
   * WISH does have an ORC.  Need to check if it the same as the GEM ORC.
1. MAPS CCR (PM600)
   * See `C:\LabVIEW Modules\Instruments\MAPS\MAPS CCR\MAPS CCR - Front Panel.vi`
1. PEARL Pressure Transducer
   * See `C:\LabVIEW Modules\Instruments\PEARL\PEARL Pressure Transducer\PEARL Pressure Transducer.vi`
1. PEARL Pressure Cell Controller
   * See `C:\LabVIEW Modules\Instruments\PEARL\PEARL Pressure Cell Controller\PEARL Pressure Cell Controller - Front Panel.vi`
1. POLARIS Sample Changer
   * See [#2173](https://github.com/ISISComputingGroup/IBEX/issues/2173)
   * See also `C:\LabVIEW Modules\Instruments\POLARIS\POLARIS Sample Changer\POLARIS SC - Front Panel.vi`
1. WISH Jaws
1. WISH Lakeshore 370
1. WISH Oscillating Radial Collimator (Galil) - see [here](/specific_iocs/motor_extensions/MERLIN,-LET-and-WISH-Oscillating-radial-collimators) for more info
1. WISH Vacuum PLC

WISH has the following devices under motion control:
1. jaws
1. XYZ stage
   * This is also referred to as/is controlling the "Alignment Flange"


WISH also tends to borrow things from other instruments. Commonly used equipment:

1. PEARL pressure controller
1. Mercury-controlled Heliox cryostat insert
1. Blue Cryostat (ITC controlled) 
1. IRIS Baratron Gas cell 
1. Automatic needle valve - see note on [ticket #6695](https://github.com/ISISComputingGroup/IBEX/issues/6695) for investigation, [ticket #4240](https://github.com/ISISComputingGroup/IBEX/issues/4240) for IOC implementation and [ticket #6777](https://github.com/ISISComputingGroup/IBEX/issues/6777) for OPI. 

## WISH SECI Configs ##
Document information about WISH SECI configs here.

Note: Most of WISH configs revolve around the WISH base config. This has been created as a component in IBEX and subsequent components for each thing that is added to the WISH base config should be added as components (i.e. the Teslatron, Strain Cell, Rotation stages etc.) 

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
WISH_base.conf                | WISH_base.comp                                                 | 01/07/2021    | -        |
WISH_base + Oxford Cryostat.conf                | WISH_base.comp,     Oxford - teslatron.comp                                              | ""    | -        |

## WISH Genie Scripts ##
Similarly, Document information about WISH SECI Genie scripts here.

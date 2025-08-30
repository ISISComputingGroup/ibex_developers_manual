# LET

This page collects information that will be useful for the implementation of the IBEX control system on LET.

## Background & Timeline ##
LET is a cold neutron multi-chopper spectrometer on TS2 at ISIS. The [LET](http://www.isis.stfc.ac.uk/instruments/let/let6414.html) web page describes the background to the instrument.

## Control System ##
It is proposed to migrate from the SECI control system to the IBEX control system in time for Cycle 2018/04.
LET does currently use IBEX to control its SKF choppers (but that's all).

## LET Equipment ##
The equipment listed below is used on LET. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
SKF | MB4150-G5 | Disk Chopper | Ethernet |  | [see High-Speed SKF Disk Chopper note](#note-high-speed-skf-disk-chopper) |
ISIS | Mk3 | Disk Chopper | Ethernet | .NET | [see ISIS Chopper note](#note-isis-disk-chopper) |
N/A | N/A | Jaws |  |  | [see Jaws note](#note-jaws)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) |[see Pfeiffer note](#note-pfeiffer)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
ISIS | Orange Cryostat | Cryogenic System | RS-232 | | [see Orange Cryostat note](#note-orange-cryostat)
Oxford Instruments | Heliox | Dilution Fridge | RS-232 | [#3739](https://github.com/ISISComputingGroup/IBEX/issues/3739) | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | [#2744](https://github.com/ISISComputingGroup/IBEX/issues/2744) | [see Oxford Instruments note](#note-oxford-instruments)
ISIS | ??? | Mezei Flipper | | [#3738](https://github.com/ISISComputingGroup/IBEX/issues/3738) | [see Mezei Flipper Notes](#note-mezei-neutron-spin-flipper)
ISIS | Furnace | High temperature furnace | RS-232 | | [see Furnace note](#note-isis-high-temperature-furnace)
Oxford Instruments | 9T | Magnet | ??? | [#2765](https://github.com/ISISComputingGroup/IBEX/issues/2765) | [see 9T Magnet note](#note-isis-9t-chopper-magnet)
Oxford Instruments | 14T | Magnet | ??? | | [see 14T Magnet note](#note-isis-14t-magnet)
[Lakeshore](http://www.lakeshore.com/Pages/Home.aspx) | 340 | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see Lakeshore note](#note-lakeshore)
ISIS | ORC | Collimator | via Galil | [#2535](https://github.com/ISISComputingGroup/IBEX/issues/2535) | [see LET Notes](#let-notes)
ISIS | McLennan | Sample Changer | via Galil | | [see LET Notes](#let-notes)
ISIS | McLennan | Rotation Stage | via McLennan | | [see LET Notes](#let-notes)
ISIS | McLennan-Newport | Rotation Stage | via McLennan | | [see LET Notes](#let-notes)

##### Note: DAE #####
Main Detector banks + several fixed monitors.

##### Note: High-Speed SKF Disk Chopper #####
LET currently has 2 high-speed SKF choppers (same as IMAT).  These are currently controlled using a mini-IBEX system.
1. SKF G5 choppers also used on IMAT (see [#1907](https://github.com/ISISComputingGroup/IBEX/issues/1907)).
   * [SKF MB4150-G5 Chopper](http://www.skf.com/uk/products/magnetic-systems/magnetic-systems-applications/neutron-chopper-instrumentation/index.html)
   * [MBScope](http://www.skf.com/uk/products/magnetic-systems/software-downloads/MBScope-Beamline-software.html) software for SKF magnetic bearing choppers.

##### Note: ISIS Disk Chopper #####
LET currently has 1 Mk3 ISIS chopper.

##### Note: Jaws #####
LET has no jaws.

##### Note: Pfeiffer #####
[Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407), used for vacuum system read-back.

##### Note: Eurotherm #####
Eurotherms in use on LET.  Used to control temperature of all top-loading CCRs, Orange cryostats, heaters and furnaces.

##### Note: Lakeshore #####
<br> **NOTE:** this entry added 07-02-2019. <br>
LET uses a Lakeshore Model 340 cryogenic temperature controller.
1. [Model 340](https://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-340/Pages/Overview.aspx).
   * According to the Lakeshore web-site, the Model 340 is now obsolete.  It has been replaced by the models 336 and 350.

##### Note: Orange Cryostat #####
Controlled via Eurotherm.

##### Note: Oxford Instruments #####
1. Dilution fridges: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx).  LET uses both Triton and Heliox dilution fridges
   * Triton
      * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
      * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
      * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
   * Heliox
      * The Heliox dilution fridge is currently (November 2018) broken and is being repaired at Oxford Instruments.  There is no ETA on when it will be fixed.  There are no experiments scheduled to use the Heliox dilution fridge.  Obviously, that will change when the Heliox is repaired.

##### Note: ISIS 9T Chopper Magnet #####
[ISIS 9T Chopper Magnet](https://www.isis.stfc.ac.uk/Pages/9T-chopper-magnet.aspx) 
See also:[IBEX Support for 9T chopper magnet](/specific_iocs/Cryogenics).

##### Note: ISIS 14T Magnet #####
LET has, in the past, used the [ISIS 14T Magnet](https://www.isis.stfc.ac.uk/Pages/14T-Diffraction-Magnet.aspx).  This magnet is currently being repaired and there is no ETA on when it might return to service.

##### Note: Mezei Neutron Spin Flipper #####
The Mezei Neutron Spin Flipper is a collection of devices (power supplies, signal generators & control PC) housed in a mobile rack. The control PC runs a Python script to control the power supplies & signal generators. The Python script accepts a set of simple commands.  The Mezei Neutron Spin Flipper is, at the time of writing, used on LET and POLREF.  In future, it may be used on other instruments too.

There is a VI to control the PSU, located here: `C:\LabVIEW Modules\Instruments\POLREF\POLREF Flipper`.  It was originally developed by Gareth Howells, but has subsequently been modified by students.  Consult with Goran Nilsson & Andrew Caruana for more details.

**N.B.:** LET plans to use this device in Cycle 2018/04.

##### Note: ISIS High temperature furnace #####
Controlled via Eurotherm.  Furnaces are used only very rarely on LET.

## LET Notes ##
LET has the following specialist systems:
1. LET specific oscillating radial collimator.  Controlled by special program downloaded into Galil.
   1. See [2535](https://github.com/ISISComputingGroup/IBEX/issues/2535)
1. LET sample changer
   * A sample changer has not often been used on LET.  From Cycle 2018/04 LET will be using a sample changer of the same design as the MERLIN sample changer (the two devices should be interchangeable).
1. LET rotation stage
   * LET has two rotation stages;
   1. A McLennan rotation stage (same as MERLIN, used with CCRs & Orange Cryostats))
   1. A McLennan-Newport rotation stage (used with the 9T Magnet)

## LET SECI Configs ##
LET has a number of SECI configurations.  Equivalent IBEX configs for the following combinations of equipment are required:
   * Eurotherm (for Cryostat or CCR) + rotation stage
   * Eurotherm (for Cryostat or CCR) + ORC + rotation stage
   * Eurotherm (for Cryostat or CCR) + dilution fridge (Triton) + rotation stage
   * Eurotherm (for Cryostat or CCR) + dilution fridge (Triton)+ ORC + rotation stage
   * Eurotherm (for Cryostat or CCR) + dilution fridge (Heliox) + rotation stage
   * Eurotherm (for Cryostat or CCR) + dilution fridge (Heliox)+ ORC + rotation stage
   * 9T Magnet + McLennan-Newport rotation stage

## LET Genie Scripts ##
LET has a number of instrument specific Genie scripts. The key scripts to be migrated to genie_python are:

Script| Purpose | Notes | 
------------ | ------------- | -------------------------------------------
`park_choppers`| It parks the choppers, of course | Needed because LET has 4 choppers
`set_ei5` | Sets chopper speed/phase | This is the LET version of `set_ei`.  It is **not** the same as `set_ei` used on other excitations instruments.  It would be helpful if `set_ei5` could be extended to better support vetoes and wiring tables.  Ignore the older versions `set_ei1` - `set_ei4`.
`mono` | | 

On LET user scripts are usually created by modifying an old user script.  Create a template genie_python script (based on an old user script) which can be used in future.


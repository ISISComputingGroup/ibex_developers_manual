This page collects information that will be useful for the implementation of the IBEX control system on MUSR.
## Background & Timeline ##
MUSR is a general purpose muon spin rotation spectrometer at ISIS, on TS1. However, the emphasis of the experimental work conducted is investigating magnetism and superconductivity.  The [MUSR](https://www.isis.stfc.ac.uk/Pages/MUSR.aspx) web page describes the background to the instrument.

## Control System ##
MUSR will migrate from the SECI control system to the IBEX control system in MMMMMMMM YYYY.

## MUSR Equipment ##
The equipment listed below is used on MUSR. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see motion note](#note-motion)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
ICE | ICECube Dilution Fridge | Oxford ICE Cube | RS-232 | | [see Oxford ICE Cube note](#note-Oxford-ICE-Cube)
[CAEN](http://www.caen.it/csite/HomePage.jsp) | V895 | Discriminator | ??? | |[see CAEN note](#note-cAEN)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Heliox | He3 Refrigerator |  | | [see Oxford Instruments note](#note-oxford-instruments)
Lakeshore | 372 | Temperature Controller |   |  | [see Lakeshore note](#note-lakeshore)
LakeShore | 340 | | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#note-lakeshore )
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#note-thurlby)
Danfysik | 8000 | PSU | RS232 | DFKPS | [see Danfysik note](#note-danfysik)
~Gossen~ | ~64D 42P~ | ~PSU~ | ~???~ | | [see Gossen note](#note-gossen)
MetroLab | PT2025 | Teslameter | ??? | | [see MetroLab note](#note-metrolab)

<a name="noteDAE"></a>
##### Note: DAE #####
See multi-detector and single-detector below.

<a name="noteMotion"></a>
##### Note: Motion #####
There is a project relating to the motion on the South Side Muons in progress, this information may be out of date

##### Note: Choppers #####
MUSR does not have a chopper.

##### Note: Jaws #####
Provide information about MUSR jaws.

##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/MUSR/EMU_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

##### Note: Oxford ICE Cube #####
1. The ICE Fridge is a dilution fridge.  
   1. **N.B.** It is **not** an Oxford Instruments device.  It is from a different manufacturer.  
   1. It cannot be compared to other models of dilution fridge.
1. The ICE control PC is referred to as an ICECube.
   1. This PC runs Windows XP.  It should not be connected to the ISIS network. 
   1. Communication with the equipment is via serial and a MOXA unit.
1. The dilution fridge temperature at low temperatures is controlled via a Lakeshore 370.
1. There is only one ICE dilution fridge which is used on MUSR mainly. It is available for EMU.
1. See ticket [#3876](https://github.com/ISISComputingGroup/IBEX/issues/3876)

Documentation can be found at : `C:\LabVIEW Modules\Drivers\ICEOxford\ICECube\Documentation`
LabVIEW client can be found at : `C:\LabVIEW Modules\Drivers\ICEOxford\ICECube\ICECube - Client.llb\ICECube - Client.vi`

##### Note: CAEN #####
The [CAEN V895](http://www.caen.it/csite/CaenProd.jsp?parent=11&idmod=49) is a 16-channel Leading Edge Discriminator.

##### Note: Oxford Instruments #####
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
   * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
1. Support for Mercury Temperature Controller was created as part of [#2840](https://github.com/ISISComputingGroup/IBEX/issues/2840)
1. Heliox devices are [He3 Sorption Refrigerators](https://nanoscience.oxinst.com/products/helium3-refrigerators/).  See [#3739](https://github.com/ISISComputingGroup/IBEX/issues/3739) and [#4549](https://github.com/ISISComputingGroup/IBEX/issues/4549).

##### Note: LakeShore #####
1. [Model 340](http://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-340/Pages/Overview.aspx): this model is now obsolete, having been replaced by the 336 and 350 models.
1. On muon instruments, the Triton fridges have an additional Lakeshore controller (the 372) to allow control and continuous readout of the sample temperature (the OI software doesn’t allow this using the in-built Lakeshore, despite the unit having a dedicated channel for the sample thermometry). 
1. [Model 372](https://www.lakeshore.com/products/categories/overview/temperature-products/ac-resistance-bridges/model-372-ac-resistance-bridge-temperature-controller) temperature controller.
1. There are [EPICS drivers](https://epics-controls.org/resources-and-support/modules/hardware-support/) for a variety of Lakeshore temperature controllers.

##### Note: Thurlby #####
1. Thurlby EX355P PSU - see [#3784](https://github.com/ISISComputingGroup/IBEX/issues/3784)
1. [Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)

##### Note: Danfysik #####
Need to check if MUSR does use Danfysik 8000 or a different model of PSU.
1. [Danfysik Power Supplies](http://www.danfysik.com/en/products/power-supplies/): model 8000 appears to have been superseded by model 8500.
1. [User and Software Manuals](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPower%20Supplies&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence) for System 8500.
1. See [#1208](https://github.com/ISISComputingGroup/IBEX/issues/1208) for comms settings.

##### Note: Gossen #####
1. ~[Gossen 64D 42P PSU](https://www.sagatron-shop.de/Gossen-Metrawatt/Laboratory-power-supply/MSP-64D-KONSTANTER/GOSSEN-MSP-64D-Lab-Power-Supply.html)~
1. Gossen PSU is no longer used on MuSR (superseded by [Thurlby](#noteThurlby))

##### Note: MetroLab #####
1. [MetroLab PT2025](https://www.metrolab.com/products/pt2025/)


## MUSR Notes ##
MUSR has the following specialist panels:
1. MUON Front End Magnet Monitoring (IOC)
1. MUON Front End Control (IOC)
1. MUSR Field Viewer (IOC)
1. MUSR Lakeshore 340 (Custom Panel)
   * See [see Lakeshore note](#noteLakeshore).  Check functionality against existing MUSR VI.
1. MUSR MUON Jaws (IOC)
1. MUSR CAEN (IOC)
   * See [see CAEN note](#noteCAEN).  Check functionality against existing MUSR VI.
1. MUSR Transverse Field (TTI EX355P or ~Gossen 64D 42P PSU~)
   * See [see Thurlby note](#noteThurlby).  Check functionality against existing MUSR VI.
   * ~See [see Gossen note](#noteGossen).  Check functionality against existing MUSR VI.~
1. HIFI MetroLab PT2025
   * See [see MetroLab note](#noteMetroLab).  Check functionality against existing MUSR VI.
1. MUON Magnets - Danfysik
   * See [see Danfysik note](#noteDanfysik).  Check functionality against existing MUSR VI.
1. MUON Magnets - [MUON Rotation Control](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/MuSR-Rotation-control)
1. MUON Magnets - [Zero Field Controller](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Zero-field-controller)
1. ~MUON TRMC2~ (TRMC2 is obsolete, no longer used)
1. MUSR Steering - [Muon Steering magnets](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/MuSR-Steering-Magnets)

MUSR has the following motion control items:
1. ~sample changer (2-axis)~ not needed (configuration item probably accidentally copied from another instrument)
1. ~transmission monitor~ not needed (configuration item probably accidentally copied from another instrument)

MUSR also has the following system:
1. MUON Script Generator (muongui.exe)

## MUSR SECI Configs ##
Document information about MUSR SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
EMU_place_holder1.conf                 | -                                                  | dd/mm/yyyy    | -        |
EMU_place_holder2.conf                 | -                                                  | dd/mm/yyyy    | -        |

## MUSR Genie Scripts ##
Similarly, Document information about MUSR SECI Genie scripts here.

## MUSR configs from EMU 
Configurations have been removed that were migrated from SECI + EMU as they are being phased out or have not been in use. Commit `63303d94400cd0270b3c07357a08cbdf5945d8e8` should still contain the configurations before removal. 
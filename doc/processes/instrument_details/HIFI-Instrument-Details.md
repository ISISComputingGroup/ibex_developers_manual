# HIFI

This page collects information that will be useful for the implementation of the IBEX control system on HIFI.
## Background & Timeline ##
HIFI is high magnetic-field muon instrument at ISIS, on TS1. The [HIFI](https://www.isis.stfc.ac.uk/Pages/HIFI.aspx) web page describes the background to the instrument.

## Control System ##
HIFI will migrate from the SECI control system to the IBEX control system in MMMMMMMM YYYY.

## HIFI Equipment ##
The equipment listed below is used on HIFI. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#hifi_note-dae)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see motion note](#hifi_note-motion)
??? |  | 4-blade jaws |  |  | [see Jaws note](#hifi_note-jaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#hifi_note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#hifi_note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#hifi_note-eurotherm)
Aeroflex/IFR | 2030 | Signal Generator | RS-232 | | [see Aeroflex note](#hifi_note-aeroflex)
Julabo | FP-50 | Water Bath | RS-232 | | [see Water Bath note](#hifi_note-water-baths)
Julabo | FP-52 | Water Bath | RS-232 | | [see Water Bath note](#hifi_note-water-baths)
~Haake~ | ~N6~ | ~Water Bath~ | ~RS-232~ | | [see Water Bath note](#hifi_note-water-baths)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#hifi_note-neocera)
ICE |  | Oxford ICE Cube | ??? | | [see Oxford ICE Cube note](#hifi_note-oxford-ice-cube)
[CAEN](http://www.caen.it/csite/HomePage.jsp) | V895 | Discriminator | ??? | |[see CAEN note](#hifi_note-caen)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#hifi_note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#hifi_note-oxford-instruments)
Oxford Instruments |  | Cryogenic Equipment | RS-232 | | [see Oxford Instruments note](#hifi_note-oxford-instruments)
LakeShore | 218 | | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore)| [see LakeShore note](#hifi_note-lakeshore )
LakeShore | 340 | | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#hifi_note-lakeshore )
Lakeshore | 372 | Temperature Controller |   |  | [see Lakeshore note](#hifi_note-lakeshore )
Metrolab | PT2025 | Teslameter |  | | [see Metrolab note](#hifi_note-metrolab)

{#hifi_note-dae}
##### Note: DAE #####
See multi-detector and single-detector below.

{#hifi_note-motion}
##### Note: Motion #####
There is a project relating to the motion on the South Side Muons in progress, this information may be out of date

{#hifi_note-jaws}
##### Note: Jaws #####
Provide information about HIFI jaws.

{#hifi_note-vacuum}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

{#hifi_note-eurotherm}
##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/HIFI/HIFI_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

{#hifi_note-aeroflex}
##### Note: Aeroflex/IFR #####
Aeroflex has been through a complicated series of sales in recent years.  The [Aeroflex manuals](https://www.avionteq.com/document/IFR-2030-opt-006-specification-sheet.pdf) are probably a good place to start, along with any existing VIs.  See also [IFR 2023A](https://www.atecorp.com/products/ifr/2023a).

There appears to be no driver for the Aeroflex 2023A in `C:\LabVIEW Modules\`. However, there is a driver for an Aeroflex 2030 in `C:\LabVIEW Modules\Drivers\Aeroflex 2030`.

{#hifi_note-water-baths}
##### Note: Water Baths #####
1. Julabo Water Bath
   * no information on specific Julabo Water Baths - maybe HIFI uses water baths from the pool?
   * consult the [Julabo commands](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/backend_system/IOCs/julabo_commands.xlsx) spreadsheet for specific details of which set of commands are used individual water baths.
1. Haake Water Bath is now obsolete (replaced by Julabo, according to instrument scientist)
   * ~Haake Water Bath (apparently the following Haake water bath: WB9)~
   * ~Haake N6 Water Bath.  Haake has now been taken over by [ThermoFisher](https://www.thermofisher.com/uk/en/home/life-science/lab-equipment/water-baths-circulators-chillers.html).  N6 model may be obsolete.  Check existing SECI VI for logic and manual (see `C:\LabVIEW Modules\Drivers\Haake N6`).~
1. See also [Water Baths](https://www.isis.stfc.ac.uk/Pages/Water-Baths.aspx) list

{#hifi_note-neocera}
##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

{#hifi_note-oxford-ice-cube}
##### Note: Oxford ICE Cube #####
What is the Oxford ICE Cube?  LabVIEW drivers are located here: `C:\LabVIEW Modules\Drivers\ICEOxford`

{#hifi_note-caen}
##### Note: CAEN #####
The [CAEN V895](http://www.caen.it/csite/CaenProd.jsp?parent=11&idmod=49) is a 16-channel Leading Edge Discriminator.
See also `C:\LabVIEW Modules\Drivers\Caen`.

{#hifi_note-oxford-instruments}
##### Note: Oxford Instruments #####
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
   * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
1. Blue Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Oxford-Variox-Cryostats.aspx) to be determined.

{#hifi_note-lakeshore}
##### Note: LakeShore #####
1. [Model 218](http://www.lakeshore.com/products/Cryogenic-Temperature-Monitors/Model-218/Pages/Overview.aspx):
1. [Model 336](http://www.lakeshore.com/products/cryogenic-temperature-controllers/model-336/Pages/Overview.aspx):
1. [Model 340](http://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-340/Pages/Overview.aspx): this model is now obsolete, having been replaced by the 336 and 350 models.
1. On muon instruments, the Triton fridges have an additional Lakeshore controller (the 372) to allow control and continuous readout of the sample temperature (the OI software doesn’t allow this using the in-built Lakeshore, despite the unit having a dedicated channel for the sample thermometry). 
1. [Model 372](https://www.lakeshore.com/products/categories/overview/temperature-products/ac-resistance-bridges/model-372-ac-resistance-bridge-temperature-controller) temperature controller.
1. There are [EPICS drivers](https://epics-controls.org/resources-and-support/modules/hardware-support/) for a variety of Lakeshore temperature controllers.

{#hifi_note-metrolab}
##### Note: Metrolab #####
1. [PT2025 NMR Precision Teslameter](https://www.metrolab.com/products/pt2025/)
   * The PT2025 is now obsolete. Replaced by model PT2026.
   * See `C:\LabVIEW Modules\Instruments\HIFI\Metrolab PT2025 NMR` for SECI VI
   * See `\\isis\shares\ISIS_Experiment_Controls\Metrolab PT2025 Teslameter` for the technical manual.


## HIFI SECI Configs ##
Document information about HIFI SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
HIFI_place_holder1.conf             | -                                                  | dd/mm/yyyy    | -        |
HIFI_place_holder2.conf             | -                                                  | dd/mm/yyyy    | -        |

## HIFI Genie Scripts ##
Similarly, Document information about HIFI SECI Genie scripts here.

## HIFI Notes ##
HIFI has the following specialist panels:
1. MUSR RF Kit
1. EMU MUON FrontEnd
1. HIFI CryoMag Client
1. HIFI Group 3 Hall Probe
1. HIFI Field Viewer
1. HIFI Laser Power
1. HIFI Laser Timing
1. HIFI Laser Client
1. HIFI Magnets
1. HIFI Metrolab PT2025 (NMR Readout)
1. MUON FrontEnd Magnet Monitoring
1. MUON Jaws

HIFI also has the following system:
1. MUON Script (generator)
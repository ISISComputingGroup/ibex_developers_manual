# ARGUS

This page collects information that will be useful for the implementation of the IBEX control system on ARGUS.

## Background & Timeline ##
ARGUS is a general purpose muon spectrometer at ISIS, on TS1. The [ARGUS](https://www.isis.stfc.ac.uk/Pages/argus.aspx) web page describes the background to the instrument.

## ARGUS Equipment ##
The equipment listed below is used on ARGUS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#argus_note-dae)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#argus_note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#argus_note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#argus_note-eurotherm)
Julabo | FP-50 | Water Bath | RS-232 | | [see Water Bath note](#argus_note-water-baths)
Julabo | FP-52 | Water Bath | RS-232 | | [see Water Bath note](#argus_note-water-baths)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#argus_note-kepco)
Kepco | BIT 4886 | I/F card | GPIB, RS-232 | | [see Kepco note](#argus_note-kepco)
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#argus_note-thurlby)
Danfysik | 8000 | PSU | RS232 | DFKPS | [see Danfysik note](#argus_note-danfysik)
TDK | Lambda Genesys | PSU | RS232 | TDK_ LAMBDA_ GENESYS | [see Genesys note](#argus_note-genesys) |
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#argus_note-neocera)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#argus_note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#argus_note-oxford-instruments)
Oxford Instruments |  | Cryogenic Equipment | RS-232 | | [see Oxford Instruments note](#argus_note-oxford-instruments)
LakeShore | 332 | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#argus_note-lakeshore )
Lakeshore | 372 | Temperature Controller |   |  | [see Lakeshore note](#argus_note-lakeshore )
LakeShore | 460 | Gaussmeter | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#argus_note-lakeshore )
Cryomagnetics | LM500| Liquid Cryogen Level Monitor | RS-232 | | [see Cryomagnetics note](#argus_note-cryomagnetics)
Leiden Cryogenics| GHS-2T-1T-700 | Dilution Fridge| | | [see Leiden Cryogenics note](#argus_note-leiden-cryogenics)

{#argus_note-dae}
##### Note: DAE #####
See multi-detector and single-detector below.

{#argus_note-vacuum-system}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

{#argus_note-eurotherm}
##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ARGUS/ARGUS_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

{#argus_note-water-baths}
##### Note: Water Baths #####
1. Julabo Water Bath
   * no information on specific Julabo Water Baths - maybe ARGUS uses water baths from the pool?
   * consult the [Julabo commands](/specific_iocs/temp_controllers/julabo_commands.xlsx) spreadsheet for specific details of which set of commands are used individual water baths.
1. See also [Water Baths](https://www.isis.stfc.ac.uk/Pages/Water-Baths.aspx) list

{#argus_note-kepco}
##### Note: Kepco #####
1. [Kepco BIT 4886](http://www.kepcopower.com/bit.htm) is an interface card for Kepco bi-polar ([BOP](http://www.kepcopower.com/bop.htm)) power supplies.  See also `C:\LabVIEW Modules\Drivers\Kepco 4886 Serial`
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).<br>  See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)

{#argus_note-thurlby}
##### Note: Thurlby #####
Thurlby EX355P PSU - see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).

[Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)

{#argus_note-danfysik}
##### Note: Danfysik #####
1. [Danfysik Power Supplies](http://www.danfysik.com/en/products/power-supplies/): model 8000 appears to have been superseded by model 8500.
1. [User and Software Manuals](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPower%20Supplies&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence) for System 8500.
1. See [#1208](https://github.com/ISISComputingGroup/IBEX/issues/1208) for comms settings.

{#argus_note-genesys}
##### Note: Genesys #####
1. [TDK Lambda Genesys Power Supplies](https://uk.tdk-lambda.com/products/programmable-power-supplies/).
1. [Safety, User and Programming Manuals](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPower%20Supplies&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence) for System 8500.
1. See also [#983](https://github.com/ISISComputingGroup/IBEX/issues/983), [#2276](https://github.com/ISISComputingGroup/IBEX/issues/2276), [#2458](https://github.com/ISISComputingGroup/IBEX/issues/2458)

{#argus_note-neocera}
##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

{#argus_note-oxford-instruments}
##### Note: Oxford Instruments #####
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : `C:\LabVIEW Modules\Drivers\Triton`
   * Triton Documentation : `C:\LabVIEW Modules\Drivers\Triton\Documentation`
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
1. Blue Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Oxford-Variox-Cryostats.aspx) to be determined.

{#argus_note-lakeshore}
##### Note: LakeShore #####
1. [Model 332](https://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-332/Pages/Overview.aspx) temperature controller.  Model 332 has now been superseded by [Model 335](https://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Model-335/Pages/Overview.aspx).
1. On muon instruments, the Triton fridges have an additional Lakeshore controller (the 372) to allow control and continuous readout of the sample temperature (the OI software doesn't allow this using the in-built Lakeshore, despite the unit having a dedicated channel for the sample thermometry). 
1. [Model 372](https://www.lakeshore.com/products/categories/overview/temperature-products/ac-resistance-bridges/model-372-ac-resistance-bridge-temperature-controller) temperature controller.
1. [Model 460](https://www.lakeshore.com/products/Gaussmeters/Model-460-3-Channel-Gaussmeter/Pages/Overview.aspx) gaussmeter.  Model 460 has now been superseded by [Model F71](https://www.lakeshore.com/products/Gaussmeters/F71-F41-teslameters/Pages/Overview.aspx).
1. There are [EPICS drivers](https://epics-controls.org/resources-and-support/modules/hardware-support/) for a variety of Lakeshore devices.

{#argus_note-cryomagnetics}
##### Note: Cryomagnetics #####
1. LM500 model appears to have been superseded by [Model LM-510 Liquid Cryogen Monitor](https://www.cryomagnetics.com/products/model-lm-510-liquid-cryogen-monitor/).  [Spec sheet for the LM500](http://www.cryomagnetics.com/manuals/LM-500c.pdf) is still available. See also spec sheets and manual on [ICPDiscussions](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FCryogenics&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence).

{#argus_note-leiden-cryogenics}
##### Note: Leiden Cryogenics #####
1. ARGUS appears to have a Leiden Dilution Fridge.
   1. Manufacturer: [Leiden Cryogenics](https://leiden-cryogenics.com/)
   1. Manufacturer VI: `C:\LabVIEW Modules\Instruments\ARGUS\ARGUS - LEIDEN Dilution Fridge`
      * The VI appears to date from 2004.
      * This model of dilution fridge (the GHS-2T-1T-700) is probably obsolete.  It is no longer listed on the web-site.

{#argus_note-mclennan}
##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.
   * muon instruments don't use motors in their sample environment


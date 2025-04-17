This page collects information that will be useful for the implementation of the IBEX control system on EMU.
## Background & Timeline ##
EMU is a new 96-detector muon spin rotation spectrometer which is optimised for zero field and longitudinal field measurements at ISIS, on TS1. The [EMU](https://www.isis.stfc.ac.uk/Pages/EMU.aspx) web page describes the background to the instrument.

## Control System ##
EMU will migrate from the SECI control system to the IBEX control system in MMMMMMMM YYYY.

## EMU Equipment ##
The equipment listed below is used on EMU. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Motion note](#note-motion)
??? |  | 4-blade jaws |  |  | [see Jaws note](#note-jaws)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
Julabo | ??? | Water Bath | RS-232 | | [see Water Bath note](#note-water-baths)
ICE |  | Oxford ICE Cube | ??? | | [see Oxford ICE Cube note](#note-oxford-ice-cube)
[CAEN](http://www.caen.it/csite/HomePage.jsp) | V895 | Discriminator | USB VXI via NI DLL | |[see CAEN note](#note-caen)
Danfysik | 8000 | PSU | RS232 | DFKPS | [see Danfysik note](#note-danfysik)
TDK | Lambda Genesys | PSU | RS232 | TDK_ LAMBDA_ GENESYS | [see Genesys note](#note-genesys) |
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#note-kepco)
Kepco | BIT 4886 | I/F card | GPIB, RS-232 | | [see Kepco note](#note-kepco)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | ITC503 | Temperature Controller |   |  | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Mercury | Pressure Controller |   |  | [see Oxford Instruments note](#note-oxford-instruments)
Lakeshore | 372| Temperature Controller |   |  | [see Lakeshore note](#note-lakeshore )
Chell | CCD100 | Pressure Transducer | RS-232 | | [see Chell note](#note-chell)
[Stanford RS](http://www.thinksrs.com/) | DG645 | Delay Generator |  |  | [see Stanford RS note](#note-stanford-rs)
Aeroflex/IFR | 2030 | Signal Generator | RS-232 | | [see Aeroflex note](#note-aeroflex)

##### Note: DAE #####
See multi-detector and single-detector below.

##### Note: Motion #####
There is a project relating to the motion on the South Side Muons in progress, this information may be out of date.

##### Note: Choppers #####
Muon instruments do not have choppers.

##### Note: Jaws #####
Provide information about EMU jaws.

##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/EMU/EMU_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

##### Note: Water Baths #####
EMU uses Julabo water baths
##### Note: Water Baths #####
1. Julabo Water Bath
   * no information on specific Julabo Water Baths - maybe EMU uses water baths from the pool?
   * consult the [Julabo commands](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/backend_system/IOCs/julabo_commands.xlsx) spreadsheet for specific details of which set of commands are used individual water baths.
   * EMU may use oil or glycol as the coolant/heating medium (Julabo/Presto A40 device). 
1. See also [Water Baths](https://www.isis.stfc.ac.uk/Pages/Water-Baths.aspx) list

##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

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
1. The [CAEN V895](http://www.caen.it/csite/CaenProd.jsp?parent=11&idmod=49) is a 16-channel Leading Edge Discriminator.
1. Documentation (\\isis\shares\ISIS_Experiment_Controls\Manuals\CAEN\V895 16-Channel Discriminator

##### Note: Danfysik #####
Need to check which model of Danfysik is used on EMU.
1. [Danfysik Power Supplies](http://www.danfysik.com/en/products/power-supplies/): model 8000 appears to have been superseded by model 8500.
1. [User and Software Manuals](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPower%20Supplies&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence) for System 8500.
1. See [#1208](https://github.com/ISISComputingGroup/IBEX/issues/1208) for comms settings.

##### Note: Genesys #####
1. [TDK Lambda Genesys Power Supplies](https://uk.tdk-lambda.com/products/programmable-power-supplies/).
1. [Safety, User and Programming Manuals](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPower%20Supplies&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence) for System 8500.
1. See also [#983](https://github.com/ISISComputingGroup/IBEX/issues/983), [#2276](https://github.com/ISISComputingGroup/IBEX/issues/2276), [#2458](https://github.com/ISISComputingGroup/IBEX/issues/2458)

##### Note: Kepco #####
1. [Kepco BIT 4886](http://www.kepcopower.com/bit.htm) is an interface card for Kepco bi-polar ([BOP](http://www.kepcopower.com/bop.htm)) power supplies.  See also `C:\LabVIEW Modules\Drivers\Kepco 4886 Serial`
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).<br>  See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)

##### Note: Oxford Instruments #####
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
   * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)
1. Support for OI ITC503 created as part of [#2593](https://github.com/ISISComputingGroup/IBEX/issues/2593)
1. Intelligent Pressure Controller - what do we know about this?

##### Note: LakeShore #####
1. On muon instruments, the Triton fridges have an additional Lakeshore controller (the 372) to allow control and continuous readout of the sample temperature (the OI software doesn’t allow this using the in-built Lakeshore, despite the unit having a dedicated channel for the sample thermometry). 
1. [Model 372](https://www.lakeshore.com/products/categories/overview/temperature-products/ac-resistance-bridges/model-372-ac-resistance-bridge-temperature-controller) temperature controller.
1. There are [EPICS drivers](https://epics-controls.org/resources-and-support/modules/hardware-support/) for a variety of Lakeshore temperature controllers.

##### Note: Chell #####
1. Experiments requiring pressure transducer. [Chell CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100)
1. Documentation (\\\isis\shares\ISIS_Experiment_Controls\CCD100)

##### Note: Stanford RS #####
1. [Stanford DG645 Digital Delay Generator](http://www.thinksrs.com/products/dg645.html)
1. See also `C:\LabVIEW Modules\Drivers\Stanford DG645`
1. Documentation (\\\isis\shares\ISIS_Experiment_Controls\Stanford_DG645_Digital_Delay_Generator)

##### Note: Aeroflex/IFR #####
Aeroflex has been through a complicated series of sales in recent years.  The Aeroflex manuals (\\\isis\shares\ISIS_Experiment_Controls\AeroflexIFR 2023A) are probably a good place to start, along with any existing VIs.  See also [IFR 2023A](https://www.atecorp.com/products/ifr/2023a).

There appears to be no driver for the Aeroflex 2023A in `C:\LabVIEW Modules\`.  However, there is a driver for an Aeroflex 2030 in `C:\LabVIEW Modules\Drivers\Aeroflex 2030`.

## EMU SECI Configs ##
Document information about EMU SECI configs here.

Configuration Name                 | Sub-Configurations                                 | Last Accessed | Required |
-----------------------------------|----------------------------------------------------|---------------|----------|
EMU_place_holder1.conf             | -                                                  | dd/mm/yyyy    | -        |
EMU_place_holder2.conf             | -                                                  | dd/mm/yyyy    | -        |

## EMU Genie Scripts ##
Similarly, Document information about EMU SECI Genie scripts here.
### Booster heater issues

Scientists initially raised concerns about intermittent invalid alarms and it appears this is due to communication failures to a mercury (see [#6286](https://github.com/ISISComputingGroup/IBEX/issues/6286)).

These intermittent caused a failure to switch on the booster heater. The reason for this was that the booster heater script refers to the `Temp_Sample` block for determining whether it should switch the heater on, and if the target temperature is higher than `Temp_Sample`, it will start using the booster heater by running `cset` on the same block. If the block is temporarily in ‘invalid’, then it certainly fails to read and set the temperature (and just carries on). [#6286](https://github.com/ISISComputingGroup/IBEX/issues/6286) was then closed with a temporary increased stream device lock timeout - from 5 to 30 seconds.

The problems from [#6286](https://github.com/ISISComputingGroup/IBEX/issues/6286) then reoccurred on the 22nd and 23rd of May 2021, which spawned tickets [#6270](https://github.com/ISISComputingGroup/IBEX/issues/6720) (issues concerning communicating with the mercury) and [#6271](https://github.com/ISISComputingGroup/IBEX/issues/6721) (issues concerning the booster heater). In [#6270](https://github.com/ISISComputingGroup/IBEX/issues/6720), there was some debate over whether there were differences in the mercury's setup on the day (some addresses of the daughter boards were changed) which could have caused the recurrence of the issue.

Investigation showed the device failed to reply as fast in busy periods and didn't reply as quickly as usual, and that a reply timeout trips up the IOC until it gets time to send the commands again and get a correct response. It was suggested that increasing the reply timeout slightly would fix this, but also that it was pertinent to investigate why on the 23rd and 22nd of May this was more prominent. Adding `@replyTimeout` handlers didn't seem to help very much either.

Sep 2021: Added a [retry mechanism](https://github.com/ISISComputingGroup/EPICS-StreamDevice/compare/master...Ticket6720_add_max_retries_for_mercury_issues) for protocols. 
Lacking documentation about whether this deployment to EMU was successful, and how above changes have affected the status of [#6271](https://github.com/ISISComputingGroup/IBEX/issues/6721). 

Marking [#6271](https://github.com/ISISComputingGroup/IBEX/issues/6721) as fixed and will be closed, please open a new issue if this reoccurs. 

## EMU Notes ##
EMU has the following specialist panels:
1. MUSR RF Kit
1. EMU Traverse field supply
1. EMU Steering Magnet
1. HIFI Metrolab PT2025 (NMR Readout)
1. [MUON Zero Field Controller](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Zero-field-controller)
1. MUON Magnets Danfysik
1. MUON FrontEnd Control
1. MUON FrontEnd Magnet Monitoring
1. MUON Jaws

EMU also has the following system:
1. MUON Script (generator)

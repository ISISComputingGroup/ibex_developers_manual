# POLREF

This page collects information that will be useful for the implementation of the IBEX control system on POLREF.

## Background & Timeline ##
POLREF is a general purpose polarised neutron reflectometer, on TS2. The [POLREF](https://www.isis.stfc.ac.uk/Pages/polref.aspx) web page describes the background to the instrument.

## Control System ##
POLREF will migrate from the SECI control system to the IBEX control system in MMMMMMMM YYYY.

## POLREF Equipment ##
The equipment listed below is used on POLREF. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
ISIS | Mk3 | Chopper | N/A |     | [see Chopper note](#note-choppers)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | Be careful of homing routines | 
Huber|  | Sample Stack | Ethernet |  |  | [see Huber note](#note-huber)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS] | [see McLennan note](#note-mclennan)
Newport | SMC100 | Motion Controller | RS-232 | [EPICS] | [see Newport note](#note-newport)
??? |  | 4-blade jaws |  |  | [see Jaws note](#note-jaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
Julabo | FP-50 | Water Bath | RS-232 | | [see Julabo note](#note-water-baths)
Julabo | FP-52 | Water Bath | RS-232 | | [see Julabo note](#note-water-baths)
~Haake~ | ~N6~ | ~Water Bath~ | ~RS-232~ | | [see Haake note](#note-water-baths)
Keithley | 2400 | Source Meter | RS-232 | | [see Keithley note](#note-keithley)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#note-keithley)
[Knauer](http://www.knauer.net/) | K6 | Electric valve drive | RS232 |  |[see Knauer note](#note-knauer)
[Knauer](http://www.knauer.net/) | 1050 | HPLC pump | ??? | | [see Knauer HPLC note](#note-knauer-hplc)
~Hitachi~ | ~L-7100~ | ~HPLC pump~ | ~???~ | | [see Hitachi note](#note-hitachi)
JASCO | PU-4180 | HPLC pump| ??? | | [see JASCO HPLC note](#note-jasco-hplc-pump)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#note-kepco)
[KEPCO](http://www.kepcopower.com/bop.htm) | BIT 4886 | I/F card | GPIB, RS-232 |  |[see Kepco note](#note-kepco)
LakeShore | 327 | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#note-lakeshore)
LakeShore | 460 | Gaussmeter | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) | [see LakeShore note](#note-lakeshore)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#note-neocera)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments |  | Cryogenic Equipment | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Scientific Magnetics | 17T Cryomag | Super conducting magnet | RS-232 | 3 Axis Super conducting magnet & VTI | see [Scientific Magnetics note](#note-scientific-magnetics)
WPI | Aladdin-1000 | Syringe Pump | ??? | | [see Syringe Pumps note](#note-syringe-pumps)

##### Note: DAE #####
See multi-detector and single-detector below.

##### Note: Choppers #####
POLREF has a Mk3 chopper.<br>

##### Note: Jaws #####
Provide information about POLREF jaws.

##### Note: Huber #####
1. [Huber](http://www.xhuber.de/en/home/).
1. According to Huber's web-site, a Huber SMC9000 is a motion controller.  See [SMC 9300](http://www.xhuber.de/en/product-groups/3-control-systems/smc-9300/) which appears to be the latest of the 9000-series and [SMC 9000](http://www.xhuber.de/fileadmin/user_upload/downloads/usermanuals/9000_1103.pdf)
   * However, in terms of POLREF, Huber seems to refer to a sample stack.  Need to get to the bottom of this confusion.  I guess it is a Huber sample stack (how many axes?) controlled by a SMC 9000 controller.

##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.

##### Note: Newport #####
1. [Newport SMC100](https://www.newport.com/f/smc100-single-axis-dc-or-stepper-motion-controller)
1. EPICS drivers for [Newport devices](https://epics.anl.gov/modules/manufacturer.php#Newport)
1. See also [#824](https://github.com/ISISComputingGroup/IBEX/issues/824)

{#noteVacuum}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/POLREF/POLREF_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

##### Note: Water Baths #####
1. Julabo Water Bath (apparently the following Julabos: WB23 )
   * consult the [Julabo commands](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/backend_system/IOCs/julabo_commands.xlsx) spreadsheet for specific details of which set of commands is used by these water baths.
1. Haake Water Bath (no longer supported at ISIS)
   1. ~Haake N6 Water Bath.  Haake has now been taken over by [ThermoFisher](https://www.thermofisher.com/uk/en/home/life-science/lab-equipment/water-baths-circulators-chillers.html).  N6 model may be obsolete.  Check existing SECI VI for logic and manual~.
1. ~See also [Water Baths](https://www.isis.stfc.ac.uk/Pages/Water-Baths.aspx) list~

##### Note: KEPCO #####
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).
   * See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)
1. [Kepco BIT 4886](http://www.kepcopower.com/bit.htm) is an interface card for Kepco bi-polar ([BOP](http://www.kepcopower.com/bop.htm)) power supplies.

##### Note: Keithley #####
1. [Keithley 2400 Series Source Meter](https://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter).<br>
See also tickets [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#2695](https://github.com/ISISComputingGroup/IBEX/issues/2695), [#2801](https://github.com/ISISComputingGroup/IBEX/issues/2801) and [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176).

##### Note: Hitachi #####
Hitachi L-7100 HPLC pump (no longer supported at ISIS).  ~Can't find L-7100 on [Hitachi web-site](http://www.hitachi-hightech.com/global/about/corporate/group/hhs (may be obsolete).  Check existing SECI VI for logic and manual.~

##### Note: JASCO HPLC Pump #####
[JASCO HPLC pump](https://jascoinc.com/products/chromatography/hplc/modules/hplc-pumps/) is a new (for ISIS) model of HPLC pump.  Jasco pumps are replacing the old Hitachi pumps.
   * See `C:\LabVIEW Modules\Drivers\Jasco PU-4180 HPLC Pump\Documentation` for documentation.
   * See also [#3743](https://github.com/ISISComputingGroup/IBEX/issues/3743) and [#3923](https://github.com/ISISComputingGroup/IBEX/issues/3923)

##### Note: Knauer #####
1. Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
   * K-6 model appears to have been superseded.  Check existing SECI VI for logic and manual.

##### Note: Knauer HPLC #####
Knauer HPLC 1050 [Knauer HPLC 1050 is discontinued.](https://www.knauer.net/en/discontinued-smartline-pump-1050-successor-azura-p-61l/p14161).  Check existing SECI VI for logic and manual.

##### Note: LakeShore #####
1. [Model 327](https://www.lakeshore.com/products/Cryogenic-Temperature-Controllers/Pages/default.aspx).  Model 327 is not listed.  Is it an obsolete model, or should it be Model-372?
1. [Model 460](https://www.lakeshore.com/products/Gaussmeters/Model-460-3-Channel-Gaussmeter/Pages/Overview.aspx).

There are [EPICS drivers](http://www.aps.anl.gov/epics/modules/manufacturer.php#Lakeshore) for a variety of Lakeshore temperature controllers.

##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

##### Note: Oxford Instruments #####
1. Support for OI ITC503 created as part of [#2593](https://github.com/ISISComputingGroup/IBEX/issues/2593)
1. Support for Mercury Temperature Controller was created as part of [#2840](https://github.com/ISISComputingGroup/IBEX/issues/2840)
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
   * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)

##### Note: Scientific Magnetics #####
1. [Scientific Magnetics](http://www.scientificmagnetics.co.uk/)
1. Model: 3 Axis Super conducting magnet & VTI
1. Implemented via LabVIEW, lvDCOM - see [#1398](https://github.com/ISISComputingGroup/IBEX/issues/1398)).

##### Note: Syringe Pumps #####
1. [WPI Aladdin-1000 Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps/al1000-220.aspx)

## POLREF Notes ##
POLREF has the following specialist panels/systems:
1. POLREF Danfysik
1. POLREF Flipper
1. POLREF Vector Network Analyser
1. SURF Galil DIO

POLREF has the following devices under motion control:
1. benches
1. coarse jaws
1. FOMs (Frame Overlap Mirror)
1. Huber
1. jaws
1. laser gimbal
1. point detector
1. Polarizer
1. reflectometer sample stack
1. rotation stage
1. transmission monitor

**Note:** (from original POLREF notes (may now be obsolete - check with Kathryn))
Note for when the time comes - check with the instrument scientist if the calibration function for the Danfysik is still used (allows for specific hysteresis curves to use between the limits in use), if it is, make sure we capture this functionality again - likely to be some SNL or a genie-python script might be able to do it instead.

## POLREF SECI Configs ##
Document information about POLREF SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
POLREF_place_holder1.conf              | -                                                  | dd/mm/yyyy    | -        |
POLREF_place_holder2.conf              | -                                                  | dd/mm/yyyy    | -        |

## POLREF Genie Scripts ##
Similarly, Document information about POLREF SECI Genie scripts here.

# SURF

This page collects information that will be useful for the implementation of the IBEX control system on SURF.
## Background & Timeline ##
SURF is a reflectometer on TS1, used primarily for liquid interface research. The [SURF](https://www.isis.stfc.ac.uk/Pages/SURF.aspx) web page describes the background to the instrument.

## Control System ##
It is proposed that SURF will migrate from the SECI control system to the IBEX control system in time for Cycle 2018/04.

## SURF Equipment ##
The equipment listed below is used on SURF. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
ISIS | Mk3 | Chopper | N/A |     | [see Chopper note](#note-choppers)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
Huber|  | Sample Stack | Ethernet |  |  | [see Huber note](#note-huber)
??? |  | 4-blade jaws |  |  | [see Jaws note](#note-jaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
Julabo | FP-50 | Water Bath | RS-232 | | [see Julabo note](#note-water-baths)
Julabo | FP-52 | Water Bath | RS-232 | | [see Julabo note](#note-water-baths)
~Grant Instruments~ | ??? | ~Water Bath~ | ~RS-232~ | | [see Grant Water Bath note](#note-water-baths)
~Haake~ | ~N6~ | ~Water Bath~ | ~RS-232~ | | [see Haake note](#note-water-baths)
[Knauer](http://www.knauer.net/) | K6 | Electric valve drive | RS232 |  |[see Knauer note](#note-knauer)
[Knauer](http://www.knauer.net/) | 1050 | HPLC pump | ??? | | [see Knauer HPLC note](#note-knauer-hplc-pump)
~Hitachi~ | ~L-7100~ | ~HPLC pump~ | ??? | | [see Hitachi note](#note-hitachi)
JASCO | PU-4180 | HPLC pump| ??? | | [see JASCO HPLC note](#note-jasco-hplc-pump)
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#note-thurlby)
Keithley | 2410 | Source Meter | RS-232 | #1826 | [see Keithley note](#note-keithley)
Keyence | LK-G | Positioning Sensor | RS-232 |  | [see Keyence note](#note-keyence)
Nima Trough | ??? | Trough | ??? | | [see Nima Trough note](#note-nima-trough)
Watson Marlow | 323 | Peristaltic Pump | ??? | | [see Peristaltic Pumps note](#note-peristaltic-pumps)
WPI | Aladdin-1000 | Syringe Pump | ??? | | [see Syringe Pumps note](#note-syringe-pumps)
WPI | SP2xx | Syringe Pump | ??? | | [see Syringe Pumps note](#note-syringe-pumps)

##### Note: DAE #####
See multi-detector and single-detector below.

##### Note: Choppers #####
SURF has a Mk3 chopper.<br>

##### Note: Jaws #####
Provide information about SURF jaws.

##### Note: Huber #####
1. [Huber](http://www.xhuber.de/en/home/).
1. According to Huber's web-site, a Huber SMC9000 is a motion controller.  See [SMC 9300](http://www.xhuber.de/en/product-groups/3-control-systems/smc-9300/) which appears to be the latest of the 9000-series and [SMC 9000](http://www.xhuber.de/fileadmin/user_upload/downloads/usermanuals/9000_1103.pdf)
   * However, in terms of SURF, Huber seems to refer to a sample stack.  Need to get to the bottom of this confusion.  I guess it is a Huber sample stack (how many axes?) controlled by a SMC 9000 controller.
   * See also [#3502](https://github.com/ISISComputingGroup/IBEX/issues/3502)

##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SURF/SURF_Eurotherms.jpg) are used to control temperature.

##### Note: Water Baths #####
1. Julabo Water Bath (apparently the following Julabos: WB7, WB30 )
   * consult the [Julabo commands](/specific_iocs/temp_controllers/julabo_commands.xlsx) spreadsheet for specific details of which set of commands is used by these water baths.
1. Grant Water Bath (no longer supported at ISIS) ~(apparently the following Grant water bath: WB27)~
   * Update (25-06-2019): Grant water baths are no longer used.  No longer any need to support them.  See [#4457](https://github.com/ISISComputingGroup/IBEX/issues/4457)
1. Haake Water Bath (no longer supported at ISIS)
   1. ~Haake N6 Water Bath (apparently the following Haake water bath: WB9).  Haake has now been taken over by [ThermoFisher](https://www.thermofisher.com/uk/en/home/life-science/lab-equipment/water-baths-circulators-chillers.html).  N6 model may be obsolete.  Check existing SECI VI for logic and manual.~
   * Update (25-06-2019): Haake water baths are no longer used.  No longer any need to support them.  See [#4456](https://github.com/ISISComputingGroup/IBEX/issues/4456)
1. See also [Water Baths](https://www.isis.stfc.ac.uk/Pages/Water-Baths.aspx) list

##### Note: Thurlby #####
[Thurlby Thandar Instruments](https://www.aimtti.com/)
1. [Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)
   * see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).
   * Often used with the `Analog_Digital_IO` script.
   * IOC & OPI updated (18-07-2019).  See [#3784](https://github.com/ISISComputingGroup/IBEX/issues/3784)

##### Note: Hitachi #####
Hitachi L-7100 HPLC pump (no longer supported at ISIS).  ~Can't find L-7100 on [Hitachi web-site](http://www.hitachi-hightech.com/global/about/corporate/group/hhs) (may be obsolete).  Check existing SECI VI for logic and manual: both VI and manual are located here: `C:\LabVIEW Modules\Drivers\Hitachi L-7100`.~
   * Update (27-06-2019): Hitachi pumps are no longer used.  No longer any need to support them.  See [#3780](https://github.com/ISISComputingGroup/IBEX/issues/3780).

##### Note: Knauer #####
1. Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
   * K-6 model appears to have been superseded.  Check existing SECI VI for logic and manual.
   * See `C:\LabVIEW Modules\Drivers\Knauer Electric Valve Drive K-6\Documentation` for existing VI.
   * The Knauer K-6 Electric Valve Drive is (nearly) always used with the [Knauer HPLC pump](#note-knauer-hplc-pump).

##### Note: Knauer HPLC Pump #####
Knauer HPLC 1050 pump [Knauer HPLC 1050 is discontinued.](https://www.knauer.net/en/discontinued-smartline-pump-1050-successor-azura-p-61l/p14161).  Check existing SECI VI for logic and manual.
   * See `C:\LabVIEW Modules\Drivers\Knauer HPLC 1050\Documentation` for existing VI.
   * See also [#3262](https://github.com/ISISComputingGroup/IBEX/issues/3262)
   * Knauer HPLC pumps are often used in pairs - so two IOCs will be needed.

##### Note: JASCO HPLC Pump #####
[JASCO HPLC pump](https://jascoinc.com/products/chromatography/hplc/modules/hplc-pumps/) is a new (for ISIS) model of HPLC pump.  Jasco pumps are replacing the old Hitachi pumps.
   * See `C:\LabVIEW Modules\Drivers\Jasco PU-4180 HPLC Pump\Documentation` for documentation.
   * See also [#3743](https://github.com/ISISComputingGroup/IBEX/issues/3743) and [#3923](https://github.com/ISISComputingGroup/IBEX/issues/3923)

##### Note: Keithley #####
1. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter)
1. See also [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176)

##### Note: Keyence #####
1. [Keyence Web-site](https://www.keyence.co.uk/index.jsp)
1. The Keyence LK-G is a laser positioning sensor (possibly superseded by a newer model).  It is used when adjusting the height of the sample stage.  Check the existing VI.
   1. See `C:\LabVIEW Modules\Instruments\INTER\Keyence LK-G` for existing VI (yes, the same device is used on INTER).
   1. Current models of [Keyence LK-G laser sensors](https://www.keyence.co.uk/products/measure/laser-1d/index.jsp)
   1. The Keyence LK-G is always in position on the instrument, although not always used.

##### Note: Nima Trough #####
Nima Trough: SECI uses a manufacturer supplied VI (see `C:\LabVIEW Modules\Drivers\Nima Trough`).  We may need to do the same in IBEX (via lvDCOM).
   * **Note:** NIMA Technologies Ltd now seems to be part of [Biolin Scientific](https://www.biolinscientific.com/ksvnima).<br>
   * The NIMA trough is used regularly on SURF.  The manufacturer supplied VI is used to view graphs showing information about thin films.
   * The manufacturer has made additional software available for download.  A copy of this software is located in `\\isis\shares\ISIS_Experiment_Controls\NIMA Trough\Nima_TR8.1.zip`.

##### Note: Peristaltic Pumps #####
1. [Watson Marlow 323 Peristaltic Pump](http://www.watson-marlow.com/gb-en/range/watson-marlow/300-tube-pumps/323d/)
1. Check existing SECI VI for logic and manual: VI and manuals are located here: 
   * `C:\LabVIEW Modules\Drivers\Watson Marlow 323 Pump`

##### Note: Syringe Pumps #####
1. [WPI Aladdin-1000 Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps/al1000-220.aspx)
1. [WPI SP2xx Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps.aspx) - check specific model.  See also [#3261](https://github.com/ISISComputingGroup/IBEX/issues/3261)
1. The Watson Marlow and WPI Aladdin-1000 syringe pumps are the ones used most frequently on SURF (usually depending on which one is available).
1. Check existing SECI VIs for logic and manual: VIs and manuals are located here: 
   * `C:\LabVIEW Modules\Drivers\WPI Aladdin-1000 Syringe Pump`
   * `C:\LabVIEW Modules\Drivers\WPI SP2XX Pumps`

## SURF Notes ##
SURF has the following specialist panels/systems:
1. INTER Keyence LK-G
1. SURF Galil AO
1. SURF Galil DIO
1. SURF Waterbath (Grant)
1. SURF Vacuum System
1. SURF Motion Control

SURF has the following devices under motion control:
1. goniometer
1. jaws
1. jaws & height
1. multi detector
1. single detector
1. supermirror
1. transmission monitor
1. XYZ stage


## SURF SECI Configs ##
Document information about SURF SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
SURF_place_holder1.conf                | -                                                  | dd/mm/yyyy    | -        |
SURF_place_holder2.conf                | -                                                  | dd/mm/yyyy    | -        |

## SURF Genie Scripts ##
Similarly, Document information about SURF SECI Genie scripts here.

This page collects information that will be useful for the implementation of the IBEX control system on CRISP.
## Background & Timeline ##
CRISP is a reflectometer instrument at ISIS, on TS1. The [CRISP](https://www.isis.stfc.ac.uk/Pages/CRISP.aspx) web page describes the background to the instrument.

## Control System ##
CRISP will migrate from the SECI control system to the IBEX control system in MMMMMMMM YYYY.

## CRISP Equipment ##
The equipment listed below is used on CRISP. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | Mk3 | Chopper | N/A |     | [see Chopper note](#noteChopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
??? |  | 4-blade jaws |  |  | [see Jaws note](#noteJaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#noteVacuum)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#noteVacuum)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
Oxford Instruments | Orange Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#noteOxfordInstruments)
Oxford Instruments | Blue Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#noteOxfordInstruments)
   |   | Closed Cycle Refrigerator | | | | [see CCR note](#noteCCR)
Julabo | FP-50 | Water Bath | RS-232 | | [see Water Bath note](#noteWaterBath)
Julabo | FP-52 | Water Bath | RS-232 | | [see Water Bath note](#noteWaterBath)
~Grant Instruments~ | ??? | ~Water Bath~ | RS-232 | | [see Water Bath note](#noteWaterBath)
~Haake~ | ~N6~ | ~Water Bath~ | RS-232 | | [see Water Bath note](#noteWaterBath)
Keithley | 2000 | Multimeter | RS-232 | | [see Keithley note](#noteKeithley)
Keithley | 2602 | Source Meter | RS-232 | | [see Keithley note](#noteKeithley)
Hirst | GM05 | Gaussmeter | ??? | | [see Hirst note](#noteHirst)
Knauer | K-6  | Electric Valve Drive | ??? | | [see Knauer note](#noteKnauer)
Knauer | 1050 | HPLC pump | ??? | | [see Knauer HPLC note](#noteKnauerHPLC)
Hitachi | L-7100 | HPLC pump| ??? | | [see Hitachi note](#noteHitachi)
Nima Trough | ??? | Trough | ??? | | [see Nima Trough note](#noteNimaTrough)
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#noteThurlby)
Watson Marlow | 323 | Syringe Pump | ??? | | [see Syringe Pumps note](#noteSyringePumps)
WPI | Aladdin-1000 | Syringe Pump | ??? | | [see Syringe Pumps note](#noteSyringePumps)
WPI | SP2xx | Syringe Pump | ??? | | [see Syringe Pumps note](#noteSyringePumps)
??? | ??? | He3 Monitor | ??? | | [see He3 Monitor note](#noteHe3Monitor)

<a name="noteDAE"></a>
##### Note: DAE #####
See multi-detector and single-detector below.

<a name="noteChopper"></a>
##### Note: Choppers #####
CRISP has a Mk3 chopper.<br>

<a name="noteJaws"></a>
##### Note: Jaws #####
Provide information about CRISP jaws.

<a name="noteVacuum"></a>
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/CRISP/CRISP_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

<a name="noteOxfordInstruments"></a>
##### Note: Oxford Instruments #####
1. Orange Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Low-Temperature-Cryostats.aspx) to be determined.  Orange cryostats are controlled via a temperature controller (e.g. Eurotherm), so nothing on the cryostat itself for IBEX to control.
1. Blue Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Low-Temperature-Cryostats.aspx) to be determined.

<a name="noteCCR"></a>
##### Note: Closed Cycle Refrigerators #####
   1. [CCR](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/CRISP/CRISP_CCR.jpg) is the most frequently used low-temperature device used in on CRISP.
[CCRs](https://www.isis.stfc.ac.uk/Pages/Closed-Cycle-refrigerators,-CCRs.aspx). Not directly computer-controlled  - controlled via Eurotherm.

<a name="noteWaterBath"></a>
##### Note: Water Baths #####
CRISP uses two types of water bath
1. Julabo (which model(s)?)
1. Grant Water Bath
   * Update (25-06-2019): Grant water baths are no longer used.  No longer any need to support them.  See [#4457](https://github.com/ISISComputingGroup/IBEX/issues/4457)
1. Haake N6 Water Bath.  Haake has now been taken over by [ThermoFisher](https://www.thermofisher.com/uk/en/home/life-science/lab-equipment/water-baths-circulators-chillers.html).  N6 model may be obsolete.  Check existing SECI VI for logic and manual.
   * Update (25-06-2019): Haake water baths are no longer used.  No longer any need to support them.  See [#4456](https://github.com/ISISComputingGroup/IBEX/issues/4456)

<a name="noteKeithley"></a>
##### Note: Keithley #####
1. [Keithley 2000 Series Multi-Meter](https://uk.tek.com/tektronix-and-keithley-digital-multimeter/keithley-2000-series-6%C2%BD-digit-multimeter-scanning).  See also [#2460](https://github.com/ISISComputingGroup/IBEX/issues/2460).
1. [Keithley 2600 Series Source Meter](https://uk.tek.com/keithley-source-measure-units/smu-2600b-series-sourcemeter).<br>

<a name="noteHirst"></a>
##### Note: Hirst #####
[Hirst GM05 gaussmeter](http://www.hirst-magnetics.com/instruments/gm05_p1.shtml)

<a name="noteHitachi"></a>
##### Note: Hitachi #####
Hitachi L-7100 HPLC pump.  Can't find L-7100 on Hitachi web-site (may be obsolete).  Check existing SECI VI for logic and manual.

<a name="noteKnauer"></a>
##### Note: Knauer #####
Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
K-6 model appears to have been superseded.  Check existing SECI VI for logic and manual.

<a name="noteKnauerHPLC"></a>
##### Note: Knauer HPLC #####
Knauer HPLC 1050 [Knauer HPLC 1050 is discontinued.](https://www.knauer.net/en/discontinued-smartline-pump-1050-successor-azura-p-61l/p14161).  Check existing SECI VI for logic and manual.

<a name="noteNimaTrough"></a>
##### Note: Nima Trough #####
Nima Trough: SECI used a manufacturer supplied VI.  We may need to do the same in IBEX (via lvDCOM).<br>
   * **Note:** NIMA Technologies Ltd now seems to be part of [Biolin Scientific](https://www.biolinscientific.com/ksvnima).<br>
   * The NIMA trough is used regularly on SURF.  The manufacturer supplied VI is used to view graphs showing information about thin films.
   * The manufacturer has made additional software available for download.  A copy of this software is located in `\\isis\shares\ISIS_Experiment_Controls\NIMA Trough\Nima_TR8.1.zip`.

<a name="noteThurlby"></a>
##### Note: Thurlby #####
Thurlby EX355P PSU - see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).

[Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)

<a name="noteSyringePumps"></a>
##### Note: Syringe Pumps #####
1. [Watson Marlow 323 Peristaltic Pump](http://www.watson-marlow.com/gb-en/range/watson-marlow/300-tube-pumps/323d/)
1. [WPI Aladdin-1000 Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps/al1000-220.aspx)
1. [WPI SP2xx Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps.aspx) - check specific model.

<a name="noteHe3Monitor"></a>
##### Note: He3 Monitor #####
He3 Monitor is an obsolete piece of equipment.  It is no longer used.  No need to support it.

## CRISP SECI Configs ##
Document information about CRISP SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
CRISP_place_holder1.conf             | -                                                  | dd/mm/yyyy    | -        |
CRISP_place_holder2.conf             | -                                                  | dd/mm/yyyy    | -        |

## CRISP Genie Scripts ##
Similarly, Document information about CRISP SECI Genie scripts here.

## CRISP Notes ##
CRISP has the following specialist panels:
1. CRISP setup dialogue
1. CRISP User Front Panel
1. CRISP analyser stage
1. INTER High Voltage
1. SURF Galil analogue output
1. SURF Galil DIO

CRISP has the following devices under motion control:
1. goniometer
1. jaws & height
1. jaws
1. multi-detector
1. single-detector
1. supermirror
1. transmission monitor
1. XYZ stage

CRISP has the following item:
1. LSS Scan calculator (is this a script?)
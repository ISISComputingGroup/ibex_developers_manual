# VESUVIO

This page collects information that will be useful for the implementation of the new control system on VESUVIO.
## Background & Timeline ##
VESUVIO (previously known as EVS) is a long established instrument at ISIS, on TS1. The [VESUVIO](http://www.isis.stfc.ac.uk/instruments/vesuvio/) web page describes the background to the instrument.  An image of VESUVIO is shown in ​[this diagram](http://www.isis.stfc.ac.uk/instruments/vesuvio/vesuvio-configuration6163.jpg).<br>

## Control System ##
VESUVIO will migrate from the SECI control system to the IBEX control system.

## VESUVIO Equipment ##
The equipment listed below is used on VESUVIO. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#noteGalil)
[Pfeiffer](https://www.pfeiffer-vacuum.com/en/products/) | TPG 26x | ISIS Vacuum System | RS232 | EPICS | [see Pfeiffer note](#notePfeiffer)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#noteMcLennan)
Oxford Instruments | Dilution Fridge | Cryogenic System | RS-232 | | [see Oxford Instruments note](#noteOxfordInstruments)
Eurotherm | All models at ISIS | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
ISIS | RAL | Furnaces | N/A | | [see Furnace note](#noteFurnace)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#noteNeocera)
Julabo | TBD | Waterbath | RS-232 | EPICS | [see Julabo note](#noteJulabo)
Chell | CCD100 | Pressure Transducer | RS-232 | | [see Chell note](#noteChell)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#noteKeithley)

<a name="noteDAE"></a>
##### Note: DAE #####
Main Detector banks

<a name="noteGalil"></a>
##### Note: Galil #####
Devices controlled by Galil: [Eulerian Cradle](http://www.xhuber.de/en/product-groups/1-positioning-devices/12-rotation/eulerian-cradles/).

<a name="notePfeiffer"></a>
##### Note: Pfeiffer #####
1. [Model TPG 26x] (https://www.pfeiffer-vacuum.com/en/products/measurement/activeline/controllers/?detailPdoId=5724)

<a name="noteMcLennan"></a>
##### Note: McLennan #####
1. The motors are set up in the following setup:
    1. MTR0101: Forward scattering foil, left
    1. MTR0102: Forward scattering foil, right
    1. MTR0201: Uranium foil
    1. MTR0202: Backward scattering foil
1. The single axis McLennan (currently Uranium foil) may be used to control one of the following other devices at a time: Rotating centre-stick, EVS Rotating centre-stick, McLennan-Newport Rotation Stage, MAPS CCR, PRISMA Omega Centre Stick, etc
1. The backward scattering foil is linked to hardware interlocks. If the cabin is open, the shutter can't be moved. In these cases, it will report being at either an upper or lower limit.

<a name="noteOxfordInstruments"></a>
##### Note: Oxford Instruments #####
1. Dilution fridge: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/dilution-refrigerators8825.html) to be determined.

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
Used to control temperature of top-loading CCRs, Furnace, Orange Cryostat devices, etc.

<a name="noteFurnace"></a>
##### Note: Furnaces #####
Vesuvio uses RAL designed furnaces - RAL5, vanadium and niobium furnaces (see [Furnaces](http://www.isis.stfc.ac.uk/sample-environment/high-temperature/standard-furnaces/standard-furnaces13745.html)).

These are controlled via a Eurotherm temperature controller.

<a name="noteNeocera"></a>
##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

<a name="noteJulabo"></a>
##### Note: Julabo #####
Experiments requiring waterbath.

<a name="noteChell"></a>
##### Note: Chell #####
Experiments requiring pressure transducer. [Chell CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100)

<a name="noteKeithley"></a>
##### Note: Keithley #####
Experiments requiring source meter. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter)

## VESUVIO SECI Configs ##
Over the years, VESUVIO is likely to have accumulated a significant collection of SECI configs. Not all of them are current (some may no longer be used, or used only infrequently). We will need to investigate how to convert them to IBEX configs.  
The config files are located in the folder `SECI\Configurations\` on the VESUVIO control server and have the extension `.conf`.  Sub-configuration files have the extension `.comp` (component).  The files with numbers as extensions (`.1`, `.2`, `.3`,etc.) are backups of the configuration and sub-configuration files.



| Configuration Name | Sub-Configurations | Last Accessed | Required |
------------ | ------------- | ------------- | ------------- |
VESUVIO_withTLCCR__31mar2015 | Sub_EVS_Base, Sub_EVS_Eurotherm_CCR | 16/09/2016 | - |
highTfurnace__oct2015 | - | 12/10/2015 | - |
EVS_Huber | eurotherm | 09/09/2015 | - |
VESUVIO_Nbfurnace__15june2015 | eurotherm | 15/06/2015 | - |
VESUVIO_emptyInstrument__26mar2015 | eurotherm | 26/03/2015 | - |
VESUVIO_emptyInstrument__16mar2015 | eurotherm | 16/03/2015 | - |
EVS Ambient | eurotherm | 22/08/2014 | - |
tempalooza | eurotherm | 13/06/2014 | - |
20130425 - EVS Ambient | - | 26/04/2013 | - |
rotating cs + cryo | - | 28/07/2011 | - |
heaters on sample 0 -100C | - | 28/07/2011 | - |
EVS Heated Can | - | 22/07/2011 | - |
EVS Cryostat | - | 22/07/2011 | - |
EVS Ambient + Platinums | - | 22/07/2011 | - |
Calibration | - | 31/03/2011 | - |
U Foil Calibration | - | 14/02/2011 | - |
rotating prisma cs | - | 14/02/2011 | - |
rotating prisma cs + cryo | - | 14/02/2011 | - |
rotating cs | - | 14/02/2011 | - |
rotating ccr | - | 14/02/2011 | - |
Neocera | - | 14/02/2011 | - |
Kelvinox | - | 14/02/2011 | - |
EVS Water Bath | - | 14/02/2011 | - |
EVS Kelvinox | - | 14/02/2011 | - |
EVS CCR | - | 14/02/2011 | - |
EVS Ambient + Cryostat | - | 14/02/2011 | - |
EVS 4K TLCCR | - | 14/02/2011 | - |
ChipIR2 | - | 14/02/2011 | - |
ChipIR | - | 14/02/2011 | - |

## VESUVIO Genie Scripts ##
Similarly, VESUVIO has built up a significant collection of genie scripts over the years. Again, many scripts are old and may no longer be used regularly. There will be a need to convert some of these scripts to genie-python, but probably not all.

## Tested IOCs ##

| What | When | Notes |
| ---- | ---- | ----- |
| Device-X | dd/mm/yyyy| some notes |


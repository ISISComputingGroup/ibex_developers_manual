# VESUVIO

```{include} migration_notes_warning.mdinc
```

This page collects information that will be useful for the implementation of the new control system on VESUVIO.
## Background & Timeline ##
VESUVIO (previously known as EVS) is a long established instrument at ISIS, on TS1. The [VESUVIO](http://www.isis.stfc.ac.uk/instruments/vesuvio/) web page describes the background to the instrument.  An image of VESUVIO is shown in ​[this diagram](http://www.isis.stfc.ac.uk/instruments/vesuvio/vesuvio-configuration6163.jpg).<br>

## VESUVIO Equipment ##
The equipment listed below is used on VESUVIO. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#vesuvio_noteDAE)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#vesuvio_noteGalil)
[Pfeiffer](https://www.pfeiffer-vacuum.com/en/products/) | TPG 26x | ISIS Vacuum System | RS232 | EPICS | [see Pfeiffer note](#vesuvio_notePfeiffer)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#vesuvio_noteMcLennan)
Oxford Instruments | Dilution Fridge | Cryogenic System | RS-232 | | [see Oxford Instruments note](#vesuvio_noteOxfordInstruments)
Eurotherm | All models at ISIS | Temperature Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#vesuvio_noteEurotherm)
ISIS | RAL | Furnaces | N/A | | [see Furnace note](#vesuvio_noteFurnace)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#vesuvio_noteNeocera)
Julabo | TBD | Waterbath | RS-232 | EPICS | [see Julabo note](#vesuvio_noteJulabo)
Chell | CCD100 | Pressure Transducer | RS-232 | | [see Chell note](#vesuvio_noteChell)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#vesuvio_noteKeithley)

{#vesuvio_noteDAE}
##### Note: DAE #####
Main Detector banks

{#vesuvio_noteGalil}
##### Note: Galil #####
Devices controlled by Galil: [Eulerian Cradle](http://www.xhuber.de/en/product-groups/1-positioning-devices/12-rotation/eulerian-cradles/).

{#vesuvio_notePfeiffer}
##### Note: Pfeiffer #####
1. [Model TPG 26x] (https://www.pfeiffer-vacuum.com/en/products/measurement/activeline/controllers/?detailPdoId=5724)

{#vesuvio_noteMcLennan}
##### Note: McLennan #####
1. The motors are set up in the following setup:
    1. MTR0101: Forward scattering foil, left
    1. MTR0102: Forward scattering foil, right
    1. MTR0201: Uranium foil
    1. MTR0202: Backward scattering foil
1. The single axis McLennan (currently Uranium foil) may be used to control one of the following other devices at a time: Rotating centre-stick, EVS Rotating centre-stick, McLennan-Newport Rotation Stage, MAPS CCR, PRISMA Omega Centre Stick, etc
1. The backward scattering foil is linked to hardware interlocks. If the cabin is open, the shutter can't be moved. In these cases, it will report being at either an upper or lower limit.

{#vesuvio_noteOxfordInstruments}
##### Note: Oxford Instruments #####
1. Dilution fridge: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/dilution-refrigerators8825.html) to be determined.

{#vesuvio_noteEurotherm}
##### Note: Eurotherm #####
Used to control temperature of top-loading CCRs, Furnace, Orange Cryostat devices, etc.

{#vesuvio_noteFurnace}
##### Note: Furnaces #####
Vesuvio uses RAL designed furnaces - RAL5, vanadium and niobium furnaces (see [Furnaces](http://www.isis.stfc.ac.uk/sample-environment/high-temperature/standard-furnaces/standard-furnaces13745.html)).

These are controlled via a Eurotherm temperature controller.

{#vesuvio_noteNeocera}
##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

{#vesuvio_noteJulabo}
##### Note: Julabo #####
Experiments requiring waterbath.

{#vesuvio_noteChell}
##### Note: Chell #####
Experiments requiring pressure transducer. [Chell CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100)

{#vesuvio_noteKeithley}
##### Note: Keithley #####
Experiments requiring source meter. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter)

## Tested IOCs ##

| What | When | Notes |
| ---- | ---- | ----- |
| Device-X | dd/mm/yyyy| some notes |


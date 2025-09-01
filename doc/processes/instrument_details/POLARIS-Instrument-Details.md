# POLARIS

This page collects information that will be useful for the implementation of the IBEX control system on POLARIS.
## Background & Timeline ##
POLARIS is a diffractometer instrument at ISIS, on TS1. The [POLARIS](http://www.isis.stfc.ac.uk/instruments/polaris/polaris4643.html) web page describes the background to the instrument.

## POLARIS Equipment ##
The equipment listed below is used on POLARIS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#polaris_noteDAE)
ISIS | Mk2 Chopper | Chopper | RS-232 |  | [see Chopper note](#polaris_noteChopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#polaris_noteGalil) | 
[JJ-XRAY](http://www.jjxray.dk/) |  | 4 x 4-blade jaws |  |  | Blades driven by Galils.  [see JJ X-Ray note](#polaris_noteJJXray)
  |  | 1 x 4-blade jaws |  |  | Blades driven by Galils.  Mounted inside sample tank
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | #169 | 
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | #216 |[see Pfeiffer note](#polaris_notePfeiffer)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG26x | Gas Handling System | RS232 | #1411 |[see Pfeiffer note](#polaris_notePfeiffer)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#polaris_noteEurotherm)
Chell | CCD100 | Pressure Transducer | RS-232 | #1827 | [see Chell note](#polaris_noteChell)
Keithley | 2400 | Source Meter | RS-232 | #1826 | [see Keithley note](#polaris_noteKeithley)
Oxford Instruments | Orange Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#polaris_noteOxfordInstruments)
Oxford Instruments | Blue Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#polaris_noteOxfordInstruments)
Oxford Instruments | Dilution Fridge (Kelvinox) | Cryogenic System |   |  | [see Oxford Instruments note](#polaris_noteOxfordInstruments)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#polaris_noteMcLennan)
ISIS | Eurotherm & Keithley | Resistivity Measurements | RS-232 | | Only an offline experiment to date [see Resistivity note](#polaris_noteResistivity)
ISIS | POLARIS Sample Changer | Sample Changer | RS-232 | | Copy of GEM device
Applied Measurements Ltd | INT2-L | Pressure Transducer | RS-232 | | Used in the Hydrothermal Reaction Cell [see Hydrothermal Reaction Cell note](#polaris_noteHydrothermal) |
ISIS | POLARIS Pressure Cell Controller | Pressure Cell Controller | RS-232 | | [see Pressure Cell Controller note](#polaris_notePressureCell)
Spellman| SL600  | high-voltage power supply | N/A | | [see Spellman note](#polaris_noteSpellman)
ISIS | CS155 centre stick | high voltage centre stick | N/A | | [see HV Centre Stick note](#polaris_noteHVCentreStick)


{#polaris_noteDAE}
##### Note: DAE #####
Main Detector banks + fixed monitors.

{#polaris_noteChopper}
##### Note: Choppers #####
One T0 chopper.<br>
Chopper is ISIS Mk2 chopper.  Mk2 choppers have a serial interface (not Ethernet like Mk3).

{#polaris_noteJJXray}
##### Note: JJ X-Ray #####
[JJ X-Ray 4-blade jaws](http://www.jjxray.dk/products/jj-x-ray-slit-systems/neutron-slits)<br>
All blades are driven by Galils.<br>
POLARIS has two screens for managing all 5 sets of jaws:

1. One screen to view & edit settings for jaw sets 1 -4 and display settings for jaw set 5
1. A separate screen (Jaws Manager) to view & edit settings for all 5 jaw sets

{#polaris_notePfeiffer}
##### Note: Pfeiffer #####

1. [Model TPG 26x](https://www.pfeiffer-vacuum.com/en/products/measurement/activeline/controllers/?detailPdoId=5724)
2. [Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407)

{#polaris_noteChell}
##### Note: Chell #####
Experiments requiring pressure transducer. [Chell CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100)

{#polaris_notePressureCell}
##### Note: Pressure Cell Controller #####
The pressure cell controller on POLARIS is a copy of the same device on PEARL.  At the current time (April 2017), it has not been used on POLARIS for some time.  However, it may be used at some future point (but probably not for another 12-18 months, by which time we should have implemented support for the pressure cell controller on PEARL).

{#polaris_noteKeithley}
##### Note: Keithley #####
Experiments requiring source meter. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter)

{#polaris_noteEurotherm}
##### Note: Eurotherm #####
Used to control temperature Orange Cryostat devices.

{#polaris_noteOxfordInstruments}
##### Note: Oxford Instruments #####

1. Orange Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.  Orange cryostats are controlled via a temperature controller (e.g. Eurotherm), so nothing on the cryostat itself for IBEX to control.
1. Blue Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.
   1. Are these the Heliox and ITC devices?
   1. The Heliox device has a sorption insert (is that relevant to the control system?)
1. Dilution fridge: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/dilution-refrigerators8825.html) to be determined.
   1. [Kelvinox dilution fridge](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/kelvinox-dilution-fridge/kelvinox-dilution-fridge13981.html)

{#polaris_noteMcLennan}
##### Note: McLennan #####
1. One McLennan is used raise/lower the sample-stick
2. Another single-axis McLennan is used to rotate the sample-stick

{#polaris_noteGalil}
##### Note: Galil #####
GALIL_02 is currently set up to use QR instead of DR mode because DR mode stopped working. This is the same issue as documented in Ticket #2191.

{#polaris_noteHydrothermal}
##### Note: Hydrothermal Cell #####
Uses the INT2-L pressure transducer.

{#polaris_noteResistivity}
##### Note: Resistivity Measurements #####
An evacuated furnace cell for measuring resistivity.  Controlled by Eurotherms and measured by Keithleys (models 2000, 2400?)

{#polaris_noteSpellman}
##### Note: Spellman High Voltage Power Supply #####
6kV, 100mA, 600W, DC power supply.  Not possible to control this device via software.

{#polaris_noteHVCentreStick}
##### Note: CS155 Centre Stick #####
Not possible to control this device via software.  It connects to the [Spellman](#polaris_noteSpellman) HV-PS.

s currently used on POLARIS here.

## POLARIS Notes ##

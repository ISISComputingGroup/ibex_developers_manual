This page collects information that will be useful for the implementation of the IBEX control system on HRPD.
## Background & Timeline ##
HRPD, the High Resolution Powder Diffractometer is an instrument on TS1 at ISIS.  It is the highest resolution neutron powder diffractometer of its type in the world.  The [HRPD](http://www.isis.stfc.ac.uk/instruments/hrpd/hrpd.html) web page describes the background to the instrument.

There is a proposal to re-build HRPD at some point in the next 3-5 years.

## Control System ##
HRPD will migrate from the SECI control system to the IBEX control system.

## HRPD Equipment ##
The equipment listed below is used on HRPD. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | N/A | Shutter | N/A| | [see Shutter note](#noteShutter)
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | #169 | [see Mk3 Chopper note](#noteMk3Chopper) |
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#noteGalil) | 
[LINMOT](http://www.linmot.com/) | [P0x-23](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf) | Linear Motors and Motion Controller | RS-232 | [#2098](https://github.com/ISISComputingGroup/IBEX/issues/2098) | [see LinMot note](#noteLinMot) |
??? | ??? | 1 x 4-blade jaws |  |  | [see Jaws note](#noteJaws)
??? | ??? | Intermediate Shutter |  | | [see Intermediate Shutter note](#noteIMShutter) |
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | #216 |[see Pfeiffer note](#notePfeiffer)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG26x | Gas Handling System | RS232 | #1411 |[see Pfeiffer note](#notePfeiffer)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
Chell | [CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100) | Pressure Transducer | RS-232 | #1827 | [see Chell note](#noteChell)
Oxford Instruments | Dilution Fridge (Kelvinox) | Cryogenic System |   |  | [see Oxford Instruments note](#noteOxfordInstruments)
Oxford Instruments | Blue Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#noteOxfordInstruments)
??? | ??? | Pressure Transducer |  |  | [see Paris-Edinburgh Press note](#notePEPress)
??? | ??? | Helium Level Meter |  |  | [see He Level Meter note](#noteHeLM)
??? | ??? | Magnet| | | [see Magnets note](#noteMagnets)
B&WTek | i-Raman Plus | Raman Spectrometer| | | [see mini-Raman Spectrometer note](#noteRamanSpect)

<a name="noteShutter"></a>
##### Note: Shutter #####
HRPD and ENGIN-X share the same primary shutter (which is directly equivalent to the single shutter used on other instruments).  HRPD and ENGIN-X also have their own secondary shutters (so that each instrument can operate independently of the other when the primary shutter is open.
1. When the primary shutter is closed, neither instrument receives neutrons.  The status of the primary shutter is available in the same way as it is for any other instrument (i.e. via the appropriate PV).
1. When the primary shutter is open, HRPD receives neutrons only if the secondary shutter is also open.  The status of the secondary shutter is not available to IBEX.

The IBEX dashboard should continue to report the status of the primary shutter.<br>
**Note:** IBEX only ever reports the status of the shutter.  IBEX _**never**_ controls the shutter (control of the shutter is part of the instrument safety system and is strictly outside the scope of IBEX).

<a name="noteDAE"></a>
##### Note: DAE #####
Main Detector banks + one working fixed monitor upstream of sample position.

<a name="noteGalil"></a>
##### Note: Galil #####
HRPD does not use any Galils at the present time.

<a name="noteLinMot"></a>
##### Note: LinMot #####
HRPD uses LinMot P0x-23 motors, controlled by LinMot drives.<br>
[LinMot User Manual](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf)

<a name="noteJaws"></a>
##### Note: Jaws #####
Single 4-blade jaws.  Mounted between guide exit and incident collimation slug.  Jaws are driven by LinMot P0x-23 motors. 

<a name="noteIMShutter"></a>
##### Note: Intermediate Shutter #####
HRPD features an "intermediate shutter".  This is hardware controlled and does **NOT** fall within the scope of IBEX (i.e. IBEX will provide no facility to control the intermediate shutter).

<a name="noteMk3Chopper"></a>
##### Note: ISIS Mk3 Choppers #####
HRPD has two ISIS Mk3 choppers.

<a name="notePfeiffer"></a>
##### Note: Pfeiffer #####

1. [Model TPG 26x] (https://www.pfeiffer-vacuum.com/en/products/measurement/activeline/controllers/?detailPdoId=5724), used on the furnace vacuum system 
2. [Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407), used on the tank/guide vacuum system 

<a name="noteChell"></a>
##### Note: Chell #####
[Chell CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100):
For future experiments requiring pressure transducer (pressure/gas flow data from gas panels). May need to consult with Chris Goodway - new transducer readouts are in progress.  CCD100 is used in the gas panel.

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
Three Eurotherms in use on HRPD.  Used to control temperature of all top-loading CCR/ He-cryostats and furnaces.

<a name="noteOxfordInstruments"></a>
##### Note: Oxford Instruments #####
Making use of these devices will be a priority for HRPD over the next 12 months (from May 2017 onwards).

1. Dilution fridge: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/dilution-refrigerators8825.html) to be determined.
   1. [Kelvinox dilution fridge](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/dilution-refrigerators/kelvinox-dilution-fridge/kelvinox-dilution-fridge13981.html)
2. Blue Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.

<a name="notePEPress"></a>
##### Note: Paris-Edinburgh Press #####
Pressure transducers for supporting use of [Paris-Edinburgh press](http://www.isis.stfc.ac.uk/sample-environment/high-pressure/clamped-cells/paris-edinburgh-cells/paris-edinburgh-cells14179.html) will be required.  HRPD may adopt same or similar configurations to PEARL.

<a name="noteHeLM"></a>
##### Note: He Level Meter #####
May be required in the future.  No further information at present. 

<a name="noteMagnets"></a>
##### Note: Magnets #####
May be required in the future.  No further information at present. 
See [magnets at ISIS](http://www.isis.stfc.ac.uk/sample-environment/high-magnetic-field/high-magnetic-field-8812.html)

<a name="noteRamanSpect"></a>
##### Note: mini-Raman Spectrometer #####
1. [B&W Tek i-Raman Plus](http://bwtek.com/products/i-raman-plus/) A Raman Spectrometer is something that HRPD would like to use at a future date (TBD).  See also SXD.

## HRPD SECI Configs ##
HRPD has numerous heritage SECI configurations only two of which are now used routinely.

1. One is used for day-to-day operation with samples at RT, in cryostats or furnace (`HRPD_Eurotherms_2.conf`).
1. The second is used with the sample changer (`HRPD_Sample_Changer_new_oct16.conf`).

All located in `C:\\Program Files (x86)\STFC ISIS Facility\SECI\Configurations`

The HRPD team would probably wish to have separate configurations for experiments involving:

1. High-pressure devices (incl. various pressure transducers)
1. Gas handling
1. Magnets
1. In-situ light scattering (laser control, spectrometer data acquisition)

## HRPD Genie Scripts ##
The critical OpenGenie scripts, for initialisation and focussing, are in `C:\\OG` (duplicated, more or less, in `C:\\scripts\OG`)

HRPD has a large collection of Genie scripts accumulated over the years, each of results from a specific user running a specific operation. A number of editable seed scripts are kept in (`C:\\scripts\keep`).  These might appropriately be converted to genie_python.

## HRPD Notes ##
Add any notes about special items of equipment, setup or conditions on HRPD that might impact the deployment and configuration of IBEX.

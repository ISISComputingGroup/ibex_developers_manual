# MAPS

This page collects information that will be useful for the implementation of the IBEX control system on MAPS.

## Background & Timeline ##
MAPS is a chopper spectrometer on TS1 at ISIS. The [MAPS](http://www.isis.stfc.ac.uk/instruments/maps/) web page describes the background to the instrument.

## MAPS Equipment ##
The equipment listed below is used on MAPS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#maps_noteDAE)
ISIS | MK3| T0 Chopper | N/C |  | [see T0 Chopper note](#maps_noteT0Chopper) |
ISIS | MK3 | Disk Chopper | Ethernet | EPICS | [see Disk Chopper note](#maps_noteDiskChopper) |
FZJ | Digital Drive | Fermi Chopper | Ethernet | TBD | [see Fermi Chopper note](#maps_noteFermiChopper) |
??? | TBD | Fermi Chopper Lift | TBD |  | [see Fermi Chopper Lift note](#maps_noteFermiLift) |
LINMOT Jaws | TBD | Motion Controller | RS232 | EPICS | [see LinMot note](#maps_noteLinMot) | 
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) |[see Pfeiffer note](#maps_notePfeiffer)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#maps_noteEurotherm)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#maps_noteMcLennan)
ISIS| | Sample Changer | via McLennan | | [see Sample Changer note](#maps_noteMcLennan)
??? | ??? | Heater | RS-232 | | controlled via Eurotherm
ISIS | RAL | Furnaces | N/A | | controlled via Eurotherm
Neocera | LTC-21 | Temperature Controller | RS-232 | [#1828](https://github.com/ISISComputingGroup/IBEX/issues/1828) | [see Neocera note](#maps_noteNeocera)

{#maps_noteDAE}
##### Note: DAE #####
Main Detector banks + several fixed monitors.

{#maps_noteT0Chopper}
##### Note: MAPS T0 Chopper #####
T0 chopper is generally operated in read-only mode (i.e. visiting scientists should **_never_** change its settings).<br>
T0 is an ISIS MK3 chopper.

{#maps_noteDiskChopper}
##### Note: MAPS Disk Chopper #####
User needs the ability to change speed & phase settings.<br>
Disk Chopper is an ISIS MK3 chopper.

{#maps_noteFermiChopper}
##### Note: MAPS Fermi Chopper #####
The fermi chopper controller is a Jülich model (FZJ - Forschungszentrum Jülich) - custom built for ISIS and believed to be a prototype being developed by both institutions.  A copy of the manual (PDF) is in the shared area.<br>
The control program will need to include various safety-critical condition monitoring routines (e.g. overspeed, bearing voltage out-of-range).  See manual for more details.<br>
The Fermi chopper on MAPS is primarily controlled via scripts.  Scripts are used to calculate the speed & phase, based on the energy and frequency (this calculation could be folded into IOC).  The OPI should merely display the energy, frequency, speed & phase, not allow the user to change them. <br>
Ideally, the Fermi Chopper should have a hierarchy of OPIs - at least, Simple UI (user) & Complex UI (manager).  Talk with the instrument scientist about what is important when we design the IOC & OPI(s).

{#maps_noteFermiLift}
##### Note: MAPS Fermi Chopper Lift #####
A lift is used to raise/lower the Fermi chopper.  Lowered means the Fermi chopper is in the beam; raised means it is out of the beam.  It would be helpful if the lift can report its status to the IBEX GUI.<br>
Lift is controlled by a PLC, therefore IBEX can report status of lift by interrogating the PLC.  IBEX will not be able to change the lift position - that will have to be done on the PLC control panel.  Make/type of PLC - to be determined.<br>
Given the above, the requirement that "The Fermi chopper must not be operated (i.e. it must not be spinning) when it is in the raised position.  Lift controls should not be accessible to the user." is automatically satisfied.<br>

{#maps_noteLinMot}
##### Note: LinMot #####
LinMots are used to drive the jaws.  There are two 4-blade sets: one named "fermi" and the other "sample" which relate to their positions in the beamline.

{#maps_notePfeiffer}
##### Note: Pfeiffer #####
[Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407), used for vacuum system read-back.  May actually be read back via PLC (same PLC that controls the Fermi Chopper Lift).

{#maps_noteEurotherm}
##### Note: Eurotherm #####
Eurotherms in use on MAPS.  Used to control temperature of all top-loading CCRs, Orange cryostats, heaters and furnaces.

{#maps_noteMcLennan}
##### Note: McLennan #####
1. One McLennan is used to control the rotating centre-stick, McLennan-Newport Rotation Stage
   1. Typically used to rotate sample (about vertical axis) into position and hold for periods of several minutes to several hours before moving on to next measurement.<br>

{#maps_noteNeocera}
##### Note: Neocera #####
Neocera is used only occasionally.  [Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

## MAPS Notes ##
Add any notes about special items of equipment, setup or conditions on MAPS that might impact the deployment and configuration of IBEX.

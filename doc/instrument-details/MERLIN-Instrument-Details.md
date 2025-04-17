# MERLIN

This page collects information that will be useful for the implementation of the IBEX control system on MERLIN.

## Background & Timeline ##
Merlin is a high count rate, medium energy resolution, direct geometry chopper spectrometer on TS1 at ISIS. The [MERLIN](https://www.isis.stfc.ac.uk/Pages/Merlin.aspx) web page describes the background to the instrument.

## Control System ##
MERLIN will migrate from the SECI control system to the IBEX control system.

## MERLIN Equipment ##
The equipment listed below is used on MERLIN. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | TBD | T0 Chopper | TBD |  | [see T0 Chopper note](#noteT0Chopper) |
ISIS | TBD | Disk Chopper | TBD |  | [see Disk Chopper note](#noteDiskChopper) |
ISIS | TBD | Fermi Chopper | TBD |  | [see Fermi Chopper note](#noteFermiChopper) |
ISIS | TBD | Fermi Chopper Lift | TBD |  | [see Fermi Chopper Lift note](#noteFermiLift) |
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#noteGalil) | 
??? | ??? | 1 x 4-blade jaws |  |  | [see Jaws note](#noteJaws)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) |[see Pfeiffer note](#notePfeiffer)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#noteMcLennan)
ISIS| | Sample Changer | via McLennan | | [see Sample Changer note](#noteSampleChanger)
ISIS| | Collimator | via Galil| | [see Oscillating Radial Collimator note](#noteORCollimator)
Sumitomo | 4K 100mm TL GM | Top-Loading Closed Cycle Refrigerator | | | [see Sumitomo note](#noteSumitomo)
ILL?| Orange Cryostat | Cryogenic System | RS-232 | | [see Orange Cryostat note](#noteOrangeCryostat)
??? | ??? | Heater | RS-232 | | controlled via Eurotherm
ISIS | RAL | Furnaces | N/A | | controlled via Eurotherm
Neocera | LTC-21 | Temperature Controller | RS-232 | [#1828](https://github.com/ISISComputingGroup/IBEX/issues/1828) | [see Neocera note](#noteNeocera)
McWhan | TIZR | Pressure Cell | N/A | | controlled manually? [see McWhan note](#noteMcWhan)

<a name="noteDAE"></a>
##### Note: DAE #####
Main Detector banks + several fixed monitors.

<a name="noteT0Chopper"></a>
##### Note: MERLIN T0 Chopper #####
T0 chopper is generally operated in read-only mode (i.e. visiting scientists should **_never_** change its settings).<br>
T0 is an ISIS Mk2 chopper.

<a name="noteDiskChopper"></a>
##### Note: MERLIN Disk Chopper #####
User needs the ability to change speed & phase settings.  Also provide the ability to park the disc.<br>
Disk Chopper is an ISIS Mk2 chopper.<br>
At present, scientists often have to press a button on the chopper electronics crate before they can change the settings.  It would be helpful if this was no longer the case (i.e. design IOC to eliminate this extra step, if possible).
We believe this "button" is the local vs computer-control switch.  If set to local, the chopper can only be controlled by the control panel on the crate.  If set to computer-control, IBEX can control the chopper.  Unfortunately, the chopper control system does not serve up the state of the local vs computer-control switch.

<a name="noteFermiChopper"></a>
##### Note: MERLIN Fermi Chopper #####
The fermi chopper is a Jülich model (FZJ - Forschungszentrum Jülich) - custom built for ISIS (therefore unique, although very similar to models installed on MAPS and MARI).  A copy of the communications manual (PDF) is [here](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/MERLIN/Fermi%20Chopper%20Communications%20Protocol.pdf) and the operating manual [here](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/MERLIN/Fermi%20Chopper%20Operating%20Manual.pdf).<br>
The control program will need to include various safety-critical condition monitoring routines (e.g. overspeed, bearing voltage out-of-range).  There are some aspects of the control system which are specific to MERLIN and will need to be incorporated into the IOC.  Ideally, they would be modular (e.g. macro, configuration file) so that the main program would be compatible between the three systems (MERLIN, MAPS, MARI).  David Keymer wrote the original VIs, which are a useful reference.<br>
The Fermi chopper on MERLIN is primarily controlled via scripts.  Scripts are used to calculate the frequency & phase, based on the energy (longer-term this calculation could be folded into IOC).  The OPI should merely display the frequency & phase, not allow the user to change them. <br>
Current system exhibits odd behaviour at 600Hz - see if we can fix this when migrating to IBEX.<br>
Ideally, the Fermi Chopper should have a hierarchy of OPIs - at least, Simple UI (user) & Complex UI (manager).  The current VI has too many details on it - instrument scientists would like to hide these.  Talk with the instrument scientist about what is important when we design the IOC & OPI(s). <br> The 600Hz issue occurs when resending the speed setpoint or "switch drive on and run"
The fermi chopper originally exhibited strange behaviour (Ticket 2628) because the high and low words of the delay setpoint were being sent in the wrong order. The order should be the low word followed by the high word. The device appeared to "take" the setpoint and the setpoint readback was correct, but the actual delay readback would go towards another value instead.

<a name="noteFermiLift"></a>
##### Note: MERLIN Fermi Chopper Lift #####
A lift is used to raise/lower the Fermi chopper.  Lowered means the Fermi chopper is in the beam; raised means it is out of the beam.  It would be helpful if the lift can report its status to the IBEX GUI.<br>
Lift is controlled by a PLC, therefore IBEX can report status of lift by interrogating the PLC.  IBEX will not be able to change the lift position - that will have to be done on the PLC control panel.  Make/type of PLC - to be determined.<br>
Given the above, the requirement that "The Fermi chopper must not be operated (i.e. it must not be spinning) when it is in the raised position.  Lift controls should not be accessible to the user." is automatically satisfied.<br>

<a name="noteGalil"></a>
##### Note: Galil #####
Galils are used to drive the jaws.

<a name="noteJaws"></a>
##### Note: Jaws #####
Single 4-blade jaw-set.  Jaws are driven by Galils.<br>
Apparently, the position of these jaws is reported via a potentiometer (rather than an encoder), which might also have implications for working with limit switches (as in, it won't be possible).

<a name="notePfeiffer"></a>
##### Note: Pfeiffer #####
[Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407), used for vacuum system read-back.  May actually be read back via PLC (same PLC that controls the Fermi Chopper Lift).

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
Three Eurotherms in use on MERLIN.  Used to control temperature of all top-loading CCRs, Orange cryostats, heaters and furnaces.

<a name="noteMcLennan"></a>
##### Note: McLennan #####
1. One McLennan is used to control the rotating centre-stick, McLennan-Newport Rotation Stage
   1. Typically used to rotate sample (about vertical axis) into position and hold for periods of several minutes to several hours before moving on to next measurement.<br>
   1. MERLIN scientists would also like to be able to oscillate the rotating centre-stick (i.e. slowly rotate back & forth between two fixed angles).
2. One McLennan is used to control the Sample Changer.

<a name="noteSampleChanger"></a>
##### Note: Sample Changer #####
The Sample Changer is driven by a McLennan motor.  It is similar (but not identical) to the sample changer used on IRIS.

<a name="noteORCollimator"></a>
##### Note: Oscillating Radial Collimator #####
The Oscillating Radial Collimator (presumably) is driven by a Galil motor controller.  Oscillates at a fixed, low frequency - 0.2Hz.  A similar system is used on LET. The mounting radius is 284.00 mm<br>
**Note: 31-07-2017:** The currently proposed design for the Oscillating Radial Collimator on MERLIN has been scrapped.  A new design will be created.  No need to progress this item until a new design is ready.

<a name="noteSumitomo"></a>
##### Note: Sumitomo #####
MERLIN has a dedicated SUMITOMO 4K 100mm TL GM CCR: [CCR-62](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/ccrs/ccr-parameters---pdf9787.pdf). Not directly computer-controlled  - controlled via Eurotherm.

<a name="noteOrangeCryostat"></a>
##### Note: Orange Cryostat #####
MERLIN will soon have a dedicated Orange Cryostat: [models](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/cryostats/cryostats8445.html) to be determined.  Eurotherm controlled.

<a name="noteNeocera"></a>
##### Note: Neocera #####
Neocera is used only occasionally.  [Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

<a name="noteMcWhan"></a>
##### Note: McWhan #####
[McWhan pressure cell](http://www.isis.stfc.ac.uk/sample-environment/high-pressure-and-gas-handling-/clamped-cells/mcwhan-clamped-cell-8653.html).  McWhan refers to the design of the cell (not to the manufacturer).  Cell cannot be controlled directly from IBEX.  It may be possible to report the current pressure via a device such as a Chell pressure transducer.
See also [General Clamped Cells](http://www.isis.stfc.ac.uk/sample-environment/high-pressure/clamped-cells/general-clamped-cells/general-clamped-cells14180.html) and [High Pressure Gas Cells](http://www.isis.stfc.ac.uk/sample-environment/sample-containers/high-pressure-gas-cells/high-pressure-gas-cells8936.html).

## MERLIN SECI Configs ##
MERLIN has a number of SECI configurations, which need to be migrated.

## MERLIN Genie Scripts ##
The critical OpenGenie scripts, for initialisation and focussing, are in `C:\\OG` (duplicated, more or less, in `C:\\scripts\OG`)

MERLIN has a number of instrument specific Genie scripts. These need to be migrated to genie_python.

## MERLIN Notes ##
Add any notes about special items of equipment, setup or conditions on MERLIN that might impact the deployment and configuration of IBEX.

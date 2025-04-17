This page collects information that will be useful for the implementation of the IBEX control system on SANS2D.
## Background & Timeline ##
SANS2D is a Time-of-Flight Small-Angle Neutron Scattering instrument, on TS2. The [SANS2D](https://www.isis.stfc.ac.uk/Pages/SANS2D.aspx) web page describes the background to the instrument.  Information about the [construction of SANS2D](https://www.facilities.rl.ac.uk/isis/projects/ts2/ts2construction/Instruments/Forms/AllItems.aspx?Paged=TRUE&PagedPrev=TRUE&p_SortBehavior=0&p_FileLeafRef=SaP%20warrant%203%20%28sans2d%20e2-e3%20platform%29%2edoc&p_ID=1829&RootFolder=%2fisis%2fprojects%2fts2%2fts2construction%2fInstruments%2fSANS2D&PageFirstRow=181&&View={776499AB-B00F-4B98-9619-3125F112A0C8}), which is useful background for understanding the operation of the instrument, is also available.

Images of SANS2D equipment can be found here [SANS2D equipment](https://github.com/ISISComputingGroup/IBEX/wiki/SANS2D-equipment-Images-GIF).

The SANS2D instrument scientists have provided a description of the [instrument beamline](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANS2D/Beam_line_descriptors(Sarah%20and%20Najet).docx) and some [schematic drawings](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANS2D/Sans2d_drawing_for%20_IBEX(Sarah%20and%20Najet).pptx).

## Mini-IBEX on SANS2D ##
This section contains relating to the mini-IBEX server on SANS2D.  This information can be deleted once SANS2D has migrated to a full IBEX server.

SANS2D is a SECI instrument, but uses the IBEX interactions for dealing with the CAEN HV.
As such, it has some setup which is not automated, but is needed to function correctly.

If NDXSANS2D is restarted, then, you will need to run start_inst (the version of IBEX is still currently that old, as the CAEN hasn't changed in that time). This should run the reduced version of the start_inst code, but it does kill SECI as well as everything else. After this SECI can be restarted.

If the HVCAEN_01 IOC doesn't automatically start, then either use the console to connect and start the IOC, or use the reset comms button on the CAEN VI which will start the IOC via the console in the background.


## Control System ##
SANS2D will migrate from the SECI control system to the IBEX control system in MMMMMMMM YYYY.

## SANS2D Equipment ##
The equipment listed below is used on SANS2D. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

See also [SANS2D Migration Notes](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANS2D/SANS2D%20Migration%20to%20IBEX%20Notes.docx)

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
ISIS | Mk3 | Chopper | N/A |     | [see Chopper note](#note-chopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
ISIS |  | Aperture | N/A |     | [see Aperture note](#note-aperture-plates)
ISIS |  | Guide | N/A |     | [see Guide note](#note-Guides)
ISIS |  | Gate Valve | N/A |     | [see Gate Valve note](#note-gate-valve)
ISIS |  | Snout Valve | N/A |     | [see Snout Valve note](#note-snout-valve)
Huber|  | Sample Stack | Ethernet |  | [see Huber note](#note-huber)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS] | [see McLennan note](#note-mclennan)
Newport | SMC100 | Motion Controller | RS-232 | [EPICS] | [see Newport note](#note-newport)
ISIS | "big" jaws | 4-blade jaws |  |  | [see Jaws note](#note-jaws)
JJ-XRay| "little" jaws | 4-blade jaws |  |  | [see Jaws note](#note-jaws)
FINS | ??? | PLC |  |  | [see Vacuum System note](#note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
Julabo | FPW55-SL | Water Bath | RS-232 | | [see Water Baths note](#note-water-baths)
Anton Paar | Viscotherm VT2 | Water Bath | RS-232 | | [see Water Baths note](#note-water-baths)
[Knauer](http://www.knauer.net/) | K6 | Electric valve drive | RS232 |  |[see Knauer note](#note-knauer)
[Knauer](http://www.knauer.net/) | 1050 | HPLC pump | ??? | | [see Knauer HPLC note](#note-knauer-hplc)
~Hitachi~ | ~L-7100~ | ~HPLC pump~ | ~???~ | | [see Hitachi note](#note-hitachi)
[Jasco](https://jascoinc.com/products/chromatography/)| LC-4000 | HPLC pump| ??? | | [see Jasco note](#note-jasco)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#note-kepco)
[KEPCO](http://www.kepcopower.com/bop.htm) | BIT 4886 | I/F card | GPIB, RS-232 |  |[see Kepco note](#note-kepco)
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#note-thurlby)
Keithley | 2400 | Source Meter | RS-232 | #1826 | [see Keithley note](#note-keithley)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#note-neocera)
[Linkam](http://www.linkam.co.uk/) | T95 |  | RS232 |  |[see Linkam note](#note-linkam)
Oxford Instruments | Triton | Dilution Fridge | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Mercury | Temperature Controller | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments |  | Cryogenic Equipment | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Birmingham | 17T Magnet | Super conducting magnet | RS-232 |  | [see Birmingham Magnet note](#note-birmingham-magnet)
Goudsmit | 2T Magnet | Electromagnet | RS-232 |  | [see Goudsmit Magnet note](#note-goudsmit-magnet)
~Omega~ | ~iBTHX~ | ~Transmitter~ | ~Ethernet~ | | [see Omega note](#note-omega)
Superlogics| 8018R | Thermocouple | RS-485 | | [see Superlogics note](#note-superlogics)
Superlogics| 8520 | Converter | RS-232| | [see Superlogics note](#note-superlogics)
~ORDELA~ | ~2100N~ | ~Ordela Detector~ |  | | [see Ordela Detector note](#note-ordela-detector)
ISIS | LOQ | Couette Cell |  | | [see Couette Cell note](#note-couette-cell)
ISIS | LOQ | T-Jump Cell |  | | [see T-Jump Cell note](#note-t-jump-cell)
WPI | Aladdin-1000 | Syringe Pump | ??? | | [see Syringe Pumps note](#note-syringe-pumps)
ISIS |  | Detector Trolleys |  | | [see Detector Trolleys note](#note-detector-trolleys)
ISIS |  | Baffle Trolleys |  | | [see Baffle Trolleys note](#note-baffle-trolleys)
ISIS |  | Beamstops |  | | [see Beamstops note](#note-beamstops)

##### Note: DAE #####
See multi-detector and single-detector below.

##### Note: Chopper #####
SANS2D has a Mk3 double-disk chopper.<br>

##### Note: Aperture Plates #####
SANS2D has 5 moveable aperture plates:
1. All plates are controlled by Galils. 
1. Plate positions (UP, CENTRE, DOWN) are defined as motion set-points.
1. Plates can also be driven to any position in their range (but this is not usual).  Plates are sometimes scanned, to check the motion set-points are still valid.
1. Plates are homed by driving the plate to a top limit switch, then driving down to a home switch.
1. Motors must remain energised after moving to prevent plates from falling under their own gravity.
1. Plates **MUST NOT** be moved when the vacuum on (there is an inhibit signal from the vacuum PLC to prevent motion).
1. There is a 6th aperture plate (between moveable plates 1 and 2), but its position is fixed.

##### Note: Guides #####
SANS2D has 5 moveable guides.  Each guide contains two channels - a collimation channel and a guide (super-mirror) channel:
1. All guides are driven by a [Beckhoff](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Beckhoff) which in turn drives Stober drives.
   * The guides are very heavy (> 3 tonnes) - that's why they need Stober drives to move them.
1. Guide positions are defined as motion set-points.
1. Guides can also be driven to any position in their range (but this is not usual).  Plates are sometimes scanned, to check the motion set-points are still valid.
1. Guides are homed by driving to a low limit switch, then driving up to a home switch.
1. Guides **MUST NOT** be moved when the vacuum is on (there is an inhibit signal from the vacuum PLC, forwarded to the Beckhoff to prevent motion).
    * When the permit is re-established, there is a monitor in `custom_records.db` which forwards the PLC value to each of the axis enabled controls.

##### Note: Gate Valve #####
SANS2D has a gate valve.  Its purpose is to allow the scientists to isolate the apertures/guide section of SANS2D from the "snout" section.
1. The gate valve can only be controlled manually.  There is no requirement for it to be controlled by IBEX.

##### Note: Snout Valve #####
The snout valve (also known as the V8 valve) is used to vent the snout section of SANS2D (once it has been isolated from the apertures/guide section by the gate valve).
1. The snout valve can only be controlled manually.  However, it is monitored by the PLC; IBEX should display the monitored values to the user.

##### Note: Scraper Aperture #####
SANS2D has a scraper aperture.  
1. Driven by a Galil.
1. Positions are defined as motion set-points.
1. Scraper can also be driven to any position in its range (but this is not usual).  Scraper is sometimes scanned, to check the motion set-points are still valid.

##### Note: Jaws #####
SANS2D has two sets of jaws:
1. One set of "small" or "little" JJ-XRay jaws, controlled by Galil.  These are only used for GISANS experiments.  When not in use they are not installed on the instrument. 
2. One set of "large" or "big" jaws, which are located inside the tank.  Also controlled by Galil.
   * The "zero-position" of the big jaws is set to be on the centre line of the vacuum tank.  However, because the detectors on SANS2D are normally offset to the left (looking towards the rear of the tank (i.e. in the direction that neutrons travel)), the big jaws are normally set to the left of the centre line of the tank.

##### Note: Huber #####
1. [Huber](http://www.xhuber.de/en/home/).
1. According to Huber's web-site, a Huber SMC9000 is a motion controller. 
   * However, at ISIS, the Huber is controlled via a Galil.  See [#3502](https://github.com/ISISComputingGroup/IBEX/issues/3502), especially for the note about amplifier cards.
   * See [SMC 9300](http://www.xhuber.de/en/product-groups/3-control-systems/smc-9300/) which appears to be the latest of the 9000-series and [SMC 9000](http://www.xhuber.de/fileadmin/user_upload/downloads/usermanuals/9000_1103.pdf).
1. SANS2D uses the Huber mini sample stack, which has its own controller (not Galil).

##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.

##### Note: Newport #####
1. [Newport SMC100](https://www.newport.com/f/smc100-single-axis-dc-or-stepper-motion-controller)
1. EPICS drivers for [Newport devices](https://epics.anl.gov/modules/manufacturer.php#Newport)
1. See also [#824](https://github.com/ISISComputingGroup/IBEX/issues/824)

##### Note: Vacuum System #####
The vacuum system on SANS2D is controlled by a FINS PLC.  IBEX does not control the PLC, but it should display information from the PLC.

TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANS2D/SANS2D_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

##### Note: Water Baths #####
1. Julabo Water Bath (apparently the following Julabos: WB15, WB16 )
   * consult the [Julabo commands](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/backend_system/IOCs/julabo_commands.xlsx) spreadsheet for specific details of which set of commands is used by these water baths.
1. Anton Paar Viscotherm VT2 (apparently the following: WB28).  It appears the Viscotherm VT2 is no longer manufactured.
1. See also [Water Baths](https://www.isis.stfc.ac.uk/Pages/Water-Baths.aspx) list

##### Note: KEPCO #####
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).<br>  See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)
   * LabVIEW VI is here: `C:\LabVIEW Modules\Drivers\KEPCO 100-10MG`
1. [Kepco BIT 4886](http://www.kepcopower.com/bit.htm) is an interface card for Kepco bi-polar ([BOP](http://www.kepcopower.com/bop.htm)) power supplies.
   * LabVIEW VI is here: `C:\LabVIEW Modules\Drivers\Kepco 4886 Serial`

##### Note: Thurlby #####
[Thurlby Thandar Instruments](https://www.aimtti.com/)
1. [Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)
   * see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).
1. See also [#3784](https://github.com/ISISComputingGroup/IBEX/issues/3784)

##### Note: Hitachi #####
Hitachi L-7100 HPLC pump (no longer supported at ISIS).  ~Can't find L-7100 on [Hitachi web-site](http://www.hitachi-hightech.com/global/about/corporate/group/hhs (may be obsolete).  Check existing SECI VI for logic and manual.~
   * Update (27-06-2019): Hitachi pumps are being retired.  No longer any need to support them.  See [#3780](https://github.com/ISISComputingGroup/IBEX/issues/3780)
   * SANS2D will not be using Hitachi pumps in future.  They will use the [Knauer](#note-knauer-hplc) or Jasco HPLC pumps.

##### Note: Knauer #####
1. Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
   * K-6 model appears to have been superseded.  Check existing SECI VI for logic and manual.
1. See also [#3781](https://github.com/ISISComputingGroup/IBEX/issues/3781)

##### Note: Knauer HPLC #####
Knauer HPLC 1050 [Knauer HPLC 1050 is discontinued.](https://www.knauer.net/en/discontinued-smartline-pump-1050-successor-azura-p-61l/p14161).  
1. Check existing SECI VI for logic and manual.
1. Support for Knauer HPLC 1050 is implemented via the following tickets:
[#3262](https://github.com/ISISComputingGroup/IBEX/issues/3262), 
[#3782](https://github.com/ISISComputingGroup/IBEX/issues/3782), 
[#3881](https://github.com/ISISComputingGroup/IBEX/issues/3881), 
[#4004](https://github.com/ISISComputingGroup/IBEX/issues/4004)

##### Note: Jasco #####
[JASCO HPLC pump](https://jascoinc.com/products/chromatography/hplc/modules/hplc-pumps/) is a new (for ISIS) model of HPLC pump.  Jasco pumps are replacing the old Hitachi pumps.
   * See [#3923](https://github.com/ISISComputingGroup/IBEX/issues/3923), [#4004](https://github.com/ISISComputingGroup/IBEX/issues/4004), [#4198](https://github.com/ISISComputingGroup/IBEX/issues/4198), [#4199](https://github.com/ISISComputingGroup/IBEX/issues/4199).

##### Note: Keithley #####
1. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter)
1. See also [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176)

##### Note: Neocera #####
* Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)
* An IOC & OPI for the Neocera were created in ticket [#1828](https://github.com/ISISComputingGroup/IBEX/issues/1828)

##### Note: Linkam #####
There are VIs for this.<br>
See also [Linkam T95 controller](http://www.linkam.co.uk/t95-system-controllers/) and tickets [#1106](https://github.com/ISISComputingGroup/IBEX/issues/1106), [#1496](https://github.com/ISISComputingGroup/IBEX/issues/1496), [#1509](https://github.com/ISISComputingGroup/IBEX/issues/1509).

##### Note: Oxford Instruments #####
1. Support for OI ITC503 created as part of [#2593](https://github.com/ISISComputingGroup/IBEX/issues/2593)
1. Support for Mercury Temperature Controller was created as part of [#2840](https://github.com/ISISComputingGroup/IBEX/issues/2840)
1. Dilution fridge: [models](https://www.isis.stfc.ac.uk/Pages/Dilution-Refrigerators.aspx) to be determined.
   * Triton LabVIEW Driver : C:\LabVIEW Modules\Drivers\Triton
   * Triton Documentation : C:\LabVIEW Modules\Drivers\Triton\Documentation
   * See also [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)

##### Note: Birmingham Magnet #####
The Birmingham 17T magnet is a superconducting magnet owned by the University of Birmingham.  The magnet comes with its own control devices & PC, all mounted in a rack.  It gets loaned out to various facilities around the country, including ISIS.  IBEX only needs to communicate with the Birmingham control PC.
1. There is information about the Birmingham 17T magnet here: `C:\LabVIEW Modules\Drivers\Birmingham 17T Magnet`.
1. Further discussion of the Birmingham 17T magnet in [#4523](https://github.com/ISISComputingGroup/IBEX/issues/4523).

##### Note: Goudsmit Magnet #####
1. [Goudsmit Magnet](https://www.isis.stfc.ac.uk/Pages/Goudsmit-Electromagnet.aspx).
1. [Goudsmit Magnet User Manual](https://www.isis.stfc.ac.uk/Pages/goudsmit-electromagnet6531.pdf).
1. Used in conjunction with a Danfysik PSU.
1. Further information is available here: `C:\LabVIEW Modules\Large Scale Structures\Goudsmit_magnet`.

##### ~Note: Omega~ #####
~[OMEGA™ iBTHX transmitter](https://www.omega.co.uk/pptst/IBTX_IBTHX.html) is a device to monitor and record barometric pressure, temperature, relative humidity, and dew point over an Ethernet network or the LOQnet.~

~**NOTE:** LOQ has switched from the OMEGA™ iBTHX (because it is unreliable) to MOXA ioLogik devices.  Should we do the same on SANS2D?~

##### Note: Superlogics #####
A Superlogics thermocouple 8018R device is used to monitor temperatures on SANS2D.  The 8018R device has a RS-485 interface.  A Superlogics RS-485/RS-232 converter is used to convert the interface to RS-232.
1. [Superlogics 8018R Thermocouple](https://www.superlogics.com/data-acquisition-99/data-acq-sensor-specific/sensor-specific-rs485/8018r.html).  The 8018R supports up to 8 input channels.
1. [Superlogics 8520 Converter](https://www.superlogics.com/data-acquisition-99/data-acq-converters/8520.html).

##### Note: Ordela Detector #####
1. [ORDELA](http://www.ordela.com/) (Oak Ridge Detector Laboratory) is a manufacturer of area-detector devices.  It is a spin-off from Oak Ridge National Laboratory.
1. The ORDELA device is no longer used on SANS2D.

##### Note: Couette Cell #####
1.  The Couette Cell is driven by a [McLennan PM1000](#note-mclennan) (compatible with a PM600).
1. See also [#3105](https://github.com/ISISComputingGroup/IBEX/issues/3105)

##### Note: T-Jump Cell #####
1. The T-Jump Cell is driven by a Keithley 2400.
1. See also [#3175](https://github.com/ISISComputingGroup/IBEX/issues/3175)

##### Note: Syringe Pumps #####
1. [WPI Aladdin-1000 Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps/al1000-220.aspx)
1. See also [#3787](https://github.com/ISISComputingGroup/IBEX/issues/3787)

##### Note: Detector Trolleys #####
SANS2D has two detector trolleys (in the vacuum tank).  One for the front detector, one for the rear detector.  The trolleys allow the detectors to be move longitudinally along the vacuum tank (z-direction in SANS2D geometry).  The detector trolleys also support beamstops.
   * driven by Galils

##### Note: Baffle Trolleys #####
SANS2D has two baffle trolleys (in the vacuum tank).  One for the front baffle, one for the rear baffle.  The baffles are both positioned between the front and rear detectors.  The baffle trolleys allow the baffles to be move longitudinally along the vacuum tank (z-direction in SANS2D geometry).  
   * driven by Galils

##### Note: Beamstops #####
SANS2D has beamstops on the front and rear detectors
1. Front Detector:
   * has a single beamstop, mounted on the detector trolley.  Rotates in the plane of the detector array.  The beamstop must not be moved when the detector is rotated (in SECI this requirement is implemented as a software inhibit).
   * has a strip beamstop, mounted on the detector trolley.  Moves linearly across the face of the detector array.  Primarily used for commissioning purposes (usually "parked" out of the way).
1. Rear Detector: 
   * has three beamstops, mounted on a pillar attached to the detector trolley.  Pillar moves linearly across the face of the detector array.  The individual beam stops move independently up/down on the pillar.
   * has a strip beamstop, mounted on the detector trolley.  Moves linearly across the face of the detector array.  Primarily used for commissioning purposes (usually "parked" out of the way).

## SANS2D Notes ##
SANS2D has the following specialist panels/systems:
1. SANS2D CAEN
1. SANS2D Detector Temperature
1. SANS2D DLS
1. LOQ Couette Cell
1. LOQ T-Jump Cell
1. SANS2D Tank
1. SANS2D Guide
1. SANS2D Vacuum System

SANS2D has the following devices under motion control:
1. goniometer
1. jaws
1. rotation stage
1. sample changer 2-axis
1. sample changer
1. stirring stages
   * See also [ControlsWork #553](https://github.com/ISISComputingGroup/ControlsWork/issues/553)
1. XYZ stage
1. 5 guide stages - driven by [Baldor drives](#sans2d-baldor-drives).

Specialist requirements:
1. There is a requirement within SANS2D to inhibit the movement of the detectors when they are powered (the CAEN HV is ON)

## SANS2D SECI Configs ##
Document information about SANS2D SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
SANS2D_place_holder1.conf              | -                                                  | dd/mm/yyyy    | -        |
SANS2D_place_holder2.conf              | -                                                  | dd/mm/yyyy    | -        |

## SANS2D Genie Scripts ##
Similarly, Document information about SANS2D SECI Genie scripts here.

## SANS2D Baldor Drives ##
SANS2D has 5 guides on the front end. Each of these has a significant weight - ~3 tonnes. The motors used to lift the guides are servo motors.  Galil controllers cannot provide sufficient power to motors capable of lifting such weights.  As a result, some Baldor drives were introduced to provide the power required to lift these guides. They are digital motion controllers that can communicate with a control system and have settings in each controller to drive the motor.

However, ISIS uses them as pseudo dumb power amplifiers only. A Galil drives the axes like a servo - it provides an analogue signal to the Baldor to ask it to drive, but no core power. The Baldor drives the axes.  Therefore, from the point of view of SECI or IBEX, the Baldor drives appear as Galil axes. 

The Baldor drives do need to be set up – but this is done independently. Historically, this entire arrangement caused a lot of problems during commissioning.  There is a bespoke homing routine in use with this setup (the need for such a thing has been questioned but, for now, a bespoke homing routine continues in use).

**Important Note:** These are the only Baldor axes at ISIS.  There is limited support (apparently Baldor has been bought out since SANS2D was commissioned). For SANS2D to operate, the axes must be operational.  The motion control group are considering whether to convert these axes to a Beckhoff system that is supportable.  At the present time (November 2018) no decision has been taken to replace the Baldor drives.  However, people are aware that support for these is limited.

## Additional Information ##
The backlash distance in IBEX converted from SECI was `-2` however(Front Det X), IBEX doesn't like it so when a motor is moved to a negative direction, it uses BVEL speed instead of VELO [5675](https://github.com/ISISComputingGroup/IBEX/issues/5657).

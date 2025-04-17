This page collects information that will be useful for the implementation of the IBEX control system on ENGIN-X.
## Background & Timeline ##
ENGIN-X is a long established instrument at ISIS, on TS1. The [ENGIN-X](http://www.isis.stfc.ac.uk/instruments/engin-x/engin-x2900.html) web page describes the background to the instrument.  ENGIN-X is dedicated to engineering science experiments. It is optimized for the measurement of strain, and thus stress, deep within crystalline materials.

## Control System ##
ENGIN-X will migrate from the SECI control system to the IBEX control system.

## ENGIN-X Equipment ##
The equipment listed below is used on ENGIN-X. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | N/A | Shutter | N/A| | [see Shutter note](#noteShutter)
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | Monitors |  | | [#265](https://github.com/ISISComputingGroup/IBEX/issues/265) | [see Monitors note](#noteMonitors)
ISIS | Mk3 Chopper | Chopper | Ethernet/.NET | [#169](https://github.com/ISISComputingGroup/IBEX/issues/169) | [see Mk3 Chopper note](#noteMk3Chopper) |
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#noteGalil) | 
[LINMOT](http://www.linmot.com/) | [P0x-23](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf) | Linear Motors and Motion Controller | RS-232 | [#2098](https://github.com/ISISComputingGroup/IBEX/issues/2098) | [see LinMot note](#noteLinMot) |
??? | ??? | 3 x 4-blade jaws |  |  | [see Jaws note](#noteJaws)
??? | ??? | 2 x collimators |  |  | [see Collimators note](#noteCollimators)
xxxx | 5-axis Sample Positioning System | | | [#435](https://github.com/ISISComputingGroup/IBEX/issues/435) | [see Sample Positioning System note](#noteSampleStack)
[Cybaman](http://www.cybamantech.co.uk/) | 3-axis Sample Positioning System |  |  |  | [see Cybaman Positioning System note](#noteCybaman)
xxxx | xxxx | ISIS Vacuum System | N/A |  | Analog only.  No computer control.
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
[Instron](http://www.instron.co.uk/) | Stress Rig | xxxx | GPIB | [#2109](https://github.com/ISISComputingGroup/IBEX/issues/2109) - [#2116](https://github.com/ISISComputingGroup/IBEX/issues/2116) | [see Stress Rig note](#noteStressRig)
SuperLogics | POE-8019(?) | Thermocouple Box | Ethernet  | [#2378](https://github.com/ISISComputingGroup/IBEX/issues/2378)  | [see Thermocouple Box note](#noteThermocoupleBox)
NI | GPIB-ENET/100| Data Acquisition Box | Ethernet | TBD | [see NI High-Speed DAQ Box note](#noteNI_DQA_Box) 

Computer control of the equipment listed below is is considered a "nice-to-have" for ENGIN-X. 

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
Leica | TM5100A | Theodolite | TBD | TBD | [see Theodolite note](#noteTheodolite)
xxxx | xxxx | Function Generator | TBD | TBD | 
xxxx | xxxx | Oscilloscope | TBD | TBD | 
[TDK Lambda](https://www.emea.lambda.tdk.com/uk/products/genesys-1u) | Genesys | Power Supply | TBD | [#983](https://github.com/ISISComputingGroup/IBEX/issues/983)| [see TDK Lambda Genesys note](#noteTDKGenesys)
Berkeley | MCP Detector | Neutron Camera | TBD | TBD | [see Berkeley MCP Detector note](#noteBerkeleyMCP) 
Basler | Pilot | Camera | GigE | TBD | [see Basler Pilot Camera note](#noteBaslerCamera) 
[Huber](https://www.xhuber.com/en/products/1-components/12-rotation/eulerian-cradles/)| [511](https://www.xhuber.com/en/products/1-components/12-rotation/eulerian-cradles/511/) | Eulerian Cradle| TBD| TBD | [see Huber note](#noteHuber)

<a name="noteShutter"></a>
##### Note: Shutter #####
ENGIN-X and HRPD share the same primary shutter (which is directly equivalent to the single shutter used on other instruments).  ENGIN-X and HRPD also have their own secondary shutters (so that each instrument can operate independently of the other when the primary shutter is open.
1. When the primary shutter is closed, neither instrument receives neutrons.  The status of the primary shutter is available in the same way as it is for any other instrument (i.e. via the appropriate PV).
1. When the primary shutter is open, ENGIN-X receives neutrons only if the secondary shutter is also open.  The status of the secondary shutter is not available to IBEX.

The IBEX dashboard should continue to report the status of the primary shutter.<br>
**Note:** IBEX only ever reports the status of the shutter.  IBEX _**never**_ controls the shutter (control of the shutter is part of the instrument safety system and is strictly outside the scope of IBEX).

<a name="noteDAE"></a>
##### Note: DAE #####
Main Detector banks (transmission bank and diffraction banks) + 2 monitors.

<a name="noteMonitors"></a>
##### Note: Monitors #####
2 fixed monitors.  Monitors operate in histogram mode.

<a name="noteMk3Chopper"></a>
##### Note: ISIS Mk3 Choppers #####
ENGIN-X has two ISIS Mk3 double-disk choppers.

<a name="noteLinMot"></a>
##### Note: LinMot #####
HRPD uses LinMot P0x-23 motors, controlled by LinMot drives.<br>
[LinMot User Manual](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf)

<a name="noteGalil"></a>
##### Note: Galil #####
As of 04/08/2017, ENGIN-X has a single Galil (support for up to 8 axes).  5 of these axes are used to control the Sample Positioning System.  2 more are used to control the collimators.<br>
When the collimators are further upgraded to 4 motors, an additional Galil rack will be required.  All 4 collimator motors should be moved to the new rack (so that all 4 can be exclusively controlled using EPICS).

<a name="noteJaws"></a>
##### Note: Jaws #####
As of April 2017, ENGIN-X has three sets of 4-blade jaws.  All three sets of jaws are driven by LinMot P0x-23 motors.  The first two sets of jaws (jaws-1 and jaws-2, counting downstream from the shutter) are buried under shielding.  The third set of jaws (jaws-3) is located near the beam snout (i.e. close to the sample, not under shielding).  

jaws-1 and jaws-2 are "traditional" four-blade jaws (i.e. each blade can be operated independently - 4 degrees of freedom).

jaws-3 also has 4 blades, but they operate as 2 linked pairs.  In jaws-3:
1. the north-south pair operate symmetrically and simultaneously.
1. the east-west pair operate symmetrically and simultaneously.

In effect, jaws-3 has only 2 degrees of freedom (instead of 4, if the blades could operate independently).  In practice, you can only control the horizontal & vertical gaps; you cannot control the position of the centre of the blades.

The initial jaws settings are documented here: [ENGIN-X Jaws Settings](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/EnginX-Jaws)

There is a plan to upgrade the third set of jaws (jaws-3) to a 4-independent-blade set, which will be driven by Galil controllers.  The timing of this upgrade is yet to be determined.  

<a name="noteCollimators"></a>
##### Note: Collimators #####
Two collimator units (to be installed in summer 2017).  Each collimator is driven by a single Galil controlled axis.

<a name="noteSampleStack"></a>
##### Note: Sample Positioning System #####
Sample Positioning System on ENGIN-X has 5 degrees of freedom.  All axis motors are controlled by Galil.
1. X - translation parallel to the beam (in the horizontal plane)
1. Y - translation perpendicular to the beam (in the horizontal plane)
1. Z - translation perpendicular to the beam (in the vertical plane)
1. W (omega) - rotation about the vertical axis
1. S (slit rails) - translation of slits (i.e. jaws-3) parallel to the beam (in the horizontal plane)

ENGIN-X uses a jog box for positioning samples.  IBEX will need to work with the existing jog-box interlock mechanism (for safety reasons).  There is an existing Galil program (i.e. a program that gets loaded into the Galil firmware) for communicating with the jog box.  IBEX needs to be set up to load this program alongside the Galil IOC (speak to Gareth to discover how to do this).

**Note:** ENGIN-X would like an IMAT-style tomography stack.  However, at the current time (April 2017), there are insufficient Galil axes on ENGIN-X to permit such a device to be used.  Need to wait until additional Galil axes can be made available.

<a name="noteCybaman"></a>
##### Note: Cybaman Positioning System #####
3 axis sample positioning system (manufactured by [Cybaman](http://www.cybamantech.co.uk/)) - 3 degrees of freedom.  Currently has its own, independent control system (which runs on a separate PC).<br>
There is also a simple LabVIEW VI which can be used to drive the Cybaman. <br>
To drive the Cybaman directly from EPICS, we'd probably need to create our own driver - this might be a lot of work for very little gain.

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
There are 3 Eurotherm devices on ENGIN-X, arranged in a single crate.  Typically used to control temperature of CryoBox and Furnace devices.

<a name="noteStressRig"></a>
##### Note: Stress Rig #####
Used to put stress on samples under test on ENGIN-X.  This device is shared between IMAT and ENGIN-X.
The ICP discussion site contains [Stress Rig documentation](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FInstron%20Stress%20Rig&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}).<br>
**Note:** Stress Rig uses GPIB communications protocol.<br>
The Stress Rig is driven from its own PC (fitted with a GPIB card).  IBEX communicates with the Stress Rig PC via the GPIB card.  See [#2338](https://github.com/ISISComputingGroup/IBEX/issues/2338) for ideas on how to test the Stress Rig IOC.

<a name="noteHuber"></a>
##### Note: Huber #####
2-degree of freedom Eulerian cradle.  The Huber can be driven from a Galil.  Gareth has created a VI to control this via SECI.

<a name="noteTheodolite"></a>
##### Note: Theodolite #####
ENGIN-X has a Leica Theodolite TM5100A, which is used to survey the instrument.  There is currently a VI to control the Theodolite from LabVIEW, but none of the current ENGIN-X team has ever needed to use the Theodolite.<br>
The [Leica web-site](https://leica-geosystems.com/en-gb) no longer lists a TM5100A model of theodolite.  It does, however, list a [TM6100A](https://www.hexagonmi.com/en-GB/products/industrial-theodolites-and-laser-stations/leica-tm6100a-industrial-theodolite) model.

<a name="noteThermocoupleBox"></a>
##### Note: Thermocouple Box #####
ENGIN-X has a Thermocouple Box, which allows for the connection of up to 8 thermocouples.  This device is often used with the furnace.  Hardware is from [SuperLogics](http://www.superlogics.com).  The device sounds like it is one of these: [POE-8019](https://web.archive.org/web/20171015083151/http://www.superlogics.com/data-acquisition/ethernet/POE-8019/86-5660.htm#). Need to consult with Matt North about continued support for this device.<br>
The command set for the Thermocouple Box is, apparently, quite simple.  It should not be too difficult to reproduce the capabilities of the existing LabVIEW VI in EPICS.

<a name="noteTDKGenesys"></a>
##### Note: TDK Lambda Genesys Power Supply #####
ENGIN-X has previously used a TDK Lambda Genesys power supply, although it was not connected to SECI.  Ask ENGIN-X team if they will need IBEX to communicate with a TDK Lambda Genesys power supply.<br>
**Note:** a generic power supply IOC & OPI would be a useful thing.

<a name="noteNI_DQA_Box"></a>
##### Note: NI High-Speed DAQ Box #####
ENGIN-X has a National Instruments (NI) [GPIB-ENET/100](http://sine.ni.com/nips/cds/view/p/lang/en/nid/10622) Ethernet-to-GPIB controller for high-speed data acquisition. It has been used to make independent voltage measurements from various points on the stress rig.  There are two options for collecting these voltage measurements in future:
1. continue to use the GPIB-ENET/100 box (integration with IBEX would need prior investigation)
2. use a "data-into-DAE" card to acquire the voltage data and embed it in the NeXus data file (will need prior consultation with the detector electronics team).

**Note:** according to the NI web-site, the GPIB-ENET/100 box is now considered obsolete.

Need to discover how data acquired by the NI High-Speed DAQ Box gets written to file.  We could use a signal generator to drive the DAQ box for testing purposes.

<a name="noteBerkeleyMCP"></a>
##### Note: Berkeley MCP Detector #####
ENGIN-X would like to use the Berkeley MCP detector (neutron camera) used on IMAT.  This device is controlled by its own PC, but it uses EPICS to communicate with IBEX.  The ENGIN-X team would like to set up the Berkeley MCP detector in the same way as IMAT. <br>
**Note:** the ENGIN-X team would also like to use a hardware box to delay the signal between the Berkeley MCP detector and its control PC.  This hardware box uses a USB interface.

<a name="noteBaslerCamera"></a>
##### Note: Basler Pilot Camera #####
ENGIN-X are consider whether it would be useful to use a high-performance GigE camera to acquire images.  A [Basler Pilot](https://www.baslerweb.com/en/products/cameras/area-scan-cameras/pilot/) area scan camera is being considered.<br>
**Note:** GigE area scan cameras can generate a lot of data (hence the need for a gigabit Ethernet interface).  If there is a decision to use a GigE area scan camera, we will need to consider acquiring additional Ethernet cards (to avoid swamping the current network) or a separate PC to capture images.

## ENGIN-X Notes ##
* For each run, ENGIN-X generates .log and .txt files from the NeXus data file.  The .txt files are "3-column" files (as opposed to the "2-column" data files used on other instruments.  We need to determine if these "3-column" files are still required in the future and, if so, document how these "3-column" files are generated.
* OpenGENIE is currently used to analyse ENGIN-X data.  In due course, the ENGIN-X team should consider migrating to Mantid.

## ENGIN-X SECI Configs ##
Document information about ENGIN-X SECI configs here.

## ENGIN-X Genie Scripts ##
Similarly, Document information about ENGIN-X SECI Genie scripts here.
* ENGIN-X currently has one large master OpenGENIE script, which is used in (almost?) all runs.  This script has to be migrated to genie_python (or to a library of genie_python methods).
* ENGIN-X also uses a position compensation script (to compensate for the movement of the target position as the sample is stretched on the stress rig).

# MARI

This page collects information that will be useful for the implementation of the IBEX control system on MARI.

## Background & Timeline ##
MARI is a chopper spectrometer on TS1 at ISIS. The [MARI](https://www.isis.stfc.ac.uk/Pages/mari.aspx) web page describes the background to the instrument.

## Control System ##
It is proposed that MARI will migrate from the SECI control system to the IBEX control system in time for Cycle 2018/04.

## MARI Equipment ##
The equipment listed below is used on MARI. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 3 | Detector Electronics | Ethernet | | [see DAE note](#note-dae)
ISIS | MK3| T0 Chopper | N/C |  | [see T0 Chopper note](#note-mari-t0-chopper) |
ISIS | MK3 | Disk Chopper | Ethernet | EPICS | [see Disk Chopper note](#note-mari-disk-chopper) |
FZJ | Analogue Drive | Fermi Chopper | RS232 | EPICS | [see Fermi Chopper note](#note-mari-fermi-chopper) |
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#note-galil) | 
??? | ??? | 1 x 4-blade jaws |  |  | [see Jaws note](#note-jaws)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) |[see Pfeiffer note](#note-pfeiffer)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#note-eurotherm)
Oxford Instruments | Dilution Fridge | Cryogenic System | RS-232 | | [see Oxford Instruments note](#note-oxford-instruments)
Oxford Instruments | Triton | Cryogen-Free Dilution Fridge | Ethernet | | [see Oxford Instruments note](#note-oxford-instruments)
ISIS| | Transmission Monitor | via McLennan | | [see Transmission Monitor note](#note-transmission-monitor)
Neocera | LTC-21 | Temperature Controller | RS-232 | [#1828](https://github.com/ISISComputingGroup/IBEX/issues/1828) | [see Neocera note](#note-neocera)
ISIS | One-Off | Cryogenic Sample Changer | ENET & RS232 | | [see Sample Changer note](#note-sample-changer)

##### Note: DAE #####
Main Detector banks + several fixed monitors.  MARI uses DAE-3.

##### Note: MARI T0 Chopper #####
T0 chopper is generally operated in read-only mode (i.e. visiting scientists should **_never_** change its settings).<br>
T0 is an ISIS MK3 chopper.

##### Note: MARI Disk Chopper #####
MARI has two ISIS MK3 disk choppers.  User needs the ability to change speed & phase settings.<br>
Ideally, the two choppers should seen as a single pair by visiting scientists; instrument scientists need the ability to control the two choppers independently (e.g. for diagnostic purposes).

##### Note: MARI Fermi Chopper #####
The fermi chopper is a Jülich model (FZJ - Forschungszentrum Jülich) - custom built for ISIS (therefore unique, although very similar to models installed on MAPS and MERLIN).  A copy of the communications manual (PDF) is [here](https://stfc365.sharepoint.com/:b:/r/sites/ISISExperimentControls/ICP%20Discussions/MAPS/Fermi%20Chopper%20Communications%20Protocol.pdf?csf=1&web=1&e=DXEcym) and the operating manual [here](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FMERLIN).<br>
The control program will need to include various safety-critical condition monitoring routines (e.g. overspeed, bearing voltage out-of-range).  There are some aspects of the control system which are specific to MARI and will need to be incorporated into the IOC.  Ideally, they would be modular (e.g. macro, configuration file) so that the main program would be compatible between the three systems (MERLIN, MAPS, MARI).<br>
David Keymer wrote the original VIs, which are a useful reference.<br>
The Fermi chopper on MARI is primarily controlled via scripts.  Scripts are used to calculate the frequency & phase, based on the energy (longer-term this calculation could be folded into IOC).  The OPI should merely display the frequency & phase, not allow the user to change them. <br>
Ideally, the Fermi Chopper should have a hierarchy of OPIs - at least, Simple UI (user) & Complex UI (manager).  The current VI has too many details on it - instrument scientists would like to hide these.  Talk with the instrument scientist about what is important when we design the IOC & OPI(s). <br>

<a name="note-galil"></a>
##### Note: Galil #####
A Galil is used to drive the jaws.

<a name="note-jaws"></a>
##### Note: Jaws #####
Single 4-blade jaw-set.  Jaws are driven by a Galil.

##### Note: Pfeiffer #####
[Model TPG 300](https://www.pfeiffer-vacuum.com/en/products/measurement/modulline/controllers/?detailPdoId=3407), used for vacuum system read-back.  May actually be read back via PLC.

##### Note: Eurotherm #####
Eurotherms are in use on MARI.  Used to control temperature of all top-loading CCRs, Orange cryostats, heaters and furnaces.

##### Note: Oxford Instruments #####
1. Dilution fridge: Triton: Cryogen-Free Dilution Fridge
1. Historically, MARI uses dilution fridges and Blue cryostats only very rarely.  Most low temperature experiments use CCRs and Orange cryostats.

##### Note: Transmission Monitor #####
MARI has a single, fixed transmission monitor.

##### Note: Neocera #####
Neocera is used only occasionally.  [Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

##### Note: Sample Changer #####
This is a single-axis cryogenic sample changer with up to 4 positions (sample cans).<br>
The changer is now in use and runs with a Mclennan controller via RS232/MOXI.
There is still a plan to use a Beckhoff controller in future.<br>
The changer is driven by an instrument script which has the rotation angle corresponding to each position hard-coded in.<br>
The script will also perform a home scan on request. This is usual done when samples are mounted.<br>
The changer should only be rotated in one direction, otherwise there is a risk the head will unscrew itself. The instrument script knows and enforces this condition.<br>
The temperature control will be handled by a Eurotherm.<br>
[Project Details](https://stfc365.sharepoint.com/sites/ISISProject-1122) and 
[Project Plan](https://tasks.office.com/stfc365.onmicrosoft.com/en-US/Home/PlanViews/8bdu_4UTBUeZwF_PB8SLIpYAESGr)

## MARI SECI Configs ##
MARI has a number of SECI configurations, which need to be migrated.

## MARI Genie Scripts ##
Critical OpenGenie scripts for initialisation and focussing.

MARI has a number of instrument specific Genie scripts. These have now been migrated to genie_python.

## MARI Notes ##
1. MARI does not currently use a script generator, but there is interest in having one in the future.

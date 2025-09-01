# SXD

This page collects information that will be useful for the implementation of the IBEX control system on SXD.
## Background & Timeline ##
SXD is a Single Crystal Diffractometer, on TS1, which uses the time-of-flight techniques. The [SXD](https://www.isis.stfc.ac.uk/Pages/SXD.aspx) web page describes the background to the instrument.

## SXD Equipment ##
The equipment listed below is used on SXD. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 / 3 | Detector Electronics | Ethernet | | [see DAE note](#sxd_note-dae)
N/A | N/A | N/A | N/A |  | [see Chopper note](#sxd_note-chopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#sxd_note-mclennan)
[LINMOT](http://www.linmot.com/) | [P0x-23](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf) | Linear Motors and Motion Controller | RS-232 | [#2098](https://github.com/ISISComputingGroup/IBEX/issues/2098) | [see LinMot note](#sxd_note-linmot) |
??? |  | 4-blade jaws |  |  | [see Jaws note](#sxd_note-jaws)
ISIS | ??? | Mirror|  |  | [see Mirror note](#sxd_note-mirror)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#sxd_note-vacuum)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#sxd_note-vacuum)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#sxd_note-eurotherm)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#sxd_note-keithley)
Kammrath and Weiss | DDS 32 | Tensile Rig | RS-232 | | [see Kammrath and Weiss note](#sxd_note-kammrath-and-weiss)
Neocera | LTC-21 | Temperature Controller | RS-232 | | [see Neocera note](#sxd_note-neocera)
ISIS | ??? | Helium Gauge |  |  |[see Helium Gauge note](#sxd_note-helium-gauge)
B&WTek | i-Raman Plus | Raman Spectrometer| | | [see mini-Raman Spectrometer note](#sxd_noteRamanSpect)

{#sxd_note-dae}
##### Note: DAE #####
Now using DAE-3.  See multi-detector and single-detector below.

{#sxd_note-chopper}
##### Note: Chopper #####
SXD does not use a chopper.

{#sxd_note-mclennan}
##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.

{#sxd_note-linmot}
##### Note: LinMot #####
SXD uses LinMot P0x-23 motors to move its jaws, controlled by LinMot drives.  SXD also uses LinMot motors to move the Mirror.<br>
[LinMot User Manual](http://www.linmot.com/fileadmin//user_upload/Downloads/software-firmware/servo-drives/linmot-talk-1-3-x/UserManual_1r3_e_recent.pdf)

{#sxd_note-mirror}
##### Note: Mirror #####
The mirror on SXD is located upstream from the jaws. Its purpose is to direct laser light from an external laser to the sample position. The reason for the mirror is that we cannot have the laser in the vacuum of the flight path, but we can have a mirror. Most of the time it is parked on the side away from the direct beam.  The mirror is positioned using LinMot motors.

{#sxd_note-jaws}
##### Note: Jaws #####
Provide information about SXD jaws.

{#sxd_note-vacuum}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

{#sxd_note-eurotherm}
##### Note: Eurotherm #####
Eurotherms are used to control temperature Orange Cryostat, CCR and Furnace devices.

{#sxd_note-keithley}
##### Note: Keithley #####
1. [Keithley 2400 Series Source Meter](https://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter).<br>
See also tickets [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#2695](https://github.com/ISISComputingGroup/IBEX/issues/2695), [#2801](https://github.com/ISISComputingGroup/IBEX/issues/2801) and [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176).

{#sxd_note-kammrath-and-weiss}
##### Note: Kammrath and Weiss #####
1. The Kammrath-Weiss tensile stress rig is controlled from a dedicated laptop running the manufacturer's software.  SECI communicates with the PC to send/read values to/from the manufacturer's software.
1. [Kammrath and Weiss](https://www.kammrath-weiss.com/en/tensile-compression-modules/).<br>
   * See also ticket [#2681](https://github.com/ISISComputingGroup/IBEX/issues/2681)

{#sxd_note-neocera}
##### Note: Neocera #####
Low temperature experiments?[Neocera LTC-21 Manual](http://www.submm.caltech.edu/~sharc/technical/LTC-21%20manual.pdf)

{#sxd_noteAttoCube}
##### Note: Attocube #####
1. [AttoCube](http://www.attocube.com/) - check existing VI.
1. There are existing [EPICS drivers](https://epics.anl.gov/modules/manufacturer.php#attocube) for Attocube devices.

{#sxd_note-helium-gauge}
##### Note: Helium Gauge #####
1. ISIS Helium Gauge  - check existing VI.

{#sxd_noteRamanSpect}
##### Note: mini-Raman Spectrometer #####
1. [B&W Tek i-Raman Plus](http://bwtek.com/products/i-raman-plus/) SXD & HRPD wish to share a Raman Spectrometer (and centre-stick). 

## SXD Notes ##
SXD has the following specialist panels/systems:
1. SXD Atto Cube
   * see [see Atto Cube note](#sxd_noteAttoCube)
1. SXD Jaws (Linmot)
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD Jaws\Screens`
1. SXD Centre Stick (PM600)
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD Centre Stick`
1. SXD Compact Focussing Device (PM600)
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD Compact Focusing Device`
   * Note from the instrument scientist: The compact focussing device (CFD) refers to a motorised mount that is permanently installed on SXD.  The CFD is a compact supermirror guide, called a trumpet, with a length of 390mm and a rectangular cross section going from 15*15mm at the entrance down to 5*5mm at the exit. It was only used for testing and never since. The mount has x, y translation and horizontal and vertical angular adjustment. There was also translation along the beam but this was removed since it caused the entire setup to droop.
1. SXD Furnace (PM600)
   * This implies that a Furnace is in use - check that it can be controlled via a Eurotherm.
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD Furnace`
1. SXD CCR (PM600)
1. SXD PE CCR (PM600)
   * These two items imply that CCRs are in use - check that they can be controlled via a Eurotherm.
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD CCR` and `C:\LabVIEW Modules\Instruments\SXD\SXD PE CCR`
1. Parma Sample Changer (PM600)
    * What about `C:\LabVIEW Modules\Parma Sample Changer` and `C:\LabVIEW Modules\Parma Sample Changer (Axis 2)`?
1. SXD Keithley Source (Keithley 2410)
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD Keithley Source`
1. SXD Foil Changer
   * See `C:\LabVIEW Modules\Instruments\SXD\SXD Foil Changer`
   * The instrument scientists don't know what this is.  Assumed obsolete.  

SXD has the following devices under motion control:
1. goniometer


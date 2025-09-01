# INTER

This page collects information that will be useful for the implementation of the IBEX control system on INTER.
## Background & Timeline ##
INTER is a high-intensity chemical interfaces reflectometer instrument at ISIS, on TS2. The [INTER](https://www.isis.stfc.ac.uk/Pages/inter.aspx) web page describes the background to the instrument.

## Control System ##

As of 23/06/2021 INTER is running IBEX.

## INTER Equipment ##
The equipment listed below is used on INTER. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#inter_noteDAE)
ISIS | Mk3 | Chopper | N/A |     | [see Chopper note](#inter_noteChopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
??? |  | 4-blade jaws |  |  | [see Jaws note](#inter_note-jaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#inter_note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#inter_note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#inter_note-eurotherm)
Julabo | FP-50 | Water Bath | RS-232 | | [see Water Bath note](#inter_note-water-baths)
Julabo | FP-52 | Water Bath | RS-232 | | [see Water Bath note](#inter_note-water-baths)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#inter_note-kepco)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#inter_note-keithley)
[Linkam](http://www.linkam.co.uk/) | T95 |  | RS232 |  |[see Linkam note](#inter_note-linkam)
[Knauer](http://www.knauer.net/) | K6 | Electric valve drive | RS232 |  |[see Knauer note](#inter_note-knauer)
[Knauer](http://www.knauer.net/) | 1050 | HPLC pump | ??? | | [see Knauer HPLC note](#inter_note-knauer-HPLC)
~Hitachi~ | ~L-7100~ | ~HPLC pump~ | ~???~ | | [see Hitachi note](#inter_noteHitachi)
[Jasco](https://jascoinc.com/products/chromatography/)| PU-4180 | HPLC pump| ??? | | [see JASCO HPLC note](#inter_note-jasco-hplc-pump)
Keyence | LK-G | Positioning Sensor | RS-232 |  | [see Keyence note](#inter_note-keyence)
Nima Trough | ??? | Trough | ??? | | [see Nima Trough note](#inter_note-nima-trough)
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#inter_note-thurlby)
Omega | iBTHX | Transmitter | Ethernet | | [see Omega note](#inter_note-omega)
Sensirion | SHT75 | Humidity Sensor| ??? | | [see Sensirion note](#inter_note-sensirion)
Watson Marlow | 323 | Peristaltic Pump | ??? | | [see Peristaltic Pumps note](#inter_note-peristaltic-pumps)
WPI | Aladdin-1000 | Syringe Pump | ??? | | [see Syringe Pumps note](#inter_note-syringe-pumps)
WPI | SP2xx | Syringe Pump | ??? | | [see Syringe Pumps note](#inter_note-syringe-pumps)
Biologic| SP200 | Potentiostat | ??? | | [see Biologic note](#inter_note-biologic)
Weeder | WTDAC-M | Analog Output Card | ??? | | [see Weeder note](#inter_note-weeder)
ISIS |  | Environment Monitor | ??? | | [see ISIS Environment Monitor note](#inter_noteISISEnvironmentMonitor)

{#inter_noteDAE}
##### Note: DAE #####
See multi-detector and single-detector below.

{#inter_noteChopper}
##### Note: Choppers #####
INTER has a Mk3 chopper.<br>

##### Note: Motion safety #####
INTER has a safety system which includes light curtains and some other bits, but these are controlled via a safety-rated PLC within a Beckhoff. It forwards a signal when it is "about to trip" motion, which we then use to send an `AB 1` command (abort all motion) to all of the galils. this is done to avoid positions being lost on open-loop axes. The actual forwarding code for this lives in `custom_records.db` in the settings area, and is loaded in by the `INSTETC` IOC. 

{#inter_note-jaws}
##### Note: Jaws #####
Provide information about INTER jaws. (After reflectometry meeting these seem to be micro jaws which they borrow from another instrument this is not a galil controlled but have not yet got any extra information)

{#inter_note-vacuum-system}
##### Note: Vacuum System #####
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

{#inter_note-eurotherm}
##### Note: Eurotherm #####
Eurotherms are used to control temperature Orange Cryostat, CCR and Furnace devices.

{#inter_note-water-baths}
##### Note: Water Baths #####
INTER uses Julabo water baths
1. Julabo (which model(s)?)

{#inter_note-kepco}
##### Note: KEPCO #####
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).<br>  See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)

{#inter_note-keithley}
##### Note: Keithley #####
1. [Keithley 2400 Series Source Meter](https://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter).<br>
See also tickets [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#2695](https://github.com/ISISComputingGroup/IBEX/issues/2695), [#2801](https://github.com/ISISComputingGroup/IBEX/issues/2801) and [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176).

{#inter_noteHitachi}
##### Note: Hitachi #####
Hitachi pumps are no longer supported at ISIS

{#inter_note-linkam}
##### Note: Linkam #####
There are VIs for this.<br>
See also [Linkam T95 controller](http://www.linkam.co.uk/t95-system-controllers/) and tickets [#1106](https://github.com/ISISComputingGroup/IBEX/issues/1106), [#1496](https://github.com/ISISComputingGroup/IBEX/issues/1496), [#1509](https://github.com/ISISComputingGroup/IBEX/issues/1509).

{#inter_note-knauer}
##### Note: Knauer #####
Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
K-6 model appears to have been superseded.  
   1. Support now implemented (28-03-2019).  See [#3781](https://github.com/ISISComputingGroup/IBEX/issues/3781).

{#inter_note-knauer-HPLC}
##### Note: Knauer HPLC #####
Knauer HPLC 1050 [Knauer HPLC 1050 is discontinued.](https://www.knauer.net/en/discontinued-smartline-pump-1050-successor-azura-p-61l/p14161). 
   1. Support now implemented (04-01-2019).  See [#3262](https://github.com/ISISComputingGroup/IBEX/issues/3262).

{#inter_note-jasco-hplc-pump}
##### Note: JASCO HPLC Pump #####
[JASCO HPLC pump](https://jascoinc.com/products/chromatography/hplc/modules/hplc-pumps/) is a new (for ISIS) model of HPLC pump.
   * See `C:\LabVIEW Modules\Drivers\Jasco PU-4180 HPLC Pump\Documentation` for documentation.
   * See also [#3743](https://github.com/ISISComputingGroup/IBEX/issues/3743) & [#3923](https://github.com/ISISComputingGroup/IBEX/issues/3923)

{#inter_note-keyence}
##### Note: Keyence #####
1. [Keyence Web-site](https://www.keyence.co.uk/index.jsp)
1. The Keyence LK-G is a laser positioning sensor (possibly superseded by a newer model).  It is used when adjusting the height of the sample stage.  Check the existing VI.
   1. See `C:\LabVIEW Modules\Instruments\INTER\Keyence LK-G` for existing VI.
   1. Current models of [Keyence LK-G laser sensors](https://www.keyence.co.uk/products/measure/laser-1d/index.jsp)
   1. The Keyence LK-G is always in position on the instrument, although not always used.
   1. Now implemented (24-07-2019).  See [#3745](https://github.com/ISISComputingGroup/IBEX/issues/3745)

{#inter_note-nima-trough}
##### Note: Nima Trough #####
Nima Trough: 
   * **Note:** NIMA Technologies Ltd now seems to be part of [Biolin Scientific](https://www.biolinscientific.com/ksvnima).<br>
   * The manufacturer has made additional software available for download.  A copy of this software is located in `\\isis\shares\ISIS_Experiment_Controls\NIMA Trough\Nima_TR8.1.zip`.
   * Support now implemented (25-05-2019).  See [#3783](https://github.com/ISISComputingGroup/IBEX/issues/3783)

{#inter_note-thurlby}
##### Note: Thurlby #####
Thurlby EX355P PSU - see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).
   * [Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)
   * IOC & OPI updated (18-07-2019).  See [#3784](https://github.com/ISISComputingGroup/IBEX/issues/3784)

{#inter_note-omega}
##### Note: Omega #####
[OMEGA™ iBTHX transmitter](https://www.omega.co.uk/pptst/IBTX_IBTHX.html) is a device to monitor and record barometric pressure, temperature, relative humidity, and dew point over an Ethernet network or the Internet.
   * OMEGA devices have proved unreliable on other instruments (e.g. ZOOM, LOQ).  Consider other types of device.

{#inter_note-sensirion}
##### Note: Sensirion #####
[Sensirion SHT75](https://www.sensirion.com/en/environmental-sensors/humidity-sensors/pintype-digital-humidity-sensors/) is a device to monitor and record humidity, temperature,… etc.
   * According to the manufacturer's web-site the SHT7x series of devices is "end-of-life" as of 31/12/2018.

{#inter_note-biologic}
##### Note: Biologic #####
[Biologic SP200](https://www.bio-logic.net/products/multichannel-conductivity/sp-200-potentiostat-galvanostat/) is a potentiostat.
   * See also [#618](https://github.com/ISISComputingGroup/IBEX/issues/618)

{#inter_note-peristaltic-pumps}
##### Note: Peristaltic Pumps #####
1. [Watson Marlow 323 Peristaltic Pump](http://www.watson-marlow.com/gb-en/range/watson-marlow/300-tube-pumps/323d/)
   * Support now implemented (14-08-2019).  See [#3786](https://github.com/ISISComputingGroup/IBEX/issues/3786)

{#inter_note-syringe-pumps}
##### Note: Syringe Pumps #####
1. [WPI Aladdin-1000 Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps/al1000-220.aspx)
   * Support now implemented (20-06-2019).  See [#3787](https://github.com/ISISComputingGroup/IBEX/issues/3787)
1. [WPI SP2xx Syringe Pump](https://www.wpi-europe.com/products/pumps--microinjection/laboratory-syringe-pumps.aspx) - check specific model.
   * Support now implemented (05-07-2018).  See [#3261](https://github.com/ISISComputingGroup/IBEX/issues/3261)

{#inter_note-weeder}
##### Note: Weeder #####
1. [Weeder WTDAC-M](https://weedtech.com/wtdac-m.html) analog output card.

{#inter_noteISISEnvironmentMonitor}
##### Note: ISIS Environment Monitor #####
1. The ISIS Environment Monitor is a device to monitor various environmental properties (temperature, pressure, humidity, etc).  There is an existing list of commands and a VI to work from.  
   * Suspect this is the Sensirion SHT75 device.

##### Note: Vacuum Chamber #####
1.  Vacuum chamber – specialist setup using HV and vacuum with some safety trips integrated (instrument scientists says this is be a high priority to enable in IBEX).  
   * Is the vacuum chamber related to the INTER High Voltage VI (listed below)?

## INTER Mirror Guides ##
INTER is due to get new mirror guides (prior to Cycle 2019/01).  There is a [sketch showing the three mirror guide sections](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/INTER/Defined%20Axis%20and%20Rotations.pdf) (MG1 - MG3).  MG1 is fixed; it requires no control.  MG2 and MG3 are moveable and, therefore, do require control.

There will be, essentially, 3 modes of operation:
   1. **no bounce:** all three sections centred in height around the incident beam height  to allow straight through beam on sample
   1. **one bounce:** this could be either from the middle section (MG2) or the focusing section (MG3), the latter being more likely
   1. **two bounces:** MG2 and MG3 both intercept the (reflected beam) with their inner bottom surface and deflect the beam up

In modes 2 and 3 several beamline components need to track: intermediate slit (S1b), slit 2, sample monitor, sample height, slit 3 and detector.


INTER has the following devices under motion control:
1. FOM
1. Jaws & Height
1. Jaws
1. Laser Gimbal
1. Reflectometer Sample Stack
1. Transmission Monitor
1. INTER Multi Detector
1. INTER Point Detectors
1. INTER Supermirror

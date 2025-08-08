# CHIPIR

This page collects information that will be useful for the implementation of the new control system on CHIPR.
## Background & Timeline ##
CHIPIR is a neutron instrument dedicated to the irradiation of microelectronics with atmospheric-like neutrons, on TS2. The [CHIPIR](https://www.isis.stfc.ac.uk/Pages/Chipir.aspx) web page describes the background to the instrument.

It was originally intended that IBEX should be piloted on CHIPIR, but commissioning of the instrument has taken longer than expected and, therefore, this idea has been shelved.  Nevertheless, there is no reason why IBEX cannot be installed on CHIPIR at some future date.

## Control System ##
CHIPIR currently uses the SECI control system.  It will migrate to the IBEX control system at a convenient date (yet to be decided).

## CHIPIR Equipment ##
The equipment listed below is used on CHIPIR. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#chipir_note-galil)
[HAMEG](https://www.rohde-schwarz.com/general_information/hameg/rohde-schwarz-company_230166.html) | HM8123 | Gated Counter |  | #109, #110, #117 | [see HAMEG note](#chipir_note-hameg)
[AGILENT](http://www.home.agilent.com/agilent/home.jspx?cc=GB&lc=eng) | E3613A | PSU |  |  | [see Agilent note](#chipir_note-agilent)
[AGILENT](http://www.home.agilent.com/agilent/home.jspx?cc=GB&lc=eng) | 33220A | Function Generator |  | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Agilent), #102, #111, #118 | [see Agilent note](#chipir_note-agilent)
[AGILENT](http://www.home.agilent.com/agilent/home.jspx?cc=GB&lc=eng) | 53220A | Counter |  | #103, #112, #119 | [see Agilent note](#chipir_note-agilent)
[TEKTRONIX](http://www.tek.com/digital-multimeter) | DMM4040 | Multimeter |  | #120 | [see Tektronix note](#chipir_note-tektronix)
[TEKTRONIX](http://www.tek.com/digital-multimeter) | DMM4050 | Multimeter |  | #121 | [see Tektronix note](#chipir_note-tektronix)
[Stanford RS](http://www.thinksrs.com/) | PS350 | PSU |  | #122 | [see Stanford RS note](#chipir_note-stanford-rs)
[Stanford RS](http://www.thinksrs.com/) | SR400 | Photon Counter |  | #123 | [see Stanford RS note](#chipir_note-stanford-rs)
ISIS |  | Filter Set | [see Galil note](#chipir_note-galil) |  | [see Filter Set note](#chipir_note-filter-set)
ISIS |  | Collimator | [see Galil note](#chipir_note-galil) |  | [see Collimator note](#chipir_note-collimator)
ISIS |  | XYZ Table | [see Galil note](#chipir_note-galil) |  | [see XYZ Table note](#chipir_note-xyz-table)
ISIS |  | Pre-sample Table | [see Galil note](#chipir_note-galil) |  | [see Pre-sample Table note](#chipir_note-pre-sample-table)
[ORTEC](http://www.ortec-online.com) | [Easy-NIM 928](http://www.ortec-online.com/Solutions/928-EASY-NIM.aspx) | MCA |  |  | [see ORTEC note](#chipir_note-ortec)
[SuperLogics](https://www.superlogics.com) | 8017 series | Data Acquisition |  |  | [see SuperLogics note](#chipir_note-super-logics)
TBD  |  | Camera |  |  | [see Camera note](#chipir_note-camera)
Beckhoff | | | | | [see Beckhoff note](#chipir_note-beckhoff)

{#chipir_note-galil}
##### Note: Galil #####
Model: [DMC2280](http://www.galilmc.com/products/dmc-22x0.php)

Other than the collimator, the only other quirk to CHIPIR's galil 02 is that the jaws in/out axis uses a non-standard homing routine - [`galil_Home_JogForwLimit.dmc`](https://github.com/ISISComputingGroup/EPICS-galil/pull/79/files#diff-64af6fffc6cf1ad849a8685d6848ae66746109ac8457de498d3fa758491681e1)

{#chipir_note-filter-set}
##### Note: Filter Set #####
Driven by Beckhoff controlled motor.<br>
See [see Galil note](#chipir_note-galil)

These are driven through `TC` using some variables for in/out readback and control. There is also some web HMI screen which IDD motion wrote which may now be defunct now that IBEX works with the filter set. 

{#chipir_note-collimator}
##### Note: Collimator #####
Driven by Galil controlled motor.<br>

This runs some [custom galil code](https://github.com/ISISComputingGroup/EPICS-galil/blob/master/GalilSup/Db/galil_CHIPIR_Collimator.dmc) but essentially does not accept moves like a normal motor. it has an encoder as an auxiliary feedback only ie. to see if it's moving, but uses physical switches fed into the Galil's digital ins for positioning. It uses a "read" thread that runs on thread 7 to monitor these during a move. 

{#chipir_note-xyz-table}
##### Note: XYZ Table #####
Driven by Galil controlled motor.<br>
See [see Galil note](#chipir_note-galil)

{#chipir_note-pre-sample-table}
##### Note: Pre-sample Table #####
Driven by Galil controlled motor.<br>
See [see Galil note](#chipir_note-galil)

{#chipir_note-hameg}
##### Note: HAMEG #####
[HAMEG](https://www.rohde-schwarz.com/general_information/hameg/rohde-schwarz-company_230166.html) has now been acquired by [Rohde & Schwarz](https://www.rohde-schwarz.com).<br>
[HM8123 Universal Counter](https://www.rohde-schwarz.com/product/hm8123-productstartpage_63493-44102.html)

{#chipir_note-agilent}
##### Note: Agilent #####
Agilent has spun-off its electronic measurement business, which now trades as [Keysight Technologies](http://www.keysight.com/main/home.jspx?cc=GB&lc=eng).<br>

1. [E3613A power supply](http://www.keysight.com/en/pd-838240-pn-E3610A/30w-power-supply-8v-3a-or-15v-2a?cc=GB&lc=eng&lsrch=true&searchT=E3613A) is now discontinued.
1. [33220A function generator](http://www.keysight.com/en/pd-127539-pn-33220A/function-arbitrary-waveform-generator-20-mhz?cc=GB&lc=eng&lsrch=true&searchT=33220A) will be discontinued from 01/12/2016.
1. [53220A counter](http://www.keysight.com/en/pd-1893411-pn-53220A/350-mhz-universal-frequency-counter-timer-12-digits-s-100-ps?nid=-33609.959903.00&cc=GB&lc=eng).

{#chipir_note-tektronix}
##### Note: Tektronix #####
[DMM4050 and DMM4040 digital multimeters](https://uk.tek.com/datasheet/dmm4050-4040-digital-multimeter)

{#chipir_note-stanford-rs}
##### Note: Stanford RS #####

1. [PS300 series high-voltage power supplies](http://www.thinksrs.com/products/PS300.htm)
2. [SR400 series photon counters](http://www.thinksrs.com/products/SR400.htm)

{#chipir_note-ortec}
##### Note: ORTEC Easy-NIM 928 #####
1. [High Performance, Multi-Function Nuclear MCA/Counter/Timer/Rate Meter](https://www.ortec-online.com/products/electronics/multichannel-analyzers-mca/basic-analog/928).

{#chipir_note-super-logics}
##### Note: SuperLogics #####
1. [8017/18/19 series - 8 Channel Analog Input Module, 16-Bit A/D Converter](https://www.superlogics.com/data-acquisition-99/data-acq-analog-input/analog-input-rs485/8017.html).<br>
Copy of manual for [8017/18/19 series](https://stfc365.sharepoint.com/:b:/r/sites/ISISExperimentControls/ICP%20Discussions/Chipir/Manuals%20for%20Equipment/Superlogics_8019R.pdf?csf=1&web=1&e=EV4XiD).

{#chipir_note-camera}
##### Note: Camera #####
Not required for day 1. Open to suggestions.

{#chipir_note-beckhoff}
##### Note: Beckhoff ####
1. Needed prior to migration, should be revisited during migration to move to using more standard motion control under IBEX
1. There are three items, a secondary shutter and 2 filters being controlled by a Beckhoff
1. Initially these will be controlled via SECI, with the Beckhoff managing the reporting and moving of the items in/out of the beam, these will be reported back to IBEX using the standard Beckhoff tagging method
1. A VI will be needed which interacts with the PVs generated by TCIOC



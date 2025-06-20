# ZOOM

This page collects information that will be useful for the implementation of the new control system on ZOOM.
## Background & Timeline ##
The [ZOOM](http://www.isis.stfc.ac.uk/instruments/zoom/zoom8060.html) web page describes the background to the instrument. Additional material is also available on the [ZOOM sharepoint](https://stfc365.sharepoint.com/sites/ISISProjects-1015/ZOOM/Forms/AllItems.aspx).  ZOOM is expected to have 36 motion axes.

The ZOOM shutter is due to open in February 2017 (see Zoom plan 28th May 2016). 

## Control System ##
ZOOM will use the IBEX control system.

## ZOOM Equipment ##
The equipment listed below is to be used on ZOOM. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | Fast Shutter |  | OMRON |  |[see Fast Shutter note](#zoom_noteFastShutter)
ISIS |Double Disc Chopper | CHOPPER | Ethernet/.NET | #170 |[see ISIS Double Disk Chopper note](#zoom_noteDDChopper)
 |  | JAWS | | #179, #180 |[see Jaws note](#zoom_noteJaws)
 | Polariser, guide & collimation unit (PGC) | | | #1233 |[see Polariser, Guide & Collimator note](#zoom_notePGC)
 |  | JAWS | | #179, #180 |
ISIS |  | Spin Flipper | | #1234 |[see SpinFlipper note](#zoom_noteSpinFlipper)
 |  | JAWS | | #179, #180 |
 |  | Alignment Laser | |  |[see Alignment Laser note](#zoom_noteLaser)
 |  | JAWS | | #179, #180 |
[JJ XRAY](http://www.jjxray.dk/) | [7-axis Sample Stack](http://www.jjxray.dk/products/positioning/multi-axis-stages/sample-stacks) [Manual](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Larmor/LARMOR%20JJXRAY%20SAMPLE%20STACK.pdf) | Sample Stack | | #304, #1238 |[see JJ X-Ray note](#zoom_noteJJXray)
 | Translation (across beam) | Sample Stack | | #1238 |[see SampleStack note](#zoom_noteSampleStack)
ISIS | Translation (along beam) | Sample Stack || #1238 |Driven by [Beckhoff](#zoom_noteBeckhoff)
ISIS | Two Tier sample changer | Sample Changer || |[see SampleChanger note](#zoom_noteSampleChanger)
 |  | Pneumatic Shutter | OMRON |  |[see Pneumatic Shutter note](#zoom_notePneumaticShutter)
ISIS | Tank Translation |  ||  |[see Tank Translation note](#zoom_noteTankTranslate)<br>Driven by [Beckhoff](#zoom_noteBeckhoff)
 |  | In/Out Monitor | | #267 |[see Monitor note](#zoom_noteMonitor)
 |  | JAWS | | #179, #180 |
 |  | Detector Motion System (DMS) | | #1236 |[see Detector Motion System (DMS) note](#zoom_noteDMS)
ISIS | DAE (2 or 3?) | Detector Electronics | Ethernet | #219 |[see DAE note](#zoom_noteDAE)
[CAEN](http://www.caen.it/csite/HomePage.jsp) | HT | Detector HV Control | Ethernet | #214 |[see CAEN HT note](#zoom_noteCAEN)
OMRON |  | PLC | Ethernet | FINS, #217 |[see OMRON PLC note](#zoom_noteOMRON)
[Galil](http://www.galilmc.com/) | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | EPICS |[see Galil note](#zoom_noteGalil)
[Beckhoff](http://www.beckhoff.co.uk/) |  | Motion Controller | TBC |  |[see Beckhoff note](#zoom_noteBeckhoff)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS VACUUM SYSTEM | RS232 | #218 |[see Pfeiffer note](#zoom_notePfeiffer)
[Julabo](http://www.julabo.com/us?p=1) | TBC | Water Bath | RS232 | #187, #188 |[see Julabo note](#zoom_noteJulabo)
 |  | PSU | TBC |  |[see Power Supply Unit note](#zoom_notePSU)
[Oxford Instruments](http://www.oxford-instruments.com/products) | ITC503 | Temp Controller | RS232 |  |[see Oxford Instruments Temperature Controller note](#zoom_noteOI_ITC503)
[Oxford Instruments](http://www.oxford-instruments.com/products) | ILM200 series | Helium Level Meter | RS232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Oxford%20Instruments) |[see Oxford Instruments Helium Level Meter note](#zoom_noteOI_ILM200)
[Eurotherm](http://www.eurotherm.co.uk/) | All models at ISIS | Temp Controller | RS232 | [ EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) |[see Eurotherm note](#zoom_noteEurotherm)
[Eurotherm](http://www.eurotherm.co.uk/) | Nanodac | Temp Controller | Ethernet| |[see Eurotherm note](#zoom_noteEurotherm)
[Thurlby](http://www.tti-test.com/) | [EX355P](http://www.tti-test.com/products-tti/text-pages/psu-ex355p.htm) | DC Power Supply | RS232 | #156 |[see Thurlby note](#zoom_noteThurlby)
[KEPCO](http://www.kepcopower.com/bop.htm) | TBC | Bi-Polar Power Supply | RS232 | #189 |[see KEPCO note](#zoom_noteKEPCO)
[Tektronix](http://www.tek.com/oscilloscope#all) | [MSO 4104B](http://www.tek.com/oscilloscope/mso4000-dpo4000) | Oscilloscope | Ethernet | #234 |[see Tektronix note](#zoom_noteTektronix)
[Tektronix](http://www.tek.com/function-generator) | [AFG 3022B](http://www.tek.com/datasheet/signal-generator/afg3000-function-generator-arbitrary-function-generators) | Function Generator | Ethernet | #237 |[see Tektronix note](#zoom_noteTektronix)
[PI](http://www.physikinstrumente.com/en/index.php) | Rotation Stage | Nano-positioning Rotation Stage | RS232 |  |[see Physik Instrument note](#zoom_notePI_Nano)
[Bio-Logic](http://www.bio-logic.info/) |  | Stopped Flow Cell | RS232 |  |[see BioLogic note](#zoom_noteBioLogic)
 | 17T Cryomag | Super conducting magnet | RS232 |  |
Oxford Instruments | 7.5T Magnet | Super conducting magnet | RS232 |  | [see 7.5T Magnet note](#zoom_note7p5TMagnet)
[Scientific Magnetics](http://www.scientificmagnetics.co.uk/) |  | 3 Axis Super conducting magnet & VTI | RS232 |  |[see Scientific Magnetics note](#zoom_noteSciMag)
[Lakeshore](http://www.lakeshore.com/Pages/Home.aspx) | All models at ISIS |  | TBC |  |[see Lakeshore note](#zoom_noteLakeshore)
 | Syringe Pumps|  | RS232 |  |[see Syringe Pumps note](#zoom_noteSyringePumps)
~[Hitachi](http://www.hitachi-hightech.com/global/about/corporate/group/hhs/)~ | ~L-7100~ | ~HPLC Pump~ | ~RS232~ |  |[see Hitachi note](#zoom_noteHitachi)
[TS-Haake](http://www.thermoscientific.com/en/products/baths.html) |  | Water Bath | RS232 |  |[see Thermo Scientific (Haake) note](#zoom_noteHaake)
[Huber](http://www.xhuber.de/en/home/) |  | Sample Stack | RS232 |  |[see Huber note](#zoom_noteHuber)
Thar |  | Pressure Cell | TBC |  |[see Thar note](#zoom_noteThar)
[Goudsmit](http://www.goudsmit-magnetics.nl/NL/) | 1T Magnet | Magnet | TBC |  |[see Goudsmit note](#zoom_noteGoudsmit)
[Anton Paar](http://www.anton-paar.com/uk-en/products/group/rheometer/) |  | Rheometer |  |  |[see Pfeiffer note](#zoom_noteAntonPaar)
ISIS |  | Couette Cell ||  |[see ISIS Couette Cell note](#zoom_noteCouette)
[McLennan](http://www.mclennan.co.uk/) |  | Motion Controller | RS232 |  |[see McLennan note](#zoom_noteMcLennan)
 |  | T-Jump Cell | RS232 |  |[see T-JumpCell note](#zoom_noteTJumpCell)
 | Dynamic Light Scattering | DLS | TBC |  |[see Dynamic Light Scattering (DLS) note](#zoom_noteDLS)
 |  | Raman Spectroscopy | TBC |  |[see Raman Spectroscopy  note](#zoom_noteRaman)
[Linkam](http://www.linkam.co.uk/) |  |  | RS232 |  |[see Linkam note](#zoom_noteLinkam)
[Keithley](http://www.keithley.co.uk/) | All models in use at ISIS |  | RS232, USB |  |[see Keithley note](#zoom_noteKeithley)
 |  | Closed Cycle Refrigerator | via Eurotherm? |  |[see CCR note](#zoom_noteCCR)


{#zoom_noteFastShutter}
##### Note: Fast Shutter #####
Location: Front End<br>
Due: Day 1<br>
As used on: SANS2D<br>

{#zoom_noteDDChopper}
##### Note: ISIS Double Disk Chopper #####
ISIS Mk3 Chopper<br>
Location: Front End<br>
Due: Day 1<br>
As used on: SANS2D<br>

{#zoom_noteJaws}
##### Note: Jaws #####
Location: Front End Vacuum Tank<br>
Due: Day 1<br>
As used on: Many instruments<br>
Testing Summer 2015<br>

{#zoom_notePGC}
##### Note: Polariser, Guide & Collimator #####
Location: Front End Vacuum Tank<br>
Due: Day 1<br>
1 horizontal motion axis controlling four 4m evacuated tubes<br>

{#zoom_noteSpinFlipper}
##### Note: SpinFlipper #####
Location: Fixed Collimation<br>
Due: Day 1<br>
4m evacuated tube & Spin-flipper unit
Spin-flipper will be controlled by 2 Kepco Power Supplies<br>

{#zoom_noteLaser}
##### Note: Alignment Laser #####
Location: Blockhouse<br>
Due: Day 1<br>
Single in/out axis<br>
No control of the alignment laser is required, other than the ability to move it in/out of the beam.  It can treated like a monitor.

{#zoom_noteJJXray}
##### Note: JJ X-Ray 7-axis Sample Stack #####
Location: Blockhouse<br>
Due: Day 1<br>
[7-axis Sample Stack Manual](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Larmor/LARMOR%20JJXRAY%20SAMPLE%20STACK.pdf)<br>
See also [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteSampleStack}
##### Note: SampleStack #####
Location: Blockhouse<br>
Due: Day 1<br>
The [JJ X-Ray sample stack](#zoom_noteJJXray) will sit on rails to allow the entire sample stack to be translated back & forth along the beam.  The rails are not perfectly straight, so there needs to be an axis allowing motion perpendicular to the rails to correct for any slight misalignment in the rails.  In other words, there are two axes for wholesale motion of the sample stack (in addition to the 7 internal axes of the sample stack itself).

  1. Across beam (i.e. perpendicular to the rails): Alignment stage for reproducibility.
  2. Along beam (i.e. along the rails): Monitoring only, no control required.<br>
See [ZOOM_Sample_Stack_Schematic](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/ZOOM/ZOOM_Sample_Stack_Schematic.pptx)

{#zoom_notePneumaticShutter}
##### Note: Pneumatic Shutter #####
Location: Blockhouse<br>
Due: Day 1<br>
As used on: SANS2D<br>

{#zoom_noteTankTranslate}
##### Note: Tank Translation #####
Location: Blockhouse<br>
Due: Day 1<br>
The tank will be moved by a motor connected to a [Beckhoff](#zoom_noteBeckhoff) controller.<br>
Monitoring only, no control required.

{#zoom_noteMonitor}
##### Note: Monitor #####
Location: Tank<br>
Due: Day 1<br>
In/Out positioning - c.f. [LARMOR](LARMOR-Instrument-Details), [IMAT](IMAT-Instrument-Details),others<br>

{#zoom_noteDMS}
##### Note: Detector Motion System (DMS) #####
Location: Tank<br>
Due: Day 1

7 axes consisting of:
   1. Baffle
   1. Detector translation
   1. Strip Beam Stop
   1. 2x Disk Beam stop - x and y movement (total: 4 axes)

{#zoom_noteDAE}
##### Note: DAE #####
Location: Screened Room<br>
Due: Day 1<br>
As used on: Many instruments<br>

{#zoom_noteCAEN}
##### Note: CAEN HT #####
Location: Screened Room<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteOMRON}
##### Note: OMRON PLC #####
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details), [IMAT](IMAT-Instrument-Details)<br>
There are up to three functions for the PLC(s) - exactly which are to be included in the computing control is TBC.  Current expectation is that the PLC will control:
   1. "Fast Shutter" (located at the front end of the beamline).  SANS2D has a similar shutter.
   1. "Pneumatic Shutter" (located in the blockhouse).  SANS2D has a similar shutter.
   1. [Pfeiffer](#zoom_notePfeiffer) TPG 300 pressure gauges


{#zoom_noteGalil}
##### Note: Galil #####
Location: Blockhouse x 1, Mezzanine x 4<br>
Due: Day 1<br>
As used on: Many instruments<br>
There are at present 39 axes to be controlled via Galil<br>

{#zoom_noteBeckhoff}
##### Note: Beckhoff #####
Location: TBC<br>
As used on: [IMAT](IMAT-Instrument-Details)<br>
The Beckhoff controller will control two axes:
   1. the motion of the JJ X-ray sample stack along the rails [see SampleStack](#zoom_noteSampleStack)
   1. the motion of the [tank](#zoom_noteTankTranslate) (enclosing the detectors & detector motion system).

IBEX is **NOT** required to actually control these two axes (that will be done independently).  IBEX is required to monitor the locations reported by the Beckhoff system - a read only driver will be required.

{#zoom_notePfeiffer}
##### Note: Pfeiffer #####
Location: TBC - alongside PLCs<br>
Due: Day 1<br>
As used on: [LARMOR](LARMOR-Instrument-Details), [IMAT](IMAT-Instrument-Details)<br>

{#zoom_noteJulabo}
##### Note: Julabo #####
Location: TBC<br>
Due: Day 1<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_notePSU}
##### Note: Power Supply Unit #####
Location: TBC<br>
Due: Day 1<br>
This is to control a magnet which will be linked to the interlocks, but there are no details at present<br>

{#zoom_noteOI_ITC503}
##### Note: Oxford Instruments Temperature Controller #####
Model: ITC503<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteOI_ILM200}
##### Note: Oxford Instruments Helium Level Meter #####
Model: ILM200 series<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteEurotherm}
##### Note: Eurotherm #####
Model: all models at ISIS<br>
Due: Day 1<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>
**Note:** ZOOM may also use a [Eurotherm Nanodac](http://www.eurotherm.co.uk/products/recorders/graphic/nanodac) to monitor detector temperatures.

{#zoom_noteThurlby}
##### Note: Thurlby #####
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteKEPCO}
##### Note: KEPCO #####
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteTektronix}
##### Note: Tektronix #####
1. Model: Oscilloscope
1. Model: Function Generator

Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteSampleChanger}
##### Note: SampleChanger #####
Location: Sample Area<br>
Due: Day 1<br>
Same as used on: SANS2D/[LARMOR](LARMOR-Instrument-Details), translations done via sample stack<br>

{#zoom_notePI_Nano}
##### Note: Physik Instrument #####
Model: Nano-positioning Rotation Stage<br>
Location: TBC<br>
[PI Software](http://www.physikinstrumente.com/en/products/prdetail.php?sortnr=1100018), [EPICS driver](http://www.aps.anl.gov/epics/modules/manufacturer.php#Physik%20Instrumente)<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteBioLogic}
##### Note: BioLogic #####
Model: Stopped Flow Cell<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteSciMag}
##### Note: Scientific Magnetics #####
Model: 3 Axis Super conducting magnet & VTI<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteLakeshore}
##### Note: Lakeshore #####
Model: all models at ISIS<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteSyringePumps}
##### Note: Pfeiffer #####
Model: all models at ISIS<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteHitachi}
##### Note: Hitachi #####
Hitachi L-7100 HPLC pump (no longer supported at ISIS).  ~Can't find L-7100 on [Hitachi web-site](http://www.hitachi-hightech.com/global/about/corporate/group/hhs) (may be obsolete).  Check existing SECI VI for logic and manual: both VI and manual are located here: `C:\LabVIEW Modules\Drivers\Hitachi L-7100`.~
   * Update (27-06-2019): Hitachi pumps are no longer used.  No longer any need to support them.  See [#3780](https://github.com/ISISComputingGroup/IBEX/issues/3780).

{#zoom_noteHaake}
##### Note: Thermo Scientific (Haake) #####
Model: Water bath<br>
Location: TBC<br>
As used on: [LARMOR](LARMOR-Instrument-Details)<br>

{#zoom_noteHuber}
##### Note: HUBER #####
Model: Sample Stack<br>
As used on: SANS2D<br>
Location: TBC<br>

{#zoom_noteThar}
##### Note: Thar #####
Model: Pressure Cell<br>
Location: TBC<br>
As used on: SANS2D, LOQ<br>

{#zoom_noteGoudsmit}
##### Note: Goudsmit #####
Model: 1T Magnet<br>
Location: TBC<br>
As used on: SANS2D, LOQ<br>

{#zoom_noteAntonPaar}
##### Note: Pfeiffer #####
Model: Rheometer<br>
Location: TBC<br>
As used on: SANS2D<br>
Currently controlled from a separate PC<br>

{#zoom_noteCouette}
##### Note: ISIS Couette Cell #####
Location: TBC<br>
As used on LOQ<br>

{#zoom_noteMcLennan}
##### Note: McLennan #####
Location: TBC<br>
Due: Day 1<br>
As used on: Many instruments<br>

{#zoom_noteTJumpCell}
##### Note: T-JumpCell #####
Location: TBC<br>
As used on: LOQ<br>

{#zoom_noteDLS}
##### Note: Dynamic Light Scattering (DLS) #####
Location: TBC<br>
As used on: SANS2D<br>
There is an interaction with a LabVIEW function that ought to be reproduced.<br>

{#zoom_noteRaman}
##### Note: Raman Spectroscopy  #####
Location: TBC<br>
As used on: INTER<br>
This may not have an existing interface, and may not need one<br>

{#zoom_noteLinkam}
##### Note: Linkam #####
Location: TBC<br>
There are VIs for this<br>

{#zoom_noteKeithley}
##### Note: Keithley #####
Model: all models in use at ISIS<br>
Location: TBC<br>
There are VIs for this<br>

{#zoom_noteCCR}
##### Note: CCR #####
Model: TBC<br>
Location: TBC<br>
Details of [Closed-Cycle Refrigerators](http://www.isis.stfc.ac.uk/sample-environment/low-temperature/ccrs/) at ISIS.

{#zoom_note7p5TMagnet}
##### Note: 7.5T Magnet #####
Model: [7.5T Magnet](https://www.isis.stfc.ac.uk/Pages/75T-Magnet.aspx)
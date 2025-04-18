# LARMOR

This page collects information that will be useful for the implementation of the new control system on LARMOR.

## Background & Timeline ##
The [LARMOR](http://www.isis.stfc.ac.uk/instruments/larmor/larmor8239.html) web page describes the background to the instrument. The layout of the LARMOR beamline is shown in [this diagram](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/LARMOR_Beamline_Diagram.pdf).
The proposed architecture for the LARMOR control system is described [here](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/Larmor%20Architecture.ppt).  We also have a list of LARMOR's [motion control components](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/LARMOR%20Beam%20Line%20-%20Motion%20Control%20Components.docx).

## Control System ##
LARMOR is currently using the IBEX control system.

## LARMOR Equipment ##
The equipment listed below is to be used on LARMOR. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS |Mk3 Chopper | CHOPPER | Ethernet/.NET | #170 |[see ISIS Mk3 Chopper note](#larmor_noteMk3Chopper)
 |  | Spin Flipper | |  |[see SpinFlipper note](#larmor_noteSpinFlipper)
Delft | Spin Echo| Spin Echo control system| TBD | TBD |[see Spin Echo System note](#larmor_noteSpinEcho)
[JJ XRAY](http://www.jjxray.dk/) | [7-axis Sample Stack](http://www.jjxray.dk/products/positioning/multi-axis-stages/sample-stacks) [Manual](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/LARMOR%20JJXRAY%20SAMPLE%20STACK.pdf) | Sample Stack | | #304 |[see JJ X-Ray note](#larmor_noteJJXray)
ISIS | [Two Tier](https://github.com/ISISComputingGroup/IBEX/wiki/TwoTierSampleChanger) | Sample Changer || |[see SampleChanger note](#larmor_noteSampleChanger)
 |  | In/Out Monitor | | #267 |[see Monitor note](#larmor_noteMonitor)
ISIS | DAE 3 | Detector Electronics | Ethernet | #219 |[see DAE note](#larmor_noteDAE)
[CAEN](http://www.caen.it/csite/HomePage.jsp) | HT | Detector HV Control | Ethernet | #214 |[see CAEN HT note](#larmor_noteCAEN)
[Galil](http://www.galilmc.com/) | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | EPICS |[see Galil note](#larmor_noteGalil)
OMRON |  | PLC | TCP/FINS | #217 |[see OMRON PLC note](#larmor_noteOMRON)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | #216 |[see Pfeiffer note](#larmor_notePfeiffer)
[Julabo](http://www.julabo.com/us?p=1) | [FL300](http://www.julabo.de/en/products/recirculating-coolers/fl300-recirculating-cooler) | Water Bath | RS232 | #187 |[see Julabo note](#larmor_noteJulabo)
[Julabo](http://www.julabo.com/us?p=1) | [FP50](http://www.julabo.de/en/products/refrigerated-circulators/refrigerated-heating-circulators) | Water Bath | RS232 | #188 |[see Julabo note](#larmor_noteJulabo)
[Eurotherm](http://www.eurotherm.co.uk/) | All models at ISIS | Temp Controller | RS232 | [ EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) |[see Eurotherm note](#larmor_noteEurotherm)
[Oxford Instruments](http://www.oxford-instruments.com/products) | ITC503 | Temp Controller | RS232 |  |[see Oxford Instruments Temperature Controller note](#larmor_noteOI_ITC503)
[Oxford Instruments](http://www.oxford-instruments.com/products) | ILM200 series | Helium Level Meter | RS232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Oxford%20Instruments) |[see Oxford Instruments Helium Level Meter note](#larmor_noteOI_ILM200)
[Thurlby](http://www.tti-test.com/) | [EX355P](http://www.tti-test.com/products-tti/text-pages/psu-ex355p.htm) | DC Power Supply | RS232 | #156 |[see Thurlby note](#larmor_noteThurlby)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#larmor_noteKepco)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 50M | Bi-Polar Power Supply | RS232 | #188 |[see Kepco note](#larmor_noteKepco)
[Tektronix](http://www.tek.com/oscilloscope#all) | [MSO 4104B](http://www.tek.com/oscilloscope/mso4000-dpo4000) | Oscilloscope | Ethernet | #234 |[see Tektronix note](#larmor_noteTektronix)
[Tektronix](http://www.tek.com/function-generator) | [AFG 3022B](http://www.tek.com/datasheet/signal-generator/afg3000-function-generator-arbitrary-function-generators) | Function Generator | Ethernet | #237 |[see Tektronix note](#larmor_noteTektronix)
[PI](http://www.physikinstrumente.com/en/index.php) | Rotation Stage | Nano-positioning Rotation Stage | RS232 |  |[see Physik Instrument note](#larmor_notePI_Nano)
[Bio-Logic](http://www.bio-logic.info/) |  | Stopped Flow Cell | RS232 |  |[see BioLogic note](#larmor_noteBioLogic)
 | 17T Cryomag | Super conducting magnet | RS232 |  |
[Scientific Magnetics](http://www.scientificmagnetics.co.uk/) |  | 3 Axis Super conducting magnet & VTI | RS232 |  |[see Scientific Magnetics note](#larmor_noteSciMag)
[Lakeshore](http://www.lakeshore.com/Pages/Home.aspx) | All models at ISIS |  | TBC |  |[see Lakeshore note](#larmor_noteLakeshore)
 | Syringe Pumps|  | RS232 |  |[see Syringe Pumps note](#larmor_noteSyringePumps)
~[Hitachi](http://www.hitachi-hightech.com/global/about/corporate/group/hhs/)~ | ~L-7100~ | ~HPLC Pump~ | ~RS232~ |  |[see Hitachi note](#larmor_noteHitachi)
[Knauer](http://www.knauer.net/) | K6 | Electric valve drive | RS232 |  |[see Knauer note](#larmor_noteKnauer)
[Linkam](http://www.linkam.co.uk/) |  |  | RS232 |  |[see Linkam note](#larmor_noteLinkam)
[Keithley](http://www.keithley.co.uk/) | All models in use at ISIS |  | RS232, USB |  |[see Keithley note](#larmor_noteKeithley)

{#larmor_noteMk3Chopper}
##### Note: ISIS Mk3 Chopper #####
Location: Front End<br>

{#larmor_noteJaws}
##### Note: Jaws #####
Location: various<br>
Driven by [Galils](#larmor_noteGalil)

{#larmor_noteSpinFlipper}
##### Note: SpinFlipper #####

{#larmor_noteSpinEcho}
##### Note: Spin Echo System #####
[Delft RF Flipper Manual](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/Delft_RF_Flipper_Manual.pdf)<br>

{#larmor_noteJJXray}
##### Note: JJ X-Ray #####
[7-axis sample stack](http://www.jjxray.dk/products/positioning/multi-axis-stages/sample-stacks)<br>
[Manual](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/LARMOR%20JJXRAY%20SAMPLE%20STACK.pdf)

{#larmor_noteSampleStack}
##### Note: SampleStack #####

{#larmor_noteMonitor}
##### Note: Monitor #####
In/Out positioning<br>
Driven by [Galils](#larmor_noteGalil)

{#larmor_noteDAE}
##### Note: DAE #####
Location: Screened Room<br>
DAE-3

{#larmor_noteCAEN}
##### Note: CAEN HT #####
Location: Screened Room<br>

{#larmor_noteGalil}
##### Note: Galil #####
Model: [DMC2280](http://www.galilmc.com/products/dmc-22x0.php)

{#larmor_noteOMRON}
##### Note: OMRON PLC #####
ISIS Bench Air Line Control

{#larmor_notePfeiffer}
##### Note: Pfeiffer #####
Location: TBC - alongside PLCs<br>
[LARMOR](https://github.com/ISISComputingGroup/IBEX/wiki/LARMOR-Instrument-Details), [IMAT](https://github.com/ISISComputingGroup/IBEX/wiki/IMAT-Instrument-Details)<br>
Due: Day 1<br>

{#larmor_noteJulabo}
##### Note: Julabo #####
Model: all models at ISIS<br>

{#larmor_noteOI_ITC503}
##### Note: Oxford Instruments Temperature Controller #####
Model: ITC503<br>
Location: TBC<br>

{#larmor_noteOI_ILM200}
##### Note: Oxford Instruments Helium Level Meter #####
Model: ILM200 series<br>

{#larmor_noteEurotherm}
##### Note: Eurotherm #####
Model: all models at ISIS<br>

{#larmor_noteThurlby}
##### Note: Thurlby #####
Model: all models at ISIS<br>

{#larmor_noteKEPCO}
##### Note: KEPCO #####
1. Model: all models at ISIS
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).<br>  See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)

{#larmor_noteTektronix}
##### Note: Tektronix #####
1. Model: Oscilloscope [MSO 4104B](http://www.tek.com/oscilloscope/mso4000-dpo4000)
1. Model: Function Generator [AFG 3022B](http://www.tek.com/datasheet/signal-generator/afg3000-function-generator-arbitrary-function-generators)

{#larmor_noteSampleChanger}
##### Note: SampleChanger #####
Similar to that used on: SANS2D, translations done via sample stack<br>
See [Two-Tier Sample Changer](https://github.com/ISISComputingGroup/IBEX/wiki/TwoTierSampleChanger)

{#larmor_notePI_Nano}
##### Note: Physik Instrument #####
Model: Nano-positioning Rotation Stage<br>
[PI Software](http://www.physikinstrumente.com/en/products/prdetail.php?sortnr=1100018), [EPICS driver](http://www.aps.anl.gov/epics/modules/manufacturer.php#Physik%20Instrumente)<br>

{#larmor_noteBioLogic}
##### Note: BioLogic #####
Model: Stopped Flow Cell<br>

{#larmor_noteSciMag}
##### Note: Scientific Magnetics #####
1. [Scientific Magnetics](http://www.scientificmagnetics.co.uk/)
1. Model: 3 Axis Super conducting magnet & VTI (see [#1398](https://github.com/ISISComputingGroup/IBEX/issues/1398)).

{#larmor_noteLakeshore}
##### Note: Lakeshore #####
Model: all models at ISIS<br>

{#larmor_noteSyringePumps}
##### Note: Syringe Pumps #####
Model: all models at ISIS<br>

{#larmor_noteHitachi}
##### Note: Hitachi #####
Hitachi L-7100 HPLC pump (no longer supported at ISIS).  ~Can't find L-7100 on [Hitachi web-site](http://www.hitachi-hightech.com/global/about/corporate/group/hhs) (may be obsolete).  Check existing SECI VI for logic and manual: both VI and manual are located here: `C:\LabVIEW Modules\Drivers\Hitachi L-7100`.~
   * Update (27-06-2019): Hitachi pumps are no longer used.  No longer any need to support them.  See [#3780](https://github.com/ISISComputingGroup/IBEX/issues/3780).


{#larmor_noteMcLennan}
##### Note: McLennan #####
Location: TBC<br>
As used on: Many instruments<br>

{#larmor_noteKnauer}
##### Note: Knauer Electric Valve Drive  #####
Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
K-6 model appears to have been superseded.  Check existing SECI VI for logic and manual.

{#larmor_noteLinkam}
##### Note: Linkam #####
Location: TBC<br>
There are VIs for this.<br>
See also [Linkam T95 controller](http://www.linkam.co.uk/t95-system-controllers/) and tickets [#1106](https://github.com/ISISComputingGroup/IBEX/issues/1106), [#1496](https://github.com/ISISComputingGroup/IBEX/issues/1496), [#1509](https://github.com/ISISComputingGroup/IBEX/issues/1509).

{#larmor_noteKeithley}
##### Note: Keithley #####
Model: all models in use at ISIS<br>
There are VIs for this<br>

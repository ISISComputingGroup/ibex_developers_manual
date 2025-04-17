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
ISIS |Mk3 Chopper | CHOPPER | Ethernet/.NET | #170 |[see ISIS Mk3 Chopper note](#noteMk3Chopper)
 |  | Spin Flipper | |  |[see SpinFlipper note](#noteSpinFlipper)
Delft | Spin Echo| Spin Echo control system| TBD | TBD |[see Spin Echo System note](#noteSpinEcho)
[JJ XRAY](http://www.jjxray.dk/) | [7-axis Sample Stack](http://www.jjxray.dk/products/positioning/multi-axis-stages/sample-stacks) [Manual](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/LARMOR%20JJXRAY%20SAMPLE%20STACK.pdf) | Sample Stack | | #304 |[see JJ X-Ray note](#noteJJXray)
ISIS | [Two Tier](https://github.com/ISISComputingGroup/IBEX/wiki/TwoTierSampleChanger) | Sample Changer || |[see SampleChanger note](#noteSampleChanger)
 |  | In/Out Monitor | | #267 |[see Monitor note](#noteMonitor)
ISIS | DAE 3 | Detector Electronics | Ethernet | #219 |[see DAE note](#noteDAE)
[CAEN](http://www.caen.it/csite/HomePage.jsp) | HT | Detector HV Control | Ethernet | #214 |[see CAEN HT note](#noteCAEN)
[Galil](http://www.galilmc.com/) | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | EPICS |[see Galil note](#noteGalil)
OMRON |  | PLC | TCP/FINS | #217 |[see OMRON PLC note](#noteOMRON)
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG300 | ISIS Vacuum System | RS232 | #216 |[see Pfeiffer note](#notePfeiffer)
[Julabo](http://www.julabo.com/us?p=1) | [FL300](http://www.julabo.de/en/products/recirculating-coolers/fl300-recirculating-cooler) | Water Bath | RS232 | #187 |[see Julabo note](#noteJulabo)
[Julabo](http://www.julabo.com/us?p=1) | [FP50](http://www.julabo.de/en/products/refrigerated-circulators/refrigerated-heating-circulators) | Water Bath | RS232 | #188 |[see Julabo note](#noteJulabo)
[Eurotherm](http://www.eurotherm.co.uk/) | All models at ISIS | Temp Controller | RS232 | [ EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) |[see Eurotherm note](#noteEurotherm)
[Oxford Instruments](http://www.oxford-instruments.com/products) | ITC503 | Temp Controller | RS232 |  |[see Oxford Instruments Temperature Controller note](#noteOI_ITC503)
[Oxford Instruments](http://www.oxford-instruments.com/products) | ILM200 series | Helium Level Meter | RS232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Oxford%20Instruments) |[see Oxford Instruments Helium Level Meter note](#noteOI_ILM200)
[Thurlby](http://www.tti-test.com/) | [EX355P](http://www.tti-test.com/products-tti/text-pages/psu-ex355p.htm) | DC Power Supply | RS232 | #156 |[see Thurlby note](#noteThurlby)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 100-10MG | Bi-Polar Power Supply | RS232 | #187 |[see Kepco note](#noteKepco)
[KEPCO](http://www.kepcopower.com/bop.htm) | BOP 50M | Bi-Polar Power Supply | RS232 | #188 |[see Kepco note](#noteKepco)
[Tektronix](http://www.tek.com/oscilloscope#all) | [MSO 4104B](http://www.tek.com/oscilloscope/mso4000-dpo4000) | Oscilloscope | Ethernet | #234 |[see Tektronix note](#noteTektronix)
[Tektronix](http://www.tek.com/function-generator) | [AFG 3022B](http://www.tek.com/datasheet/signal-generator/afg3000-function-generator-arbitrary-function-generators) | Function Generator | Ethernet | #237 |[see Tektronix note](#noteTektronix)
[PI](http://www.physikinstrumente.com/en/index.php) | Rotation Stage | Nano-positioning Rotation Stage | RS232 |  |[see Physik Instrument note](#notePI_Nano)
[Bio-Logic](http://www.bio-logic.info/) |  | Stopped Flow Cell | RS232 |  |[see BioLogic note](#noteBioLogic)
 | 17T Cryomag | Super conducting magnet | RS232 |  |
[Scientific Magnetics](http://www.scientificmagnetics.co.uk/) |  | 3 Axis Super conducting magnet & VTI | RS232 |  |[see Scientific Magnetics note](#noteSciMag)
[Lakeshore](http://www.lakeshore.com/Pages/Home.aspx) | All models at ISIS |  | TBC |  |[see Lakeshore note](#noteLakeshore)
 | Syringe Pumps|  | RS232 |  |[see Syringe Pumps note](#noteSyringePumps)
~[Hitachi](http://www.hitachi-hightech.com/global/about/corporate/group/hhs/)~ | ~L-7100~ | ~HPLC Pump~ | ~RS232~ |  |[see Hitachi note](#noteHitachi)
[Knauer](http://www.knauer.net/) | K6 | Electric valve drive | RS232 |  |[see Knauer note](#noteKnauer)
[Linkam](http://www.linkam.co.uk/) |  |  | RS232 |  |[see Linkam note](#noteLinkam)
[Keithley](http://www.keithley.co.uk/) | All models in use at ISIS |  | RS232, USB |  |[see Keithley note](#noteKeithley)

<a name="noteMk3Chopper"></a>
##### Note: ISIS Mk3 Chopper #####
Location: Front End<br>

<a name="noteJaws"></a>
##### Note: Jaws #####
Location: various<br>
Driven by [Galils](#noteGalil)

<a name="noteSpinFlipper"></a>
##### Note: SpinFlipper #####

<a name="noteSpinEcho"></a>
##### Note: Spin Echo System #####
[Delft RF Flipper Manual](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/Delft_RF_Flipper_Manual.pdf)<br>

<a name="noteJJXray"></a>
##### Note: JJ X-Ray #####
[7-axis sample stack](http://www.jjxray.dk/products/positioning/multi-axis-stages/sample-stacks)<br>
[Manual](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Larmor/LARMOR%20JJXRAY%20SAMPLE%20STACK.pdf)

<a name="noteSampleStack"></a>
##### Note: SampleStack #####

<a name="noteMonitor"></a>
##### Note: Monitor #####
In/Out positioning<br>
Driven by [Galils](#noteGalil)

<a name="noteDAE"></a>
##### Note: DAE #####
Location: Screened Room<br>
DAE-3

<a name="noteCAEN"></a>
##### Note: CAEN HT #####
Location: Screened Room<br>

<a name="noteGalil"></a>
##### Note: Galil #####
Model: [DMC2280](http://www.galilmc.com/products/dmc-22x0.php)

<a name="noteOMRON"></a>
##### Note: OMRON PLC #####
ISIS Bench Air Line Control

<a name="notePfeiffer"></a>
##### Note: Pfeiffer #####
Location: TBC - alongside PLCs<br>
[LARMOR](https://github.com/ISISComputingGroup/IBEX/wiki/LARMOR-Instrument-Details), [IMAT](https://github.com/ISISComputingGroup/IBEX/wiki/IMAT-Instrument-Details)<br>
Due: Day 1<br>

<a name="noteJulabo"></a>
##### Note: Julabo #####
Model: all models at ISIS<br>

<a name="noteOI_ITC503"></a>
##### Note: Oxford Instruments Temperature Controller #####
Model: ITC503<br>
Location: TBC<br>

<a name="noteOI_ILM200"></a>
##### Note: Oxford Instruments Helium Level Meter #####
Model: ILM200 series<br>

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
Model: all models at ISIS<br>

<a name="noteThurlby"></a>
##### Note: Thurlby #####
Model: all models at ISIS<br>

<a name="noteKEPCO"></a>
##### Note: KEPCO #####
1. Model: all models at ISIS
1. [Kepco BOP 100-10MG PSU](http://www.kepcopower.com/bophimod.htm).<br>  See also [#3005](https://github.com/ISISComputingGroup/IBEX/issues/3005)

<a name="noteTektronix"></a>
##### Note: Tektronix #####
1. Model: Oscilloscope [MSO 4104B](http://www.tek.com/oscilloscope/mso4000-dpo4000)
1. Model: Function Generator [AFG 3022B](http://www.tek.com/datasheet/signal-generator/afg3000-function-generator-arbitrary-function-generators)

<a name="noteSampleChanger"></a>
##### Note: SampleChanger #####
Similar to that used on: SANS2D, translations done via sample stack<br>
See [Two-Tier Sample Changer](https://github.com/ISISComputingGroup/IBEX/wiki/TwoTierSampleChanger)

<a name="notePI_Nano"></a>
##### Note: Physik Instrument #####
Model: Nano-positioning Rotation Stage<br>
[PI Software](http://www.physikinstrumente.com/en/products/prdetail.php?sortnr=1100018), [EPICS driver](http://www.aps.anl.gov/epics/modules/manufacturer.php#Physik%20Instrumente)<br>

<a name="noteBioLogic"></a>
##### Note: BioLogic #####
Model: Stopped Flow Cell<br>

<a name="noteSciMag"></a>
##### Note: Scientific Magnetics #####
1. [Scientific Magnetics](http://www.scientificmagnetics.co.uk/)
1. Model: 3 Axis Super conducting magnet & VTI (see [#1398](https://github.com/ISISComputingGroup/IBEX/issues/1398)).

<a name="noteLakeshore"></a>
##### Note: Lakeshore #####
Model: all models at ISIS<br>

<a name="noteSyringePumps"></a>
##### Note: Syringe Pumps #####
Model: all models at ISIS<br>

<a name="noteHitachi"></a>
##### Note: Hitachi #####
Hitachi L-7100 HPLC pump (no longer supported at ISIS).  ~Can't find L-7100 on [Hitachi web-site](http://www.hitachi-hightech.com/global/about/corporate/group/hhs) (may be obsolete).  Check existing SECI VI for logic and manual: both VI and manual are located here: `C:\LabVIEW Modules\Drivers\Hitachi L-7100`.~
   * Update (27-06-2019): Hitachi pumps are no longer used.  No longer any need to support them.  See [#3780](https://github.com/ISISComputingGroup/IBEX/issues/3780).


<a name="noteMcLennan"></a>
##### Note: McLennan #####
Location: TBC<br>
As used on: Many instruments<br>

<a name="noteKnauer"></a>
##### Note: Knauer Electric Valve Drive  #####
Knauer K-6 Electric Valve Drive.  [Knauer web site](https://www.knauer.net)<br>
K-6 model appears to have been superseded.  Check existing SECI VI for logic and manual.

<a name="noteLinkam"></a>
##### Note: Linkam #####
Location: TBC<br>
There are VIs for this.<br>
See also [Linkam T95 controller](http://www.linkam.co.uk/t95-system-controllers/) and tickets [#1106](https://github.com/ISISComputingGroup/IBEX/issues/1106), [#1496](https://github.com/ISISComputingGroup/IBEX/issues/1496), [#1509](https://github.com/ISISComputingGroup/IBEX/issues/1509).

<a name="noteKeithley"></a>
##### Note: Keithley #####
Model: all models in use at ISIS<br>
There are VIs for this<br>

# SANDALS

This page collects information that will be useful for the implementation of the IBEX control system on SANDALS.
## Background & Timeline ##
SANDALS is a diffractometer instrument at ISIS, on TS1. The [SANDALS](https://www.isis.stfc.ac.uk/Pages/sandals.aspx) web page describes the background to the instrument.

## Control System ##
SANDALS will migrate from the SECI control system to the IBEX control system in January 2018.

## SANDALS Equipment ##
The equipment listed below is used on SANDALS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | N/A | Chopper | N/A |     | [see Chopper note](#noteChopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | | 
??? |  | 2-axis jaws |  |  | [see Jaws note](#noteJaws)
ISIS | ??? | ISIS Vacuum System |  |  |[see Vacuum System note](#noteVacuum)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#noteVacuum)
Pfeiffer | TPG26x | Vacuum Gauge | RS-232 | EPICS | [see Vacuum Pump note](#noteVacuumPump)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
Oxford Instruments | Orange Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#noteOxfordInstruments)
Oxford Instruments | Blue Cryostat| Cryogenic System |   |  | [see Oxford Instruments note](#noteOxfordInstruments)
   |   | Closed Cycle Refrigerator | | | | [see CCR note](#noteCCR)
ISIS | Furnace | Furnace |   |  | [see ISIS Furnaces note](#noteISISFurnaces)
ISIS | SANDALS Sample Changer | Sample Changer | RS-232 | | [see SANDALS Sample Changer note](#noteSampleChanger)
Julabo | FP-50 | Water Bath | RS-232 | | [see Water Bath note](#noteWaterBath)
Julabo | FP-52 | Water Bath | RS-232 | | [see Water Bath note](#noteWaterBath)
~Haake~ | ~???~ | ~Water Bath~ | ~RS-232~ | | [see Water Bath note](#noteWaterBath)
Chell | CCD100 | Pressure Transducer | RS-232 | | [see Chell note](#noteChell)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#noteKeithley)

<a name="noteDAE"></a>
##### Note: DAE #####
Main Detector banks + fixed monitors.

<a name="noteChopper"></a>
##### Note: Choppers #####
SANDALS has no choppers.<br>
A T0 chopper _might_ be installed on SANDALS at some point in the distant future (but there are no definite plans, so for all practical purposes there are no choppers on SANDALS).<br>
_**Note:**_ NIMROD does not have choppers either.

**Note:** There is a proposal to fit a chopper to SANDALS in February 2020.  The chopper would be a SKF G5 chopper (as used on IMAT and LET - see also [#1907](https://github.com/ISISComputingGroup/IBEX/issues/1907).

<a name="noteJaws"></a>
##### Note: Jaws #####
SANDALS has a single set of jaws controlled by a [Parker controller](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_Parker_Controller.jpg), which is not currently controlled by SECI.  There is no requirement to support the Parker system in IBEX, although it would be very convenient if such a thing were possible.

It is proposed to replace the Parker controller with a Galil DMC4040 controller (see [#3259](https://github.com/ISISComputingGroup/IBEX/issues/3259)).

<a name="noteVacuum"></a>
##### Note: Vacuum System #####
The vacuum pressure on SANDALS is the pressure in the SANDALS tank/chamber itself.  SANDALS only needs to monitor the vacuum pressure; scientists do not want to control the vacuum system from IBEX.  The vacuum pressure is also displayed on [a gauge mounted on the "fence"](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_fence.jpg) that surrounds SANDALS.
TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

<a name="noteVacuumPump"></a>
##### Note: Vacuum Pump #####
SANDALS uses a [vacuum pump](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_Turbo_Pump.jpg) (in conjunction with CCRs).  A TPG26x is used to measure the pressure.
TPG26x support was originally implemented via [#1411](https://github.com/ISISComputingGroup/IBEX/issues/1411), [#2379](https://github.com/ISISComputingGroup/IBEX/issues/2379) and [#2578](https://github.com/ISISComputingGroup/IBEX/issues/2578)

<a name="notePLC"></a>
##### Note: Gate Valve PLC #####
SANDALS has an [Omron PLC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Omron-FINS) to control two gate valves, one of which has not been set up yet. `GV2` is currently in use and has been set up in SANDALS' base component. The PV for the V1 valve already exists so is ready to create blocks for when it is set up correctly, but currently nothing is wired up on the PLC end. We can still read the status for it. 

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_Eurotherms.jpg) are used to control temperature Orange Cryostat, CCR and Furnace devices.

<a name="noteOxfordInstruments"></a>
##### Note: Oxford Instruments #####

1. Orange Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Low-Temperature-Cryostats.aspx) to be determined.  Orange cryostats are controlled via a temperature controller (e.g. Eurotherm), so nothing on the cryostat itself for IBEX to control.
   1. Orange cryostat is used occasionally on SANDALS.
1. Blue Cryostat: [models](https://www.isis.stfc.ac.uk/Pages/Low-Temperature-Cryostats.aspx) to be determined.
   1. Blue cryostat is very rarely used on SANDALS.
   1. Are these the Heliox and ITC devices?
   1. The Heliox device has a sorption insert (is that relevant to the control system?)
1. SANDALS does not use Dilution fridges.

<a name="noteCCR"></a>
##### Note: Closed Cycle Refrigerators #####
   1. [CCR](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_CCR.jpg) is the most frequently used low-temperature device used in on SANDALS.
[CCRs](https://www.isis.stfc.ac.uk/Pages/Closed-Cycle-refrigerators,-CCRs.aspx). Not directly computer-controlled  - controlled via Eurotherm.

<a name="noteISISFurnaces"></a>
##### Note: ISIS Furnaces #####
More information on [IRIS Furnaces](https://www.isis.stfc.ac.uk/Pages/High-temperature.aspx).  Furnaces are controlled via a temperature controller (e.g. Eurotherm), so nothing on the furnace itself for IBEX to control.

<a name="noteSampleChanger"></a>
##### Note: SANDALS Sample Changer #####
The [SANDALS sample changer](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_Sample_Changer_bottom.jpg) can hold up to 15 samples.  It has recently been upgraded to use a [Beckhoff PLC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Beckhoff) which controls the jaws as well. 
<a name="noteWaterBath"></a>
##### Note: Water Bath #####
SANDALS uses two types of water bath, both Julabo models: FP-50 and [FP-52](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/SANDALS/SANDALS_Julabo_FP52.jpg).  
See [supported Julabo models](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Julabo) for more details.
SANDALS uses the FP-52 model of Julabo most frequently (used in conjunction with the [Sample Changer](#noteSampleChanger)).  Sometimes SANDALS uses water as the coolant/heating medium; sometimes it uses oil or glycol as the coolant/heating medium (Julabo/Presto A40 device).  SANDALS has also used Haake water bath in the past, but none of the current instrument scientists know anything about this (so it might have been a one-off).

<a name="noteChell"></a>
##### Note: Chell #####
Experiments requiring pressure transducer. [Chell CCD100](http://www.chell.co.uk/product_details/flow-products/chell-ccd100).  See also [#1827](https://github.com/ISISComputingGroup/IBEX/issues/1827).
**Note:** also ask about Gas Panel/Baratron

<a name="noteKeithley"></a>
##### Note: Keithley #####
Experiments requiring source meter. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter).<br>
See also [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826).

## SANDALS SECI Configs ##
Document information about SANDALS SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
SANDALS_place_holder1.conf             | -                                                  | dd/mm/yyyy    | -        |
SANDALS_place_holder2.conf             | -                                                  | dd/mm/yyyy    | -        |

## SANDALS Genie Scripts ##
Similarly, Document information about SANDALS SECI Genie scripts here.

## SANDALS Notes ##
Add any notes about special items of equipment, setup or conditions on SANDALS that might impact the deployment and configuration of IBEX.


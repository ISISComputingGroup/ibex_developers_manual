# EMMA

```{include} migration_notes_warning.mdinc
```

This page collects information that will be useful for the implementation of the IBEX control system on EMMA.
## Background & Timeline ##
EMMA is an instrument at ISIS, on TS1 and used primarily for test purposes. The primary users of EMMA are the sample environment team and the detector team.  There appears to be no web pages (or other material) describing the background to the instrument.

Instrument scientist contact is **Jeffrey Sykora**.

## EMMA Equipment ##
The equipment listed below is used on EMMA. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes | Use in ISIS Cycle |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------|--------------
ISIS | DAE 2 & 3 | Detector Electronics | Ethernet | | [see DAE note](#emma_noteDAE)|17_1
ISIS |  | Monitors |  |  | [see DAE note](#emma_noteDAE)|17_1
ISIS | Mk2 Chopper | Chopper | RS-232 | See [#2130](https://github.com/ISISComputingGroup/IBEX/issues/2130) | [see Chopper note](#emma_noteChopper)|??
SKF |  | Fermi Chopper | RS-232 |  | [see FermiChopper note](#emma_noteFermiChopper)|??
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | |17_1
ADC |  | 1 x 4-blade jaws |  |  | Blades driven by Galils.  [see Jaws note](#emma_noteJaws)
ISIS | TPG300 | ISIS Vacuum System |  |  |[see Vacuum System note](#emma_noteVacuum)
ISIS |  | YZ Table | [see Galil note](#emma_noteYZTable) |  | [see YZ Table note](#emma_noteYZTable)
ISIS |  | Rotation Stage | [see Galil note](#emma_noterotationstage) |  | [see RotationStage note](#emma_noterotationstage)
EURO-THERM | | Temperature Controller |
[CAEN](http://www.caen.it/csite/HomePage.jsp) | HT | Detector HV Control | Ethernet | [#212](https://github.com/ISISComputingGroup/IBEX/issues/212) |[see CAEN HT note](#emma_noteCAENHT)

The following items are on EMMA's wish-list.  They are items for the future (i.e. support is not required until such times as the individual items can be procured).

Manufacturer | Model | Type | Connection | Driver | Notes | Use in ISIS cycle
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------|----------
[CAEN](http://www.caen.it/csite/HomePage.jsp) |   | Digitiser | Ethernet |  |[see CAEN Digitiser note](#emma_noteCAENDigitiser)
Acqiris |  | Digitiser | RS-232 | | [see Acqiris Digitiser note](#emma_noteAcqirisDigitiser)
NI |  | Digitiser | RS-232 | | [see NI Digitiser note](#emma_noteNIDigitiser)
[Tektronix](http://www.tek.com/oscilloscope#all) |  | Oscilloscope | Ethernet | |[see Tektronix note](#emma_noteTektronix)

{#emma_noteDAE}
##### Note: DAE #####
Main Detector banks + fixed monitors.
EMMA has 4 monitors:

1. Monitor 1: stationary; located after the T0 chopper
1. Monitor 2: stationary; located after the Fermi chopper
1. Monitor 3: stationary; located between the jaws and the Y-Z table
1. Monitor 4: currently stationary, but would like it to be moveable in future; located after the rotation stage

{#emma_noteChopper}
##### Note: Choppers #####
One T0 chopper.<br>
Chopper is ISIS Mk2 chopper.  Mk2 choppers have a serial interface (not Ethernet like Mk3).
See [#2130](https://github.com/ISISComputingGroup/IBEX/issues/2130) for IOC & OPI for Mk2 chopper.<br>
The front panel of the Mk2 chopper control crate (located in the EMMA rack) looks like this:
* [wide angle view](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FEMMA%2FEMMA%5FT0%5FChopper%5FFront%5FPanel%5F%28wide%29%5F2017%5F06%5F05%2Ejpg&viewid=45d81cb9%2D9571%2D4a80%2Da5cc%2D2cb4871703a3&parent=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FEMMA)
* [zoomed-in view](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FEMMA%2FEMMA%5FT0%5FChopper%5FFront%5FPanel%5F%28zoom%29%5F2017%5F06%5F05%2Ejpg&viewid=45d81cb9%2D9571%2D4a80%2Da5cc%2D2cb4871703a3&parent=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FEMMA)

{#emma_noteFermiChopper}
##### Note: Fermi Chopper #####
EMMA has a single Fermi chopper (manufactured by SKF).<br>
Link to [Manual](https://stfc365.sharepoint.com/:b:/r/sites/ISISExperimentControls/ICP%20Discussions/EMMA/Mirrortron-SKF%20892-0053%20MB350PC_R%20Rev%20C.pdf?csf=1&web=1&e=hctyNH)<br>
The Fermi chopper control crates (located in the EMMA rack) look like this:
* [Front View (upper & lower crates)](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FEMMA%2FEMMA%5FSKF%5FFermiChopper%5FController%5FFront%5FUpper%5FLower%5F2017%5F06%5F05%2Ejpg&viewid=45d81cb9%2D9571%2D4a80%2Da5cc%2D2cb4871703a3&parent=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FEMMA)
* [Rear View (upper crate)](https://stfc365.sharepoint.com/:i:/r/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA_SKF_FermiChopper_Controller_Rear_Upper_2017_06_05.jpg?csf=1&web=1&e=GzrImg)
* [Rear View (lower crate)](https://stfc365.sharepoint.com/:i:/r/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA_SKF_FermiChopper_Controller_Rear_Lower_2017_06_05.jpg?csf=1&web=1&e=qJrYiI)

{#emma_noteFermiChopperLift}
##### Note: Fermi Chopper Lift #####
The Fermi chopper is lifted into position by a Galil controlled motor.<br>
The Fermi chopper must not be operated when it is not in the beam (i.e. in the parked/upper position)
There is a hardware interlock to prevent the Fermi chopper from being operated in the parked position.  This interlock is implemented in the Galil controller, via a Galil program (described in the [EMMA chopper lifter - Handover](https://stfc365.sharepoint.com/:w:/r/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA%20chopper%20lifter%20-%20Handover.docx?d=wafc19324e3354636b5ab702a140668aa&csf=1&web=1&e=A6BnDe) document).  

{#emma_noteJaws}
##### Note: Jaws #####
EMMA has one four-blade set of jaws.  All blades driven by motors connected to Galil controllers.
Jaw set is manufactured by Advanced Design Consultancy.

{#emma_noteVacuum}
##### Note: Vacuum System #####
The vacuum system ([TPG300](https://stfc365.sharepoint.com/:i:/r/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA_TPG300_2017_06_05.jpg?csf=1&web=1&e=k6q5ew)) on EMMA is currently (06/03/2017) not operational.  Outside possibility that it may be operational by cycle 2017/02.

{#emma_noteYZTable}
##### Note: Y-Z Table #####
Driven by Galil controlled motors.
[Photograph of Y-Z table](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA_Y_Z_Table_2017_06_05.jpg).

{#emma_noteRotationStage}
##### Note: Rotation Stage #####
Driven by Galil controlled motors.
[Photograph of Rotation Stage](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA_Rotation_Stage_2017_06_05.jpg).  It sits on top of the Y-Z table when in use.

{#emma_noteCAENHT}
##### Note: CAEN HT #####
CAEN high-voltage system is a [SYS2527](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/EMMA/EMMA_CAEN_HV_PSU_2017_06_05.jpg) (see tickets: #212, #241, #320, #419, #424)

{#emma_noteCAENDigitiser}
##### Note: CAEN Digitiser #####
For the future - it's on the wish list (model not currently known).

{#emma_noteAcqirisDigitiser}
##### Note: Acqiris Digitiser #####
For the future - it's on the wish list.
Desired model is Acqiris digitiser - PXI8570 controller chassis with DC 440 (400MS/s 100 MHz) digitiser card.<br>
Note that Acqiris is now part of Keysight (see [Keysight digitizers](http://www.keysight.com/en/pc-1128783/High-Speed-Digitizers-and-Multichannel-Data-Acquisition-Solution?cc=GB&lc=eng)).

{#emma_noteNIDigitiser}
##### Note: NI Digitiser #####
For the future - it's on the wish list.
Desired model is National Instruments digitiser - PXIe-1082 chassis, PXIe-8135 controller and a PXIe-5162 digitizer (5GS/s and 1.5GHz).
See [NI Digitizers/Oscilloscopes](http://sine.ni.com/np/app/main/p/bot/no/ap/mi/lang/en/pg/1/sn/n17:mi,n21:40,n24:PXI-FSLASH-CompactPCI/).

{#emma_noteTektronix}
##### Note: Tektronix #####
For the future - it's on the wish list.  Desired models are:
1. [Tektronix Oscilloscope DPO7000](http://www.tek.com/oscilloscope/dpo7000-digital-phosphor-oscilloscope)
1. [Tektronix Oscilloscope MSO4054](http://www.tek.com/oscilloscope/mdo4000c-mixed-domain-oscilloscope)


## EMMA Notes ##
Add any notes about special items of equipment, setup or conditions on EMMA that might impact the deployment and configuration of IBEX.
1. Screenshots of [EMMA VIs](https://github.com/ISISComputingGroup/ControlsWork/issues/239)

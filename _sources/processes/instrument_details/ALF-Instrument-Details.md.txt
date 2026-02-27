# ALF

```{include} migration_notes_warning.mdinc
```

This page collects information that will be useful for the implementation of the new control system on ALF.

### Background & Timeline
The ​ALF web page describes the background to the instrument.

### GUI
ALF will use the IBEX control system.

### ALF Equipment
The equipment listed below is used on ALF. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table). 

Manufacturer | Model | Type | Connection | Driver | Notes
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | [#218](https://github.com/ISISComputingGroup/IBEX/issues/218) |[see DAE note](#alf_noteDAE)
[Galil](http://www.galilmc.com/) | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | EPICS |[see Galil note](#alf_noteGalil)
 |  | JAWS | | | [#179](https://github.com/ISISComputingGroup/IBEX/issues/179), [#180](https://github.com/ISISComputingGroup/IBEX/issues/180) |[see Jaws note](#alf_noteJaws)
unknown | 6-axis | Goniometer |  |  |[see Goniometer note](#alf_noteGoniometer)

{#alf_noteDAE}
##### Note: DAE #####
Location: Screened Room<br>
DAE-2

{#alf_noteGalil}
##### Note: Galil #####
Model: [DMC2280](http://www.galilmc.com/products/dmc-22x0.php).<br>
Photograph of [ALF Galil Crate](https://stfc365.sharepoint.com/:i:/r/sites/ISISExperimentControls/ICP%20Discussions/ALF/ALF_Galil_Crate.jpg?csf=1&web=1&e=tteUae).<br>
Note that GALIL_02 had trouble communicating asynchronously so Freddie switched it to synchronous (done by making the third argument of `GalilCreateController("Galil", "$(GALILADDR02)", 20)` negative in `galil2.cmd`).

{#alf_noteJaws}
##### Note: Jaws #####
Location: various<br>
Driven by [Galils](#alf_noteGalil).<br>
Photograph of [ALF Slits/Jaws](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FALF%2FALF%5FSlits%2Ejpg&viewid=45d81cb9%2D9571%2D4a80%2Da5cc%2D2cb4871703a3&parent=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FALF).

{#alf_noteGoniometer}
##### Note: Goniometer #####
Model: 6-axis Goniometer, unknown model & manufacturer.<br>
Driven by [Galils](#alf_noteGalil).<br>
See [ALF Goniometer Axes](/specific_iocs/motor_extensions/ALF-Goniometer-Axes) for details of how the Goniometer is set up and configured.<br>
Photographs of [ALF Goniometer (1)](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FALF%2FALF%5FGoniometer%5F1%2Ejpg&viewid=45d81cb9%2D9571%2D4a80%2Da5cc%2D2cb4871703a3&parent=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FALF) and [ALF Goniometer (2)](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FALF%2FALF%5FGoniometer%5F2%2Ejpg&viewid=45d81cb9%2D9571%2D4a80%2Da5cc%2D2cb4871703a3&parent=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FALF).

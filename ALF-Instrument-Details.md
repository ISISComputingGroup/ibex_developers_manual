## ALF

This page collects information that will be useful for the implementation of the new control system on ALF.

### Background & Timeline
The ​ALF web page describes the background to the instrument.

### GUI
ALF will use the IBEX control system.

### ALF Equipment
The equipment listed below is used on ALF. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table). 

Manufacturer | Model | Type | Connection | Driver | Notes
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | [#218](https://github.com/ISISComputingGroup/IBEX/issues/218) |[see DAE note](#noteDAE)
[Galil](http://www.galilmc.com/) | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | EPICS |[see Galil note](#noteGalil)
 |  | JAWS | | | [#179](https://github.com/ISISComputingGroup/IBEX/issues/179), [#180](https://github.com/ISISComputingGroup/IBEX/issues/180) |[see Jaws note](#noteJaws)
unknown | 6-axis | Goniometer |  |  |[see Goniometer note](#noteGoniometer)

<a name="noteDAE"></a>
##### Note: DAE #####
Location: Screened Room<br>
DAE-2

<a name="noteGalil"></a>
##### Note: Galil #####
Model: [DMC2280](http://www.galilmc.com/products/dmc-22x0.php).<br>
Photograph of [ALF Galil Crate](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ALF/ALF_Galil_Crate.jpg).<br>
Note that GALIL_02 had trouble communicating asynchronously so Freddie switched it to synchronous (done by making the third argument of `GalilCreateController("Galil", "$(GALILADDR02)", 20)` negative in `galil2.cmd`).

<a name="noteJaws"></a>
##### Note: Jaws #####
Location: various<br>
Driven by [Galils](#noteGalil).<br>
Photograph of [ALF Slits/Jaws](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ALF/ALF_Slits.jpg).

<a name="noteGoniometer"></a>
##### Note: Goniometer #####
Model: 6-axis Goniometer, unknown model & manufacturer.<br>
Driven by [Galils](#noteGalil).<br>
See [ALF Goniometer Axes](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/ALF-Goniometer-Axes) for details of how the Goniometer is set up and configured.<br>
Photographs of [ALF Goniometer (1)](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ALF/ALF_Goniometer_1.jpg) and [ALF Goniometer (2)](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ALF/ALF_Goniometer_2.jpg).

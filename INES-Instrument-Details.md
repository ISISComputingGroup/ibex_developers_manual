This page collects information that will be useful for the implementation of the IBEX control system on INES.
## Background & Timeline ##
INES is a powder diffractometer instrument at ISIS, on TS1. The [INES](https://www.isis.stfc.ac.uk/Pages/ines.aspx) web page describes the background to the instrument.

## Control System ##
INES will migrate from the SECI control system to the IBEX control system in late October 2018 (prior to Cycle 2018/03).

## INES Equipment ##
The equipment listed below is used on INES. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
ISIS | N/A | Shutter | | | [see Shutter note](#noteShutter)
ISIS | DAE 2 | Detector Electronics | Ethernet | | [see DAE note](#noteDAE)
ISIS | Mk3 | Chopper | N/A |     | [see Chopper note](#noteChopper)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Galil%20Motion%20Control) | [see Galil note](#noteGalil) | 
??? |  | 4-blade jaws |  |  | [see Jaws note](#noteJaws)
ISIS | N/A | ISIS Vacuum System |  |  |[see Vacuum System note](#noteVacuum)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232 | EPICS | [see Vacuum System note](#noteVacuum)
Eurotherm | Temperature Controller | All models at ISIS | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm  note](#noteEurotherm)
Keithley | 2410 | Source Meter | RS-232 | | [see Keithley note](#noteKeithley)

<a name="noteDAE"></a>
##### Note: DAE #####
INES uses DAE-2.  INES has 2 fixed monitors.

<a name="noteShutter"></a>
##### Note: Shutter #####
INES shares a shutter with TOSCA.  INES needs to know the status of the TOSCA shutter.<br>
INES also has a secondary shutter.  The status of the secondary shutter cannot currently (September 2018) be read (it requires the installation of an appropriate electronic device to provide a signal).  At the present time, INES has no need to monitor the secondary shutter via IBEX (for the same reasons, the secondary shutter cannot be monitored with SECI).

<a name="noteChopper"></a>
##### Note: Choppers #####
INES has a Mk3 chopper, which is shared with TOSCA.  The chopper is usually set up to suit both instruments.<br>
TOSCA is first in the beamline, but INES needs to know the chopper settings.  User should not be able to change the chopper settings (i.e. protect these with Manager Mode).

<a name="noteGalil"></a>
##### Note: Galil #####
INES has two Galil controllers.  Used to control jaws, XY table, goniometers, transmission monitors.

<a name="noteJaws"></a>
##### Note: Jaws #####
INES has a 4-blade jaws.  The jaws were manufactured in Italy, but are driven by Galil.

<a name="noteVacuum"></a>
##### Note: Vacuum System #####
INES occasionally uses a vacuum tank, which is mounted on the sample table (the XY table gets removed first!).
INES would like to be able to monitor the vacuum pressure in IBEX.<br>
The vacuum is monitored using a TPG300 pressure gauge.  TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

<a name="noteEurotherm"></a>
##### Note: Eurotherm #####
[Eurotherms](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/INES/INES_Eurotherms.jpg) are used to control temperature in the vacuum tank.

<a name="noteKeithley"></a>
##### Note: Keithley #####
1. [Keithley 2400 Series Source Meter](https://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter).<br>
See also tickets [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#2695](https://github.com/ISISComputingGroup/IBEX/issues/2695), [#2801](https://github.com/ISISComputingGroup/IBEX/issues/2801) and [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176).
1. Keithley 2410 is used only rarely (for neutron instrumentation projects)

## INES SECI Configs ##
Document information about INES SECI configs here.

Configuration Name                     | Sub-Configurations                                 | Last Accessed | Required |
---------------------------------------|----------------------------------------------------|---------------|----------|
5_Axis                                 | -                                                  | 14/02/2011    | -        |
AncientCharm                           | -                                                  | 14/02/2011    | -        |
Blank                                  | -                                                  | 18/02/2011    | -        |
Eurotherms & Keithley                  | Keithley                                           | 06/06/2014    | Yes      |
Eurotherms                             | -                                                  | 19/05/2014    | Yes      |
Goniometer                             | -                                                  | 01/07/2011    | Yes      |
INES Base                              | -                                                  | 28/04/2014    | Yes      |
practice                               | -                                                  | 14/02/2011    | -        |
Sample_Changer                         | -                                                  | 01/07/2011    | Yes      |
TEST                                   | -                                                  | 19/08/2010    | -        |
Tomography                             | -                                                  | 24/05/2011    | -        |

## INES Genie Scripts ##
Similarly, Document information about INES SECI Genie scripts here.

## INES Notes ##
INES has the following specialist panels:
1. INES IV
   1. This is a SECI VI, customised for INES.  We should check what information it displays that is not already included in the standard IBEX dashboard.  A new OPI may be required.
1. GEM Jaws
   1. **Note:** GEM has been upgraded and now has new jaws.  "GEM Jaws" may refer to the old GEM jaws VI.
   1. Check if the behaviour of the standard jaws OPI meets the needs of INES.
1. Walter SE `Rotacq2` 
   1. This refers to an old rotation stage, which is no longer used.

INES has the following devices under motion control:
1. Goniometer
   1. INES has 2 goniometers: one large, one small.
   1. Both goniometers are controlled by Galil controllers.
1. Jaws
   1. The jaws are controlled by Galil controllers.
1. Sample Changer
   1. INES has a 4 position sample changer, controlled by a Galil controller.
1. Transmission Monitor
   1. Transmission monitors on INES are fixed.
1. Neutron Camera
   1. Used to take images of the samples.  Camera is mounted on a single vertical axis.  Users should have the ability to move the camera in and out of the beam only.  The instrument scientist would like the ability to control precise position of the camera (using manager mode).
1. XY Table
   1. INES XY table is used to move the sample parallel (y-axis) and perpendicular (x-axis) to the beam.  Controlled by a Galil controller.
   1. The XY table will be upgraded (probably sometime before April 2019) with the addition of a rotational stage.  The rotation axis will be the vertical axis (z-axis) and will also be controlled by a Galil.

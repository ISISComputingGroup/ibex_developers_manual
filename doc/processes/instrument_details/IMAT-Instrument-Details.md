# IMAT

This page collects information that will be useful for the implementation of the new control system on IMAT.
## Background & Timeline ##
The [IMAT](http://www.isis.stfc.ac.uk/instruments/imat/imat8259.html) web page describes the background to the instrument.  Additional material is also available on the [IMAT sharepoint](http://www.facilities.rl.ac.uk/isis/projects/ts2/phase2instruments/IMAT/Forms/AllItems.aspx).

Slides sets from IMAT operational review of 21st May 2014 are available: [Intro](http://www.facilities.rl.ac.uk/isis/projects/ts2/phase2instruments/IMAT/Reviews/IMAT%20Operational%20Review%20intro.pdf), [Science](http://www.facilities.rl.ac.uk/isis/projects/ts2/phase2instruments/IMAT/Reviews/IMAT%20Operational%20Review%20-Science.pdf), [Engineering](http://www.facilities.rl.ac.uk/isis/projects/ts2/phase2instruments/IMAT/Reviews/IMAT%20Operational%20Review%20-%20Main.pdf).

The presentation [IMAT Overview](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_Overview.pptx) provides an overview of the IMAT system from a computing/control perspective.

## Control System ##
IMAT will use the IBEX control system.

## Data Collection ##
Discussions regarding IMAT data collection requirements are documented in [Minutes (15/10/2014)](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_DataCollection_Storage_Minutes_15Oct2014.pdf) and [Minutes (28/04/2015)](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_DataCollection_CCDcamera_28April2015_Notes.docx). The [proposed file formats](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_DataCollection_Format_proposal_v2.docx) are also documented.

## IMAT Equipment ##
The equipment listed below is used on IMAT. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
[SKF](http://www.skf.com/group/products/magnetic-systems/magnetic-systems-applications/neutron-chopper-instrumentation/index.html) | Double Disc Chopper | CHOPPER | Ethernet/Modbus | #617, #622 | [see SKF Choppers note](#imat_noteSKFChoppers) 
[SKF](http://www.skf.com/group/products/magnetic-systems/magnetic-systems-applications/neutron-chopper-instrumentation/index.html) | T0 Chopper | CHOPPER | Ethernet/Modbus | #617, #622 | [see SKF Choppers note](#imat_noteSKFChoppers) 
[SKF](http://www.skf.com/group/products/magnetic-systems/magnetic-systems-applications/neutron-chopper-instrumentation/index.html) | Double Disc Chopper | CHOPPER | Ethernet/Modbus | #617, #622 | [see SKF Choppers note](#imat_noteSKFChoppers) 
[Pfeiffer](http://www.pfeiffer-vacuum.com/products/measurement/container.action) | TPG 300 | ISIS Vacuum System | RS232 | #216 | 
OMRON PLC | | | TCP/FINS | #215 | [see OMRON PLC note](#imat_noteOMRONplc) 
ISIS | Sample Attenuator | Pneumatic Actuator | | | [see Beam Attenuator note](#imat_noteBeamAttenuator)
ISIS | Pin Hole Selector | | | #265 | [see Pinhole Selector note](#imat_notePinhole)
ISIS | JAWS | GALIL-based | Ethernet | #178, #179 | [see Jaws note](#imat_noteJaws)
ISIS | Incident Slits | GALIL-based | Ethernet | #178, #179 | [see Incident Slits note](#imat_noteSlits)
ISIS | Monitors |  | | #265 | [see Incident Slits note](#imat_noteMonitors)
 | 7-axis Sample Positioning System | | | #435 | [see Sample Positioning System note](#imat_noteSampleStack)
ISIS |  | Sample Environment | Various |  | [see Sample Environment note](#imat_noteSampleEnvironment)
TBD | TBD | Camera Positioning Robot | TBD | | [see Camera Positioning Robot note](#imat_noteCameraRobot)
UC(Berkeley) | Camera1 | Med. Res. CCD Imaging Camera | Specific to camera | | [see Berkeley Camera note](#imat_noteBerkeleyCamera)
CNR | Camera2 | | | | [see Messina Camera note](#imat_noteMessinaCamera)
CNR | Camera Focussing | | | | [see Messina Camera note](#imat_noteMessinaCamera)
ISIS | DAE 2 or 3? | Detector Electronics | Ethernet | |  [see DAE note](#imat_noteDAE)
Mantracourt | ADW15 | Load cell meter | RS232 or RS485 | |  [see Mantracourt note](#imat_noteMantracourt)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet | EPICS | | 
Newport | [M-ILS50PP](https://web.archive.org/web/20130828020800/http://search.newport.com:80/?q=*&x2=sku&q2=ILS50PP) | Linear Stage, Stepper Motor | Ethernet | EPICS | [see Newport Motor note](#imat_noteNewportMotor)

{#imat_noteSKFChoppers}
##### Note: SKF Choppers #####
IMAT will have three sets of choppers: a double-disk chopper, a T0 chopper and a second double-disk chopper.  All three SKF choppers use the same control system: see [SKF Modbus/TCP interface](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/892-0117%20Rev%20B%20modbus%20(Updated%202014-10-17).pdf) for details.  Instrument scientists would like to control choppers as 5 independent disks.  There is also a need to "park" the choppers in the open position (to allow white beam imaging).

{#imat_noteBeamAttenuator}
##### Note: Beam Attenuator #####
The purpose of beam attenuator is to protect the sample & camera while either is being positioned.  The time taken to open/close the beam attenuator is about 1s.  Driven by pneumatic actuator between limits (2 limit switches).  Position is In/Out. Must communicate with sample positioner - needs both automatic operation and manual control.  Also communicate with data acquisition (c.f. Pause/resume on SANS2D) and camera system.  See [IMAT Fast Shutter](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_FastShutter.pptx) for a diagram. **Note:** the beam attenuator was originally known as the "fast shutter", but this name is now deprecated. See also: [IMAT Sample Attenuator Minutes](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_SampleAttenuator_M5_computing_minutes_29Oct2014.docx).

{#imat_noteOMRONplc}
##### Note: OMRON PLC #####
The OMRON PLC will be used to control gate valves and instrument vacuum.  It will also be used for control of the pneumatic actuator for the Beam Attenuator.

{#imat_notePinhole}
##### Note: Pinhole Selector #####
The Pinhole Selector is a wheel containing mounts for 6 pinhole apertures - set positions for each.  Single axis motion control (stepper motor). Controlled by Galil.  See [IMAT Pin Hole Selector](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_PinHoleSelector.pptx) for a diagram.  See also: [IMAT Pin Hole Selector Details](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/PinholeSelector_2014.pdf) and [IMAT Pin Hole Selector Minutes](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_PinholeSelector_Computing_minutes_28Nov2014.docx).

{#imat_noteJaws}
##### Note: Jaws #####
5 x beam-collimating jaw-sets, controlled by Galil. <br>See [IMAT Jaws & Collimating Slits](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_Jaws_Collimating_Slits.pptx) for a diagram.  See also: [IMAT Jaws/Slits Minutes](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Jaws-Slits_computing_minutes_17Nov2014.docx)

{#imat_noteSlits}
##### Note: Slits #####
X-Y slits (2 linear translations), controlled by Galil. <br>See [IMAT Jaws & Collimating Slits](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_Jaws_Collimating_Slits.pptx) for a diagram.

{#imat_noteMonitors}
##### Note: Monitors #####
6 monitors, controlled by Galil. In/Out set positions.

1. M1 is positioned immediately upstream of the first double-disk chopper.
2. M2 is positioned immediately upstream of the second double-disk chopper.
3. M3 is positioned immediately downstream of the second double-disk chopper.
4. M4 is positioned immediately downstream of the pin-hole selector.
5. M5 is positioned immediately downstream of the beam attenuator.  See [IMAT M5 Monitor](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_M5Monitor.pptx) for a diagram of the M5 monitor.
6. M6 position - to be communicated. 

{#imat_noteSampleStack}
##### Note: Sample Positioning System #####
Comprises upper and lower stacks.<br>
Lower stack has X, Y & Z translational degrees of freedom, plus rotational degree of freedom about the Z-axis. Z range = 0-1000mm, X & Y ranges = +/-500mm. Rotation is 0-370 degrees.<br>
Upper stack will be an "off-the-shelf" tomography stack (3 rotational degrees of freedom). Most axes motors will be controlled by Galil (using Galil 4400 firmware).<br>
Some axes motors will be controlled by a Beckhoff system (further details required).<br>
Sample stack needs to communicate with fast shutter.<br>
See [IMAT Sample Positioning System](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_SamplePositioning.pptx) for a diagram. 

{#imat_noteSampleEnvironment}
##### Note: Sample Environment #####
For information about the IMAT sample environment see: [​IMAT Sample Environment](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_SampleEnvironment_Dec2014.pdf) and [IMAT Sample Environment Minutes](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_SampleEnvironment_Minutes_17Dec2014.docx). 

{#imat_noteCameraRobot}
##### Note: Camera Positioning Robot #####
Details of robot positioning system are yet to be decided.  In practice, control of the camera positioning robot may be handled separately from the instrument control system.  See [IMAT Camera](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_Computing_Camera.pptx) for a illustration of the concept. 

{#imat_noteBerkeleyCamera}
##### Note: Berkeley Camera #####
Medium resolution CCD Imaging Camera.  The camera is being manufactured by UC(Berkeley). Assumption is that this camera will have its own control PC. 

{#imat_noteMessinaCamera}
##### Note: Messina Camera #####
High resolution CCD Imaging Camera.  The camera is being manufactured by CNR (University of Messina). Camera is being manufactured by CNR. Control of Andor i334T is via USB 2.0 connector. Camera will have its own control PC. See [IMAT Camera Autofocussing System​](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/RevSciInstrum_84_093701_IMAT%20Camera.pdf) for more details.<br>
Focussing of camera is performed using a 1 x linear motor, controlled by Newport. See [IMAT Camera Autofocussing System​](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/RevSciInstrum_84_093701_IMAT%20Camera.pdf)​ for more details.  2 x motors to control mirror tilt.  Further details in the ​[camera handbook](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_CCD_camera_handbook.pdf) and [​camera electronics](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_CCD_camera_electronics_handbook.pdf) handbook.

This camera has its own control PC that runs the IOCs. The hostname can be found in the `globals.txt`.

{#imat_noteDAE}
##### Note: DAE #####
12+ racks for 20K detector elements.

{#imat_noteMantracourt}
##### Note: Mantracourt #####
Used to measure load on IMAT sample stack .

{#imat_noteNewportMotor}
##### Note: Newport Motor #####
Newport Linear Stepper Motor. 50mm linear travel. Used to focus CNR camera.
Does this motor have its own controller h/w, or does it need a separate controller?
Further details in the [camera handbook](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_CCD_camera_handbook.pdf) and [​camera electronics](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/IMAT/IMAT_CCD_camera_electronics_handbook.pdf) handbook.

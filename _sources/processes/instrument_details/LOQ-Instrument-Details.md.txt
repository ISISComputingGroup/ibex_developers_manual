# LOQ

```{include} migration_notes_warning.mdinc
```

This page collects information that will be useful for the implementation of the IBEX control system on LOQ.
## Background & Timeline ##
LOQ is a time-of-flight SANS instrument instrument at ISIS, on TS1. The [LOQ](https://www.isis.stfc.ac.uk/Pages/LOQ.aspx) web page describes the background to the instrument.

It has 3 collimation apertures (only A2 is computer-controlled), 4 monitors (insertion/removal of M3 is computer-controlled), and 2 detectors (an ORDELA He-3 MWPC 'main' detector and a annular 4-module 'high-angle' scintillator detector, _neither of which move!_). _There are no jaw sets on LOQ._

## LOQ Equipment ##
The equipment listed below is used on LOQ. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. as necessary).

For a _minimally functional instrument_:

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- |------------| ------------- | -------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet   | | [see DAE note](#loq_note-dae)
ISIS | n/a | LiveView |            | | [see Live View note](#loq_note-live-view)
ISIS | Mk3 | Chopper | N/A        |     | [see Chopper note](#loq_note-choppers)
GALIL | [DMC2280](http://www.galilmc.com/products/dmc-22x0.php) | Motion Controller | Ethernet   | [EPICS] | [see Galil note](#loq_note-galil)
ORDELA | 2661N | Ordela Detector |            | | [see Ordela Detector note](#loq_note-ordela-detector)
NI | ??? | Fieldpoint | Ethernet   | | [see Ordela Detector note](#loq_note-ordela-detector)
~Omega~ | ~iBTHX~ | ~Transmitter~ | ~Ethernet~ | | ~[see Omega note](#loq_noteOmega)~
~Omega~ | ~PAC~ | ~Intelligent Controller~ | ~Modbus~   | | ~[see Omega PAC note](#loq_note-omega-pac)~
MOXA | ioLogik | Remote I/O Controller | Ethernet   | | [see MOXA ioLogik note](#loq_note-moxa-iologik)
ISIS | ??? | ISIS Vacuum System |            |  |[see Vacuum System note](#loq_note-vacuum-system)
Pfeiffer | TPG300 | Vacuum Gauge | RS-232     | EPICS | [see Vacuum System note](#loq_note-vacuum-system)
Eurotherm | Temperature Controller | All models at ISIS | RS-232     | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#Eurotherm) | [see Eurotherm note](#loq_note-eurotherm)
Julabo | FP-51 | Water Bath | RS-232     | | [see Water Bath note](#loq_note-water-baths)
ISIS | n/a | Julabo Valve |            | | [see Water Bath note](#loq_note-julabo-valve)
ISIS | LOQ | Sample Changer |            | | [see Sample Changer note](#loq_note-sample-changer)
ISIS | LOQ | Sample Changer Scan |            | | [see Sample Changer Scan note](#loq_note-sample-changer-scan)

There is then a wide range of alternative sample environment used on a much less frequent basis, listed below in (approximate) decreasing order of importance: 

Manufacturer | Model | Type | Connection | Driver | Notes |
------------ | ------------- | ------------- | ------------- | ------------- | -------------------------------------------
CNR-ISIS | n/a | DLS | RS232 & Ethernet | | [see DLS note](#loq_note-dls) - commissioning soon
Thar | ISIS | Pressure Cell | | | [see Pressure Cell note](#loq_note-pressure-cell)
Danfysik | 8000 | PSU | RS232 | DFKPS | [see Danfysik note](#loq_note-danfysik)
Anton-Paar | Physica MCR-501 | Rheometer | | | [see Rheometer note](#loq_note-rheometer)
ISIS | RAL | V/Nb Furnace | | | [see Furnace note](#loq_note-furnace)
ISIS | RAL | Muon Optical Furnace | | | [see Furnace note](#loq_note-furnace)
ISIS | | CCR | | | [see Cryo note](#loq_note-cryo)
ISIS | | Orange Cryostat | | | [see Cryo note](#loq_note-cryo)
ISIS | LOQ | Couette Cell | | | [see Couette Cell note](#loq_note-couette-cell)
McLennan | PM600 | Motion Controller | RS-232 | [EPICS](http://www.aps.anl.gov/epics/modules/manufacturer.php#McLennan%20Servo%20Supplies) | [see McLennan note](#loq_note-mclennan)
Unilever| | Extensional-Flow Cell | | |
ISIS | LOQ | T-Jump Cell | | | [see T-Jump Cell note](#loq_note-t-jump-cell)
Keithley | 2400 | Source Meter | RS-232 | #1826 | [see Keithley note](#loq_note-keithley)
Biologic| ??? | Stop-Flow Cell | | |
Thurlby | EX355P | PSU | ??? | | [see Thurlby note](#loq_note-thurlby)
Huber| SMC 9000 | Motion Controller | Ethernet |  | [see Huber note](#loq_note-huber)

{#loq_note-dae}
##### Note: DAE #####
Also see Ordela Detector note below.

{#loq_note-live-view}
##### Note: Live View #####
1. LOQ has a SECI VI for visualising the data being acquired on the ORDELA detector in real-time. This is essential to efficient instrument operations and will need implementing in Ibex.
2. If it were possible to extend the functionality to include the high-angle detector that would be very welcome.

{#loq_note-choppers}
##### Note: Choppers #####
LOQ has an ISIS Mk3 chopper.<br>

{#loq_note-galil}
##### Note: Galil #####
LOQ Galil drives 4 axes: Sample Changer _height _ stage, Sample Changer _vertical_ stage, A2, and M3.

{#loq_note-ordela-detector}
##### Note: Ordela Detector #####
1. [ORDELA](http://www.ordela.com/) (Oak Ridge Detector Laboratory) is a manufacturer of area-detector devices.  It is a spin-off from Oak Ridge National Laboratory. Detector installed is a Model 2661N He-3 MWPC.
2. This detector is currently controlled (HV on/off, setting discriminator levels) by proprietary W95-era software running on a dedicated PC. The same PC also features a NI DAQ card which can be used to record data independently of the LOQ DAE. This facility is only ever used for detector diagnostics.
3. **LOQ's reliance on an ageing PC/software combination to turn the detector on/off and set the discriminator levels is a significant single-point-of-failure which has been flagged for many years but only recently received any resource (ask DPK). As part of the Ibex migration this issue should be addressed.**
4. The NI Fieldpoint device measures the detector voltage, the discriminator voltage and the detector temperature on three separate channels on separate modules (see VI).  The plan is to replace this obsolete device with an NI cDAQ (model 9185?) with the appropriate modules as this is currently supported in IBEX.
5. The ORDELA detector can be damaged as a result of the neutron count rate being too high. Software is required to detect this over count rate (via the ISISICP) and move an aperture into a position to block the beam (axis controlled by Galil motion controller). Settings should be available to enter the over count rate level and the duration of the over count rate before any action is deemed necessary. The aperture has three discrete positions for normal operation. To block the beam it needs to be moved to the closest mid point of these positions. A message needs to be reported to a contact list and a corresponding message displayed on the instrument screen to identify a problem has been detected. 
(VI references : 1. C:\LabVIEW Modules\DAE\DAE Detector Check.vi 2. C:\LabVIEW Modules\Instruments\LOQ\LOQ Detector Protect\LOQ Detector Protect.llb\LOQ - Detector Protect - Front Panel.vi)

{#loq_noteOmega}
##### ~Note: Omega~ #####
~[OMEGA™ iBTHX transmitter](https://www.omega.co.uk/pptst/IBTX_IBTHX.html) is a device to monitor and record barometric pressure, temperature, relative humidity, and dew point over an Ethernet network or the LOQnet. It is attached to the rear of the ORDELA detector.~

{#loq_note-omega-pac}
##### ~Note: Omega PAC~ #####
~The OMEGA™ iBTHX (see above) is not reliable.  It has been decided to replace it with a [OMEGA™ PAC Controller](https://www.omega.co.uk/pptst/OME-WISE-7000_SERIES.html) device to monitor and record temperature.~

{#loq_note-moxa-iologik}
##### Note: MOXA ioLogik #####
Both the OMEGA™ iBTHX and OMEGA™ PAC devices (see above) have proved unreliable.  It has been decided to use [MOXA ioLogik 12XX](https://www.moxa.com/en/products/industrial-edge-connectivity/controllers-and-ios/universal-controllers-and-i-os/iologik-e1200-series) devices to monitor and record temperature & voltage on the ORDELA detector.

{#loq_note-vacuum-system}
##### Note: Vacuum System #####
1. There are 2 vacuum gauges on LOQ. Both are TPG300's. One is atop the Galil at the sample position monitoring the collimation, and the other is integrated into the detector tank pumping system.
2. Only the detector tank TPG300 was read back in SECI. There are two sensors, one at the pump, and one on the tank.
3. **It is highly desirable to have the collimation TPG300 integrated into Ibex too.**
4. TPG300 support is implemented via [#216](https://github.com/ISISComputingGroup/IBEX/issues/216) and [#2063](https://github.com/ISISComputingGroup/IBEX/issues/2063)

{#loq_note-eurotherm}
##### Note: Eurotherm #####
Eurotherms are used to control the temperature of Orange Cryostats, CCRs and Furnace devices. And also to measure voltages from other sensors.

{#loq_note-water-baths}
##### Note: Water Baths #####
LOQ routinely uses 2 Julabo Water Baths. Both are Model FP-51's. In an emergency (ie, a bath failure) we would use Julabos from the ISIS inventory which include Model FP-50's and Model FP-52's.

> The LOQ Julabo baths act in a pair, and depend on the external/internal status. If the baths are not behaving as you would expect, check whether internal and external have been flipped. We will check out of cycle if this could be caused by IBEX rebooting.

{#loq_note-julabo-valve}
##### Note: Julabo Valve #####
**There is an electrically-operated solenoid valve to allow scripted control of which Julabo Water Bath is thermostating the Sample Changer. This is implemented in SECI and will need replicating in Ibex.**<br>
A similar device could also be used on SANS2D, so a driver for the Julabo Valve will be valuable elsewhere.

{#loq_note-sample-changer}
##### Note: Sample Changer #####
1. The LOQ Sample Changer is driven by a Galil. It sits on a Height Stage which is also driven by a Galil. This combination accounts for >90% of sample environment usage on LOQ.
2. In SECI the Sample Changer can be driven 'manually' from a VI, or 'autonomously' from GCL scripts.
3. **Sample Changer scripts are created by a VB application called LOQscript developed by MJC. An Ibex-compatible equivalent of LOQscript will need to be provided.**

{#loq_note-sample-changer-scan}
##### Note: Sample Changer Scan #####
1. A VI called LOQ SC Scan allows the sample positions on the Sample Changer to be 'scanned in' using the LOQ alignment laser and the output recorded on a photocell. It was written by GDH.
2. The photocell is connected to a [Thor Labs Model PM100A power meter](https://www.thorlabs.com/thorproduct.cfm?partnumber=PM100A).

{#loq_note-dls}
##### Note: Dynamic Light Scattering #####
1. **This apparatus should be ready to commence commissioning in Autumn 2018.** Commissioning will take place on LOQ but the apparatus is intended to be available on LOQ, SANS2D, LARMOR and ZOOM.
2. The apparatus contains a 100 mW Coherent OBIS visible laser with the facility for remote control.
3. The scattered laser light will be processed by an LS Instruments multi-channel, multi-tau, correlator.
4. For further information see ticket [#3361](https://github.com/ISISComputingGroup/IBEX/issues/3361).

{#loq_note-pressure-cell}
##### Note: Pressure Cell #####
The Thar Pressure Cell normally just integrates with the Eurotherm controller.

{#loq_note-danfysik}
##### Note: Danfysik #####
1. : Currently a Danfysik Model 8000 controller is integrated into an ageing GEC power supply, but the GEC unit is due to be replaced in the near future as part of ISIS-wide obsolescence. It will most likely be replaced by a Danfysik power supply. Richard Hale may be able to advise what model.
   1. There is a possibility that the GEC power supply will be replaced prior to December 2018.  The replacement power supply will be a Danfysik 8500 Model 859.
2. [Danfysik Power Supplies](http://www.danfysik.com/en/products/power-supplies/)
3. [User and Software Manuals](https://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/Allhttps://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/Forms/AllItems.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FPower%20Supplies) for System 8500.
4. See [#1208](https://github.com/ISISComputingGroup/IBEX/issues/1208) for comms settings.

{#loq_note-rheometer}
##### Note: Rheometer #####
1. This device is controlled by proprietary software (on a dedicated PC).  Manufacturer is reluctant to allow it to be integrated with ISIS software (i.e. SECI or IBEX).
2. We have in the past used a Eurotherm controller to send a trigger pulse to initiate actions by the proprietary software.
3. Manuals describing the use of the Anton-Paar Physica MCR-501 Rheometer are located here: `\\isis\shares\ISIS_Experiment_Controls\AntonPaar_Physica_MCR501`.

{#loq_note-furnace}
##### Note: Furnaces #####
Furnaces normally just integrate with the Eurotherm controller.

{#loq_note-cryo}
##### Note: CCRs and Cryostats #####
1. CCR's and Cryostats normally just integrate with the Eurotherm controller.
2. _LOQ does not use Cryomagnets. Ever!_

{#loq_note-couette-cell}
##### Note: Couette Cell #####
1. The Couette Cell is driven by a [McLennan PM1000](#loq_note-mclennan) (compatible with a PM600).
2. See also [#3105](https://github.com/ISISComputingGroup/IBEX/issues/3105)

{#loq_note-mclennan}
##### Note: McLennan #####
Support for McLennan devices is well established (see [#1099](https://github.com/ISISComputingGroup/IBEX/issues/1099) and [#1100](https://github.com/ISISComputingGroup/IBEX/issues/1100) and subsequent tickets.

{#loq_note-t-jump-cell}
##### Note: T-Jump Cell #####
1. The T-Jump Cell is driven by a Keithley 2400.
2. See also [#3175](https://github.com/ISISComputingGroup/IBEX/issues/3175)

{#loq_note-keithley}
##### Note: Keithley #####
1. [Keithley 2400 Source Meter](http://uk.tek.com/keithley-source-measure-units/keithley-smu-2400-series-sourcemeter)
2. See also [#1826](https://github.com/ISISComputingGroup/IBEX/issues/1826), [#3176](https://github.com/ISISComputingGroup/IBEX/issues/3176)

{#loq_note-thurlby}
##### Note: Thurlby #####
1. Thurlby EX355P PSU - see [#155](https://github.com/ISISComputingGroup/IBEX/issues/155) and [#198](https://github.com/ISISComputingGroup/IBEX/issues/198).
2. [Thurlby Thandar Instruments EX355P PSU](https://www.aimtti.com/product-category/dc-power-supplies/aim-ex-rseries)

{#loq_note-huber}
##### Note: Huber #####
1. [Huber](https://www.xhuber.com/en/).
2. According to Huber's web-site, a Huber SMC9000 is a motion controller.  See [SMC 9300](https://www.xhuber.com/en/products/3-control/smc-9300/) which appears to be the latest of the 9000-series and [SMC 9000](https://www.xhuber.com/fileadmin/user_upload/downloads/usermanuals/9000_1103.pdf)
3. The Huber device has not been used on LOQ for some time: <br>
_I believe this device was a one-off use by a former member of the instrument team. SMK._<br>
It should not be considered a priority for support on LOQ.  See also [#3502](https://github.com/ISISComputingGroup/IBEX/issues/3502)

## LOQ Notes ##
LOQ has the following specialist panels:
1. <None>

LOQ has the following devices under motion control:
1. Aperture (A2)
   * The aperture device is a plate with 3 different sized aperture holes.  The Galil drives the plate to one of 3 predefined positions (each corresponding to one of the aperture holes).  It would be useful to create a 4th position, corresponding to a solid portion of the aperture plate (so that it can be used to block the beam).
2. Sample Changer (translation & vertical)
   * The sample changer moves in a grid fashion - left/right translation across the beam and up/down vertical translation.  Sample changer positions can be set directly in mm, or  via preset positions (defined in a file, which is edited regularly).  The preset positions use several naming conventions, according to the type of sample rack in use.
3. Transmission Monitor (M3)
   * moves in/out of the beam.


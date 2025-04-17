> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Magnetometers, Fluxgates, and other Magnetic Field Sensors](Fluxgates)

# Bartington

There is a system in use by the North Side Muon beamlines from [Bartington](https://www.bartington.com) that will be used to measure the magnetic field in the sample position. These will be read in the same way as the existing magnetic sensors on those beamlines, which is via a NI DAQ 9215 card with a simple calibration to translate the Voltage output from the fluxgate into a field reading in each of three directions: X, Y, and Z.

The PSU for the system is a [model PSU 1](https://www.bartington.com/psu1/) from Bartington.
   * an Operator's manual is here: `\\isis\shares\Manuals\Bartington\PSU1_OM2443.pdf`

The Probe has the identifier MAG-13MC70 (see [MAG-13 series](https://www.bartington.com/mag-13/))
   * an Operator's manual is here: `\\isis\shares\Manuals\Bartington\Mag-13_OM3143.pdf`

Digital manuals have yet to be located.

We are able to borrow the hardware to verify the Voltage to Gauss/Tesla relationship and to test the IOC functionality.

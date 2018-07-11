Details for the B&W Tek i-Raman Plus spectrometer which is to be used on [HRPD](https://github.com/ISISComputingGroup/IBEX/wiki/HRPD-Instrument-Details).

These notes relate to issue [#3302](https://github.com/ISISComputingGroup/IBEX/issues/3302)

### Minute for meeting on 2018-07-10

* Silvia Capelli, who works on SXD, attended the meeting with an interest in using the spectrometer on SXD (SXD is currently on SECI).
* Rory Potter has been given a USB stick with the manual and SDK for the spectrometer.
* The functions that will be required are:
    * Power of the laser: 0 - 100%
    * Length of count (in ms)
	* Number of counts
	* Choice of what pieces of data to plot (< 10 choices for each coordinate)
* The data outputted by the spectrometer is a small CSV file with a few hundred rows and less than 10 columns which contains points from a 2d plot.
* The scientists would like the CSV file created by the spectrometer to contain timestamps to allow them to match up the spectrometer data with the neutron data.
* Currently they can run the spectrometer using the B&W software on a laptop.
* The spectrometer connects via USB to a device running it.
* Ideally, the scientists would like the spectrometer to be run from IBEX.
* The spectrometer contains a class 3B LAZER. Because of this, the device is on a trolley with the laptop used to run it in an interlock.
* Dominic has agreed for us to interact with the spectrometer on Friday afternoon (2018-07-14).
* Dominic is off on holiday from next week until the end of the month so we won't be able to interact with the spectrometer during that time.
* The device is not needed until next year on HRPD or SXD.
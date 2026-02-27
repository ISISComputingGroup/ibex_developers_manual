# RAMAN Spectrometer

Details for the B&W Tek i-Raman Plus spectrometer which is to be used on [HRPD](https://github.com/ISISComputingGroup/IBEX/wiki/HRPD-Instrument-Details).

The  B&W Tek i-Raman Plus spectrometer in HRPD is a model BWS465-532S. Dom claims that the spectrometer is USB2.0. The model page suggests that it is USB3.0/2.0 compatible.

These notes relate to issue [#3302](https://github.com/ISISComputingGroup/IBEX/issues/3302).

The SDK can be found on the private ISIS share.

### USB interface

Talked with Chris about how to interface with the device. He suggests we start with a USB-to-anywhere adapter box to see if we can talk to it over Ethernet using the control software, BWSpec. We will go down in a couple of weeks when Dom is back to test interfacing with the device. 

If this does not work, we will have to have a separate machine running the IOC for the device. However, we may want to run the IOC on a separate machine if we want the spectrometer to be portable. On the other hand, the spectrometer is used in HRPD off the beamline so it may be their property.

### Minute for meeting on 2018-07-13 in HRPD
Present: Rory Potter, David Keymer, Dominic Fortes, Alexandra Gibbs.

* Found out the model code and USB type of the device (documented above).
* Dom showed us how he takes a reading using the proprietary software, BWSpec. The steps he would go through are as follows:
    1. He first sets the length of time he wants the integration to be done.
    1. He first takes a single "dark" spectra reading. 
    1. He then sets the laser power and the number of integrations to be done.
    1. He then tells the spectrometer to "acquire" which takes in the readings.
* Using BWSpec, you can take multiple integrations. Dom suggested that the software does something clever with these multiple integrations. The manual suggests that the software just overlays the data points collected from each reading. Clarifying what happens from a data collection point of view and how many integrations get written to the output file will be needed.
* The reason Dom want to integrate with IBEX is so that he can take readings using the spectrometer using a script in between times when the beam is active.
* Dom is happy with just some buttons to tell the spectrometer to scan. In the future, he would like to see a 2d scatter graph, like in the BWSpec software, while readings are being taken.
* I communicated our concern about the USB connection with him and explained that we can try to use a USB to ethernet adapter. Kathryn and Freddie have suggested that we could run a separate PC connected to the device which runs the IOC - like with the Tritons. I will talk to Chris about the options we have communicating with the device.
* The device number is not mentioned in the SDK list of devices supported. This may cause problems.
* The device being USB should allow us to use the USB3.0 specific functions in the SDK.
* Dom will send over a copy of the CSV file he wants the data to be written to for analysing using the proprietary software BWIQ.

### Minute for meeting on 2018-07-10
Present: Rory Potter, David Keymer, John Holt, Dominic Fortes, Silvia Capelli.

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
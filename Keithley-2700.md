The Keithley 2700 is a multimeter. There is no "general-purpose" IOC for this device, but there is an IOC in development for use with the 2700 on the HIFI CRYOMAG.

It can be used to measure many things including voltage and current (AC and DC) and resistance. On HIFI it measures the temperature at different locations on the cryomagnets. This is achieved by measuring resistances (using FRES measurement), then comparing these readings with a calibration file and interpolating a temperature value from this. It also calculates the temperature drift between measurements, in part to check the stability of the magnet. 

The component in use on HIFI measures 20 channels, 101-110 and 201-210, and each of these channels can use a separate calibration file for interpolating the temperatures.

### Setting up the Device 

> **NOTE** The IOC does work with a MOXA, but the legacy VI does _not_. If you intend to run it with a VI, it bust be done via a USB to RS232 adapter straight into your machine.

Plug the device into the mains, and into a MOXA via its RS-232 port on the back. 

Pressing the power button (lower left on the front panel) should make it turn on and beep. 

Make sure that it is set up to use RS-232 - press (don't hold) the shift key and press the enter key on the front panel. Make sure RS-232 is set to ON. 

Make sure that the Keithley is using its rear measurement inputs. `REAR` should be displayed on the right edge of the display. If not, press the button on the right edge of the front panel, labelled _Front/Rear Inputs_. 

Test that you can now talk to it by connecting to it via PuTTY or something similar, and sending it `*IDN?` and make sure you get the device name back.

### The Buffer

> This section has been included because a lack of clear understanding of buffer operation has caused many issues during development

The device features an on-board buffer which can be used to store measurements. It can store between 2 and 55,000 measurements, each of these can contain several bits of information including the actual measurement, the timestamp of the measurement, the channel it was taken from, and a few other parameters which can be found in the manual. 

Setting the buffer size can be done using SCPI command `TRAC:POIN <int>` where int is an integer between 2 and 55,000. Note that the buffer is zero-indexed, so sending `TRAC:POIN 10` sets up a buffer with index locations 0-9. 

Use the SCPI command `TRAC:DATA:SEL? <intX>,<intY>` where `intX` is the starting index in the buffer that you wish to read from, and `intY` is the number of readings you wish to return. e.g. `TRAC:DATA:SEL? 10,5` will return the stored readings at index locations 10,11,12,13,14. If there are no readings stored in any of those locations, the Keithley will produce error code -222, which is essentially an array out of bounds error. You also cannot set `intY` to 0, this will produce the same error. NOTE that the <> brackets are not needed in the command.

This is how the protocol file works, and you can also send these commands via a remote connection client like PuTTY. See the Keithley 2700 manual for a full list of supported SCPI commands. 

#### Buffer Reading Logic

In the `COUNT:CALC` record in `keithley2700.db` there is a long logic statement designed to catch all cases when attempting to read from the buffer. The statement is: 

`(A>=B)?(A-B):((A=0)?(C-B):A)`

Where: 
* A = the next *free* buffer location.
* B = the buffer index to begin reading from.
* C = the size (length) of the buffer.

It calculates the number of readings to retrieve from the buffer. 

The typical case is when `A>=B`. In this case, the we want to retrieve from the starting index in the buffer up to the next free location (not inclusive). i.e. we start at index 0, the next *free* location is 2, so we retrieve 2-0 = 2 readings from the buffer, starting from index 0. 

When 'A<B' it means that either the buffer is full but there are still unretrieved readings, where A reports 0 (since that is the next location it would write to after clearing the buffer), or that the buffer has cleared and begun storing a new set of readings.

In the first case, we retrieve a count of `C-B` readings, which will give the number from the starting index position (B) to the end of the buffer. e.g. if the buffer length (C) is 10, and the starting index (B) is 8, we get 10-8 = 2 buffer readings to retrieve (at indices 8 and 9, since the buffer is 0-indexed). 
In the second case, we have failed to retrieve the readings at the end of the buffer. This is because when the device begins writing a new set of readings it first clears the full buffer. In this case, we can only read the new set of readings, the count of which is A, starting from index 0.



### Drift

The calculation used to calculate the drift uses information from the previous scan (including the previously calculated drift) and the information from the new scan. 

> NOTE: the code contains a logic statement `if ((!isnan(temp_change_over_time)) && (isnan(previous_drift)))` which states that if the temp change over time exists (∆temp/∆time) and the previous drift does NOT exist (i.e. this is the first reading) then the new drift is just (∆temp/∆time) multiplied with the time constant. Otherwise, it is also summed with the previous drift factor

![drift-calculation]

Where 

![delta-temp]

![delta-time]

![d-n]

![d-p]


[//]: # (URLs for latex images)

[drift-calculation]: http://mathurl.com/y77q3ex2.png

[d-n]: http://mathurl.com/ydykpgb5.png

[d-p]: http://mathurl.com/ycpzu8wu.png

[delta-temp]: http://mathurl.com/ybcns6ud.png

[delta-time]: http://mathurl.com/y8lccdz7.png

### Interpolation

The Keithley utilises the [convert record](Convert-Record) to interpolate a temperature from a resistance reading. It uses a Spline fit to do this, implemented in `User1DTableSub.c` in the support directory. 

The setup part of this function includes an in-place swap of the data points in the y axis. This is because `csmbase` automatically sorts both axis of data points into ascending order, but maintains the links between an x data point and a y data point for use in the convert record's built in interpolation functions. 

After reading the calibration table, `csm` calls `coordinate_sort()` and `coordinate_update_backlinks()` on the x and y arrays. This calls `qsort` and puts them in ascending order (of value). `csm` relies on the index (stored in a struct with the actual data point) to determine which element in one array corresponds to the correct element in the other array, meaning that an array can be reordered without any problems arising because of this. 

Because the user defined `User1DTableSub` does not utilise the `csm` back end (and therefore the data point links) the original order of the y axis must be preserved, so it is swapped back again in the in-place swap. 

For a more thorough explanation, see `coordinate_sort()` and `coordinate_update_backlinks()` and the doc comments in `csmbase.c` (found in `C:\Instrument\Apps\EPICS\support\csm\master\csmApp`)

### Unit Tests

The device utilises [googletest](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Setting-up-googleTest-to-work-with-EPICS-build-process) to test the drift functionality. It does this using real-world recorded values from a previous run. The tests can be found in the support directory for the keithley, in `Keithley_2700Sup\tests` and can be run using `make test` from the top level support directory, or using `run_tests.bat` for slightly more colourful output.
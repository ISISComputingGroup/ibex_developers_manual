The Keithley 2700 is a multimeter. There is no "general-purpose" IOC for this device, but there is an IOC in development for use with the 2700 on the HIFI CRYOMAG.

It can be used to measure many things including voltage and current (AC and DC) and resistance. On HIFI it measures the temperature at different locations on the cryomagnets. This is achieved by measuring resistances (using FRES measurement), then comparing these readings with a calibration file and interpolating a temperature value from this. It also calculates the temperature drift between measurements, in part to check the stability of the magnet. 

The component in use on HIFI measures 20 channels, 101-110 and 201-210, and each of these channels can use a separate calibration file for interpolating the temperatures.

### Setting up the Device 

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

### Drift

The calculation used to calculate the drift uses information from the previous scan (including the previously calculated drift) and the information from the new scan. 

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
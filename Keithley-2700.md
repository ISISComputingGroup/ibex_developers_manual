The Keithley 2700 is a multimeter. There is no "general-purpose" IOC for this device, but there is an IOC in development for use with the 2700 on the HIFI CRYOMAG.

It is used on HIFI to measure the temperature at different points on the cryomagnets. This is achieved by measuring resistances, then comparing these readings with a calibration file and interpolating a temperature value from this. It also calculates the temperature drift between measurements, in part to check the stability of the magnet. 

The component in use on HIFI measures 20 channels, 101-110 and 201-210, and each of these channels can use a separate calibration file for interpolating the temperatures.

### Setting up the Device 

Plug the device into the mains, and into a MOXA via its RS-232 port on the back. 

Pressing the power button (lower left on the front panel) should make it turn on and beep. 

Make sure that it is set up to use RS-232 - press (don't hold) the shift key and press the enter key on the front panel. Make sure RS-232 is set to ON. 

Make sure that the Keithley is using its rear measurement inputs. `REAR` should be displayed on the right edge of the display. If not, press the button on the right edge of the front panel, labelled _Front/Rear Inputs_. 

Test that you can now talk to it by connecting to it via PuTTY or something similar, and sending it `*IDN?` and make sure you get the device name back.

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
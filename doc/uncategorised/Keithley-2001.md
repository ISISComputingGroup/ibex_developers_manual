The Keithley 2001 is a digital multimeter.

## Configuring the IOC

*  To configure the IOC, the user needs to set `ACTIVATE_CHAN_%d` macros to `1` in the client or `globals.txt`. In the macro, `%d` is a two-digit, zero-padded number between 1 and 10, e.g. `01`, `05` or `10`.

* If one channel is activated, then the device reads the value using a single-shot protocol. If more than one channel is active, it scans through all of these channels quickly intern with a delay. The delay between scans is specified by the `SCAN_DELAY` macro in seconds.

## Limitations of the IOC

* The IRIS OPI and IOC macros are configured to allow the user only to activate channels 1,2,3,4,6,7,8,9.

* The IOC is configured to only read DC voltage using the `VOLT:DC` measurement functions. This is the default behaviour of the device after the reset command, `*RST`, has been sent.

* The OPI is designed to allow to view readings, view error messages and code, and reset the IOC in case the IOC gets into an error state.

## Troubleshooting

* If there are any problems, try clicking the "Reset IOC" button on the OPI.

* If the device is not scanning on any channels, check that the IOC macros have been set in either the client or in `globals.txt`.
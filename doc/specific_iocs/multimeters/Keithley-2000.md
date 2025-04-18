# Keithley 2000

Note: this page refers to *generic* keithley 2000 multimeter support. For scanning calorimetry experiments (IRIS) see [keithley 2001](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Keithley-2001). For HIFI cryomagnet (2700, but uses a comparable protocol) see [keithley 2700](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Keithley-2700).

The keithley 2000 is a general-purpose multimeter which is portable and can be used on many beamlines. It is a pure multimeter, not a source meter (c.f. 2400 series, which are also capable of sourcing currents).

We have generic support for reading the following variables from a keithley 2000:
- AC Voltage or Current
- DC Voltage or Current
- Resistance (2 wire or 4 wire)

Note that only one of these variables can only be read at a time. The keithley 2000 can be made to "scan" it's input channels for specific applications (for example, see IRIS calorimetry / KHLY2001 IOC), but that is considered out of scope for the generic device support.

## Communication

- Device takes a male 9-way serial connection with no null modem.
- Device has configurable terminators on the device and in the IOC (via `IEOS`/`OEOS` macros). The terminator can be any of `\r`, `\n`, `\r\n` or `\n\r`. When entering these as macros, the slashes must be doubled, e.g. `\\r\\n`.
- Device can be very slow to respond and get streamdevice timeouts just after changing measurement modes. This is due to internal relays in the keithley switching over and taking time to acquire a new measurement.


## Troubleshooting

### Error `-231` and beeping when trying to read the keithley

Try sending `:INIT:CONT OFF` to the keithley via hterm/hyperterm, then reconnect the IOC.
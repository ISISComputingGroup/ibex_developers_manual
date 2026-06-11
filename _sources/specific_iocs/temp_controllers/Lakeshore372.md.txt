# Lakeshore 372

The Lakeshore 372 is a temperature controller used to control the temperature on dilution fridges - mostly triton fridges. At ISIS, these are only in use on the muon beamlines, as they operate the fridges with a "weak thermal link" which means that the sample would otherwise take a long time to warm up again. The Lakeshore 372 provides a small heater which sits on the sample, and all of the temperature control is done via this heater.

### Connection details

The Lakeshore 372 is an ethernet device. By default it communicates on port 7777. All messages are terminated with `\r\n`. To connect to the device make sure it is in DHCP mode.

### PID settings

The Lakeshore 372 only accepts integers for the I (integral) & D (derivative) PID parameters. Floating-point numbers are only acceptable for the P (Proportional) parameter.
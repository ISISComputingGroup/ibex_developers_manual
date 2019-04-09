# Lakeshore 340

The lakeshore 340 is a device used by LET to monitor the temperature of a sample when it is being cooled by a dilution fridge inside the 9T magnet.

This lakeshore has four measurement channels, each of which exposes a temperature and a raw measurement (usually a resistance from a thermocouple). The device supports multiple independent temperature control loops, however we only use one of these loops.

The device itself has a large amount of functionality, however the IOC (and corresponding labview driver) only expose a fraction of it. The functionality exposed by the drivers is:
- Set and read back a temperature setpoint (it only ever sets and reads back the setpoint for control loop 1).
- Reads 4 temperature channels
- Reads the "raw" (resistance) measurements from these same 4 channels
- Set and read P, I and D values
- Set and read the PID mode (one of `Manual PID`, `Zone`, `Open Loop`, `Auto-tune PID`, `Auto-tune PI` or `Auto-tune P`)
- Set and read whether the control loop is on
- Set and read the maximum temperature setpoint
- Reads the heater output as a percentage
- Set and read maximum heater power as a percentage
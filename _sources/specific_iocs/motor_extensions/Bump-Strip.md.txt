# Bump Strips

Some instruments use bump strips as a safety feature. These are sensors placed on the physical beamline, which "trip" when touched, killing all motion immediately. They can plug into digital input ports on the Galil which then reads `0` for TRIPPED and `1` for NOT TRIPPED. Which port this is is specific to the instrument and you may have to talk to the scientists to find out.

At the moment, we do not handle the safety aspect of it in software (i.e. disable setting positions on axes), we just provide indicators in the GUI.

### Setup

The GUI gets the status from the PV `MOT:BUMP_STOP` which is always loaded by IOC `GALIL_01`. At the moment, we only have one PV for the overall bump strip status of the instrument, i.e. we do not support a signal per controller. 

If no input source is configured, this PV will default to "UNAVAILABLE". The input source can be set via macro by creating a file `<INST>\configurations\galil\bumpStop.cmd`.

This should contain a single line followed by a blank line e.g.
```
epicsEnvSet "BUMPSTOP_IN" "MOT:DMC03:Galil0Bi4_STATUS"

```
In this case this expects the signal to come from digital input port 4 (*Bi04*) on Galil controller 3 (*DMC03*) 
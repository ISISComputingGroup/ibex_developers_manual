# Setup

![](https://github.com/ISISComputingGroup/ibex_developers_manual/blob/master/images/riken_changeover.PNG?raw=true)

# Macros

The PSUs are set up in daisy chains. Macros are prefixed with (for example) `CHAIN1_`. Each chain of PSUs is talking on a completely independent COM port.

Additionally, the IOC talks to DAQ MX to do some changeover logic, which is implemented in SNL inside the IOC.

To run this IOC you will need to install the DAQMX binaries - available on the national instruments website (it is a rather large installer so it is not installed by default).

# Debugging

### Whole chain of PSUs won't talk
- Double check that the moxa port is set to RS-422 mode. **This setting needs to be done in the moxa itself (via the webpage) - IBEX can't do it!**
# Setup

![](https://github.com/ISISComputingGroup/ibex_developers_manual/blob/master/images/riken_changeover.PNG?raw=true)

# Macros

The PSUs are set up in daisy chains. Macros are prefixed with (for example) `CHAIN1_`. Each chain of PSUs is talking on a completely independent COM port.

Additionally, the IOC talks to DAQ MX to do some changeover logic, which is implemented in SNL inside the IOC.

To run this IOC you will need to install the DAQMX binaries - available on the national instruments website (it is a rather large installer so it is not installed by default).

# Hardware notes / Changeover sequences

### RB2 mode change

- RB2 is a power supply that can be put into three distinct modes: BEND1 (beam goes one way), BEAM2 (the other way), and SEPTUM (beam splits both ways). RB2, although one physical supply, has two control boards. The first control board (called "RB2" in our system) supplies current for either BEND1, BEND2, or half of SEPTUM mode. The second control board ("RB2-2" in our system) is *only* used in SEPTUM mode and supplies the other half of the current.
  * We check that BOTH RB2 and RB2-2 are powered off before allowing an RB2 mode change to take place.

### Port 3/4 changeover

- The port 3/4 changeover sequence is similar in that certain power supplies must be OFF before the 

# Debugging

### Whole chain of PSUs won't talk
- Double check that the moxa port is set to RS-422 mode. **This setting needs to be done in the moxa itself (via the webpage) - IBEX can't do it!**

### Changeover sequence won't start - PLC indicates "waiting for IBEX to respond".

IBEX will only let the changeover sequence proceed if it gets "off" readings WITHOUT ALARMS from the power supplies it cares about. For RB2 mode change these are "RB2" and "RB2-2", for port 3/4 change these are RQ18, RQ19 and RQ20.

### Changeover sequence won't finish

RB2 mode change:
- Sometimes RB2 does not properly acknowledge the request to change from the PLC. The PLC will then sit there in it's changeover state waiting for the PSU to be in the correct state. To fix this, need to go down in person to RB2 and press the button on the front panel to put it into the mode the PLC expects (it will then detect this and the changeover will finish)

Port changeover:
- The port changeover depends on three rotary switches which are located in the corner between ports 3 and 4 (near some HV power supplies). These switches can, and often do, get out of sync with each other. To fix this state, the misbehaving switch has to be manually forced back into place. The switches are interlocked and you will need a permit to access them. Contact Tim Carter in the first instance.
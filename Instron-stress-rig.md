Note: this page relates to an older-style GPIB-connected stress rig, which we talk to via a GPIB converter box. For documentation about the ethernet-connected rig (i.e. the 100kN rig on ENGIN-X) see https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Instron-stress-rig---MiniTower

# Setup

The Instron stress rig is a National Instruments GPIB device. It requires some special setup to get going:

- The Ethernet GPIB box requires an NI `488.2` (GPIB) driver. This can be installed from `\\isis\installs\Installs\Applications\LabVIEW\GPIB-ENET bits\GPIB Software`.
  - Note, **the version of GPIB MUST be 2.7 (from the share above), later versions WILL NOT WORK WITH THE STRESS RIG!** This is due to some kind of licensing handshake in newer versions of NI `488.2` (GPIB) of which older hardware (such as the stress rig) does not understand.
- Run the installer as an administrator, accept the defaults. It will unzip, then install. It takes a while to install.
- You then need to map the ENET box. Usually this means going into NI-MAX and finding devices - it should come up (otherwise, you may have to find and enter it's IP address manually).
- The driver should now be able to communicate (if not, see troubleshooting section below)

# Getting the rigs set up

There are two rigs: 50kN and 100kN.

To turn on the actuator for the 100kN rig, there are three buttons on the front labelled "O", "I", "II". Press these in order to enable the actuator.

To turn on the actuator for the 50kN rig, Press and hold the "Hydraulics on" button for at least 10 seconds. You should hear the hydraulic system engage (also, the hydraulic lines will change position slightly as pressurised gas enters the system). Then press actuator "off", "low", "high" (in order) to enable the actuator.

# Hardware debugging

### Hydraulics keep tripping off and status is "oil too hot"

Check if the cooling water circuit for TS1 south side is turned on. If not, the instron's oil might heat up too much which causes the hydraulics to trip when moving the rig. This happens regardless of whether IOC, LabVIEW, or manual control is used to move the actuator. Additional symptoms are a rig status of "HYD. PUMP SHUTDOWN" and the red status light on the control panel being solidly on (and not being able to clear it).

If the cooling water is off, there is a circulation pump that can be used to run the rig in low-force mode: ask the scientists.

### General comms failures / stress rig in invalid state

This can be triggered by sending commands the stress rig doesn't like, or sending valid commands too quickly. Sometimes the control panel of the stress rig will claim it is simultaneously in two control modes (which is impossible).

The stress rig can be power cycled using the process below (note: if unsure, check with scientists first, as it may need recalibrating after this process)
- Turn off the stress rig PC (white/beige pc located under the stress rig)
- Turn off the GPIB box (this looks similar to a router, located under the stress rig near to the stress rig PC)
- Wait a few seconds
- Turn on the stress rig PC
- Wait several minutes. The stress rig will go through a self-test phase. You need to wait for this process to be complete.
- If you need to calibrate the rig, the following sequence on the console should be used: "Load channel: setup" -> "cal" -> "cal" -> "auto" -> "go" (if you are unsure about this ask the scientists)
- Turn back on the GPIB box. 
- After the GPIB box has been turned on for a short time (e.g. 1 minute) the driver (LabVIEW or IOC) should be ready to connect.
- GPIB box LEDs - PWR should be orange, LNK 10/100 should be green. Other LEDs will be flickering depending on connection. Box might have a slightly dodgy connection (not sure about this, but check it) so ensure the LEDs are as described.

### Weird comms issues

The stress rig on ENGIN-X is mapped from both ENGINX and ENGINX_SETUP. **Only one of these computers should talk to the stress rig at a time!** If you get strange comms issues, check that the "other" computer is not also trying to talk at the same time.

### Hydraulics won't re-enable after panic stop

A panic stop sends the `C23,0` command to the stress rig. To quote from the instron manual:

> If this command is sent with the Off parameter, actuator manifold pressure is turned Off immediately, and the Actuator On button is disabled.

To re-enable the actuator (hydraulics control), first check that the cause of the panic stop is no longer an issue. Then you may need to send the command `C23,1` to the stress rig via the arbitrary command interface on the stress rig OPI once the rig is back in a safe state. 

If the above command fails, restarting the hardware and then the IOC should boot the stress rig back up with the actuator enabled.

# Driver

The stress rig driver uses the following DB files:
- `controls.db` - provides basic PVs such as stopping the rig, getting the status, changing control channels, etc
- `controls_channel.db` - provides PVs that are common to each channel (Position, Stress, Strain), e.g. setpoints, readbacks, step times
- `controls_channel_specific.db` - add on PVs for the above - used to add PVs for some channels that don't exist on others
- `controls_waveform.db` - provides the PVs dealing with the waveform generator
- `logging.db` - provides the PVs to do with logging to a file

The protocol is defined in [`C:\Instrument\Apps\EPICS\support\instron\master\instronSup`](https://github.com/ISISComputingGroup/EPICS-instron/blob/master/instronSup/devinstron.proto)

# Gotchas / Unusual things
- Every "write" command (commands starting with C or P) must be preceded by `P909,1` (switch to computer control mode) and `C904,0` (disable watchdog). For convenience there is the `setControlModeCom` function in the protocol file which does these for you.
  * If you forget to do this, the rig's hydraulics will trip, requiring a physical button push to reset them
- Every "write" command (commands starting with C or P) must be followed by `P909,0` (switch to front panel control mode)
- We have had issues with PVs dropping off to zero while being read from the stress rig. To solve this, use a `:RAW` record which does a read, and monitor it using `CP` from another record. This fixes the issue of getting zeroes.
  * Might be a bug in EPICS and/or the interface between the VISA driver and EPICS. At the moment the above solution seems to be the easiest way to cure the symptoms.
- PVs in the stress rig don't scan by themselves typically, they are triggered from one of two read loops:
  * `READ_SLOW` scans at 1 Second interval
  * `READ_VAR` reads at a rate that can be varied by the user
  * In the `READ_VAR` loop the `.1 Second` option has been removed, this is too fast for the rig to handle
- If something works in LabVIEW but not in EPICS, or vice-versa, NI Input/Output trace (NI Spy) can be very useful to compare the traffic and spot any differences.
- The waveform generator does not like receiving setpoints in quick succession. This can cause a fault with the following symptoms (see also https://github.com/ISISComputingGroup/IBEX/issues/2802):
  * The "remote" light on the hardware control panels remains lit
  * The hardware control panel crashes (it may display that it's in two control channels simultaneously - this is usually impossible)
  * The hydraulics will trip.
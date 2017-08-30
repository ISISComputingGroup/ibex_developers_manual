# Setup

The Instron stress rig is a National Instruments GPIB device. It requires some special setup to get going:

- The Ethernet GPIB box requires a driver for the LabVIEW driver. This can be installed from `\olympic\Babylon5\Public\GHowells\NI GPIB`
- Run the installer as an administrator, accept the defaults. It will unzip, then install. It takes a while to install.
- You then need to set up the ENET box, Gareth or Freddie can show you how to set this up
- LabVIEW vi located at : `C:\LabVIEW Modules\Instruments\ENGINX\Stress Rig\Stress Rig - System Functions.llb\Stress Rig - 100 kN Stress Rig.vi`
- On running the vi, you will get some dialogs – just ok through them. The indicators should then be updating.
- If you can't get the labview to talk at all, the stress rig might need to be power cycled. @GDH-ISIS and @FreddieAkeroyd know how to do this. The basic instructions are below:
  * Turn off the stress rig PC (white/beige pc located under the stress rig)
  * Turn off the GPIB box (this looks similar to a router, located under the stress rig near to the stress rig PC)
  * Wait a few seconds
  * Turn on the stress rig PC
  * Wait several minutes. The stress rig will go through a self-test phase. You need to wait for this process to be complete.
  * If you need to calibrate the rig, the following sequence on the console should be used: "Load channel: setup" -> "cal" -> "cal" -> "auto" -> "go" (if you are unsure about this ask the scientists)
  * Turn back on the GPIB box. 
  * After the GPIB box has been turned on for a short time (e.g. 1 minute) the driver (LabVIEW or IOC) should be ready to connect.

# Driver

The stress rig driver uses the following DB files:
- `controls.db` - provides basic PVs such as stopping the rig, getting the status, changing control channels, etc
- `controls_channel.db` - provides PVs that are common to each channel (Position, Stress, Strain), e.g. setpoints, readbacks, step times
- `controls_channel_specific.db` - add on PVs for the above - used to add PVs for some channels that don't exist on others
- `controls_waveform.db` - provides the PVs dealing with the waveform generator
- `logging.db` - provides the PVs to do with logging to a file

The protocol is defined in `C:\Instrument\Apps\EPICS\support\instron\master\instronSup`

# Gotchas
- Every "write" command (commands starting with C or P) must be preceded by `P909,1` (switch to computer control mode) and `C904,0` (disable watchdog). For convenience there is the `setControlModeCom` function in the protocol file which does these for you.
- Every "write" command (commands starting with C or P) must be followed by `P909,0` (switch to front panel control mode)
- We have had issues with PVs dropping off to zero while being read from the stress rig. To solve this, use a `:RAW` record which does a read, and monitor it using `CP` from another record. This fixes the issue of getting zeroes.
- PVs in the stress rig don't scan by themselves typically, they are triggered from one of two read loops:
  * `READ_SLOW` scans at 1 Second interval
  * `READ_VAR` reads at a rate that can be varied by the user
- If something works in LabVIEW but not in EPICS, or vice-versa, NI Input/Output trace (NI Spy) can be very useful to compare the traffic and spot any differences.
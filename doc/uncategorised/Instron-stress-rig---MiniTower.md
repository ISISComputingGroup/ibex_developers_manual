Note: this page relates to a newer-style ethernet-connected stress rig, which we talk to via a manufacturer DLL. For documentation about the GPIB-connected rig (i.e. the 50kN rig on ENGIN-X) see https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Instron-stress-rig


# Physical setup

The stress rig has several components:
- The physical rig hardware, in which the sample sits.
- A controller, which plugs directly into the physical rig hardware, and has an ethernet port on the back
- The ethernet port on the controller is plugged into the control PC via a **direct** ethernet connection. This connection should **not** be going via a switch or the ISIS network in any way.
  * Note, this "control PC" is **NOT** the `NDX` machine or equivalent, it is a separate machine. Currently a small-form-factor PC named `enginx-stress-1`
  * The network between the stress rig controller and `enginx-stress-1` is a point-to-point private network. The relevant network adapter on `enginx-stress-1` should be set to an IP address of `10.0.0.1` with netmask `255.0.0.0`. The stress rig controller is on `10.0.0.2` and should respond to `ping` if it is working.
- The control PC has a physically separate RJ45 port (currently a USB-to-ethernet converter) used to connect to the ISIS network.
- There is an "MMI" controller which plugs into the control PC via USB - and also simultaneously into the instron controller via a separate cable.

The manufacturer software ("Console") **MUST** be running on the control PC for the rig to work. Some functions (calibrations, setup, advanced diagnostics) are only available via the "console" software.

# IOC

We will run an IOC on the control PC, which can be viewed and eventually controlled from the NDX.

Due to needing to link against the 32-bit manufacturer DLL (`Arby.dll`) for communication, we need to deploy a 32-bit EPICS build to the control PC. Ticket https://github.com/ISISComputingGroup/IBEX/issues/7326 will define our approach to this computer in more detail.

The manufacturer software ("Console") must be running in the background while the IOC is attempting to talk - otherwise the rig will not work.

# Troubleshooting

### Cannot connect via remote desktop to `enginx-stress-1`

- Check the machine is powered on - it travels with the stress rig and may not necessarily always be plugged in!
- Check the machine is connected to the ISIS network via it's motherboard port, and to the stress rig via the USB-ethernet adapter.
- Connect a monitor to find out the machine's IP address - it is sometimes slow to update in the nameserver, but can be accessed via remote desktop if you know the IP directly.
- For username/password details for this machine, see keeper.

### ArbySPY

The instron software contains a module called "ArbySPY" which can be used to trace all commands being sent to the rig, no matter their source. As such it is possible to find out what Console is doing to make sure that IBEX can replicate these same commands.

### Command rejected - frame in control

Solution: You need to press the physical button on the front of the stress rig to restore computer control. This cannot be done automatically as it trips the hydraulics intermittently when attempted

### Cannot change channel - "function inhibited - channel not calibrated"

Solution: Ask scientists to load a calibration for the relevant channel using the Console application.

### Setpoints are relative rather than absolute

Verify that the `C1,1` command is **NOT** being used - this is buggy in the Arby interface. Need to use the following sequence instead (this is already done by the protocol file - but any arbitrary commands sent to the rig may also need to be adjusted):

```
C500,1;C38,1
C916,0
C914,4
C916,2
C372
```

### "TestLog" keeps popping up complaining about "next mode must be enabled to send this command" or similar

This happens when a move is started from IBEX. We are not sure why the rig believes C38 is invalid - but it **is** required in order to actually start the move.

Solution: ignore these spurious errors.

### "TestLog" complains about various things as the IOC is started

Solution: ignore these errors - they do not impact functionality.

### "TestLog" complains about a wide variety of problems (frame error, fan error, power state, non-corporate pack detected, Crosshead unclamped, Emergency stop pressed, AC power failure)

This happens if the rig controller is switched off. 

Solution: turn the rig controller back on (and wait ~2 mins for it to connect to console again)

### Cannot start the instron "Console" application

This has been seen on a previous stress rig control PC. We are unsure of the cause.

Consider how much time you want to spend on this issue - we can only provide very limited support for instron's console application, and complex support queries might be best to send to instron directly.

It is possible to re-install the software from `\\isis\shares\ISIS_Experiment_Controls\Manuals\Instron_Stress_Rig\MiniTower (Ethernet - Arby)\installer`
- This should only be attempted as a last resort and will take some time to set up, and will need instrument scientist involvement to recommission/recalibrate the rig once done.
- When it asks for a system ID, this is on a sticker on the rig itself, and also stored at `\\isis\shares\ISIS_Experiment_Controls\Manuals\Instron_Stress_Rig\MiniTower (Ethernet - Arby)\ENGIN-X Instron Control Tower System ID.jpg`
- You will need to restore calibrations from `\\isis\shares\ISIS_Experiment_Controls\Manuals\Instron_Stress_Rig\MiniTower (Ethernet - Arby)\ENGIN-X 100kN rig calibration files 2022-09-01` after reinstalling

### Hydraulics randomly trip

Cause is currently unknown.

### Communications sometimes randomly fail

Cause is currently unknown.
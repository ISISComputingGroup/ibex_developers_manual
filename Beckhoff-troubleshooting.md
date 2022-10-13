> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff) > [Beckhoff troubleshooting](Beckhoff-troubleshooting)

# Beckhoff troubleshooting

As we don't really handle any logic minus the motor record aliasing, there isn't much to go wrong (in theory) - sometimes for numerous reasons such as motion logic changing etc. the `.tpy` file that maps over memory addresses to human readable names can go out of date. 

**The first thing to do if an issue occurs is open a device screen which is pointing to the "Beckhoff engineering view" and check all axes for an error ID.**
**If the records in here are in link alarm, it's likely that there is a comms issue OR the TPY file is out of date - see below.**
**If not, and there are error IDs for any axis, the beckhoff has thrown an error. You may be able to hit "reset" and resolve this, if not contact the IESG or the IDD Motion team. **

### "TPY file needs updating"
If nothing whatsoever is working, moves aren't sending and enabling/disabling is not working, an outdated `.tpy` file could be the cause. 

To remedy this: 
1. Stop the `TC` IOC from IBEX.
1. Obtain a valid/up to date `.tpy` file, either sent from the motion team or from the controller (usually under `C:\TwinCAT\3.1\Boot\Plc\`, named `port_852.tpy`, you can remote desktop in using the PLC's IP address and use a file explorer to copy it from its Windows environment)
1. Place above `.tpy` file in `C:\Instrument\Settings\Config\NDX<instname>\configurations\twincat\` - it will need to be called whatever it was before or whatever it was in the config (it's passed in via a macro) - it's usually called `tc_project_app.tpy`
1. Start the `TC` IOC again from IBEX. This should re-generate the `.db` file in the above directory and you should now have working communication. The table of motors may take a while to update so to check if things are working it may be easiest to use the `Beckhoff Engineering` device screen. If this does not exist on an instrument, create it. 

### Safety systems
Safety systems such as light curtains or bump strips will throw the controller into error (and usually disable all axes) as opposed to just stopping movement like on a Galil. The green reset button on each beamline should clear the error and re-enable. 

### Motor not responding to set points, no errors in log, "controller error" message
In this case, navigating to the TwinCAT Beckhoff Controller OPI, selecting the troublesome axis, then pressing "load" then "reset" cleared the issue.

### `currentTime::getCurrentTime(): time discontinuity detected`
This is a weird error that seems to occur sometimes when running a Beckhoff simulator on a dev machine. To stop it you need to do run `unsettick.bat` script in `tcioc\master` and reboot. NB this should never happen on an instrument machine as they do not run simulated Beckhoffs. 

## Twincat Beckhoff Engineering View
#### Error: `19250`
To resolve, a physical restart was necessary - Contact Electrical and Electronic User Support Group to resolve
Once a physical restart has taken place, load each axis and reload to check the error status has returned back to 0. 

#### Error: `17510` or `19209`
Occur during physical restart, and may remaining if physical restart was unsuccessful.
Once a successful physical restart has taken place, they should go away. - Contact Electrical and Electronic User Support Group to resolve this

#### Error: `18000`
Axes may not move at all when under `18000` error. To resolve, reset using Beckhoff Engineering View and / or perform homing routine.

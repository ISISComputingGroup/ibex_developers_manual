# Beckhoff troubleshooting

As we don't really handle any logic minus the motor record aliasing, there isn't much to go wrong (in theory) 

**The first thing to do if an issue occurs is open a device screen which is pointing to the "Beckhoff engineering view" and check all axes for an error ID. note you have to press the load button to load an axis.**
- If the records in here are _all_ in alarm, it's likely that there is a comms issue. See "ADS route and pinging" below. 
- If not, and there are error IDs for any axis, the beckhoff has thrown an error. You may be able to hit "reset" and resolve this, if not contact the IESG or the IDD Motion team. 
- If the axis does not have the "enabled" light on, try and enable it. If this does not work there is probably some form of interlock stopping this from working, such as light curtains, bump strips etc. or the axis is in an error which prevents it from being enabled - see below.

## ADS route and pinging
an easy thing to check to see if a beckhoff is actually reachable is to
- ping `192.168.1.22x` (usually 221)
  * Note, not all beckhoffs reply to ping. You can RDP into them, so try this as well.
- from the NDX system tray right click the twincat icon, then routing -> edit routes. check there is an `x` or padlock symbol in the "connected" column. 

if neither of these work the cable has probably fallen out or the Beckhoff has gone down. 

## Twincat Beckhoff Engineering View

### Error: `xxxxx`
This is an issue reporting from the Beckhoff itself. you may be able to reset the error and get moving again. otherwise contact IESG to resolve. A list of error IDs are available from the [TwinCAT documentation](https://infosys.beckhoff.com/english.php?content=../content/1033/tcdiagnostics/513122571.html&id=3090135020933951410). 

### Safety systems
Safety systems such as light curtains or bump strips will throw the controller into error (and usually disable all axes) as opposed to just stopping movement like on a Galil. The green reset button on each beamline should clear the error and re-enable. 

## Virtual axes do not accept two setpoints in quick succession

See https://github.com/ISISComputingGroup/IBEX/issues/8339 for a detailed description of the issue.

The solution is to set `.DLY` to 0.25 in the motor record (which causes a 250ms "settle time" after motions).


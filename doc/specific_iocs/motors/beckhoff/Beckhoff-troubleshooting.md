# Beckhoff troubleshooting

As we don't really handle any logic minus the motor record aliasing, there isn't much to go wrong (in theory) 

**The first thing to do if an issue occurs is open a device screen which is pointing to the "Beckhoff engineering view" and check all axes for an error ID. note you have to press the load button to load an axis.**
- If the records in here are _all_ in alarm, it's likely that there is a comms issue. See "ADS route and pinging" below. 
- If not, and there are error IDs for any axis, the Beckhoff has thrown an error. You may be able to hit "reset" and resolve this, if not contact the IESG or the IDD Motion team. 
- If the axis does not have the "enabled" light on, try and enable it. If this does not work there is probably some form of interlock stopping this from working, such as light curtains, bump strips etc. or the axis is in an error which prevents it from being enabled - see below.

## ADS route and pinging
an easy thing to check to see if a Beckhoff is actually reachable is to
- ping `192.168.1.22x` (usually 221)
  * Note, not all Beckhoffs reply to ping. You can RDP into them, so try this as well.
- from the NDX system tray right click the TwinCAT icon, then routing -> edit routes. check there is an `x` or padlock symbol in the "connected" column. 

if neither of these work the cable has probably fallen out or the Beckhoff has gone down. 

## TwinCAT Beckhoff Engineering View

### Error: `xxxxx`
This is an issue reporting from the Beckhoff itself. you may be able to reset the error and get moving again. otherwise contact IESG to resolve. A list of error IDs are available from the [TwinCAT documentation](https://infosys.beckhoff.com/english.php?content=../content/1033/tcdiagnostics/513122571.html&id=3090135020933951410). 

### Safety systems
Safety systems such as light curtains or bump strips will throw the controller into error (and usually disable all axes) as opposed to just stopping movement like on a Galil. The green reset button on each beamline should clear the error and re-enable. 

## Virtual axes do not accept two setpoints in quick succession

See https://github.com/ISISComputingGroup/IBEX/issues/8339 for a detailed description of the issue.

The solution is to set `.DLY` to 0.25 in the motor record (which causes a 250ms "settle time" after motions).

## Instrument specific Beckhoff information

### SANDALS - Jaws and Sample Changer

SANDALS has a Beckhoff PLC which serves the Jaws permanently, and the Sample Changer when it is plugged in (over an ethercat network)

Some of these axes are relatively-encoded, so need to be homed/calibrated before use after a power cycle. At the moment we use the `.ATHM` field to indicate this, so if the home icon is not shown on the Table of Motors the axes have not been calibrated and will error when a move is attempted.

The Sample changer has some `pt100` sensors for temperature mounted on it, these are fed in through the Beckhoff as extra fields. These are loaded by [this `.db`](https://github.com/ISISComputingGroup/EPICS-motorExtensions/blob/master/sandalsSampleChangerApp/Db/sandals_sample_changer_beckhoff_extras.substitutions)

### INTER - Detector tank including Jaws 4

This is currently the most complex implementation of using a Beckhoff PLC as it handles kinematics between physical axes and flight paths, traditionally "worked out" by the Reflectometry server. It has some custom routines which can be accessed from the PLC HMI or through the `INTER Beckhoff Diagnostics` device screen in IBEX.

It also controls some Jaws on the front of the tank. 

### LARMOR - Detector Bench

This is a single axis. It lets IBEX know about an air PLC signal as it requires an air bearing to move. This is fed in by [this `.db`](https://github.com/ISISComputingGroup/EPICS-motorExtensions/blob/master/larmorBeckhoffExtrasApp/Db/larmor_beckhoff_extras.substitutions) and the bump strip signal is flipped and sent to the bump strip PV which is shown in the banner to indicate that motion has tripped.

### IMAT - Rotation and Height stage

This is currently just two axes, with no real quirks on our side. 

### SURF - Cloche motion and jaws 1&2

SURF's motion involves the tank, including the supermirror and frame-overlap mirror, as well as Jaws 1 and 2. This has had issues with encoder radiation in the past which has required a PLC power cycle, which in turn then requires a power restore. In order to get this properly working, [this ticket](https://github.com/ISISComputingGroup/IBEX/issues/8464) needs to be completed.


> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [Motors Trouble Shooting](Motors-Trouble-Shooting)

## General

### Position needs to be restored 

Positions of the motor can be restored/set without setting an offset. These can be needed if the motor power cycles for example on a power cut. The recommendation is to do a home if possible but if not the position can be set without this.

1. Find the latest value from the archive with:
    ```
    SELECT t.name, s.smpl_time, s.float_val FROM archive.sample s
    LEFT JOIN archive.channel t ON s.channel_id = t.channel_id
    WHERE t.name LIKE "%MOT:MTR0101%RBV%"
    AND s.smpl_time > "2017-11-16 00:00:00"
    ORDER BY s.channel_id, s.smpl_time DESC;
    ```
1. Open the motor details opi for given motor
1. Click on `Set` in `Calibration` area
1. Set the `User` `MoveAbs` to the value from the query above
1. Click on `Use` in `Calibration` area

## Galil

### Can not communicate with the Galil

This is not shown well in the OPI it just has weird values. Look in the log file to check near `GalilCreateController` it says `sevr=info Connected to XXX t 1000 -mg 0, DMC2280 Rev 1.0o-CM, 46949, IHB IHD` not `sevr=major connect: 5004 OPEN ERROR.  Galil::Galil() failed to open Ethernet host`

If it isn't connected try to ping the control address. If this isn't alive check, via the serial cable, the Galil address. The command for this is `IA?`.

### The Galil reports being at home when it is at a limit, not at the limit switch

Ensure the limit_as_home flag is correctly set, see [here](Galil#configure-galil-crate-1)

### The axis will not move, a message gets put in the log of "Begin not valid with motor off"

There is a Galil specific PV called `MTRXXXX_AUTOONOFF_CMD` which controls whether an axis automatically powers up when given a move. The default setting is Off, it should be set to On.

### The axis will not move away from a limit, a message gets put in the log of "move failed, `wlp` active" or "Wrong limit protect stop motor"

There is a Galil specific PV called `MTRXXXX_WLP_CMD` which controls whether an axis treats both limits as high and low. The default setting is On, it should be set to Off.

### Something is Weird I want Maximum Debugging

Maximum debugging can be achieved by adding to your st.cmd:

    epicsEnvSet("GALIL_DEBUG_FILE", "galil_debug.txt")

This will generate a file containing all the commands sent and received from the Galil.

### No communication with Galil even on restart of IOC

If in doubt it is best to plug a serial cable directly into the control box and see if you can see anything. When connected correctly it should give a colon, `:`, after pressing return.
If you get a `>` this means that it has got into an internal configuration mode which you can't get out of without rebooting the Galil. This has been seen when communicating with 4000 series through the ethernet cable.

### Galil position is not stable at setpoint

If a Galil is particularly worn, or carries an unusually heavy load, it may not stay where it is after going to a setpoint but sag down slightly. In those cases it might help to turn the "auto de-energise" setting on the Galil off (the PV is `MTRXXXX_AUTOONOFF_CMD`). This setting decides whether the Galil automatically powers off when stationary or not. Note that if this is turned off, the Galil will just stay in whichever state it was last (pv to check: `MTRXXXX_ON_STATUS`), so you may have to manually switch the power on the Galil back on again (pv to set: `MTRXXXX_ON_CMD`), otherwise it will not move.

**Do check with the instrument scientists before you change this.** If a motor is always powered when it is not meant to be, it may overheat.


### Differences between SECI and IBEX

Check out [this spreadsheet](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/galil%20gotchas.xlsx) for information on speeds, accelerations, homing, and random extra bits of code that might be needed before/after moves, on startup, when homing.

Check out [this page](Homing-Galils-under-SECI) if you need to see what the SECI homing routines do.
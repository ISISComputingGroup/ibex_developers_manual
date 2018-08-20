> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [McLennan](McLennan-motors)

The McLennan motor is a controller that support multiple independent motors.

### Velocity
The McLennan motor velocity is set with the *VELO***n** IOC macros. The value set is in `mm/second`. The motor resolution is set with the *MRES***n** IOC macros and as in units of `mm/step`. The velocity value set on the device will be the velocity divided by the motor resolution, and will be in units of `step/second`.

### Acceleration
Acceleration is far less intuitive than velocity. The acceleration value on the device is the acceleration in units of `step/s^2`. It is calculated as the IOC macro values of velocity divided by the product of the motor resolution and acceleration. The IOC macro acceleration is therefore the number of seconds under linear acceleration to reach maximum speed.

### Setting the motor offset
*Note that this applies equally to other motor types.*

Sometimes it is desirable to change the reported position of the motor without it physically moving, effectively changing the origin of the axis. This can be achieved through EPICS by applying an offset to the reported motor position. In order to apply a fixed offset:

1. Start the motor IOC
1. Go into the `Motors` perspective in the client
1. Bring up the OPI for the desired motor by double clicking the relevant square in the table
1. Click on `More details...`
1. In the `Calibration` section, switch `Cal` from `use` to `set`
1. Either
    1. Change the `Off` field to apply an offset to the current position
    1. Change the current position directly by changing the `MoveAbs` `User` field in the `Drive` section
1. **Don't forget** to switch the `Cal` field back to `Use` once you're done or the motor won't move.

### Homing
The McLennan driver is currently set so that it will execute a constant velocity (`CV`) move to the next limit switch at a velocity equal to the base velocity. The base velocity is set to match the main velocity set via the IOC macros at startup. This can be edited in the motor details panel.

### Configuring axes
When configuring a particular axis, an `axes.cmd` file is required in `C:\Instrument\Settings\config\[INSTMACHINE]\configurations\mclennan`. See the the [motion control](https://github.com/ISISComputingGroup/IBEX/wiki/Motion-Control) pages for additional details. It is often desirable to set up a number of axes depending which controller, and which axis is in use. There are specific environment variables set up to let you do this. The following example shows a stretching rig set up on `MOT0201` and a linear sample changer on `MOT0101`:

```
$(IFMTRCTRL1)$(IFAXIS1) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STACK:LIN,mAXIS=MTR0101")
$(IFMTRCTRL2)$(IFAXIS1) dbLoadRecords("$(AXIS)/db/axis.db","P=$(MYPVPREFIX)MOT:,AXIS=STRETCH:LIN,mAXIS=MTR0201")
```

You can see the environment variables being used at the start of the line. The available variables are:

- `IFMTRCTRLn`: The line is run if the controller number for the motor is `n` where `n` is between 1 and 24. This corresponds to the `MTRCTRL` IOC macro.
- `IFAXISn`: The line is run if the axis number for the motor is `n` where `n` is between 1 and 8. This corresponds to the `AXISn=yes` IOC macro.

Note that the equivalent `IFNOT...` environment variables also exist but are typically of less use.

Also note that the two environment variables combine as an `and` operation when used in this form. That is, the line will only execute if both conditions are met. There is currently no way to combine the environment variable with an `or` operator.

## Reset on move

The IBEX McLennan driver is set to send a reset command on any request to move. This is intended to clear errors (e.g. tracking abort) and avoid the need for power cycling that would clear the position.

## Reset on stop

The IBEX McLennan driver sends the following sequence of commands when a stop is requested:

```
STOP
RESET
STOP
```

The first stop will stop the motor as part of the normal operation and the 2nd and 3rd command will have no effect. If the motor enters an error state during a move, the first stop will have no effect and the 2nd and 3rd command will stop it. The first command is necessary since the 2nd and 3rd commands will not cause it to stop under normal operation. 
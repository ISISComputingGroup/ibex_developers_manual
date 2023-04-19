> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC)
 > [Motor IOCs](Motor-IOCs) > [McLennan](McLennan-motors)

The McLennan motor is a controller that support multiple independent motors.

**WARNING: Unlike many other motor controllers that remember settings through autosave the McLennan exclusively uses macros. This means for changing parameters in a persistent way you will need to change them in the IOC configuration rather than the motor details panel**

## Behaviour

### Velocity
The McLennan motor velocity is set with the *VELO***n** IOC macros. The value set is in `mm/second`. The motor resolution is set with the *MRES***n** IOC macros and as in units of `mm/step`. The velocity value set on the device will be the velocity divided by the motor resolution, and will be in units of `step/second`.

### Acceleration
Acceleration is far less intuitive than velocity. The acceleration value on the device is the acceleration in units of `step/s^2`. It is calculated as the IOC macro values of velocity divided by the product of the motor resolution and acceleration. The IOC macro acceleration is therefore the number of seconds under linear acceleration to reach maximum speed.

### Setting the motor position/offset
See [Set the raw position of the motor without moving it](Set-the-raw-position-of-the-motor-without-moving-it)

### Homing

There are several homing modes on the McLennan set via the home macro. The choice of mode depends on the motor, all but 0 are controlled by some SNL. Modes are:

* 0: Controller does internal home to an external home signal.
* 1: Do a reverse constant velocity move until limit switch is hit, but do not zero the motor (this is deprecated)
* 2: Send a reverse home signal to the controller and then zero the motor
* 3: Do a reverse constant velocity move until limit switch is hit then zero the motor
* 4: Send a forward home signal to the controller and then zero the motor

The velocity of the constant velocity move is set to be a 1/10 of the normal velocity unless the macro is set to change it.

**There is a [special homing sequence for Vesuvio](Vesuvio-homing-sequence) because it doesn't quite work until ticket [5739](https://github.com/ISISComputingGroup/IBEX/issues/5739) is done**

**There is a [special homing sequence for HRPD low temp sample changer](HRPD-homing-sequence) because it doesn't quite work until ticket [5739](https://github.com/ISISComputingGroup/IBEX/issues/5739) is done**

The way this works in the code is that the motor driver send the correct home (or no home) dependent on the mode set in [`request_mode`](https://github.com/ISISComputingGroup/EPICS-motor/blob/master/motorApp/MclennanSrc/devPM304.cc#L163), for [SNL](https://github.com/ISISComputingGroup/EPICS-motor/blob/master/motorApp/MclennanSrc/homing.st) then takes care of other moves.

### switch settings

Rotary switch SW1 and SW2 give axis address, address is 10*SW1 + SW2

SW3

* 1=ON 2=OFF gives serial baud 9600, see manual for other combinations 
* 3=OFF 7bit even parity, or     3=ON 8bit no parity
* 4=OFF
* 5=ON  (quiet command reply mode, required by EPICS driver)
* 6=OFF
* 7=OFF
* 8=OFF

SW4 controls encoder termination, with OFF=single ended (TTL), ON=differential pair (RS422). Not for us to change, leave to motion engineers.

### Encoder resolution
Key macro is `ERES`, this is not the same as the ERES in the motor record, it is actually the encoder ratio written `M/E` providing `motor_steps_per_revolution / encoder_steps_per_revolution`. So `actual_position_steps = encoder_steps_readback * encoder_ratio`. For closed loop mode to work this needs to be correct so that `commanded_motor_steps_moved = encoder_steps_moved * encoder_ratio`. It is possible to work this out by e.g. going to console, doing a small MR relative move and comparing command (CP) and actual (AP) position. `dbior` on an ioc now shows these values, as does the `QP` command at the motor low level serial interface. The Raw encoder steps is `IP` or `Input Position` which is scaled by encoder ratio to give actual position. If encoder and motor move in opposite directions, add a minus sign.

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

### Reset on move

The IBEX McLennan driver is set to send a reset command on any request to move. This is intended to clear errors (e.g. tracking abort) and avoid the need for power cycling that would clear the position.

### Reset on stop

The IBEX McLennan driver sends the following sequence of commands when a stop is requested:

```
STOP
RESET
STOP
```

The first stop will stop the motor as part of the normal operation and the 2nd and 3rd command will have no effect. If the motor enters an error state during a move, the first stop will have no effect and the 2nd and 3rd command will stop it. The first command is necessary since the 2nd and 3rd commands will not cause it to stop under normal operation. 

### Creep Speed CS for home to datum

Quick note on this learnt from SECI; It appears that the SC command which set the speed for HD (home to datum) may be limited in it range. We don't think it can be set faster than the normal speed and maybe be limited to 400. Investigate when and if we need this.

## Setup, Trouble Shooting and Usage

### Setting up the unit

When starting the unit:

1. Start the controller
1. Start/restart the IOC (so that it can send the motor and encoder resolutions to the controller)
1. Home the device

### I've booted up a McLennan and can't get it moving

Try using the macros for an axis other than 1 (2 or 3) in the ibex GUI. The axis to be driven by the buttons on the front panel are set by a position dial inside the driver, so these might not work with the motor you need to control.

Additionally if it moves a short distance and stops it may be going into Tracking abort. This happens when the encoder and motor resolutions are incorrect/incompatible. The first thing to do is to restart the McLennan and then the IOC so that the values are resent. If this does not fix it then check the settings are correct. 

### McLennan moves but doesn't stop at desired position

If the McLennan moves but does not stop at the position you requested it could be that the encoder and motor resolutions have not been sent to the controller. This must be done whenever the unit is restarted and is done by restarting the IOC.

### Homes are very slow

*In homing modes other than 2*, the McLennan homes via SNL and uses `JVEL` as it's speed. `JVEL` defaults to `VELO/10` if not set, so try increasing the jog speed and see if this speeds up homes

*In homing mode 2*, the McLennan uses an internal homing routine. This uses the "creep speed" which IBEX now _does_ set as of https://github.com/ISISComputingGroup/IBEX/issues/4815. If you need to manually make homing faster, do the following:
- Set `JVEL` to an appropriate speed for homing via IBEX configuration macros
- Ensure it is propagated down to motor record, look in motor details OPI
- Disconnect IOC and connect a terminal emulator (e.g. putty, hterm, hyperterm) to the device
- Issue `<axis number>QA\r\n` (e.g. `1QA\r\n` for axis 1) to print the current settings of the motor
- Look for Jog speed
- Issue `<axis number>SC<jog speed>\r\n` with the jog speed you just looked up
- Reconnect the IOC and check that homes now work appropriately. 

Note that the creep speed for the PM600 at least is limited to 800 steps per second. We cater for this in the motor record and set it to the `HVEL` value if lower than 800 and otherwise set it to 800. 

## Mclennan does not communicate

Most McLennans have 2 RS232 ports, for daisy chain in&out. The out port is **required** to have an rs-232 terminator installed in it, this looks similar to a null modem and bridges two pins. **If this terminator is not installed the mclennan will not communicate at all using any comms settings**.

## Office McLennan Settings

The office McLennan need the following:

1. No Null terminator or gender changer (if using a straight-through male-female cable from a PC)
  * Note: If the mclennan has two ports (for daisy chaining), the out port MUST have an RS232 terminator in it. This looks similar to a null modem and bridges two serial pins. If this is not present, the motor controller will not communicate.
1. `BAUD` 9600
1. `BITS` 8
1. `AXIS 3` yes (all others no)
1. `MODE3` CLOSED
1. `ACCL3` 1
1. `VELO3` 0.5
1. `ERES3` 400/4096
1. `MTP3` 4000

# McLennan

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

mclennan/*
```

The McLennan motor is a controller that support multiple independent motors. It is often used at ISIS for rotation stages.

**WARNING: Unlike many other motor controllers that remember settings through autosave the McLennan exclusively uses macros. This means for changing parameters in a persistent way you will need to change them in the IOC configuration rather than the motor details panel, otherwise they will get lost on IOC restart. We now plan to make these settings appear read-only in the motor view to avoid any confusion **

Instructions on how to convert a **labview mclennan ini file** are at the end of this document in the [converting values from labview](#converting-values-from-labview) section

## Behaviour

### Motor Resolution
The motor resolution is set with the *MSTP***n** IOC macros and in units of `steps/mm` (same as in SECI/labview), this will be inverted by the IOC internally as the EPICS motor record `MRES` field uses the inverse `mm/step`. 

### Encoder Resolution
The encoder ratio rather than encoder resolution is set with the *ERES***n** IOC macros, this is a string like `400/4096` and bears no direct relation to the EPICS motor record `ERES`. As the mclennan driver pretends to be open loop (no encoder present as per `MSTA` field) whatever mode it is running in, the motor record `ERES` is not actually used and is set to `0` in the `st.cmd` and will then display as the same value as motor record `MRES` when later viewed. So ignore the encoder resolution value displayed on the motor record screen.  

The encoder ratio written `M/E` is providing `motor_steps_per_revolution / encoder_steps_per_revolution`, in SECI/labview this was referred to as `Numerator / Demoninator`. So `actual_position_steps = encoder_steps_readback * encoder_ratio`. For closed loop (encoder feedback) controller mode to work this ratio needs to be correct so that `commanded_motor_steps_moved = encoder_steps_moved * encoder_ratio`, if the ratio isn't right the motor will fail to get position leading to many retries and an error. It is possible to work out the ratio by e.g. going to motor console (PuTTY/hterm), doing a small MR relative move and comparing command position (CP) and actual position (AP). `dbior` command on an ioc window now shows these values, as does the `QP` command at the motor low level serial interface. The Raw encoder steps is `IP` or `Input Position` which is scaled by encoder ratio to give actual (AP) position. If encoder and motor move in opposite directions, add a minus sign to encoder ratio.

### Velocity
The McLennan motor velocity is set with the *VELO***n** IOC macros, the value set is in `mm/second`, same units as EPICS motor record uses.

### Acceleration
The IOC macro *ACCL***n** for acceleration is the the number of seconds under linear acceleration to reach maximum speed, the same convention as the EPICS motor record (The acceleration value on the device itself is the acceleration in units of `step/s^2`, this is calculated in the IOC as velocity divided by the product of the motor resolution and ACCL value). 

### Setting the motor position/offset
See [Set the raw position of the motor without moving it](Set-the-raw-position-of-the-motor-without-moving-it)

### Homing

There are several homing modes on the McLennan set via the `HOME` macro. The choice of mode depends on the motor, modes 1 and 3 (constant velocity homes to limit switches) are controlled in software by SNL, others by controller `HD` (home to datum) command. Modes are:

* 0: Controller does internal home to an external home signal (not normally used).
* 1: Do a reverse constant velocity move (jog) until limit switch is hit, but do not zero the motor (this is deprecated)
* 2: Do a hardware reverse (-) direction search for a home signal and then zero the motor
* 3: Do a reverse constant velocity move (jog) until limit switch is hit then zero the motor.
* 4: Do a hardware forward (+) direction search for a home signal and then zero the motor
* 5: Move to forward limit, do a hardware reverse direction search for a home signal and then zero the motor
* 6: Move to reverse limit, do a hardware forward direction search for a home signal and then zero the motor

The constant velocity move uses JVEL and is set to be a 1/10 of the normal velocity unless the macro is set to change it.

**There is a [special homing sequence for Vesuvio](mclennan/Vesuvio-homing-sequence) because it doesn't quite work until ticket [5739](https://github.com/ISISComputingGroup/IBEX/issues/5739) is done**

**There is a [special homing sequence for HRPD low temp sample changer](mclennan/HRPD-homing-sequence) because it doesn't quite work until ticket [5739](https://github.com/ISISComputingGroup/IBEX/issues/5739) is done**

The way this works in the code is that the motor driver send the correct home (or no home) dependent on the mode set in [`request_mode`](https://github.com/ISISComputingGroup/EPICS-motor/blob/master/motorApp/MclennanSrc/devPM304.cc#L163), for [SNL](https://github.com/ISISComputingGroup/EPICS-motor/blob/master/motorApp/MclennanSrc/homing.st) then takes care of other moves.

### Controller Switch settings

Rotary switch SW1 and SW2 give axis address, address is 10*SW1 + SW2

DIP Switch SW3

* 1=ON 2=OFF gives serial baud 9600, see manual for other combinations 
* 3=OFF 7bit even parity, or     3=ON 8bit no parity
* 4=OFF (no hardware flow control)
* 5=ON  (quiet command reply mode, required by EPICS driver)
* 6=OFF 
* 7=OFF (rs232)
* 8=OFF (no terminator for rs485)

SW4 controls encoder termination, with OFF=single ended (TTL), ON=differential pair (RS422). Not for us to change, leave to motion engineers.

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

The McLennan now prints its current mode of operation (moving, homing, Idle, tracking abort etc) and any error messages to the IOC log file/ioc command window screen. 

### Setting up the unit

When starting the unit:

1. Start the controller
1. Start/restart the IOC (so that it can send the motor and encoder resolutions to the controller)
1. Home the device

### I've booted up a McLennan and can't get it moving (properly)

Check the `MCLEN` IOC log file for error messages and also examine output from `dbior` and `dbior * 1` typed at the IOC console window. 

If it doesn't move at all try using the macros for an axis number other than 1 (e.g. 2 or 3) in the ibex GUI. The axis to be driven by the buttons on the front panel are set by a position dial inside the mclennan crate, so you may not be be trying to control the correct axis id.

If it moves a short distance and stops it may be going into `Tracking abort`. A tracking abort means the encoder and motor step counters have got further apart than expected during the move, this could be due to: 
* The encoder and motor resolutions are incorrect/incompatible, so "expected" and "actual" position are diverging. The first thing to do is to restart the McLennan hardware and then the IOC so that the values are resent. If this does not fix it then check the settings are correct. 
* you are trying to accelerate or move too quickly, or possibly move too slowly, meaning there is a time lag between the motor pulses being sent and the motor response. Try changing these parameters. See end of this page if you need to change the tracking abort window.
 
### McLennan moves but doesn't stop at desired position

If the McLennan moves but does not stop at the position you requested it could be that the encoder and motor resolutions have not been sent to the controller or are incorrect. This must be done whenever the unit is restarted and is done by restarting the IOC.

### Lots of parity errors in log file

check `Controller Switch settings` above - if IBEX has been set to use 7 bit even parity but the crate dip switch is set at 8 bits no parity, then this could lead to parity errors being generated. Make sure the IBEX MCLEN IOC and the crate agree on this setting.  

### Homes are very slow

*In homing modes 1 and 3*, the McLennan homes via SNL and uses `JVEL` as it's speed. `JVEL` defaults to `VELO/10` if not set, so try increasing the jog speed and see if this speeds up homes

*In other homing modes*, the McLennan uses an internal homing routine. This uses the "creep speed" which IBEX now _does_ set as of https://github.com/ISISComputingGroup/IBEX/issues/4815. If you need to manually make homing faster, do the following:
- Set `HVEL` macro to an appropriate speed for homing via IBEX configuration macros
- Restart the IOC

Note that the creep speed for the PM600 at least is limited to 800 steps per second. We cater for this in the motor record and set it to the `HVEL` value if lower than 800 and otherwise set it to 800. 

## Mclennan does not communicate

Most McLennans have 2 RS232 ports, for daisy chain in&out. The out port is **required** to have an rs-232 terminator installed in it, this looks similar to a null modem and bridges two pins. **If this terminator is not installed the mclennan will not communicate at all using any comms settings**.

## Office McLennan Settings

The office McLennan(s, there are two) needs the following:

1. No Null terminator or gender changer (if using a straight-through male-female cable from a PC)
  * Note: If the mclennan has two ports (for daisy chaining), the out port MUST have an RS232 terminator in it. This looks similar to a null modem and bridges two serial pins. If this is not present, the motor controller will not communicate.

Use following IOC macro setting:



_note: the comms settings should be labelled on the device, so refer to those_

1. `BAUD` 9600 
1. `BITS` 7
1. `PARITY` even
1. `AXIS3` yes (all others no)
1. `MODE3` CLOSED
1. `ACCL3` 1
1. `VELO3` 0.5
1. `ERES3` 400/4096
1. `MSTP3` 4000

## getting debug output/information

console to IOC and type `dbior` for basic information. For extended information pass a higher report level to dbior e.g. `dbior drvPM304 1` (the `drvPM304` is the mclennan driver name and restricts details to just that, the second argument is the debug level. You can use `*` instead of `drvPM304` but will then get extended details for `asyn` and other loaded drivers too)
  
## converting values from labview

if you need to convert a previous SECI/labview mclennan ini file, these are usually found in `c:\labview modules\Drivers\Mclennan PM600\INI Files` on the NDX computer. A file will have an entry like:
```
[M0]
Name = "Mclennan Newport"
Enabled = TRUE    
Units = "deg"
Com Port = 7 
Axis Address = 1    
Baud Rate = 9600    
Data Bits = 8    
Parity = 0    
Stop Bits = 10    
Acceleration = 40000    
Velocity = 10000    
Motor steps per unit = 8000.000000    
Encoder counts per unit = 1000.000000    
Correction Gain = 70    
Window = 50    
Creep Speed = 5000    
Creep Steps = 0    
Settling Time = 0    
Jog Speed = 10000    
Control Mode = 4    
BackOff Steps = 0    
Deceleration = 40000    
Upper limit = 180.000000    
Lower Limit = -180.000000    
Enable State = 1    
KF = 0    
KP = 10    
KS = 0    
KV = 0    
KX = 0    
Numerator = 8.000000    
Denominator = 1.000000    
Homing Method = 2    
Homing Speed = 10000    
Home Offset = 0.000000    
Apply Home Position = TRUE    
Home Position = 0.000000    
Apply Home Offset = FALSE    
```
Calculate the appropriate MCLEN IOC macros as follows:
  
* `Axis Address = 1` and `Enabled = TRUE` so we set `AXIS1=yes` and then set other macros with a suffix of `1`
* `Name = "Mclennan Newport"` so we set `NAME1 = Mclennan Newport`
* `Motor steps per unit = 8000.000000` so we set `MSTP1 = 8000` (which will lead to an EPICS motor record MRES of 0.000125)
* `Encoder counts per unit = 1000.000000` this is not used directly, but see comment on `Numerator` and `Denominator` below
* `Velocity = 10000` this is in steps per second, so we divide by motor steps per unit to get units per second  (10000 / 8000), `VELO1 = 1.25`
* `Acceleration = 40000` this is in steps / s^2, we divide velocity by acceleration (10000 / 40000) to get the acceleration time `ACCL1 = 0.25`
* `Units = "deg"` so we set `UNIT1 = deg`
* `Jog Speed = 10000` so like velocity above we divide by steps (10000 / 8000) to get `JVEL1 = 1.25`
* `Upper limit = 180.000000` is already in proper units so set `DHLM = 180.0`    
* `Lower Limit = -180.000000` is already in proper units so set `DLLM = -180.0`
* `Homing Speed = 10000` so divide by motor steps (10000/8000) to get `HVEL1 = 1.25`
* `Numerator = 8.000000` and `Denominator = 1.000000` refer to the encoder ratio components so we set `ERES1 = 8/1` (This should be the equivalent numeric ratio to `Motor steps per unit`/`Encoder counts per unit` which is true here as 8000 / 1000 == 8 / 1 )
* `Home Position = 0.000000` IOC always applies a dial home position of 0, if labview value is non-zero set `OFST1` IOC macro to this value
* `Control Mode = 4` in labview `4` is "closed loop stepper" so set `CMOD1 = CLOSED` (if labview was `1` that means "open loop stepper" so would set `CMOD1 = OPEN`. We don't currently handle other values and they are not used at ISIS as far as we know)
* `Homing Method = 2` for labview 0=none; 1=home signal+; 2=home signal-; 3=reverse limit,home signal+; 4=forward limit,home signal-;5=reverse limit;6=forward limit. So labview method `2` is a *reverse direction hardware home* so after examining the [Homing](#homing) section above the equivalent ibex IOC mode is `HOME1 = 2`     
* `Window = 50` this is the end of move check window before an internal mclennan retry. It is a bit like the retry deadband of the motor record, but done at the controller. If a moves plus retries completes and is still outside this Window, an error will be signalled. So we set `WIN1 = 50`
* `Creep Steps = 0` number of steps to approach final position at the slower `Creep speed` in the final phase of a move. So we set `CRST1 = 0`    
* `Settling Time = 0` how long motor readback must be within `Window` of requested position at end of move, if not achieved triggers a timeout abort. So we set `SETL1 = 0`
* `BackOff Steps = 0` used for backlash correction. We can set `BOST1 = 0` but this is the default anyway.

Some labview values do not currently have macros and get IOC defaults. Edit MCLEN IOC `st-motor-init.st` if you need to temporarily change them and then create a ticket to add a proper IOC macro

* `Correction Gain = 70` this is equivalent to the IOC default `PCOF = 0.7` for a stepper motor
* `Creep Speed = 5000` only important for us if `Creep Steps` > 0 as this is temporary set to `HVEL` during a home so does not now affect homes.

Some mclennan values were not covered in labview but exist in MCLEN IOC `st-motor-init.st`

* Tracking window - a parameter used to determine if a *TRACKING ABORT* should be signalled, it is the max allowed difference between current and requested position during a move (also known as the *following error*). This may get triggered by a motor being told to move/accelerate quicker than it can, or move too slowly and so stalling, or an incorrect encoder ratio so motor and encoder get out of step, or incorrect encoder values being returned from the hardware
* Not Complete/Time-Out time - the max time at end of a move for any settling/auto corrections etc. to take place, otherwise triggers a *NOT COMPLETE/TIMEOUT ABORT* This could mean the `Window` mclennan parameter is too small and cannot be achieved, try increasing relevant `WIN*` macro. 

## useful commands for debugging from a terminal session

Command syntax is `aXXnnn` where `a` is address, `XX` command, `nnn` optional argument e.g. `1HD-1` homes axis 1 to datum in negative direction.
```
CO - query current operation
OS - query status
QA - query all parameters
QM - query modes
QP - query positions
QS - query speeds
```
modes give a bit pattern - see manual for meaning
 
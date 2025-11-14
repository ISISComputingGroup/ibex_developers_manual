# Cryogenic SMS PSU design

## Requirements

These are used to power the HIFI Cryomag. There are four, one (higher max current) controls the main switched cryomagnet, the other three (lower max current) control the X, Y, and Z 'shim' coil magnets. They are capable of driving the main cryomagnet up to a field of ~4.9 Tesla.

Magnet cool downs typically take several days, warm ups take a similar length of time. It usually sits at 3-4K, the temperature is monitored by a Keithley 2700.

They are connected via USB to serial RS-232 directly to the NDXHIFI_CRYOMAG PC.

All commands have a longhand and a shorthand version which can be found in the manual on our network share. The emulator has been made such that it can deal with the longhand or the shorthand, since it must be tested against the VI for compatibility, and the VI uses shorthand commands (vs the IOC which uses longhand).

Commands can reply with a myriad of options. Some of these are time stamped, some are not. These are also listed in the manual on the network share.


## IOC Structure

The IOC itself has multiple layers. On the surface, there is an EPICS db file with some values 
populated by `get` commands in a stream device proto file, some setpoints that eventually lead 
to `set` commands in that same proto, and a series of calc records. These PVs are the ones the 
OPI reads and writes to. For basic interactions, this is all you need to know.

However, behind the scenes you may notice that many of the user-facing setpoints don't actually 
directly write out anywhere, and the ones that do are not exposed to users via the OPI, and also 
don't seem to be written to/triggered from anywhere in the db. This is because there is a driver 
in `CRYOSMSDriver.cpp` built off of asynPortDriver (hereafter referred to as "the driver") 
sitting on top of the IOC, which is looking at what the user is setting and  what the device is 
currently doing, then writing out to relevant "hidden" setpoints (`:_SP` rather than `:SP`). 
This allows it to get the device to an end-state the user wants without them having to know 
about all the intermediate steps needed to get there, and also making sure the magnet doesn't 
quench.

Attached to the driver is a queued state machine, implemented with a thread that 
decides when to pop events from a queue to an implementation of boost's meta state machine. This 
part of the system is mostly just to ensure all the reads, writes, waits, etc. happen 
consistently and in the  right order. 

Safety is the number one concern of this system, and if there appears to be an overly  
complicated implementation for something, chances are that if it wasn't there it could lead to  
a magnet quench. This needs to happen at IOC level because the PSU itself will happily quench 
the magnet if you give it the wrong commands.

## Initialisation
### Macros
The IOC has the following macros. A small number (e.g. T_TO_A) are used by the db, but the 
majority are only used by the driver. At the bottom of the main file, you can see them 
being loaded via the usual method for an asynPortDriver. Upon initialising the driver, 
these values are loaded into a map of the form `MACRO_NAME: [macro_value]` called `envVarMap`, which 
other methods reference whenever they need to check a macro. 

| Macro                      | 	Description                                                                                                                        | 	Defaults |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------|
| MAX_CURR                   | 	Define the maximum current that is allowed                                                                                         |           |
| T_TO_A                     | 	The conversion value between Tesla and Amps for the system                                                                         |           |
| MAX_VOLT                   | 	Set the maximum voltage for the system                                                                                             |           |
| WRITE_UNIT                 | 	Which unit to write to the PSU in                                                                                                  | 	Amps     |
| WRITE_UNIT_TIMEOUT         | 	How long in seconds to wait after write unit is  changed before resetting it to `WRITE_UNIT`                                       |           |
| DISPLAY_UNIT               | 	Which unit will be used when displaying the value from the PSU                                                                     | 	Gauss    |
| RAMP_FILE                  | 	Location of file containing ramp rates 	                                                                                           |           |
| ALLOW_PERSIST              | 	Whether or not to allow setting of persistent values                                                                               | 	No       |
| USE_SWITCH                 | 	Whether or not to monitor and set switches on and off                                                                              | 	No       |
| SWITCH_TEMP_PV             | 	PV address of switch temperature                                                                                                   |           |
| SWITCH_HIGH                | 	The value at which the switch will be considered warm                                                                              | 	3.7      |
| SWITCH_LOW                 | 	The value at which the switch will be considered cold                                                                              | 	3.65     |
| SWITCH_STABLE_NUMBER       | 	The number of readings past a threshold needed before the switch can be considered warm/cold                                       | 	10       |
| HEATER_TOLERANCE           | 	The tolerance between the magnet and lead currents before considering them as close enough to allow the leads to warm              | 	0.2      |
| SWITCH_TIMEOUT             | 	The time to allow for the switch to warm or cold after turning the heater on/off before considering there to be an error situation | 	300      |
| SWITCH_TEMP_TOLERANCE      | 	needs clarification 	                                                                                                              |           |
| HEATER_OUT                 | 	The heater output to be used                                                                                                       |           |
| USE_MAGNET_TEMP            | 	Whether to act if the Magnet Temperature is out of range                                                                           | 	No       |
| MAGNET_TEMP_PV             | 	The PV address of the magnet temperature                                                                                           |           |
| MAX_MAGNET_TEMP            | 	Maximum allowed temperature of magnet                                                                                              | 	5.5      |
| MIN_MAGNET_TEMP            | 	Temperature below which there is potentially an error reading temperature from the magnet                                          | 	1        |
| COMP_OFF_ACT               | 	Whether to act if magnet temperature is out of range                                                                               | 	No       |
| NO_OF_COMP                 | 	Number of compressors in the system                                                                                                | 	2        |
| COMP_1_STAT_PV             | 	The PV address for the status of the first compressor 	                                                                            |           |
| COMP_2_STAT_PV             | 	The PV address for the status of the second compressor 	                                                                           |           |
| FAST_RATE                  | 	The ramp rate to use for the fast ramps                                                                                            | 	0.5      |
| FAST_PERSISTENT_SETTLETIME | 	The number of seconds to settle after a ramp fast to persist                                                                       | 	5        |
| PERSISTENT_SETTLETIME      | 	The number of seconds to settle after a ramp to persist                                                                            | 	60       |
| FILTER_VALUE               | 	The value to use to filter the target reached calculation                                                                          | 	0.1      |
| FAST_FILTER_VALUE          | 	The value to use to filter the target reached calculation when ramping fast to a target                                            | 	1        |
| NPP                        | 	The npp value when calculating whether or not the target has been reached                                                          |           |

### Startup Checks
As some of the checks needed to be run upon initialisation are only possible after the db has 
initialised, they are run in the `onStart()` method that only runs when the `INIT` PV (with 
`PINI` 1) writes out. This method checks various macros to determine whether certain modes of 
operation should be enabled/disabled:

All writes to the device will be disabled in any of these situations:

- `T_TO_A` not supplied and `CRYOMAGNET` is `Yes` 
- `MAX_CURR` not supplied
- `ALLOW_PERSIST` is on, but any of the subsequently required variables (`FAST_FILTER_VALUE, FILTER_VALUE, NPP, FAST_PERSISTENT_SETTLETIME, FAST_RATE`) are missing
- `USE_SWITCH` is on, but any of the subsequently required variables (`SWITCH_TEMP_PV, SWITHCH_HIGH, SWITCH_LOW, SWITCH_STABLE_NUMBER, HEATER_TOLERANCE, SWITCH_TIMEOUT, SWITCH_TEMP_TOLERANCE, HEATER_OUT`) are missing
- `USE_MAGNET_TEMP` is on, but any of the subsequently required variables (`MAGNET_TEMP_PV, MAX_MAGNET_TEMP, MIN_MAGNET_TEMP`) are missing
- `COMP_OFF_ACT` is on, but any of the subsequently required variables (`NO_OF_COMP, MIN_NO_OF_COMP, COMP_1_STAT_PV, COMP_2_STAT_PV`) are missing

Additionally, the driver will initialise various variables and send several commands to the 
PSU based on user provided macros:

- The Tesla-Amps conversion rate will be set to `T_TO_A` if `CRYOMAGNET` is set to `Yes` 
- The maximum allowed current will be set to `MAX_CURR`
- The maximum allowed voltage will be set to `MAX_VOLT`
- The heater output will be set to `HEATER_OUT`
- The file named in `RAMP_FILE` will be used to populate a ramp table, consisting of values for 
  the fastest safe ramp within a field range, and the maximum field strength of that range.
  - More info on ramp rates in [Performing a Ramp](#performing-a-ramp) 
- The ramp rate will be set to an appropriate value read from the ramp table based on the current 
  value of the field
- Finally, a thread containing the event queue, a thread which continually checks certain values,
  and the meta state machine are all started

If no errors occur throughout this process, it will then write 1 back to `INIT`, which will show 
as "Startup complete". If the IOC doesn't seem to be starting correctly, check this PV to figure 
out if you need to debug whether/where `onStart()` is hitting an error.

## Unit Conversion

The PSU defaults to displaying, and sending/receiving via its USB interface, the values for 
current it is outputting to the coils in terms of Amps. It can, however, also output the field 
strength in Tesla that will be achieved for a given current if it is provided with a conversion 
factor from current to field strength. This conversion factor will likely vary from magnet to 
magnet as it is determined by the geometry, material properties, etc. of the magnet itself. We 
tell the PSU which to display on its front panel and use for communication through the 
`OUTPUTMODE:_SP` PV based on `WRITE_UNIT`.  

```{note}
The shim magnets on HIFI are  also operated using these PSUs and this IOC, however the 
Tesla-Amps conversion factor is far outside what the PSU considers a valid range (as these are 
not cryomagnets). For these, we set `CRYOMAGNET` to "No", to tell our IOC not to even try 
writing `T_TO_A` to the PSU. Instead, we only read/write in Amps and perform all conversions in 
the IOC.
```

Users additionally often wish to have the PSU output shown as the resulting field strength in 
Gauss (10,000 Gauss = 1 Tesla), which is set to be the default value displayed. In order to convert 
between values read from the device, you will see several calcs in the db converting from 
`[value]:RAW`, which will be in `WRITE_UNIT`, to `[value]:AMPS`, `[value]:FIELD:TESLA`, and `[value]
:FIELD:GAUSS` before finally the user-facing `[value]` selects which of these to use based on 
`DISPLAY_UNIT`.

In the driver meanwhile, values that are read from user-facing PVs in the db are taken 
to be supplied in terms of `DISPLAY_UNIT`, and are converted back and forth between values based on 
need for certain calculations, before being sent to the device in `WRITE_UNIT`.

Instrument scientists also wished to be able to temporarily change `WRITE_UNIT` for use cases 
which were never made clear (as of the author Lilith's memory in Nov 2025, this may be so that 
they can tinker with values physically on the PSU?). Nonetheless, this functionality is 
available to them. The PV `OUTPUTMODE:SP` lets users change the write unit for a time period set 
by `WRITE_UNIT_TIMEOUT`, which is propagated through the driver by changing the value 
mapped in `envVarMap` before writing to the device using `OUTPUTMODE:_SP`. At the end of the 
macro-defined timeout, the checks thread will automatically change everything back to the 
`WRITE_UNIT` specified by macros.

## Event Queue

The event queue is a double-ended queue which is used to queue up state transitions to be  
performed on the state machine. It is processed in a while loop on the `eventQueueThread`, which 
determines when to pop an event and push it to the state machine based on factors that vary by 
whichever state the state machine is currently in (for example, making sure the PSU is at a ramp 
target before leaving the "ramping" state). Throughout the driver, events are pushed to either 
end of this queue (usually the back) by various methods.
Within this queue, individual events are stored inside  variant objects from the boost variant 
library in order to preserve typing (boost msm fires events based on the typing of the object 
being passed to it).

## Queued State Machine

The IOC makes use of a queued state machine, based upon the meta state machine library from 
boost. This is stored in a separate file from the driver, `QueuedStateMachine.h`, as it is 
header-based.
Here, possible states, events (things that prompt state changes) and actions (code to perform on 
given state transitions) are defined, alongside a table of possible transitions and the 
respective actions to process when performing them. 

```{note}
To avoid a circular dependancy, the state machine imports a dummy version of the main driver, 
defined in `StateMachineDriver.h`, which the main driver inherits from and then overloads the 
methods of.
```

## Sets Sent to the Driver

As most of the values used by the driver are read directly by it from the db, there are only a 
handful of PVs that actually send values to the driver themselves:

### Output Mode

As described in [Unit Conversion](#unit-conversion), temporarily tells the PSU to communicate in 
different units.

### Init

Starts the initialisation process described in [Startup Checks](#startup-checks). This only 
happens once per boot.

### Heater response deconstruction

The PSU's reply to asking whether the magnet heater is on can get complicated, so it is sent to 
c++ to be dealt with instead of using stream device (It's possible that this could all be done 
in stream device, and if you want to do this, by all means make a ticket).

The response is of the form `HEATER STATUS: {OFF|ON}` if it is either on or off with the magnet 
at 0T, or `HEATER STATUS: OFF AT {value} {units}` if it is off with the magnet holding a field 
of `{value}` in units of `{units}`. This is then filtered through to relevant heater readback 
and `OUTPUT:PERSIST` PVs. The PV `OUTPUT:COIL` then switches which pv it reads from based on 
whether the heater is on or off (on - `OUTPUT`, technically the current through the magnet's 
leads; off - `OUTPUT:PERSIST`), as it represents the definitive value of the magnet's output.

```{important}
If the heater is off and the magnet has current running through it, this means that is in 
superconducting or "persistent" mode. If you ramp the current in the leads away from this (e.g. 
to 0 if the  user selects to ramp leads to 0 after ramping the magnet), the leads MUST be ramped 
back to the persistent current before switching the heater back on, else the magnet will quench 
as the previously superconducting current rapidly changes to meet the current through the leads. 
```

### Start

Tells the driver to perform a ramp based on settings provided to other PVs. See [Performing a 
Ramp](#performing-a-ramp 

### Pause

Setting this to 1 pushes a "pause" event to the state machine, then suspends the event queue 
thread. If the PSU is ramping, the "pause" event will tell it to pause, and will put the state 
machine into the paused state which can only be left by resuming or aborting.  
Immediately responds with an "acknowledge" message.

Setting this to 0 will place a "resume" event at the front of the event queue, then restart the 
event queue thread to immediately process it, putting the state machine back into a ramping state. 
The ramp will then continue as before. 

### Abort

Similar to Pause, when abort is set to 1 it will process an "abort" event immediately, however 
it will not suspend the state machine. It will then attempt to stop any warming or cooling by 
queuing a "cool" or "warm" respectively. If the PSU was instead ramping, it will pause the ramp, 
set the PSU ramp endpoint to the current output, empty the rest of the event queue, then resume 
sso that the PSU immediately accepts that the ramp has reached its target at its current output. 


## Performing a Ramp

When [Start](#start) is processed, the driver will attempt to construct a queue of state 
transitions in the event queue which will make the properties of the magnet be what the user has 
specified. this is done by the method `setupRamp()`

First, the driver checks whether the magnet is currently in persistent mode. If it is, it will 
queue a fast ramp of the leads to bring them to the persistent current if this is needed, then 
it will warm the magnet up to take it out of persistent mode.

```{note}
The leads can be ramped much faster than the coils, so a seperate ramp rate set by the 
macro `FAST_RATE` is used when ramping only them. 
```

Next, the driver will take the current field strength in the magnet as the start point and the 
desired field strength set in `OUTPUT:SP` as the end point. It will then compare these points to 
the ranges of field strengths in the ramp table. If both are within the same range (and same 
polarity, more on that later), it will simply queue a ramp event set to the end point at the 
relevant ramp rate for that range, then a "target reached" event. If however, the start and end 
points are in different field ranges in the ramp table, it will queue up ramp events to each of the 
field range maxima, at ramp rates that correspond to the ranges that each ramp will be going 
through, in the order that the maxima will be encountered in on the route between the start and 
end point. After each of these individual ramp events, it will also queue a "target reached" 
event for immediately after it.

In the cases where the start point and end point have opposite polarities, the above process 
will be performed first by going from the start to 0, then from 0 up to the end point.

Finally, the driver will queue a cooldown event if the user wants the magnet to be persisting at 
the end point, and will ram the leads to 0 if the user wants that to happen also.

### Ramp Events

Ramps are passed to the state machine with four values:
- their endpoint
- the ramp rate to use to get the endpoint
- the polarity of the endpoint (only needed when going from 0)
- ramp type (e.g. whether this is a fast ramp of the leads)

When processed, the driver will set the PSU's output midpoint (in the context of 
0 - arbitrary midpoint - max; midpoint doesn't have to be half of max and rarely is) and its 
ramp rate, then tell it to ramp to the midpoint. If a ramp's start point is 0, it will first 
make sure the polarity set on the PSU is the same as the enpoint's polarity. 

After being processed, the event queue thread will wait until the PSU's output is within a 
tolerance of the ramp's endpoint and the PSU is reporting that it is holding at target, then 
process the target reached event. 

### Target Reached Events

The events which are queued after each ramp mostly exist to better delineate between ramps in 
the state machine. The other function of them is that they  will each check if the en point 
their individual ramp reached is the end point specified by the user - the final end point. If 
it is, they will make the driver wait for a period of time specified by relevant hold/settle  
time macros before letting it carry on with any further events.

## Statuses

There are a variety of statuses that can be put to the `STAT` pv. Some of them contain extra 
contextual messages, but broadly there are the following cases:
- Ready - The driver and PSU both are not currently doing anything, and are ready for user inputs
- Ramping - The PSU is ramping its output
- Paused - Either the user or an internal check has caused a ramp to pause
- Holding/Settling - The PSU claims to have finished what it was doing, the driver is waiting 
  for things to settle briefly before it either goes into ready or starts its next task
- Cooling/Warming - The heater has recently been switched off or on,  we are waiting until its 
  temperature is consistently below/above `SWITCH_LOW` or `SWITCH_HIGH` respectively
- Aborting - Something has caused the driver to abort, it is in the process of stopping everything
- Processing - The driver only goes into this status when it can no longer say that its previous 
  status is valid, but it has yet to achieve a subsequent status. For example, when `START:SP` 
  is set, it goes from Ready to Processing, then goes to Ramping once the first ramp has started.
  If the driver is reporting this status for a long time, it means something has gone wrong in 
  its queue somewhere and it needs restarting   
  
### The READY PV

The `READY` PV is simply a boolean pv that  simplifies the `STAT` PV. Either the driver is ready,
and can accept commands, or it is not.

## Automatic Pausing/ Aborting

The "checks" thread created during [startup checks](#startup-checks) will run through its loop 
twice per second, decrementing/checking against any ongoing timers, pausing the ramps for safety if 
not enough compressors are active, and checking for quenches.

### Quenches

The magnet can quench if it is ramped too aggressively, or if its temperature drifts too high. 
If the PSU detects a quench, it reports that it thinks the magnet has quenched. The IOC will 
interpret this and halt all queued actions. It will stay in this state until the IOC is restarted.

```{important}
The PSU lacks any safety measures to prevent you from ordering it to perform actions that will 
quench a magnet. It will happily turn on the heater when the magnet is at 10T and the leads are 
at 0. This is why the driver is so careful about everything it sends 
```

## Behind the scenes PVs

When the driver sends a value to the PSU, it does so by setting a relevant PV ending in `:_SP`, 
which then sends a command to the PSU via stream device. This does mean that there are all sorts 
of PVs which can be tinkered with to sidestep the driver and manually define/start ramps or 
toggle the heater. Yes, you can use these if you really want to, but only do so if you are 
absolutely sure you're not quenching the magnet. That cumbersome driver is there for a reason.

## Other IOCs that Interface with CRYOSMS 

If you write any other IOCs that interface with the CRYOSMS, please make note of them here. If 
you use [Behind the scenes PVs](#behind-the-scenes-pvs) in them please also write a 
justification of why your use-case is safe.

### HIFIMAGS

Most of the magnet control on HIFI is done via the HIFIMAGS IOC, which is a series of db files 
that get pointed to 4 CRYOSMS IOCS (main magnet, shims for x y and z axis) and a snl state 
machine which controls when you are and aren't allowed to change set points within HIFIMAGS. 
There is an OPI that goes alongside this IOC, which helps scientists consolidate the main 
numbers they care about from across the system in one place.

### HIFI's Zero Field Controller

HIFI also has a zero field IOC, which uses [Behind the scenes PVs](#behind-the-scenes-pvs) to 
perform tiny, quick ramps on the shim coils to compensate for stray magnetic field. This is safe 
because it is only the non-cryomagnet coils being used. Additionally, if this IOC is in use, the 
individual CRYOSMS IOCs being linked to will lock all other input, and refuse to make heater 
changes.
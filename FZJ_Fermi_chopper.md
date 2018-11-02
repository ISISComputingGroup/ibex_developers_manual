# FZJ fermi chopper, as used on MERLIN and MAPS

This device has a relatively complex IOC due to some communication issues we have had with the chopper. The following things are non-standard:
- Custom checksum algorithm in stream device. This is specific to this fermi chopper.
- `aSub` record to parse a response string from the hardware.
- `aSub` record to decide how to send the speed setpoint to the device
- `aSub` record to decide whether a given command is allowed to be sent
- `SNL` state machine to ensure that setpoints and their readbacks stay in sync (for both gate width and phase delay)
- There is logic in the DB records to prevent sending a speed setpoint that is equal to the current speed setpoint readback.
- There is (equipment) safety logic in the IOC. For more details see below.

# Unexpected Delay / Speed / Gate Width settings

### Delay: high and low byte ordering

The delay setpoint can be wrong if the high byte and low byte of the setpoint are received in the wrong order. The observed behaviour in this state is that the setpoint readback will appear to be correct, but the actual delay will home in on a different (incorrect) value. Resending the delay setpoint in the correct order fixes this state.

This problem has been solved by defining the order of the packets in the stream device protocol, including an appropriate wait between them. For more details, see [#2628](https://github.com/ISISComputingGroup/IBEX/issues/2628).

### Gate width setpoint readback is wrong

Occasionally the device will get confused and reset its gate width to a semi-random value. Resending the gate width causes it to pick up the correct value again. This problem is mitigated in the driver by having a state machine which keeps the gate width and gate width readback in sync.

### Set commands are ignored

Sometimes the chopper crate simply ignores a setpoint which was sent. Unfortunately the crate does not respond to a set command so we can't tell if there was a comms error. This problem is mitigated in the driver by having state machines which keep the setpoints and their readbacks in sync for gate width, phase delay and chopper speed.

Additionally, the chopper speed is now put under run control as part of Merlin's `set_ei` script to make it more obvious if the chopper speed isn't in the expected range.

### 600Hz issue [Specific to Merlin]

At 600Hz, the chopper exhibits strange behaviour:
- If the speed setpoint is already 600Hz and a speed setpoint of 600Hz is resent, the chopper gets confused. The phase delay will appear to be zero forever. To get out of this state, need to send a different setpoint, wait for the actual device speed to drop (e.g. to 599Hz), and then 600Hz can be set successfully. This problem is mitigated in the driver by not sending a speed setpoint which is equal to the current speed setpoint readback.
- If the device is at 600Hz and already spinning, sending the "switch drive on and run" command causes the same bug as above. This problem is mitigated in the driver by disallowing the "switch drive on and run" command from being sent if the chopper speed is >595Hz and the setpoint readback is 600Hz and the drive generator is already on.

For more details, see [#2741](https://github.com/ISISComputingGroup/IBEX/issues/2741)

# Chopper won't phase correctly / delay is fluctuating wildly

### Synchrotron off

The phase delay of the chopper is a delay between the synchrotron pulse and the phase of the chopper. If the synchrotron is not running these numbers will be essentially random - this is nothing to worry about.

# Drive turns off unexpectedly

There are a variety of hardware & software conditions that can cause the chopper to spin down.

### Hardware / firmware conditions
Firstly, check in the "advanced" tab of the OPI - any of the following will cause the device to spin down:
- Interlock open (the scientists know how to reset this)
  * Note, the interlock only has to report "open" for a moment for the chopper to spin down. If the vacuum gauge is faulty, it may trip the interlock momentarily, which will cause the chopper to spin down but when subsequently looking at the OPI the interlock will appear OK. If this is the case then contact the chopper group as this is a hardware fault and is not something we can compensate for in software.
- Electronics or motor temperatures too hot (not sure where the firmware limit is - may be 50C according to manual but this is not clear) 
- A few other (less common) conditions indicated by red interlock LEDs on the OPI

### Software conditions
There are (equipment) safety checks in the IOC which will cause the IOC to request a spin down:
- If the electronics temperatures or motor temperatures go above 45 Celsius. 
  * **Electronics overheats occur somewhat frequently on Merlin, especially during hot weather.**
  * Need to wait for create to cool sufficiently and then spin the chopper back up as normal.
  * Instrument scientists aware of this and know how to reset it.
- If the auto zero voltages are out of range (absolute value higher than 3 volts)
- If the actual chopper speed is above 606Hz
- If the magnetic bearing is off while the chopper is at speed

# Crate does not respond / Crate responds infrequently

### VISA vs Asyn serial [Specific to Maps]
An issue was seen when first commissioning the MAPS fermi under EPICS. Symptoms were very odd:
- Cannot communicate using VISA nor Asyn under EPICS
- If chopper crate and instrument PC are power cycled, may need to run labview driver once before epics can talk. We are still not sure why this is.
- If EPICS+Visa is subsequently run, it will upset the comms and will need to run the labview to "clear" the error

### Shortened status command [Specific to Maps]
On MAPS, the crate's communications layer can fail, causing the device to ignore the standard polling command (`#0000000$`). To recover from this state, send the shortened command `0$` repeatedly until you get a response. The IOC should automatically do this whenever it detects no response to the standard command.

# Chopper refuses to spin up

### IOC command logic

There is logic in the IOC to prevent sending commands which would put the chopper into a disallowed state. For example, it is not permitted to send "switch drive on and run" if the magnetic bearings are off. Check the IOC log - there should be entries saying either "...sending command to device..." or "...refusing to send command to device...".

# Chopper veto stuck on

### Veto cable not properly plugged in

Ask DAE experts to unplug and re-plug in the veto cable.
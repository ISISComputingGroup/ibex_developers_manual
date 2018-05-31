# FZJ fermi chopper, as used on MERLIN

This device has a relatively complex IOC due to some communication issues we have had with the chopper. The following things are non-standard:
- Custom checksum algorithm in stream device. This is specific to this fermi chopper.
- `aSub` record to parse a response string from the hardware.
- `aSub` record to decide how to send the speed setpoint to the device
- `aSub` record to decide whether a given command is allowed to be sent
- `SNL` state machine to ensure that setpoints and their readbacks stay in sync (for both gate width and phase delay)
- There is logic in the DB records to prevent sending a speed setpoint that is equal to the current speed setpoint readback.

# 600Hz issue

At 600Hz, the chopper exhibits strange behaviour:
- If the speed setpoint is already 600Hz and a speed setpoint of 600Hz is resent, the chopper gets confused. The phase delay will appear to be zero forever. To get out of this state, need to send a different setpoint, wait for the actual device speed to drop (e.g. to 599Hz), and then 600Hz can be set successfully. This problem is mitigated in the driver by not sending a speed setpoint which is equal to the current speed setpoint readback.
- If the device is at 600Hz and already spinning, sending the "switch drive on and run" command causes the same bug as above. This problem is mitigated in the driver by disallowing the "switch drive on and run" command from being sent if the chopper speed is >595Hz and the setpoint readback is 600Hz and the drive generator is already on.

For more details, see [#2741](https://github.com/ISISComputingGroup/IBEX/issues/2741)

# Delay is wrong

The delay setpoint can be wrong if the high byte and low byte of the setpoint are received in the wrong order. The observed behaviour in this state is that the setpoint readback will appear to be correct, but the actual delay will home in on a different (incorrect) value. Resending the delay setpoint in the correct order fixes this state.

This problem is mitigated in the driver by having a state machine which keeps the actual delay and the delay setpoint in sync.

For more details, see [#2628](https://github.com/ISISComputingGroup/IBEX/issues/2628)

# Gate width setpoint readback are wrong

Occasionally the device will get confused and reset its gate width to a semi-random value. Resending the gate width causes it to pick up the correct value again.

This problem is mitigated in the driver by having a state machine which keeps the gate width and gate width readback in sync.

# Drive turns off unexpectedly

There are safety checks in the IOC. 
- If the electronics temperatures or motor temperatures go above 45 Celsius.
- If the auto zero voltages are out of range
- If the actual chopper speed is above 606Hz
- If the magnetic bearing is off while the chopper is at speed
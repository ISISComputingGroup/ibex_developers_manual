The Keithley 2290 is a high-voltage power supply.

The Model 2290-10 model that we have outputs up to 10kV with a maximum output current of 1mA.
(NB, the user manual - incorrectly - says the maximum current is 1uA.)

There is also a 2290-5 model which outputs up to 5kV.

The output voltage is programmable.
Other programmable parameters include voltage limit, current limit and trip current.

The unit is remotely controllable by means of a GPIB or RS-232 port.
There is also an analog input.

### Setting up the Device
The IOC works with a MOXA connected to the RS-232 port.

Plug the device into the mains, and into a MOXA via its RS-232 port on the back. 

Pressing the power button (lower right on the front panel) should make it turn on and beep.

The 'High voltage' switch (lower left on the front panel) is a 3-position switch.
To enable remote computer control, the switch needs to be in the middle position.
The upper 'ON' position enables output under local control only.
The lower 'OFF/RESET' position disables output.

### Confirming communication
Test that you can now talk to it by connecting to it via PuTTY or something similar.
Send `*IDN?`, you get the device name back.

### Probable errors
- If the 'High voltage' switch is not in the middle position, it will be possible to communicate with the unit, but any attempt to turn the HV on will result in an 'Execution error'. This is treated as an alarm condition by the IOC.
  Set the switch to the correct position, acknowledge the alarm and turn the HV on again.
- If the voltage setpoint is set to greater that the voltage limit, this will also result in an 'Execution error'.
- If the set voltage or current limits or trips are exceeded, this will be treated as an alarm condition by the IOC.
  Correct the cause of overload and acknowledge the alarm.
- If the external interlock is tripped, this will be treated as an alarm condition by the IOC.
  Correct the cause of the interlock and acknowledge the alarm.

### Testing with hardware
- Set the voltage setpoint, readback voltage should change to match. 'Stable' is likely to be off for some seconds.
- With a resistive load fitted, set the 'Current limit' to less than the measured value. This causes the readback voltage to drop so that the measured current is at the set limit. This will cause the 'Current limited' alarm to be set to 'MINOR'.
- Restore the 'Current limit' to more than the load current at the set voltage. The readback voltage should be at the setpoint again, and the alarm will clear.
- Remove the external interlock connector. This causes the output to trip and sets the 'Interlock tripped' alarm to 'MAJOR'.
- Replace the external interlock connector. The output remains tripped until the alarm is acknowledged. Operation then returns to normal. 
- 'Trip reset mode' is in the 'MAN' position:
  - Set the 'Current trip' to less than the load current. This causes the output to trip and sets the 'Current tripped' alarm to 'MAJOR'.
  - Set the 'Current trip' to greater than the load current. The output remains tripped until the alarm is acknowledged. The operation returns to normal.
- 'Trip reset mode' is in the 'AUTO' position:
  - Set the 'Current trip' to less than the load current. This causes the output to trip and sets the 'Current tripped' alarm to 'MAJOR'. However, the auto trip reset re-enables the output after some seconds (resulting in another trip).
  - Set the 'Current trip' to greater than the load current. The trip / trip cycling stops and operation returns to normal. The alarm will still need to be acknowledged.


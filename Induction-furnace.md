# Induction furnace

Device is being developed by Jakob Ahlburg at Aarhus university.

Internally it uses several pieces of hardware - a Julabo, a power supply etc but we only talk to an arduino controller (via serial). The arduino controller contains the PID controller and all logic that is needed to drive the device at the hardware level.

Serial command set is on manuals shared drive.

# Protocol

The device supports two serial protocols:
- One via the Arduino USB port at 115200 baud. This gives extra debug information but as it is USB we can't use it with a moxa.
- One via an additional external RS232 connection at 9600 baud. This is the connection which the IOC uses. Note that there are some differences in the protocols, so it is not possible to swap the IBEX driver onto the other connection without modifying the protocol file. Notably, the USB connection will give unsolicited messages containing debug information. We should not need to use this in general to control the device.

# Hardware notes

- If the device is powered off, it will reply with (semi-consistent) junk on the serial line.
- The start/stop buttons are just shortcuts for setting the PSU fan, power supply output, oscillation on or off.
- Usually running an experiment follows the following workflow:
  * Input a setpoint
  * Start furnace
  * [Change setpoints as required]
  * Stop furnace
  * Most parameters on the "advanced" screen do not need to be changed for most experiments.


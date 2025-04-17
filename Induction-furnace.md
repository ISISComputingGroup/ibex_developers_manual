# Induction furnace

Device is being developed by Jakob Ahlburg at Aarhus university.

Internally it uses several pieces of hardware - a Julabo, a power supply etc but we only talk to an arduino controller (via serial). The arduino controller contains the PID controller and all logic that is needed to drive the device at the hardware level.

Serial command set is on manuals shared drive.

# Blocks

This furnace can change temperature **extremely** quickly (e.g. 30seconds to ramp from room temperature to ~800C ). When setting up blocks to log temperature, ensure that it is set to "monitor with deadband" rather than "periodic scan for change", otherwise the heating curve may be missed in the data file and result in confusing output.

The temperature stability of the furnace is approximately 0.1 - 1.0C depending on temperature and sample. This can be used as a deadband (check with the user what accuracy is required in log files).

Two temperatures are measured, users will probably want to log both:
- Furnace temperature (thermocouple 1): This is what the PID controller controls on.
- Sample temperature (thermocouple 2): This is a separate thermocouple attached to the sample. It may read several hundred degrees less than the furnace temperature when the furnace is in operation.

# Protocol

The device supports two serial protocols:
- One via the Arduino USB port at 115200 baud. This gives extra debug information but as it is USB we can't use it with a moxa.
- One via an additional external RS232 connection at 9600 baud. This is the connection which the IOC uses. 

Note: there are some differences in the protocols, so it is not possible to swap the IBEX driver onto the USB connection without modifying the protocol file. Notably, the USB connection will give unsolicited messages containing debug information. We should not need to use the USB connection to control the device.

# Arduino code

We have been given a (potentially out of date) version of the arduino code, which is on the share. This can be used as a reference point if needed, but we should not in general need to use it or modify it in any way.

# Hardware notes

- If the device is powered off, it will reply with (semi-consistent) junk on the serial line.
- The start/stop buttons are just shortcuts for setting the PSU fan, power supply output, oscillation on or off.
- Usually running an experiment follows the following workflow:
  * Input a setpoint
  * Start furnace (this will set up several of the parameters on the "advanced" screen automatically - this is done in the hardware)
  * [Change setpoints as required]
  * Stop furnace
  * Most parameters on the "advanced" screen do not need to be changed except by expert users

# Temperature limits

The furnace can reach very high temperatures, however depending on the melting temperature of the sample holder, the safe maximum temperature varies:
| Material | Max T (C) |
| Aluminium | 500 |
| Steel | 1000 |
| Graphite | 1600 |
| Quartz | 1500 |
| Single crystal sapphire | 1600 |

Where "safe" refers to the sample holder not melting (it has been confirmed that this is not a personnel safety risk, merely an inconvenient clean-up if it does melt). **These limits are now enforced by the furnace controller, so the IOC merely needs to set the appropriate sample holder material.**



# Transtechnik Power Supply

The Transtechnik power supply is a modular system being used on RIKEN for cross-field magnets. Similar models are also used on the ISIS Accelerator.

Each power supply module provides 100A typically - so for a rack containing a controller and 5 power supply modules, this indicates a 500A supply. Max voltage is 125V.

## Macros/configuration

| Macro | Meaning |
| --- | --- |
| `PS_ADDR` | The address of the power supply. Note that addressing "all" power supplies using `000` does *NOT* work for these power supplies. To determine the address of the power supply, navigate through the menus on the front of the physical power supply until you find an option for local mode, then navigate to "PSU address" and check it, then put the power supply back into remote. |
| `VOLT_FULLSCALE` | The maximum voltage that this power supply can deliver, in V. If unknown, ask scientists for advice. |
| `CURR_FULLSCALE` | The maximum current that this power supply can deliver, in A. Each power supply module delivers 100A, so a rack with 5 modules plus a controller is a 500A supply. If unknown, ask scientists for advice. |

Known settings are:

| Instrument | Location | `PS_ADDR` | `VOLT_FULLSCALE` | `CURR_FULLSCALE` | Serial comms settings |
| --- | --- | --- | --- | --- | --- |
| Test (for RIKEN) | R6 DCLAB | `005` | `125` | `500` | **RS422** 9600/8/None/1, 9-way cable, no null modem |
| RIKEN XFD1 | Mezzanine | `001` | `125` | `100` | **RS422** 9600/8/None/1, 9-way cable, no null modem |
| RIKEN XFD2 | Mezzanine | `002` | `125` | `100` | **RS422** 9600/8/None/1, 9-way cable, no null modem |
| RIKEN XFD3 | Mezzanine | `003` | `125` | `100` | **RS422** 9600/8/None/1, 9-way cable, no null modem |


## Driver logic

The IBEX driver contains a state machine which waits for the power supply to complete certain actions before proceeding. Physically this corresponds to waiting for an inrush current.

In particular, the following commands are known to be problematic:
- `N` -> Turns power supply on, no response. Note that a wait of 20s is enforced after this command is sent before setting any currents etc (due to PSU inrush current). In particular, setting new current within 20s of this command may be ignored.
- `RS` -> Note that a wait of 20s is enforced after this command is sent before turning supply on. In particular, turning on the supply within 20s may be ignored.

The state machine in IBEX enforces appropriate delays between the reset, power, and set current commands.

## Troubleshooting

### No interlocks are displayed but power supply can't be turned on

On this power supply, the interlock lights will go off once the interlock is *physically* cleared, but the power supply will still be in a tripped state until a reset is sent. There is no easy way to display this in IBEX. Solution: send a reset, wait for the enforced delay time, and then try to turn on again.

### No Communication with device

- Check address and serial port settings above
- Check that the appropriate port(s) on the MOXA NPort are set to **RS422** mode.  This is done via its configuration webpage. (Most likely to occur after replacing a MOXA NPort unit).
# TPG26x

The TPG26x is shorthand for multiple devices with the same interface. They all measure pressure based on sensors that are plugged in. See https://www.pfeiffer-vacuum.com/en/products/measurement/activeline/controllers/?detailPdoId=5724 manual is also in `C:\LabVIEW Modules\Drivers\Pfeiffer TPG26x\Documentation`.

## Simulator

Simulator PVs are:

| Name | Description |
| ---  | ---  |
| `SIM `           | 1 to switch simulation on, 0 off |
| `SIM:UNITS `     | 1-3 for the different units |
| `SIM:X:PRESSURE` | To set the pressure readback (X is 1 or 2) |
| `SIM:X:ERROR `   | To set the error, 0 - 6; 0 is no error (X is 1 or 2) |

## Emulator

Set up the port with in the st.cmd and run the simulator. There are several backdoor command to set the internal state, telnet to the emulator and then issue:

| Command | Argument | Description |
| ---     | ---       | ---  |
| `emulator:set:pressureX` | <pressure> | Set the pressure of sensor X (X 1 or 2) |
| `emulator:set:errorX` | <error 0-6> | Set the error of sensor X (X 1 or 2) |
| `emulator:set:units` | <error 1-3> | Set the units |


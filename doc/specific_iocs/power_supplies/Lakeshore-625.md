# Lakeshore 625
### Description
Lakeshore 625 is a superconducting magnet power supply used for small to medium sized superconducting magnets.
The 625 has a compliance voltage range of ±5 V (nominal, both source and sink) and a current range of ±60 A.

### Setting up the Device
- Set the baud rate on the device to 9600. Plug in the device over serial and note the COM port. Add the IOC (LKSH625) to your configuration on IBEX and edit it to set the COM port and the baud rate if not set to 9600.

### Testing with hardware
- With a resistive load fitted, set the current setpoint, allow for the device to ramp up to this value.

### Quirks
- Difference between compliance voltage and voltage limit. Compliance voltage is akin to a safety/soft limit whereby its the highest voltage the device can be set to. Voltage limit is a hard/hardware limit whereby it defines the actual limit of what the device will output.
- Ramp rates and segmented ramp rates. The standard ramp rate will do as expected, change to the new setpoint at the supplied rate. Segmented ramp rates allow for a piecewise function of ramp change- e.g., you may tell the device that under ramp segment 1, from 0-20A it must ramp at 1A/s, and at segment 2 from 20-40A it must ramp at 2A/s.
- Persistent Switch Heater must first be turned on via PSH:ENABLE (Param) and then can be controlled via STAT:PSH (Mode).

### Operation
Items that can be set include:
- Output Field (0.0000 - ±60.1000E+00 T)
- Output Current (0.0000 - ±60.1000 A)
- Output Compliance Voltage (0.1000 - 5.0000 V)
- Trigger Output Current (0.0000 - ±60.0000 A)
- Enable segmented ramp rate (Enabled/Disabled)
- Ramp Segments (1-5) (Current and Ramp Rate)
- Output Current Ramp Rate (0.0001 - 99.999 A/s)
- Computed Magnetic Field Parameters (0.0010 - 1.0000 T/A)
- Current, Voltage (compliance and safety) and Ramp Rate Limits 
- Persistent Switch Heater Mode (Off/On/Overide)
- Persistent Switch Heater Parameters (Enabled/Disabled, 10 - 125 mA and 5 - 100 s)
- Quench Parameters (0.0100 - 10.000 A/s)

### Other
The IOC to facilitate use of this was implemented under https://github.com/ISISComputingGroup/IBEX/issues/8782.

Baud = 9600

Data = 7

Parity = odd

Stop = 1

The manual can be found at `file://isis/shares/ISIS_Experiment_Controls/Manuals/Lakeshore_superconducting_magnet_power_supply/lakeshore625_manual.pdf`.
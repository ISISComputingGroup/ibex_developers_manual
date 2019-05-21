> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > WPI Aladdin Syringe Pump

# Documentation

Documentation is available for the pump at `C:\LabVIEW Modules\Drivers\WPI Aladdin-1000 Syringe Pump`

# Connection Details
  
|      RS-232C Specifications  |   |
|---------------|------------------|
|     Baud rate | 19200, 9600, 2400, 1200, or 300 Baud       |
|     Start bits| 1 bit            |
|     Stop bits | 1 bit            |
|        Parity | None             |
|   Data length | 8 bit            |
|  Flow control | Hardware         |

Command Syntax:
 - Communication command is terminated with <CR>.
 - Communication return starts with <STX> and is terminated with <ETX>. 

Command float formatting:

The device requires strict formatting on its floats. The output value must fit 5 characters and be within the range `9999. to .9999`.

# Specifications

### Networked Pumps

Multiple pumps can be daisy chained together and controlled via a single IOC. Each pump has an address which can be set using the `ID:SP` record. By default (and in a single pump configuration) this is `00`.

### Volume Units

The device has it's own logic for setting the units of volume to be pumped `VOLUME:UNITS` based on the diameter of the syringe installed in the pump `DIAMETER`. In testing it was found that: Diameter <= 14.00mm - uL, Diameter > 14.00mm = mL. A small warning about this has been placed on the OPI to inform users.

### Rate Units

The units for the rate can be selected but will only be set when setting the `RATE:SP`. You can resend the same set point to set newly selected rate units.


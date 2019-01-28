> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > [JASCO HPLC Pump](JASCO-HPLC-Pump)

# Documentation

Documentation is available for the pump at `\\ISIS\shares\ISIS_Experimental_Controls\Manuals\Jasco__PU-4180 HPLC Pump`

# Connection Details
  
|      RS-232C Specifications  |   |
|---------------|------------------|
|     Baud rate | 4800 Baud        |
|     Stop bits | 2 bit            |
|        Parity | None             |
|   Data length | 8 bit            |
|  Flow control | Xon/Xoff control |

Notes:
 - Communication command is terminated with CR.
 - Communication return is terminated with CR and LF. 

# Pump Control

The device has the ability to control a number of parameters for a pump:

- Flowrate (in mL/min)
- Pressure Maximum and Minimum (in kg/cm^2)
-- Setting these values will result in an error output and stop the pump if exceeded during a executed program.

NB: The devices display screen does not show current pump status information when in operation.




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

- Flowrate (in mL/min): `FLOWRATE:SP`
- Pressure Maximum and Minimum (in kg/cm^2): `PRSSURE:MAX:SP`, `PRESSURE:MIN:SP`
-- Setting these values will result in an error output and stop the pump if exceeded during a executed program.
- Composition components (A, B, and, C in %): `COMP:{}:SP`.

The user can then start the pump by using the `START:SP` record. The pump can be stopped using the `STOP:SP`

The user can also select a timed run for either a set time or volume. The user must first set a time `TIME:RUN:SP` (in seconds) or volume `TIME:VOL:SP` (in mL). Then a pump can begin by using the `TIMED:SP` record.

NB: The devices display screen does not show current pump status information when in operation.

# Troubleshooting

It has been observed that the pump can be in some state where the components will not correctly change when the `set_component` command is sent. This is thought to occur when the device has a local manual component mode set on the device. In testing one way this was resolved was by manually sending the `8 pump set` command, which corresponds to reset and rerun of the program. You can then stop the pump and it should have cleared this state and you can use the IOC as per usual. 
# Thurlby TTI EX355P

## Documentation

Documentation is available for the pump at `"\\ISIS\shares\ISIS_Experiment_Controls\Manuals\Thurlby-Thandar-TTIEX355P"`

## Connection Details
  
|      RS-232C Specifications  |   |
|---------------|------------------|
|     Baud rate | 9600 Baud        |
|     Stop bits | 1 bit            |
|        Parity | None             |
|   Data length | 2 bit            |
|  Flow control | Xon/Xoff control |

**Notes:**
*    Communication command is terminated with CR and LF.
*    Communication return is terminated with CR. 

## Operation

The Thurlby Thandar TTI PLP power supply series is a simple programmable bench power supply.

Items that can be set include :

* Output voltage.
* Output current.
* Output On/Off.
* Voltage limit.
* Current limit.

The device operates in two modes; Constant Current (CI) or Constant Voltage (CV). By default, and on reset, the device is in CV mode. In CV mode the current set point acts as a current limit whilst the current output is 0. CI mode is activated when the load resistance and voltage combination would mean that a current would flow above the current set point. In CI mode, the voltage set point acts as a voltage limit and the voltage output is dynamically calculated. In this mode, there is an active current output. 

## Current and Voltage limits

The IOC has macros for the voltage limits (`MAX_VOLT`, `MIN_VOLT`) and current limits (`MAX_CURR`, `MIN_CURR`). These can be changed so that in the event of a different model of PSU, alternative limits are supported. The TTI355 supports `I = 0.01, 5.0` and `V = 0.0, 35.0`.

## Trouble shooting 

The device has an error state which indicates when the device has received a command value outside the instruments limits. 
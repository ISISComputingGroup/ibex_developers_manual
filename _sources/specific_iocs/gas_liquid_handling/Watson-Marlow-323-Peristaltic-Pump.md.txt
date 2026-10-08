# Watson-Marlow 323 Peristaltic Pump

## Documentation

Documentation is available for the pump at `\\ISIS\shares\ISIS_Experiment_Controls\Manuals\Watson-Marlow__323`

## Connection Details
  
|      RS-232 Settings         |   |
|---------------|------------------|
|     Baud rate | 9600 Baud        |
|     Stop bits | 2 bit            |
|        Parity | None             |
|   Data length | 8 bit            |
|  Flow control | None             |

Notes:
 - Communication command is terminated with CR.
 - Communication return is terminated with CR. 

## Pump Control

The device has the ability to control a number of parameters for a pump:

- Rotation speed (in rpm with minimum of 3 and maximum of 400): `SPEED`
- Direction (Clockwise or Anti-Clockwise): `DIRECTION`
- Status (Running or Stopped): `STATUS`


The user can also start the pump by using the `START:SP` record. The pump can be stopped using the `STOP:SP` record.

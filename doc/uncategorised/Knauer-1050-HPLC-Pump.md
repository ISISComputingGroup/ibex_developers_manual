> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > Knauer 1050 HPLC Pump

# Documentation

Documentation is available for the pump at `\\ISIS\Shares\ISIS_Experiment_Controls\Manuals\knauer 1050 HPLC`

# Connection Details
  
|      RS-232C Specifications  |   |
|---------------|------------------|
|     Baud rate | 115200; 38400, 19200, 9600 Baud       |
|     Stop bits | 1 bit            |
|        Parity | None             |
|   Data length | 8 bit            |
|  Flow control | Hardware |

Notes:
 - Communication command is terminated with CR.
 - Communication return is terminated with CR. 


# Specifications

### Pump heads

The 1050 was designed to provide exceptionally precise and reliable solvent delivery for a wide range of HPLC applications. The pump can be fitted with either a 10 or 50 ml/min pump heads that will be RFID recognised for auto set-up. Depending on the head used there are maximum flow rates, pressures and accuracies:

|                        | 10 ml/min                                 | 50 ml/min                               |
|------------------------|-------------------------------------------|-----------------------------------------|
| Flow rate range        | 0.001 to 9.000                            | 0.01 to 50.00 ml/min                    |
| Max. delivery pressure | 400 bar (40 MPa, 5 800 psi) < 10 ml/min   | 200 bar (20 MPa, 2 900 psi) < 25 ml/min |
|                        |                                           | 150 bar (15 MPa, 2 200 psi) < 50 ml/min |
| Flow rate accuracy     | deviation ≤ 1 %                           | deviation ≤ 1 %                         |
| Flow rate precision    | RSD ≤ 0.1 %                               | RSD ≤ 0.3 %                             |

### Remote/Local modes

The pump starts in `LOCAL` mode, and when in this state you are able to access the devices front panel and make changes as well as remotely poll the device status. The device mode can be toggled into `REMOTE` mode using the `MODE:SP` record, and this will result in the device accepting remote instructions but it will lock the devices front panel.

### Gradient Controls

The device can pump with a composition of 4 components, A, B, C and, D. These gradients can be set using the `COMP:X:SP` (replacing X with the desired component). However the sum of these gradients must be equal to 100%. If not correctly set then you will be unable to start the pump until this is resolved.

### Pressure Limits

The high and low pressure limits can be set using the `PRESSURE:MIN:SP` and `PRESSURE:MAX:SP` records. If a limit is reached during a pump then the pump will stop.

### Flow Rate/Min

The devices desired flow rate per minute can be set using the `FLOWRATE:SP` record.

### Pump Control

The user can set the pump to run for either a set time/volume, or a continuous pump. These can be set using `STOP:SP`, `START:SP`, and, `TIMED:SP`. 

To specify a run time the `TIME:SP` record can be used, and to set a desired volume the `VOL:SP` record can be used.

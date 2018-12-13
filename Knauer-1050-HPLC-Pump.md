> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > Knauer 1050 HPLC Pump

# Documentation

Documentation is available for the pump at `\\ISIS\Shares\ISIS_Experimental_Controls\Manuals\knauer 1050 HPLC`

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

The pump starts in `Local` mode, and when in this state you are able to access the devices front panel and make changes as well as remotely poll the device status. The device can be set into `Remote` mode using the `REMOTE_MODE:SP` record, and this will result in the device accepting remote instructions but it will lock the devices front panel. `Local` mode can be restored with the `LOCAL_MODE:SP` record. 

### Gradient Controls

The device can (if the correct pump head is installed) make use of 4 channels (A, B, C and D). These gradients can be set using the `CON:X:SP` (replacing X with the desired channel). However the sum of these gradients must be equal to 100%. If not correctly set then you will be unable to start the pump until this is resolved.

### Pressure Limits

The high and low pressure limits can be set using the `PRESS:LIM:LOW:SP` and `PRESS:LIM:HIGH:SP` records. If a limit is reached during a ramp then the pump will stop.

### Flow Rate/Min

The devices desired flow rate per minute can be set using the `FLOW:SP` record.

### Ramp Control

If the device is set to remote mode and the gradients are correctly set, then a ramp can begin. To start a ramp the `PUMP:START:SP` can be used to start a ramp and `PUMP:STOP:SP` will stop the ramp. It should be noted that if a run has be issued via the devices front panel while in local mode, the remote command for stop can still be issued.

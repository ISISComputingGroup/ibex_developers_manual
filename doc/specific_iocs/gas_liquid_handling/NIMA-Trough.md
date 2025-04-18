# NIMA Trough

The NIMA Trough is used to fabricate thin films of material. 

## Specifications

The implementation for IBEX uses an lvDCOM solution. The IOC connects to a VI interface to process set points and read back values. When the IOC is started, it attempts to boot the Labview VI. In general use, the VI will be open with its graphing view along side the IBEX client.

## Running the IOC

The NIMA trough IOC is not compatible with versions of the VI that are older than 2019-02-15. Ensure you update and VI drivers you have locally from source safe. Updated drivers should be available on DEMO.

## Simulation

When not connected to a physical device the NIMA Trough VI has an example data file (graph plot) and will respond to record processing. This allows you to observe some of the state and field behaviour. For example, you can process opening the barriers, and the VI will indicate the barriers are opening.

## Physical Setup

The Nima trough is a large metal container in which is a tray with a motor and sensor connected. This is connected to a control box (beige about 30cm x 15cm x 5cm). The control box has two LEDs on it labelled V1 and V2 they should both be lit for correct operation. The LED are

- V1: unknown (maybe power or connection to the motors)
- V2: connection to the serial port. If this is unlit there is a problem with the serial communication either at the software level or hardware level. During recent diagnosis the VI appeared to claim it could stop the barrier (but not start the barrier) and there were lots of OKs in the message box but the cable was broken so it was not communicating; i.e. be wary that the VI is claiming it can communicate.

## Troubleshooting

### Unable to start a run

The NIMA Trough GUI can perform 3 runs, and each is individually saved to a file. Once these 3 files have been written too, you are unable to begin further runs. A pop-up on the NIMA Trough warns you that files must be deleted in order to continue recording runs. This is shown below with the 3 runs tab highlighted in red:

From the IOC perspective though you will simply be unable to begin a run, and there is no warning that the number of runs has been reached, but the pop-up on the NIMA Trough interface should be clear. If you are unable to begin runs from the IOC it's worth checking the NIMA Trough GUI to ensure there are free files available to write to.

### Units for Area

By default on the NIMA Trough the area is in cm^2, however this can be changed. Since we use an lvDCOM wrapper around an interface to the main NIMA Trough GUI, we are unable to access the unit information. The EGU of the area record is cm^2 by default, so if there are issues with it having unexpected values it's worth checking to see if the NIMA Trough GUI has had it's units altered. We were informed that it is expected that cm^2 will be used exclusively.


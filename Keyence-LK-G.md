> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Sensors](Sensors)

The Keyence LK-G Series are modular High-speed, High-accuracy
CCD Laser Displacement Sensor devices.

## Mode control

This device has two modes: Communication (Set-up) and Measure. Fields on the device, such as the head measurement mode or measurement offsets can only be set when the device is in set-up mode. Measurements can only be made when the device is in measure mode.

To keep the process of scripting and user control simple, the device is put into measurement mode and will switch to communication mode (at the protocol level) when a set point is changed. The `MODE` record can be interrogated to determine the current operating mode for debugging. 

To stop the device from constantly switching modes, the scan rate for records that need Measure mode can be changed ([#7376](https://github.com/ISISComputingGroup/IBEX/issues/7376)). The default scan rate for these records is `5 second` and can be set to `Passive`. If new records are needed that use Measure mode, they can be added to the `seq` record `SCAN` so their scan rate can be controlled as well.

# On IOC Start

When the IOC device starts the device will be placed into Measurement mode.

# Documentation

Documentation is available for the pump at `\\ISIS\Shares\ISIS_Experiment_Controls\Manuals\Keyence__LK-G`

# Connection Details

|      RS-232C Specifications  |   |
|---------------|------------------|
|     Baud rate | 115200; 57600, 38400, 19200, 9600 Baud       |
|     Stop bits | 1 bit            |
|        Parity | None             |
|   Data length | 8 bit            |
|  Flow control | None        |
| Data delimiter | CR |

## Communications

Serial settings (baud rate, parity) can, if required, be changed via the manufacturer's software. Ensure the IOC matches the physical device. Device communicates using a straightforward ASCII protocol with carriage-return terminators (`\r`).

## IOC

The IOC is very straightforward, incorporating simple get and put records.
Communication is serial and utilises the EPICS StreamDevice protocol. A summary of the commands is given below:

|Command | Syntax | Description |
| ------- | ------ | ----------- |
| Get ID | *idn? | Returns the model number and firmware version |
| Set Position | pos=n | Moves the wheel to filter position n |
| Get Position | pos?  | Position Query |
| Set Position Count | pcount=n | Sets the wheel type where n is 6 or 12 |
| Get Position Count | pcount? | Returns the wheel type |
| Set Trigger Mode | trig=0 | Sets the external trigger to the input mode |
|                  | trig=1 | Sets the external trigger to the output mode |
| Get Trigger Mode | trig?  | Returns the trigger mode |
| Set Speed Mode | speed=0 | Sets the move profile to slow speed |
|                | speed=1 | Sets the move profile to high speed |
| Get Speed Mode | speed? | Returns the move profile mode |
| Set Sensor Mode | sensors=0 | Sensors turn off when wheel is idle to eliminate stray light |
|                 | sensors=1 | Sensors remain active |
| Get Sensor Mode | sensors? | Returns the sensor mode |
| Set Baud Rate | baud=0 | Sets the baud rate to 9600 |
|               | baud=1 | Sets the baud rate to 115200 |
| Get Baud Rate | baud? | Returns the baud rate where 0 = 9600 and 1 = 115200 |
| Save Settings | save | This will save all the settings as default on power up |

Notes:
- Default framing is 115.2 kbaud, 8 data bits, 1 stop bit, no parity, no flow control.

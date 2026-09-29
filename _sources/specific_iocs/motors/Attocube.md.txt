# Attocube

_Not to be confused with the [SXD Attocube](SXD-Attocube)_

## The Controller

The Attocube ANC350 Piezo controller was supported in IBEX but is currently mothballed as it's not actively used on any beamlines. Code is of course in git, see [here](https://github.com/ISISComputingGroup/IBEX/issues/4488) for where it was mothballed. The controller can be communicated with over USB or over Ethernet. IBEX uses the Ethernet communications. 

### Enabling Ethernet

The controller does not come with Ethernet enabled as standard, it must be purchased separately (the hardware is there but the firmware needs it unlocked). Before a new Attocube is installed ensure in good time that the Ethernet control has been purchased. It will either be enabled at the factory or you will be provided a code to enable it. You can enter this code by connecting via USB and using the `daisy` software provided by Attocube on purchase of a controller. This software can also be used to set the IP address and subnet mask. Unfortunately the device uses a static IP, as such you will need to get an IP registered for the hall (talk to Chris about this). This software is in the usual place where we store manuals.

## The Driver
The driver was originally written by Observatory Sciences, but is now officially being maintained by us. It is quite an old style EPICS motor controller but is functional. It communicates with the device using is a relatively simple binary format, documented below:

### The Protocol
This is not meant to be an extensive documentation of the protocol, I merely understood enough to implement a [basic emulator](https://github.com/ISISComputingGroup/EPICS-DeviceEmulator/tree/master/lewis_emulators/attocube_anc350). Each packet sent between the device and IOC contains a header with the following information:

| Information | Type                      | Description |
|-------------|---------------------------|-------------|
| Length      | 4 byte integer, LSB first | The length of the rest of the packet **Not including these 4 bytes** |
| Opcode      | 4 byte integer, LSB first | The action that the driver wishes to perform 0 for set, 1 for get and 3 for ack |
| Address     | 4 byte integer, LSB first | The memory address to read or write to |
| Index       | 4 byte integer, LSB first | Normally the axis that you're reading/writing to |
| Correlation Number      | 4 byte integer, LSB first | Used to match up the response, the driver will increment this for each packet |

### Set

When a set is sent to the controller it will look like:

| Information | Type                      | Description |
|-------------|---------------------------|-------------|
| Header      | As above. | As above. |
| Data | Array of 4 byte integers, LSB first | The data to actually write. |

The response will just be a header with the acknowledgement opcode.

### Get

When a get is sent to the controller it will just be a header with the get opcode. The response will be:

| Information | Type                      | Description |
|-------------|---------------------------|-------------|
| Header      | As above. | As above. |
| Reason | 4 byte integer, LSB first | Whether the get was successful, 0 if all ok |
| Data | Array of 4 byte integers, LSB first | The data to read from the specified memory address. |

So an example of communications may be:

To controller: `10 00 00 00 01 00 00 00 15 04 00 00 02 00 00 00 8b 00 00 00`

Reply: `18 00 00 00 03 00 00 00 15 04 00 00 02 00 00 00 8b 00 00 00 00 00 00 00 ca 00 00 00`

Here the IOC is getting the value of memory address `0x0415` on axis 0, which is the position of the axis. It receives a value of 202 steps.

This protocol was reverse engineered from the description [here](https://github.com/ISISComputingGroup/EPICS-attocubeANC350/blob/master/anc350App/src/ucprotocol.h) which gives a lot more information.

## The Memory Addresses
The general protocol mostly just reads and writes to some memory address. There are too many addresses to list here, instead a good reference is at the end of the [supplied docs](https://github.com/ISISComputingGroup/EPICS-attocubeANC350/blob/master/docs/ANC350_Developers_Manual.pdf) or in the [code itself](https://github.com/ISISComputingGroup/EPICS-attocubeANC350/blob/master/anc350App/src/devAnc350.h).
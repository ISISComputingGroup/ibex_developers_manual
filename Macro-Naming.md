> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Macro naming

# Macro Naming Scheme

As well as the [macros used in PVs](PV-Naming#macros) there are other Macros that we should set as standard. When an IOC is acquired from another source they may use the same term for different items, we should probably do some fancy substitutions so that our macro setting locations (via the configurations editor in the GUI, or via globals.txt) remain consistent. These eventually take a format, which is easily seen in globals.txt, of IOC_0n__MACRO=value, where n is the indicator of which macro is under consideration. (Note, existing IOCs may not conform, and may need to be updated at some point.) 

Once a macro has been set consider whether it should be added into the configuration so the user can set it. To do this see the instructions in [IOC Finishing Touches](IOC-Finishing-Touches).

Where there are multiple instances of a device within an IOC (e.g. SDTEST, GENESYS) then a number should be added to the end of the macro to indicate which macro it is.

| Macro | Description | Default Value (for st.cmd) |
| --- | --- | --- |
| DEV_TYPE | The Device Type where one IOC handles multiple devices (e.g. the Danfysik PSU IOC) | Varies by device |
| PORT | The COM port to use | Do not set this to a default |
| HOST | The host name or IP address of the device, can include the port separated by a colon | Do not set this to a default | 
| ADDR | Secondary address information, e.g. on RS485 | Varies by device |
| BAUD | The Baud rate of a serial device | Varies by device |
| BITS | The number of bits in the serial interface | Varies by device |
| PARITY | The parity of the serial interface | Varies by device |
| STOP | The number of stop bits used by the serial interface | Varies by device |
| IEOS | The end of line signal for input within asyn | Varies by device |
| OEOS | The end of line signal for output within asyn | Varies by device |
| SOFTFLOWCNTL | Software (xon/xoff) flow control within asyn | Varies by device |
| HWFLOWCNTL | Hardware (crtscts) flow control within asyn | Varies by device |
| OEOS | The end of line signal for output within asyn | Varies by device |
| CALIB_PATH | The path to the folder containing calibration files for that IOC/function (e.g. resistance/temperature or current/magnetic field) | Varies by type of calibration |
| CALIB_FILE | The name of the specific file in that folder to use | |
| DEVSIM | Device should be simulated 1 - yes, 0 - no. (Provided by IBEX backend and can be set in the GUI) | 0 |
| IFDEVSIM | Set to ' ' if device is being simulated; otherwise '#' (Provided by IBEX backend) |  |
| IFNOTDEVSIM | Set to '#' if device is being simulated; otherwise ' ' (Provided by IBEX backend) |  |
| RECSIM | IOC should simulate at the record level 1 - yes, 0 - no. (Provided by IBEX backend and can be set in the GUI) | 0 |
| IFRECSIM | Set to ' ' if device is being record simulated; otherwise '#' (Provided by IBEX backend) |  |
| IFNOTRECSIM | Set to '#' if device is being record simulated; otherwise ' ' (Provided by IBEX backend) |  |
| DISABLE | Should communications be disabled 1 - yes, 0 - no. (Provided by IBEX backend and can be set in the GUI) | 0 |
| LVDCOM_HOST | The host of the LVDcom vi (see [Creating IOC wrapper VI](Creating-IOC-wrapper-VI)). | "" |
| LVDCOM_OPTIONS | LVDcom options for starting the vi (see [Creating IOC wrapper VI](Creating-IOC-wrapper-VI)). | 6 |
| LVDCOM_USER | LVDcom user; not to be added to `config.xml`. It can be set only through the local globals.txt (see [Creating IOC wrapper VI](Creating-IOC-wrapper-VI) for more). | "" |
| LVDCOM_PASS | LVDcom passphrase; not to be added to `config.xml`. It can be set only through the local globals.txt (see [Creating IOC wrapper VI](Creating-IOC-wrapper-VI) for more). | "" |

# Specific Macros that we might need to set

There are some macros that need to be set which have specific names, and do not fit into the convention which it might be good to know about easily for setting up an IBEX system. Or which might highlight things that should be changed to conform. The macros for SDTEST are not included as there are many of them to consider.

| IOC | Macro | Description | Suggested Values |
| --- | --- | --- | --- |
| global | SIMULATE | This can be used to check whether or not you are a simulated instrument | `1` to simulate, `0` for a live system|
| ISISDAE01 | DAEDCOM | This is whether ISISDAE uses DCOM to talk to isisicp, or loads ISISICP internally. | `1` is normal and recommended on instrument, `0` is if you do not want to run isisicp e.g. dcom problems on MUONFE |
| ISISDAE01 | DAEHOST | This is the IP address of the DAE host | `localhost` |
| GALIL_0n | GALILADDR | This is the IP address of the Galil | `None` when simulating |
| HVCAEN_0n | HVCAENIPn | This is the IP address for the CAEN | |
| FINS_0n | PLCIP | The IP address for the PLC | |
| TPG300_0n | TTY | The COM port for the TPG 300 (should be changed to conform) | |
| GALIL_0n | MTRCTRL | The motor controller number, e.g. it's 08 in :MOT:MTR0805 | |
| CONEXAGP_0n | MTRCTRL | The motor controller number, e.g. it's 08 in :MOT:MTR0805 | |
| SMC100_0n | MTRCTRL | The motor controller number, e.g. it's 08 in MOT:MTR0805 | |
| PIMOT_0n | MTRCTRL | The motor controller number, e.g. it's 08 in MOT:MTR0805 | |
| ECLAB_0n | IPADDR | IP Address of the device | |
| LKSH336_0n | IPADDR | IP Address of the device | |



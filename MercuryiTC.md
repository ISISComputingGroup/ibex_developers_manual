> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Temperature Controllers](Temperature-Controllers) > [Mecury iTC](MercuryiTC)

The Mercury iTC is a configurable temperature controller from oxford instruments ( [Manual](http://lmu.web.psi.ch/docu/manuals/bulk_manuals/OxfordInstruments/Dolly_Mark_II/Mercury_iTC_manual_Issue_05.pdf) ).

It contains various slots into each slot a variety of devices can be placed. For the purposes of the this document the mother board is treated as a slot too, it contains a temperature sensor and a heater.

Types of daughter boards are:
 * temperature sensor
 * Heater
 * Auxiliary board (general purpose and stepper motors)
 * Pressure sensor
 * Cryogen
 * GPIB board (communications)

In the future we may want to develop a full epics IOC for it and there is a possible Diamond IPC driver at  http://controls.diamond.ac.uk/downloads/support/OxInstCryojet/ currently there is an LvDCOM driver.

# Communications

The device should be talked to via serial at a baud rate of 57600. This is variable on the front panel, but **only while the device is in local mode.**

## Driver

Currently the driver only measures and sets the following:

### Temperature

#### Setup

To activate a card you must set the related IOC macro in globals.txt. The macro sets the final part of the front panel name. The front panels are called `Mercury - Front Panel <I> - Temp <N>.vi` where <I> is the Mercury index (also the IOC index) and <N> is the card index 1 for the first temperatue card, 2 for the second etc. The following macros set the <I> for the 4 possible IOC slot:

| Macro | Usual Value | IOC Name | 
| ----  | ----------- | -------- | 
| MERCURY_01__VI_TEMP_1 | 1 | %MYPVPREFIX%MERCURY_01:1 |
| MERCURY_01__VI_TEMP_2 | 2 | %MYPVPREFIX%MERCURY_01:2 |
| MERCURY_01__VI_TEMP_3 | 3 | %MYPVPREFIX%MERCURY_01:3 |
| MERCURY_01__VI_TEMP_4 |   | %MYPVPREFIX%MERCURY_01:4 |
| MERCURY_02__VI_TEMP_1 |   | %MYPVPREFIX%MERCURY_02:1 |
| etc                   |   |                          |

#### Important PVs

* `TEMP` Current temperature
* `TEMP:SP` Set point for temperature controller
* `TEMP:SP:RV` Read back of the set temperature point
* `NAME` Name associated with the card

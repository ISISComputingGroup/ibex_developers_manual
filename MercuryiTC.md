> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Temperature Controllers](Temperature-Controllers) > [Mercury iTC](MercuryiTC)

The Mercury iTC is a configurable temperature controller from oxford instruments ( [Manual](http://lmu.web.psi.ch/docu/manuals/bulk_manuals/OxfordInstruments/Dolly_Mark_II/Mercury_iTC_manual_Issue_05.pdf) ).

It contains various slots into each slot a variety of devices can be placed. For the purposes of this document the motherboard is treated as a slot too, it contains a temperature sensor and a heater.

Types of daughter boards are:
 * temperature sensor
 * Heater
 * Auxiliary board (general purpose and stepper motors)
 * Pressure sensor
 * Cryogen
 * GPIB board (communications)

In the future, we may want to develop a full epics IOC for it and there is a possible Diamond IPC driver at  http://controls.diamond.ac.uk/downloads/support/OxInstCryojet/ currently there is an LvDCOM driver.

# Communications

The device should be talked to via serial at a baud rate of 57600. This is variable on the front panel, but **only while the device is in local mode.**

The screens look like:

![Comms general](backend_system/IOCs/MercuryITc/comms1.jpg)
![Comms detailed](backend_system/IOCs/MercuryITc/comms2.jpg)

## Driver

Currently, the driver only measures and sets the following:

### Temperature

#### Setup

To activate a card you must set the related IOC macro. The macro sets the final part of the front panel name. The front panels are called `Mercury - Front Panel <I> - Temp <N>.vi` where <I> is the Mercury index (also the IOC index) and <N> is the card index 1 for the first temperatue card, 2 for the second etc. The following macros set the <I> for the 4 possible IOC slot:

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
* `TEMP:SP` Setpoint for temperature controller
* `TEMP:SP:RV` Read back of the set temperature point
* `NAME` Name associated with the card

### He Level

The helium level can be monitored by setting the macro VI_LEVEL_1 to point at the correct vi in a similar fashion to the temperature.

### Example

In this example the front panel on the Mercury look:

![front panel showing 6 areas](backend_system/IOCs/MercuryITc/front_panel.jpg)

This mercury has 3 temperature sensors, Sample_Rod, VTI_DB6 and PT2_DB7, the VTI has a heater attached to the second temperature. This means it needs:

- `VI_TEMP_1` set to 1, 
- `VI_TEMP_2` set to 2, 
- `VI_TEMP_3` set to 3, 

The temperature controls are on the 1st and 2nd temperature and so on the first and second tab on the mercury device screen. NB the device screen also needs these macros set.

This also has a pressure gauge which we currently can't read remotely.

For info here is a detailed temp loop:

![detailed front board](backend_system/IOCs/MercuryITc/detailed_temp_board.jpg)

## OPI

The OPI has macros that relate to the macros set at the IOC level.

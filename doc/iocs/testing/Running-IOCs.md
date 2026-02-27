# Running IOCs locally

## Start the IOC

Either:

* start the IOC through the GUI. 
  * If this is a new IOC you will need to run `make iocstartups` in the EPICS folder for the IOC to be displayed in the GUI.
* start the IOC through the console (ctrl + x)
* switch off/on auto start (ctrl + t)
* start the IOC by running `runIOC.bat st.cmd` (in `iocBoot/Appdir`)

## IOC in procServ using the Console

Open an epics terminal a list all running instruments with

    console -M localhost -x

To interact with an IOC use

    console -M localhost <IOC_NAME>

console will attempt to complete the name if you only give part of it and will give you possible options. Once in the console:
* `ctrl-t` : toggles the auto-restart setting
* `ctrl-x` : starts and stops the IOC
* `crtl-e` `c` `.`: exits the console

# Simulation Mode

TO switch an IOC to simulation mode the default is

    caput <IOC PV NAME>:SIM 1

## Macros

It is possible to set macros for an IOC either through the IBEX GUI or using the globals.txt file. Loaded in using [icpconfig](../tools/icpconfig).

### Globals.txt

The globals.txt is file is held in `C:\Instrument\Settings\config\NDW_____\configurations`. In here, global macros are set with `<macro name>=<value>`, and macros specific for an IOC are set with `<ioc name>__<macro name>=<value>`

e.g.

    GALIL_01__GALILADDR=130.246.51.169
    GALIL_01__MTRCTRL=2
    GALIL_03__MTRCTRL=3
    GALIL_03__DEVSIM=1
    EGXCOLIM_01__RECSIM=1

:::{caution}
Inline comments are not possible within `globals.txt`, so should be on a new line. If added inline they may be read as part of the configuration value.*
:::

## Reading a Compressed Hex PV

Use the following to read a waveform PV of a compressed hexed string

    caget -t -S <PV NAME>|uzhex

(uzhex - think unzip hex)

## Troubleshooting

[See IOC and device Troubleshooting](../Troubleshooting)


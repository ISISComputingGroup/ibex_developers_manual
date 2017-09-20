> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Running IOCs

# Running the IOC

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
* `ctrl-x` : starts and stops the IOC
* `crtl-e` `c` `.`: exits the console

# Simulation Mode

TO switch an IOC to simulation mode the default is

    caput <IOC PV NAME>:SIM 1

# Macros

It is possible to set macros for an IOC either through the IBEX GUI or using the globals.txt file. 

## Globals.txt

The globals.txt is file is held in `C:\Instrument\Settings\config\NDW1407\configurations` in here you set macros global macros are set with `<macro name>=<value>` macros specific for an IOC are set with `<ioc name>__<macro name>=<value>`

e.g.

    SIMULATE=1
    GALILNUMCRATES=6
    GALIL_01__GALILADDR01=None
    GALIL_02__GALILADDR02=None
    GALIL_03__GALILADDR03=None

# Reading a Compressed Hex PV

Use the following to read a waveform PV of a compressed hexed string

    caget -t -S <PV NaME>|uzhex

(uzhex - think unzip hex)

# Troubleshooting

[See IOC and device Troubleshooting](IOC-And-Device-Trouble-Shooting)


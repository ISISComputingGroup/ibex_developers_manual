# Humidity Controller

The Humidity controller, also known as the RH Controller (Relative Humidity), is a device manufactured by Lacerta Technology https://www.lacerta-technology.com/ that is used on IMAT from time to time, but visits are often several years apart. The equipment has two USB to serial adapter connections (one to read humidity, one to control water temperature that manages the humidity) that need to both be plugged into a PC, often one of the IMAT camera PCs is used for this. The experiment is driven from the vendor software that loads an experiment file specifying what humidity they desire, we run a program on the PC where the vendor program resides that reads the humidity value and then pushes it to one of the user variables on NDXIMAT specifically   `IN:IMAT:PARS:USER:R0`  A block is then defined on NDXIMAT to reference this. The vendor software uses the old Windows DDE protocol to share values locally. There is no setting of values provided by ibex, just logging of humidity. A user written script on NDXIMAT will collect images in a loop, possibly rotating the sample too. Humidity changes will be driven from sequences programmed into the vendor software that has no way to drive ibex, hence ibex needs to log the humidity to the data files to allow the imaging data to be analysed correctly later.        

## on NDXIMAT
- make sure name of the PC running vendor software is in the gateway write access list for PVs as it needs to write to  `IN:IMAT:PARS:USER:R0`. If you need to add it, restart IBEX server afterwards. 
- add a block pointing to this PV

## On separate PC connected to humidity controller
- Install vendor software on PC
- connect the two USB to serial adapters between PC and equipment
- use device manager on PC to check what serial ports have been chosen for the adapters, usually COM4 and COM5 but not always. You need to know which refers to the humidity controller and which the water controller.
- In the vendor software interface add the instrument if not already present, it is a version 1 humidity controller
- check device communication settings page, make sure COM port is correct for both devices and baud rate is 9600
- copy across `C:\Instrument\Apps\EPICS\support\WinDDE\master` from NDXIMAT to somewhere on this PC e.g. in the users area
- in the `bin\windows-x64` double click on `run_windde.bat`  (this start the program to pull values from the vendor software and send to the PV on NDXIMAT)
- the program window should just start printing the humidity value, if you see "access denied" printed probably means an NDXIMAT gateway access security issue with the PC name
- if this pc reboots, `run_windde.bat` will need running again
 

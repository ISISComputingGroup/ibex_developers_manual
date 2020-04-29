> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Choppers](Choppers) > [SKF MB4150g5 Chopper](SKF-MB4150g5-Disk-Chopper-Controllers)

### SKF MB4150g5 Disk Chopper Controllers

These controllers are a development of the [MB350g3](SKF-MB350g3-Chopper) previously used on LET for its disk choppers and now repurposed on EMMA for its Fermi.  The G5 is an Ethernet device using a MODBUS protocol to communicate, and are generally installed on the instrument private networks.

### Current Installations

There are currently **three** controllers on LET (original choppers 3 & 4, and now 5) and **five** on IMAT (two double-disk choppers and a T0).

### Addressing Schema

LET - These controllers have been allocated addresses in the range _xxx.xxx.xxx.8x_, which is under the control of the Experimental Controls Group.  Since installation, the addresses were in the original range of xxx.xxx.xxx.18x, but problems were encountered when installing two additional controllers (see ticket [5033](https://github.com/ISISComputingGroup/IBEX/issues/5033) for details).

IMAT - These controllers are still in the original range of _xxx.xxx.xxx.18x_, but it is planned to reallocate them in the interests of consistency.

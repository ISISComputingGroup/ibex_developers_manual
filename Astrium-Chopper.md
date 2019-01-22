> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Astrium Chopper](Astrium-Chopper)

### These are installed on LET as Choppers 1 and 5

Note that these controllers are to be retired end of 2019.

## Software Architecture ##

The IOC for the Astrium choppers works similarly to that of the [Mk3](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/MK3-Chopper) in that it uses a .NET C# DLL to communicate with the servers running the chopper control programs. [[https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/image/Astrium.svg]]

## Hardware quirks ##

**Chopper 1 (NCS016)**

If the control program on the chopper PC is restarted for any reason, a reset will need to be performed before the chopper can be calibrated (which is also needed after a program restart).  This is done with a physical toggle switch on the monitoring system crate in the top of the left-hand cabinet.  (Fault LED 8 on the same card will be illuminated showing the error).

This cabinet is normally locked and so an instrument scientist will need to be contacted to gain access.


**Chopper 5 (NCS017)**

It is believed that the reset is not required on this system.
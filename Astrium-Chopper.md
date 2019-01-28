> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Astrium Chopper](Astrium-Chopper)

### These are installed on LET as Choppers 1 and 5

Note that these controllers are to be retired end of 2019.

## Software Architecture ##

The IOC for the Astrium choppers works similarly to that of the [Mk3](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/MK3-Chopper) in that it uses a .NET C# DLL to communicate with the servers running the chopper control programs. The architecture can be described as:

![](https://github.com/ISISComputingGroup/ibex_developers_manual/blob/master/images/Astrium.svg)

The red part of this diagram is written in C++/CLI to communicate with the .NET AstriumComms.dll and builds to another dll called Astrium.dll, which lives in the support directory. The green part is the asyn driver that communicates with Astrium.dll. StreamDevice is then used to communicate with this driver so as to leverage the formatting abilities of protocol files.

## Hardware quirks ##

* Sending a calibrate when the device has already been calibrated causes the chopper to get into a state that must be physically restarted to fix. Disallowing this is implemented into the IOC.
* When a frequency is set the device multiplies it by 10 e.g. sending 1Hz to the device will cause the chopper to run at 10Hz
* There is a resonance that means the chopper cannot run at 180Hz, this is reflected in the control scripts on LET
* There is a resume command in the C# dll. This does nothing.
* The frequency SP_RBV from the device always reads zero.

## Chopper 1 (NCS016) ##

If the control program on the chopper PC is restarted for any reason, a reset will need to be performed before the chopper can be calibrated (which is also needed after a program restart).  This is done with a physical toggle switch on the monitoring system crate in the top of the left-hand cabinet.  (Fault LED 8 on the same card will be illuminated showing the error).

This cabinet is normally locked and so an instrument scientist will need to be contacted to gain access.

### Photograph of the actual crate

![](https://github.com/ISISComputingGroup/ibex_developers_manual/blob/master/images/Astrium%20Monitoring%20Crate.JPG)

The toggle switch is labelled _quit failure_ and LED 8 can be seen to the right of the potentiometer labelled _adjust threshold_.

## Chopper 5 (NCS017) ##

It is believed that the reset is not required on this system.
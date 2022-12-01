> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [HTS Magnet](HTS-Magnet)

## HTS Magnet System
![20221130_140744](https://user-images.githubusercontent.com/14823767/204819524-231b166f-1085-4ad6-b43e-59eb3096af49.jpg)


Consists of an electromagnet powered by two KEPCO PSUs in master/slave configuration with monitoring by a Smartmonitor.

### KEPCO Power Supplies

The master KEPCO PSU (the uppermost in the rack) is connected to a MOXA NPort socket via a bespoke cable (_NOT_ standard MOXA cable) with an RJ45 (8P8C) on one end and an RJ11 (6P6C) on the other.  This flat grey cable is supplied with the device and is labelled accordingly (believed to be the only one and to date, no working spares exist).  The serial/remote/RS232 socket on the KEPCO is labelled "Trigger" and is in the bottom left corner of the rear panel.

The slave PSU is connected to the master (current output is shared between the two), with both connected to the Smartmonitor.

### Smart Monitor

The Smartmonitor is a _READ ONLY_ device which monitors the PSUs and magnet.  It shows the safe operating limits, hard limits and the current voltages and temperatures of the connected KEPCO.  Its only connection to the control system is via Ethernet on the private instrument network.  It has a fixed IP address on the R80 network, which is x.x.38.184. It has not yet been set up for R55 but if so the MAC address is available in the manuals area needed for setting up a new IP reserve.

The device can be configured with its webserver which should be at `<static ip>:8080`; this can be used to configure a different static IP address or to enable DHCP. 

The status command response on the Smartmonitor does not match what we have written in the "manual" (which is just an email chain) and adds a timestamp before the last status character - [#7397](https://github.com/ISISComputingGroup/IBEX/issues/7397) addresses this issue.

### Newport SMC100 Motion Controller

This system is also used with an [SMC100](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/SMC100) single axis stage to position the sample inside the magnet itself.

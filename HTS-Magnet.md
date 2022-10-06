> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [HTS Magnet](HTS-Magnet)

### HTS Magnet System

Consists of an electromagnet powered by two KEPCO PSUs in master/slave configuration with monitoring by a Smartmonitor.

The Smartmonitor is a _READ ONLY_ device which monitors (& controls?) the PSUs and magnet.  Its only connection to the control system is via Ethernet on the private instrument network.  It has a fixed(?) IP address of 192.168.0.11, which is not on the same subnet as the private network and so may need additional configuration of the NDX to enable communication.

The master KEPCO PSU (the uppermost in the rack) is connected to a MOXA NPort socket via a bespoke cable (_NOT_ standard MOXA cable) with RJ45 (8P8C) on one end and RJ11 (6P6C) on the other.  This flat grey cable is supplied with the device and is labelled accordingly (believed to be the only one and to date, no working spares exist).  The socket on the KEPCO is labelled "Trigger" and is in the bottom left of the rear panel.  The slave PSU is connected to the master, with both connected to the Smartmonitor.

This system is also used with an [SMC100](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/SMC100) single axis stage to position the sample inside the magnet itself.

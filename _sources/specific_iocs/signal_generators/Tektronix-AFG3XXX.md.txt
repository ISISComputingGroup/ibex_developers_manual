# Tektronix AFG3XXX

The Tektronix AFG3XXX is a signal generator.

It has an OPI for very basic controls, such as a trigger button and readbacks/setters for frequency, voltage and voltage offset. The underlying IOC provides many other commands however an arbitrary function generator is a very complex device to control remotely and therefore not all SCPI commands have been ported through to EPICS.  

The trigger PV is a `bo` type but calls `*TRG` on the device which generates a trigger event.

It is an ethernet device (ignore bits of log which mention GPIB - we are talking to it via ethernet). They respond to ping when on the network, and are usually set to use DHCP. The IP address can be found from front panel of the device.

If plugged into network after being turned on, the physical device & ioc might need a power cycle in order to talk properly from IBEX.
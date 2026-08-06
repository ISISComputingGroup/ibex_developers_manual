## Prologix GPIB Adapter

The [Prologix GPIB-ETHERNET adapter](https://prologix.biz/) is a GPIB -> Ethernet adapter that is supported by EPICS asyn via the `prologixGPIBConfigure` command 
and is used by some of our aeroflex and PS300 series devices.

The device support DHCP but it may not work across a network gateway, so when testing best be on the same network as the adapter. The MAC address is written on the adapter.

See `<Experiment Controls share>\prologix_gpib` for a manual and also the `netfinder` and `prologix configurator` programs if you need them.
You can run `netfinder` on the same network as the adapter to find its IP address and/or change it to DHCP.
The `prologix configurator` program lets you change other settings on the device, but is generally not needed by us as
the main ones are set by asyn when it connects. See the [adapter FAQs](https://prologix.biz/resources/frequently-asked-questions/gpib-ethernet-controller-faq/) for more details.


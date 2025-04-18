> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC)

**PSU COM Ports disappearing**

Symptom: The COM ports for the Cryogenic Inc. Power Supplies are missing from the Device Manager (these are inbuilt USB to serial adapters within the devices, they install a driver which allows them to appear as COM ports)
Solution: Turn the PSU off at the main switch, unplug the USB cable from the PSU, unplug any connections via hubs and their power as well, reconnect everything and power everything on, and the COM ports should be available again
# Power distribution units

A PDU, or Power Distribution Unit, is a large power strip with multiple power outlets to supply electricity to a number of attached devices. They may or may not have surge protection. Advanced PDUs provide surge protection, real-time monitoring and remote access.

### LINDY PDU

The Lindy PDU has been implemented on IBEX GUI using an IOC that uses the SNMP interface to view, monitor and update outlets. There are 8 outlets on the strip and they can be individually turned on or off from IBEX. Lindy also comes with a web interface and there is also separate configuration software that can be downloaded if required from the web site, which would probably be needed to set a static IP address (however DHCP can be enabled via a button press - see below). To run on the IBEX the IP of the PDU is required to be configured on the IOC macros.
Further info [here](https://www.lindy.co.uk/power-c8/power-distribution-unit-pdu-c347) for user manual etc. The manual is also in `<controls share>\Manuals\Lindy_ipower`

### IP address 

As described in the manual, you can press the function button on the device to see the IP address or change its mode between dhcp/static
```
Function Button:
a. Press and release this button to turn off the warning audible alarm. The overload alarm can’t be stopped by pressing this button.
b. Pressing the button and releasing it after 2 beeps will show up the unit’s IP address.
c. Pressing the button and releasing it after 4 beeps changes the IP address mode from fixed to DHCP and vice versa. 
d. Pressing the button and releasing it after 6 beeps restarts the network interface.
```




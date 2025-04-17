# Micro-epsilon confocal range finder

**IOC Name: MECFRF**

This device is used on CRISP to measure distances. It is an ethernet device. It has an IP address assigned by DHCP, but only after is explicitly told to do so. If the device is power cycled you will need to tell it to reacquire an address.

# Protocols

The manual specifies several different protocols on several buses (RS485, Ethernet, EtherCAT). The protocol we are using is documented in the manufacturer manual under a section called "Measurement Data Transmission to a Server via Ethernet"

It streams data continuously rather than having an explicit read command.

The IOC attempts to detect if the messages from the device don't start with the expected header, and if that is the case, resets the TCP connection to try and get the messages back in sync.
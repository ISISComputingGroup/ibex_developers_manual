> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power-Distribution-Unit-(PDU)](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Power-Distribution-Unit-(PDU))

## Power Distribution Unit (PDU)

A PDU, or Power Distribution Unit, is a large power strip with multiple power outlets to supply electricity to a number of attached devices. They may or may not have surge protection. Advanced PDUs provide surge protection, real-time monitoring and remote access.

### LINDY PDU

The Lindy PDU has been implemented on IBEX GUI using an IOC that uses the SNMP interface to view, monitor and update outlets. There are 8 outlets on the strip and they can be individually turned on or off from IBEX. Lindy also comes with a web interface. To run on the IBEX the IP of the PDU is required to be configured on the IOC.
Further info [here](https://www.lindy.co.uk/power-c8/power-distribution-unit-pdu-c347) for user manual etc.




> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Partially Supported Devices](Partially-Supported-Devices) > [DMA4500m Density Meter](DMA4500m-Density-Meter)

This is not a fully supported device, this was to allow a visiting scientist to run their IOC. Their code is [available]( https://bitbucket.org/europeanspallationsource/m-epics-dma4500m/src/master/).

It is a densitometer which currently measures density and temperature. 

## Troubleshooting

### Connection

The connection status is not reflected in the PVs so you need to print out the communication string to see if it is communicating.

### Measurement Mode

The data it sends back is dependent on its measurement mode. Currently the protocol supports 3 values being returned the density, temperature and condition. This was modified from the above version which also included the specific gravity. The indication that this isn't working is that the density stays at its initial value and show a `UDF` alarm. 


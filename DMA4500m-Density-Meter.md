> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > [DMA4500m Density Meter](DMA4500m-Density-Meter)

The device's IOC was originally developed at ESS, then updated to match ISIS requirements and conventions. The original code is available [here]( https://bitbucket.org/europeanspallationsource/m-epics-dma4500m/src/master/).

It is a densitometer which currently measures density and temperature.

## Documentation
Vendor documentation is available at `\\ISIS\shares\ISIS_Experimental_Controls\Manuals\AntonPaar__DMA4500`.

## Connection Details
  
|      RS-232C Specifications  |   |
|---------------|------------------|
|     Baud rate | 9600 Baud        |
|     Stop bits | 1 bit            |
|        Parity | None             |
|   Data length | 8 bit            |
|  Flow control | None             |

Notes:
 - Commands and returned values are terminated with CR
 - Only one command should be sent per second


## Simulation
The IOC logic is fairly complex and uses features not supported by RECSIM, so RECSIM has not been implemented for this device.

## Measurement Mode
The data sent back by the device is parsed according to the current measurement mode, which is set by `$(MEASUREMENT_MODE)` macro. Currently, the only supported modes are `DENSITY_ONLY` (for measuring density, temperature and measurement validity) and `DENSITY_AND_SPECIFIC_GRAV` (same values plus specific gravity).

From the device's point of view, the measurement results are returned by the `getdata` command. The quantities to be measured and their position in the results list are determined by the active "method". Methods are defined by the user using the device's GUI, and they can include a large number of different quantities in any order specified by the user. The device does offer a `getdatahead` command to get the name and position of the quantities returned by `getdata`, but there is no easy way of parsing the output of this command to automatically make sense of the results list. For this reason, we need to manually add a measurement mode for every method used at ISIS, and users must make sure to set the `$(MEASUREMENT_MODE)` macro in IBEX to match the method they're using.

## IOC diagram:
![Diagram of DMA4500M IOC](https://github.com/ISISComputingGroup/ibex_developers_manual/blob/master/images/dma4500m_ioc_diagram.png)



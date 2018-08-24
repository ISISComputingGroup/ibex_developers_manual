> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Cryogenics](Cryogenics)

IOC for devices connected with cryogenic.

* [Cryogenics_Ltd Helium Level Gauge](Cryogenics-Ltd-Helium-Level-Gauge)
* [Triton](Triton)

## Information about Low Temperature Devices

### Closed Cycle Refrigerators (CCRs)
These are controlled using Eurotherms.  No need to communicate directly with the CCR itself.

### Orange Cryostats
These are controlled using Eurotherms.  No need to communicate directly with the Cryostat itself.

### Variox (Blue) Cryostats
These are manufactured by Oxford Instruments (OI).  They are controlled by 2 devices: 
   * Intelligent Temperature Controller (ITC) (See [#1389](https://github.com/ISISComputingGroup/IBEX/issues/1389), [#3189](https://github.com/ISISComputingGroup/IBEX/issues/3189))
   * Intelligent Level Meter (ILM) (See [#1390](https://github.com/ISISComputingGroup/IBEX/issues/1390))

### ISISStat
Controlled by a Mercury ITC (See [#1199](https://github.com/ISISComputingGroup/IBEX/issues/1199))

A Mercury ITC may or may not be the same thing as an Oxford Instruments ITC. <br>
(**Can someone please clarify: is there any difference between a Mercury ITC and an OI ITC?**)

### Oxford Flow through Cryostats
We have not yet encountered one of these (when we do, please update this section).

### Triton Dilution Fridge
Triton dilution fridges are "parasitic" devices.  They need to be used in conjunction with a cryostat or CCR which provides the initial cooling down to a low temperature.  The dilution fridge then provides the final stage of cooling, down to a very low temperature.  Triton dilution fridges can be used with, either
   * Variox (Blue) Cryostats
      - controlled via ILM & ITC (see above)
   * CCRs
      - controlled via Eurotherm (see above)
      - See also [#2886](https://github.com/ISISComputingGroup/IBEX/issues/2886), [#2915](https://github.com/ISISComputingGroup/IBEX/issues/2915)

**Note:** it may be possible to run a Triton dilution fridge in a non-parasitic fashion, but we haven't encountered this situation (yet).  In practice, the Triton IOC might actually be indifferent to parasitic and non-
parasitic modes of operation. 

### 7.5T magnet
The 7.5T magnet is controlled by 3 devices:
   * Intelligent Power Supply (IPS) (See [#1391](https://github.com/ISISComputingGroup/IBEX/issues/1391))
   * Intelligent Temperature Controller (ITC) (See [#1389](https://github.com/ISISComputingGroup/IBEX/issues/1389), [#3189](https://github.com/ISISComputingGroup/IBEX/issues/3189))
   * Intelligent Level Meter (ILM) (See [#1390](https://github.com/ISISComputingGroup/IBEX/issues/1390))

See also [#2593](https://github.com/ISISComputingGroup/IBEX/issues/2593)

### 9T chopper magnet 
The 9T Chopper magnet is controlled by 3 devices:
   * Intelligent Power Supply (IPS) [#1391](https://github.com/ISISComputingGroup/IBEX/issues/1391)
   * Intelligent Temperature Controller (ITC) (See [#1389](https://github.com/ISISComputingGroup/IBEX/issues/1389), [#3189](https://github.com/ISISComputingGroup/IBEX/issues/3189))
   * Intelligent Level Meter (ILM) (See [#1390](https://github.com/ISISComputingGroup/IBEX/issues/1390))

See also [#2765](https://github.com/ISISComputingGroup/IBEX/issues/2765)

### 2T 3D Vector magnet 
The 2T 3D vector magnet is manufactured by Scientific Magnetics (i.e. not Oxford Instruments) so it does not use ILM, IPS, ITC.  It has its own control system for which the manufacturer has provided LabVIEW VIs:
   * we interface with these via lvDCOM (See [#1398](https://github.com/ISISComputingGroup/IBEX/issues/1398))

### Helium Level Gauge
Does what is says on the tin - measures the level of helium in a cryostat.
   * support for Cryogenics Ltd He Level Gauge  - See [#2350](https://github.com/ISISComputingGroup/IBEX/issues/2350)

### Other related tickets:
See [#1286](https://github.com/ISISComputingGroup/IBEX/issues/1286)
See [#1287](https://github.com/ISISComputingGroup/IBEX/issues/1287)
See [#1392](https://github.com/ISISComputingGroup/IBEX/issues/1392)

> [Wiki](Home) > [Deployment](Deployment) > [Migrate an Instrument Control PC](Migrate-an-Instrument-Control-PC) > [Migrating Galil Motors from SECI to IBEX](Migrating-Galil-motors-from-SECI-to-IBEX) > Physically connecting Galils via Ethernet

> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Galil](Galil) > [Migrating Galil Motors from SECI to IBEX](Migrating-Galil-motors-from-SECI-to-IBEX) > Physically connecting Galils via Ethernet


As part of migrating an instrument from SECI to IBEX, its Galil motors need to be migrated from serial to Ethernet. In addition to the [software configuration](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Migrating-Galil-motors-from-SECI-to-IBEX.), this requires the Galil controllers to be physically connected to the private ports on the NDH machine's network switch.

Below is a diagram of an example setup for the cabling on a fictional instrument:

![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_developers_manual/motors/galil_ethernet.png)

#### Notes
- Lines represent Ethernet cables
- The counting house which contains the NDH machine is often located in or adjacent to the instrument cabin (but not always)
- There are two notable bottlenecks which may require intermediate switches depending on the number of Galil controllers present:
    - Free ports in the block house near the racks (purple in the diagram)
    - Private network ports (green in the diagram)

### Preparation steps (if possible)
- Find out where the racks are located within the block house
- Find out where free network ports are located within the block house
- Find out where the network switch with private ports is in relation to the patch panel
- Plan how to patch all controllers through to the private network ports and note the number of switches and the number / length of cables required

### Installation
1. Get the appropriate cables / switches from the store room (currently located in R6, entrance by the mound opposite R2, then the first door on the left)
1. In the blockhouse, wire up the controllers to the wall ports. Note the number of the the wall ports used as they correspond to the port in the counting house. Label the used port with "private network" (otherwise people may try to just plug a different device into the port later)
1. In the counting house, connect the corresponding port on the patch panel leading to the block house to the private port on the network switch. Label each cable with the controllers it connects to (e.g. `MOT01-04`)
1. After all the cables have been connected, you can confirm the PC is talking to each Galil controller by pinging their network addresses (assuming they have already been configured already) i.e.
    - `ping 192.168.1.201` for controller 1
    - `ping 192.168.1.202` for controller 2
    - etc.
1. If any of the controllers are not responding, look at the cabling again to diagnose any issues with the physical connection (e.g. cable is damaged or not plugged in properly, switch not powered on, etc.) and repeat
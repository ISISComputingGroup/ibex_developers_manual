Note: this page relates to a newer-style ethernet-connected stress rig, which we talk to via a manufacturer DLL. For documentation about the GPIB-connected rig (i.e. the 50kN rig on ENGIN-X) see https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Instron-stress-rig


# Physical setup

The stress rig has several components:
- The physical rig hardware, in which the sample sits.
- A controller, which plugs directly into the physical rig hardware, and has an ethernet port on the back
- The ethernet port on the controller is plugged into the control PC via a **direct** ethernet connection. This connection should **not** be going via a switch or the ISIS network in any way.
  * Note, this "control PC" is **NOT** the `NDX` machine or equivalent, it is a separate machine. Currently a desktop PC.
- The control PC has a physically separate RJ45 port (currently a USB-to-ethernet converter) used to connect to the ISIS network.
- There is an "MMI" controller which plugs into the control PC via USB.

The manufacturer software ("Console") **MUST** be running on the control PC for the rig to work.

# IOC

We will run an IOC on the control PC, which can be viewed and eventually controlled from the NDX.

Due to needing to link against the 32-bit manufacturer DLL (`Arby.dll`) for communication, we need to deploy a 32-bit EPICS build to the control PC. Ticket https://github.com/ISISComputingGroup/IBEX/issues/7326 will define our approach to this computer in more detail.

The manufacturer software ("Console") must be running in the background while the IOC is attempting to talk - otherwise the rig will not work.
> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) > [Omron FINS](Omron-FINS)

The Omron FINS is a PLC controlled via a driver first written at Diamond, see [here](https://github.com/ISISComputingGroup/EPICS-FINS). The IOC works by loading an instrument specific `FINS_01.cmd` in `configurations/fins`, which will load an instrument specific `db` from `ioc/master/FINS/db`. The dbs in here are usually created from a number of templates matching specific memory addresses to PVs. Currently the following specific FINS PLC installations are supported in IBEX:

* IMAT FINS PLC
* LARMOR air PLC
* SANS2D vacuum PLC
* WISH vacuum PLC
* ZOOM vacuum PLC
* Helium Recovery PLC - stores information needed for the Helium Level Monitoring project

### PLC init

The fins PLC communication is set up with the following:

```
finsUDPInit(<port Name>, <address>, <protocol>, <simulate>)
```
where:

- port name: ASYN port name (usually PLC)
- address: ip address of the PLC 
- protocol: which protocol to use
    - "TCP": use TCP communication
    - "TCPNOHEAD": use TCP comms, but without FINS-TCP header. This is required (and should only be used for) the devsim IOC tests
    - anything else: use UDP protocol
- simulate: whether to simulate calls
    - 0: Do not simulate (real device or devsim)
    - 1: Simulate (don't send commands), this is required for recsim as it lets device initialisation complete successfully with no device

### Testing the FINS IOC in the Ioc Test Framework

In contrast to the normal operation of a FINS PLC, the instrument specific `FINS_01.cmd` file that should be used for the IOC Tests for a FINS PLC should be placed in an instrument specific folder in [ioc\master\FINS\exampleSettings](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master). This cmd file should have the appropiate finsUDPInit calls for devsim or recsim, as detailed below, and also the usual `dbLoadRecords` call to load the instrument specific db.

### Testing the FINS IOC in DevSim

If you want to test the IOC for a FINS PLC in devsim mode, you need to add to the FINS_01.cmd file used by that specific FINS IOC the line:
```
$(IFDEVSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 0, "$(PLCNODE=)")
```  

At the same time, the file should either not have any other finsUDPInit call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.

### Testing the FINS IOC in RecSim

If you want to test the IOC for a FINS PLC in recsim mode, you need to add to the FINS_01.cmd file used by that specific FINS IOC the line:
```
$(IFRECSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 1, "$(PLCNODE=)")
```  

At the same time, the file should either not have any other finsUDPInit call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.

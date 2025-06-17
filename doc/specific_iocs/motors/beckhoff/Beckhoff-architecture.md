# Beckhoff IOC Architecture

We have an EPICS motor record implementation which interfaces some intermediate PVs, spun up by AdsDriver and [The Beckhoff Motor Extensions](https://github.com/ISISComputingGroup/EPICS-motorExtensions/tree/master/beckhoffApp)

This was originally done so we could drop-in [`AdsDriver`](https://github.com/ISISComputingGroup/adsDriver) in place of another ADS EPICS module (`tcIOC`) and debug EPICS to ADS more easily by bypassing the motor modules if we saw a comms issue. In future, we could build [`AdsDriver`](https://github.com/ISISComputingGroup/adsDriver) into our motor module directly so we avoid this extra step. 

This means that the EPICS motor record is essentially doing `dbgf` and `dbpf` to read and write to these PVs respectively, rather than just setting something on a device like a normal motion controller like a [Mclennan] or [Galil]. 


# Beckhoff IOC Architecture

[TC](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/TC) is the IOC responsible for communication with Beckhoff PLCs at ISIS.

At IOC startup, it uses [a command](https://github.com/ISISComputingGroup/adsDriver/blob/main/adsApp/src/ioc_commands.cpp#L139) to get the number of motion axes. Note that this may be more than 8, in which case we have to use [some logic](https://github.com/ISISComputingGroup/EPICS-ioc/blob/master/TC/iocBoot/iocTC-IOC-01/st-common.lua#L51) to alias `MTR0109` to `MTR0201` so we can display it in the IBEX GUI's table of motors.  

We have an EPICS motor record implementation which TC uses that interfaces some intermediate PVs, spun up [at runtime](https://github.com/ISISComputingGroup/EPICS-ioc/blob/97e2bd77c5909ff2f1b6c0cda7f175366b379102/TC/iocBoot/iocTC-IOC-01/st-common.lua#L30) per-axis by AdsDriver using [The Beckhoff Motor Extensions](https://github.com/ISISComputingGroup/EPICS-motorExtensions/tree/master/beckhoffApp)  `.db` files.

This was originally done so we could drop in [`AdsDriver`](https://github.com/ISISComputingGroup/adsDriver) in place of another ADS EPICS module ([`tcIOC`](https://github.com/ISISComputingGroup/EPICS-tcIoc)) and debug EPICS to ADS communications more easily by bypassing the motor modules if we saw an issue. In the future, we could build [`AdsDriver`](https://github.com/ISISComputingGroup/adsDriver) calls into our motor module directly so we avoid this extra step.

This means that the EPICS motor record is essentially doing `dbgf` and `dbpf` as documented in the {external+EPICS:doc}`EPICS IOC Test Facilities <appdevguide/IOCTestFacilities>` respectively to read and write to these PVs, rather than just setting something on a device like a normal motion controller like a {doc}`../McLennan-motors` or {doc}`../Galil`. 

`TC` also does some things "outside" the motor record such as forwarding the device's velocities to the motor record. This is because the PLC is commissioned with a sensible velocity in most cases and we don't want to overwrite this information, and it may change on the PLC due to safety system overloads and so on. We also do the same for axis description (to the `.DESC` field) - see {ref}`beckhoff_manual_commission_step`.

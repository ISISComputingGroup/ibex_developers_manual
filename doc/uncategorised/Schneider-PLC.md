These are controlled by the `SCHNDR` iocs and are used on various instruments, such as to monitor value status or pressure (a TPG300 can for example feed data into the PLC inputs). Communication is by modbus protocol using EPICS modbus support. 

Relevant IOC config macros are:

* `MODE`: `TCP`, `RTU` or `ASCII` to specify PLC connection mode. We generally use either `TCP` or `RTU`.
* `PORT`: Serial COM Port of PLC for `RTU` or `ASCII` mode
* `IPADDR`: IP address of PLC for `TCP` mode
* `IPPORT`: TCP will connect on default modbus 502 port, set this if different.

To configure EPICS records for PLC specific variables, set macros such as `DEVCMD1` to a CMD file base name in the `devices` subdirectory which should be loaded. For example on GEM we set `DEVCMD1` to `GEMGateValve` to load `devices/GEMGateValve.cmd`. Currently there is only `DEVCMD1` but if there were cross instrument files that were useful to load, or a plc talked to multiple separate devices, then adding `DEVCMD2` may be useful in future

[PLC IOC files](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/SCHNDR/iocBoot/iocSCHNDR-IOC-01)
 


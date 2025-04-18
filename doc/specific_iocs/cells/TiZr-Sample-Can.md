# TiZr Sample Can

The main project is one that sees the building and integration of a sample can such as was used in an experiment in the mid-1990s. The sample container is designed to contain steam at 580K and 95 bar. This will be used for an experiment on NIMROD.

The assembly will consist of a stainless steel reservoir for the sample (either H20 or D20) which will then be evaporated into the TiZr cell. The pressure will generally be managed by the temperature. A manually controlled needle valve will be used during setup to limit the pressure should the reservoir be overfilled. A pressure gauge which outputs 0V to 10V will be used to report the pressure.

From an IBEX perspective, the standard Triple Eurotherm on NIMROD will be used to read and control the temperature of the reservoir and the cell, with readings for the cell from both the top and bottom of the cell. Another Eurotherm crate will be brought in to read the temperature of the pipework after the cell and the pressure within the cell.

In a meeting on the 20th of April 2020, no other data collection or recurring calculations were identified, which means that the IBEX setup is limited to configuration items, and as such, no tickets have been created at this time.

In a meeting on the 19th of June 2020, an awareness of a need to reduce the impact of potential human error was realised and IBEX issue #5494 was created to handle that

## TiZR cell inhibitor IOC

Takes two PVs as macros (PV-A and PV-B). Each PV has a maximum value set on them (PV-A-Max, PV-B-Max) and PV-A has a safe value (all of these are defined as macros). Each of PV-A and PV-B are allowed to exceed their max individual values separately but not at the same time (i.e. the exclusive or is allowed: PV-A > PV-A-Max XOR PV-B > PV-B-Max). If both exceed their maximum values (i.e. PV-A > PV-A-Max and someone sets PV-B > PV-B-Max or vice versa) then the given safe value is written to PV-A. 

When the safe value is written the TIZRWARNING will be set into alarm for 5 seconds and then the alarm is cleared, unless, the pv is still out of range in which the alarm is persisted in which the safe value would be continuously written to the PV (this could occur if writing the safe value is rejected or the safe value > PV-A-Max). 

Currently, if PV-B > PV-B-Max and a value is written to PV-A where value > PV-A-Max, the value will be set to PV-A for a brief period and then the safe value will be written to PV-A again overwriting this. We could change this by setting the DRVH on PV-A whilst inhibiting based on the PV-B value.

The support module is here https://github.com/ISISComputingGroup/EPICS-TiZr and the ioc at https://github.com/ISISComputingGroup/EPICS-ioc in the TIZR folder.
> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) > [RIKEN PLC](RIKEN-PLC)

### Introduction

The main PLC on RIKEN is a "Schneider Electric M580" and is responsible for controlling and monitoring the various systems on the beamlines, e.g. vacuum equipment and magnet cooling.  The Schneider PLC IOC (`SCHNDR_01`) runs on `NDXRIKENFE` and provides access to designated PLC registers (memory addresses) via the ASyn MODBUS driver.

### Registers and Variables

The groups of variables and their associated registers are defined in the document [`RIKEN PLC IBEX Specification`](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/RIKEN%20FE/RIKEN%20PLC%20IBEX%20Specification%20-%20Issue%20G_TC.docx) (which can be found in the RIKEN FE ICP Discussions area of SharePoint) and are as follows: (all are read-only, apart from the vacuum valve controls, see below)

- Separator vacuum status
- Solenoid status
- Kickers water, vacuum and MOL (Magnet Off Light) status
- Kickers status and output (voltage and current)
- GH (Gauge Head) vacuum gauge status
- LV (Line Valve), AMGV (All Metal Gate Valve) and FSOV (Fast Shut Off Valve) vacuum valve status
- LV, AMGV, FSOV, control (**writable** from IBEX, but only to **open** the valves)
- BP (Backing Pump) and TP (Turbo Pump) vacuum pump status 
- PIV (Pump Isolation Valve) interlock status
- LV, AMGV, FSOV, BPV1 interlock status
- BB (BeamBlocker) status and information
- Magnets Klixon interlock status (a _Klixon_ is a thermal switch which opens/closes at a set temperature)
- Magnets cooling water flow status, rate and temperature
- RBox (Rectifier Box) and bypass interlock status
- MOL (Magnet Off Light) status (purely the status of the _bulb_, not the magnet state)

### Connection

The PLC is connected to the ISIS Controls Network using a fixed/static IP address.  It is currently patched directly into the main switch in the R55 Hub Room which has a port configured via a VLAN.  The PLC also has a "local" network to connect to its satellite nodes and HMI screens.

### Location

The PLC is physically located on the ground floor of the RIKEN area in R55, the ISIS TS1 Experiment Hall, in the end rack of a block of five (labelled **RR5**).

### Configuration Files

IOC macro values are specified in the `globals.txt` file in the settings area. There are macros to specify the connection type (TCP in this case), IP address of the PLC and which configuration (`CMD`) file to load.  Macros are not defined in the IOC configuration screen of the client to avoid accidental editing, and because the values are very unlikely to change.

The CMD file (`RIKENFE.cmd`) is located in the [`devices`](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/SCHNDR/iocBoot/iocSCHNDR-IOC-01/devices) directory of the IOC.

The DB file (`RIKENFE.db`) is generated using a set of template files which correspond to types of PLC variables and readback values.  The substitution and CMD files follow the structure of the Specifications document referenced above, and so it is advised to read them in parallel when required.  See the [`DB`](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/SCHNDR/SCHNDR-IOC-01App/Db) area of the IOC directory.

The PLC IOC also loads a separate DB file (`RIKENFE_TEMPMON.db`) for monitoring temperatures of a selection of magnets (RQ1, RQ2, RB1) and is purely for logging purposes.  This is at the request of the Electrical Controls Group who are performing an experimental analysis.

The IOC called RKNMNTR is designed to deal with calculating the magnet temperatures based on the PSU currents on RIKENFE (SCHNDR IOCs).
Currently it provides raw volt reading, ADC volt, actual volt, resistance and temperature per tap for magnets RQ1, RQ2, RB1 on the following PV patterns respectively:

- `IN:RIKENFE:<magnet>:<tap>:VOLT:RAW`
- `IN:RIKENFE:<magnet>:<tap>:VOLT:ADC`
- `IN:RIKENFE:<magnet>:<tap>:VOLT`
- `IN:RIKENFE:<magnet>:<tap>:RES`
- `IN:RIKENFE:<magnet>:<tap>:TEMP`

where `<magnet>` is RQ1, RQ2 or RB1 and `<tap>` is between TAP01-TAP24.

> **Note**
> This IOC will be live on RIKENFE on the next deploy.

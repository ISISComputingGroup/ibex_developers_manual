> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) > [RIKEN PLC](RIKEN-PLC)

### Introduction

The main PLC on RIKEN is responsible for controlling and monitoring the various systems on the beamlines, e.g. vacuum equipment and magnet cooling.  The Schneider PLC IOC runs a CMD file specific to RIKEN which then loads a specific DB file to give access to designated PLC registers (memory addresses) via the ASyn MODBUS driver.

The groups of variables are defined in the document [`RIKEN PLC IBEX Specification`](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/RIKEN%20FE/RIKEN%20PLC%20IBEX%20Specification%20-%20Issue%20G_TC.docx) (which can be found in the RIKEN FE ICP Discussions area of SharePoint) and are as follows: (all are readonly, apart from the vacuum valve controls, see below)

- Separator vacuum status
- Solenoid status
- Kickers water, vacuum and MOL (Magnet Off Light) status
- Kickers status and output (voltage and current)
- GH (Gauge Head) vacuum gauge status
- LV (Line Valve), AMGV (All Metal Gate Valve) and FSOV (Fast Shut Off Valve) vacuum valve status
- LV, AMGV, FSOV, control (**writable** ````from IBEX, but only to **open** the valves)
- BP (Backing Pump) and TP (Turbo Pump) vacuum pump status 
- PIV (Pump Isolation Valve) interlock status
- LV, AMGV, FSOV, BPV1 interlock status
- BB (BeamBlocker) status and information
- Magnets Klixon interlock status (a _Klixon_ is a thermal switch which opens/closes at a set temperature)
- Magnets cooling water flow status, rate and temperature
- RBox (Rectifier Box) and bypass interlock status
- MOL (Magnet Off Light) status (purely the status of the _bulb_, not the magnet state)

The PLC IOC also loads a separate DB file (TEMPMON) for monitoring temperatures of a selection of magnets (RQ1, RQ2, RB1) and is purely for logging purposes.  This is at the request of the Electrical Controls Group who are performing an experimental analysis.

### Connection and Configuration

The PLC is connected to the ISIS Controls Network using a fixed/static IP address which is specified in the `globals.txt` file.  Also in this file are macros to specify the connection type (TCP in this case) and which configuration (`CMD` file) to load.  The PLC also has a "local" network to connect to its satellite nodes and HMI screens.

### Files

The DB file is generated using a set of template files which correspond to types of PLC variables and readback values.  The substitutions file follows the structure of the Specifications document referenced above, and so it is advised to read them in parallel when required.


> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) > [RIKEN PLC](RIKEN-PLC)

### Introduction

The main PLC on RIKEN is responsible for controlling and monitoring the various systems on the beamlines, e.g. vacuum and magnet cooling.  The Schneider PLC IOC loads a DB file specific to RIKEN which then gives access to designated PLC registers (memory addresses) via the ASyn MODBUS driver.  The groups of variables are as follows: (all are readonly, apart from the vacuum valve controls)

- Separator vacuum status
- Solenoid status
- Kickers water, vacuum and MOL (Magnet Off Light) status
- Kickers status and output (voltage and current)
- GH (Gauge Head) vacuum gauge status
- LV (Line Valve), AMGV (All Metal Gate Valve) and FSOV (Fast Shut Off Valve) vacuum valve status
- LV, AMGV, FSOV, control (writable from IBEX)
- BP (Backing Pump) and TP (Turbo Pump) vacuum pump status 
- PIV (Pump Isolation Valve) interlock status
- LV, AMGV, FSOV, BPV1 interlock status
- BB (BeamBlocker) status and information
- Magnets Klixon interlock status (a _Klixon_ is a thermal switch which opens/closes at a set temperature)
- Magnets cooling water flow status, rate and temperature
- RBox (Rectifier Box) and bypass interlock status
- MOL (Magnet Off Light) status (purely the status of the _bulb_, not the magnet)

The PLC IOC also loads a separate DB file (TEMPMON) for monitoring temperatures of a selection of magnets (RQ1, RQ2, RB1) and is purely for logging purposes.  This is at the request of the Electrical Controls Group who are performing an experimental analysis.

# RIKENFE

```{include} migration_notes_warning.mdinc
```

This page contains information pertinent to the automation of the RIKEN Front End Beamline Control at ISIS.

## Background ##
ISIS have taken over management of the RIKEN facility at ISIS.  Various systems on the RIKEN facility are being upgraded over time.

## Control System ##
Control of the RIKEN Front End hardware will be migrated to IBEX in a series of phases.  Therefore, there will be a period of mixed operation, in which some devices will be controlled via the existing RIKEN control system and others are controlled by IBEX.

## Timeline ##
| Task/Event | Date | Notes |
| --- | --- | --- |
| PSU control | Summer 2018 | Upgrade PSU control.  See [#2813](https://github.com/ISISComputingGroup/IBEX/issues/2813), [#3150](https://github.com/ISISComputingGroup/IBEX/issues/3150). |
| ARGUS Magnets | Summer 2018 | Changes to ARGUS magnets (no further details). |
| Replace PLC | Easter 2019 | Preferred replacement PLC is a [Schneider Modicon M580 - ePac](https://www.schneider-electric.co.uk/en/product-range/62098-modicon-m580---epac). |
| Mitsubishi PSU | No date yet | Part of cryogenics system.  May be controlled via its own dedicated PC. |

## Equipment ##
The table below captures what the Experiment Controls Group knows about the RIKEN Front End hardware (as of September 2018).

| Manufacturer | Model | Type | Connection | Driver | Notes |
| --- | --- | --- | --- | --- | --- |
| Danfysik | XXXX | PSU | RS232 | DFKPS | [see PSUs note](#note-psus) |
| GEC | XXXX | PSU | RS232 | ??? | [see PSUs note](#note-psus) |
| Schneider | ???? | PLC | RS232 | ModbusRTU | PLC is, or is similar to, a [Schneider Electric Quantum PLC](https://www.schneider-electric.co.uk/en/product-range-download/538-modicon-quantum). |
| | | Kicker | ??? | | Currently not functional.  No immediate plans to make it so. |
| | | Separator | ??? | | Separator PSUs are due to be replaced (no timescale yet) |
| Pfeiffer | TPG300 | Vacuum Monitor | RS232 | TPG300 | There are ~7 of these.  Assumed to have RS232 cards. |
| Pfeiffer | TCP350 | Turbo Pump | TCP/IP | TCP350 | |
| National Instruments| DAQmx| Data Acquisition | TCP/IP | | Used to communicate with PLC & PSUs |

##### Note: PSUs #####
1. The RIKEN PSUs are physically a mixture of Danfysik, GEC, and Japanese power supplies. However, they are all fitted with Danfysik control boards.  So as far as IBEX is concerned they are all Danfysik devices.
1. The Danfysik control boards talk a slightly different protocol than the other Danfysiks (as used on Muon-FE, EMU, LOQ and other instruments).  For this reason, they require their own IOC.  All of the power supplies on RIKEN-FE are controlled by a single IOC. 
1. We have no record of the actual Danfysik model number to which these boards correspond (it is quite possible that they don't correspond to any standard Danfysik), so we have no Danfysik manuals for these particular boards.  The best we information we have is the documents stored in the `RIKEN_power_supplies` sub-folder in the Experiment Controls Group's Manuals share.



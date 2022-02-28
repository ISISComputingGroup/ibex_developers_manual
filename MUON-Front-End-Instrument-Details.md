This page contains information pertinent to the automation of the Muon Front End Beamline Control at ISIS.

## Background & Timeline ##
The system is due on line September 2016.

## Control System ##
Whilst the Front End control will be undertaken under IBEX, it must integrate with SECI as well as part of the system is to be used on existing instruments. Some of the IOCs will only be controlled from instrument PCs, whilst in some situations only monitoring will be required.

## Equipment ##
| Manufacturer | Model | Type | Connection | Driver | Notes |
| --- | --- | --- | --- | --- | --- |
| Danfysik | 8000 | PSU | RS232 | DFKPS | Created, some outstanding changes needed.  See #1208 for comms settings. |
| Danfysik | 9100 | PSU | RS232 | DFKPS | Created, some outstanding changes needed.  See #1208 for comms settings. |
| Danfysik | 8800 | PSU | RS232 | DFKPS | Created, some outstanding changes needed.  See #1208 for comms settings. |
| TDK | Lambda Genesys | PSU | RS232 | TDK_ LAMBDA_ GENESYS | Created, setup required |
| Glassman | PG200P2.5 | PSU | via PLC | | |
| | | Kicker | via PLC | | This is monitoring of a relay state |
| | | Momentum Slits | via Galil | Galil | This is a separate project, and the same Galil controls the individual beamline jaws. See [see Barndoors and Momentum Slits note](#noteMomentumSlits) |
| Pfeiffer | TPG300 | Vacuum Monitor | RS232 | TPG300 | |
| | | Valve Control | via PLC | | This is the monitoring of various valves |
| Galil | DMC2280 | Motor Controller | Ethernet | EPICS | |
| | | PLC | | | This will be a modbus connection, as it is an existing PLC. The details are still unconfirmed |

<a name="noteMomentumSlits"></a>
## Barndoors and Momentum Slits ##
The barn doors and momentum slits control the muon beam delivered to the 3 muon instruments: HIFI, muSR and EMU.  The control of these devices is described on the [Barndoors & Momentum-Slits](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Barndoors-and-Momentum-Slits-on-MUON-Front-End) page.

<a name="noteMotion"></a>
##### Note: Motion #####
There is a project relating to the motion on the South Side Muons in progress, this information may be out of date
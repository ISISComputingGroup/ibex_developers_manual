# Introduction

This is controlling the flow of helium in a cryostat, via a needle valve, based on a lookup table implemented in the hardware. The underlying hardware is a Eurotherm (Modbus) controller, and `automaticNeedleValve.db` adds some extra settings on top.

The needle valve operation revolves around two modes: manager mode and setpoint mode. The latter has the two modes _'Automatic'_ and _'Manual'_, which dictate the behaviour of the needle valve:
* Automatic mode: 
  * Temperature (`TEMP`) is writable and readable
  * Flow (`MANUAL_FLOW`) can only be read
* Manual mode:
  * Flow (`MANUAL_FLOW`) is writable and readable
  * Temperature (`TEMP`) can only be read

# Main records
### `automaticNeedleValve.db`
| PV | Description | Access |
| -- | -- | -- | 
| `FLOW`| "Flow" Flow readback from transducer | Read only | |
| `VALVE_DIR` | Valve Direction; **0 = Closing, 1 = Opening** | Read only | |
| `FLOW_SP_MODE_SELECT` | Flow Setpoint Select; **0 = Auto setpoint mode, 1 = Manual setpoint control** | Read/Write | |
| `MANUAL_FLOW` | Manual flow setpoint; Reliant on `FLOW_SP_MODE_SELECT` being at 1 (i.e. Manual) | Read/Write | |
| `FLOW_SP_LOWLIM` | Low setpoint limit for flow control | Read/Write | |
| `NEEDLE_VALVE_STOP` | Ability to 'inhibit' Loop 2 | Read/Write ||

### Other
| PV | Description | Access |
| -- | -- | -- | 
| `TEMP`| Temperature readback from Eurotherm | Read/Write | |

# Access control architecture
There are two mechanisms at work controlling SP access rights here; setpoint mode and manager mode.

### Manager mode
All writable items are _only_ accessible when manager mode is enabled (e.g., `$(P)CS:MANAGER`=1): 

### Setpoint mode
As detailed above, the access rights to the `MANUAL_FLOW` and `TEMP` PVs is controlled partially via setpoint mode.

These rights are managed via a series of fanout/seq records, which set `0` or `1` to the `.DISP` field (see [EPICS: Fields Common to All Record Types](https://epics.anl.gov/base/R7-0/6-docs/dbCommonRecord.html)) of each of these PVs, depending on the mode:
|  | Auto | Manual |
| -- | -- | -- | 
| Flow | `.DISP`=1 | `.DISP`=0 |
| Temperature | `.DISP`=0 | `.DISP`=1 |

### Summary
For a very explicit summary of write access for these two PVs, see  below:

#### `MANUAL_FLOW` 
|  | `FLOW_SP_MODE_SELECT`=0 (Auto) | `FLOW_SP_MODE_SELECT`=1 (Manual) |
| -- | -- | -- | 
| `CS:MANAGER`=0 (Off) | Read only | Read only |
| `CS:MANAGER`=1 (On) | Read only | Readable & Writable |

#### `TEMP` 
|  | `FLOW_SP_MODE_SELECT`=0 (Auto) | `FLOW_SP_MODE_SELECT`=1 (Manual) |
| -- | -- | -- | 
| `CS:MANAGER`=0 (Off) | Read only | Read only |
| `CS:MANAGER`=1 (On) | Readable & Writable | Readable only |



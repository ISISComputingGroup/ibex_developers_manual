# EPICS PV Naming Scheme
Suggestions for naming of PVs at ISIS. As of EPICS base 3.14.12 record names can be up to 60 characters long, but full PV name can be longer. 

Basic idea is to describe function in the PV name, not hardware/technology - the PV name is the purpose of a channel and is abstracted from the underlying hardware; an individual IOC name can however reflect technology/hardware/implementation. Note: do not use the `:` character in an IOC name.

For multiple devices, follow device name with 1, 2  etc. (should we use `MOTOR1`, `MOTOR_1` or `MOTOR:1:` ?) Probably `MOTOR1` . We could try fixed formatting the number e.g. MOTOR01, but then if we have less than 10 we are adding an unnecessary 0 and if we get more than 100 the rule is broken. So no zero prefixing is probably simplest. 

All characters in names should be uppercase. We will use `:` as hierarchy separator, `_` to delimit distinct characters in device name

Basic scheme format is `Domain:subdomain:technicalarea:device:subdevice:signal`

PV names are restricted to alphanumerical, plus `_` and `:` so `[A-Z0-9_:]*` Items that might have multiple instances must not end with a number as this would be confused with a 01,02 etc suffix used to enumerate multiple instances. 

PV names must start with a letter and must not end with `_` for now (maybe adopt NSLS2 convention of trailing `_` = private names?)

We can create a separate PV name to describe actual hardware type 

# Signal Qualifiers
These are added after a signal to indicate it is a setpoint etc. So for the TEMP signal

| ...:HEATER:TEMP | Current temperature |
| …:HEATER:TEMP:SP | Temperature set point (requested value) – this is the value that was input in software and sent to the equipment. Write to this PV to change a setpoint |
| …:HEATER:TEMP:SP:RBV  (read-only) | This is the setpoint “readback”  from hardware, which may differ from SP sent above if e.g. the hardware was unable to exactly match the requested value. Also if the SP was changed by some other mechanism (e.g. manually on the hardware) :SP would not reflect this, but :SP:RBV would |

Note:  RBV suffix can be used more generally e.g. For P,I,D values you could have …:P and …:P:RBV 

Note: For comparison, the SNS are using [camel case](http://en.wikipedia.org/wiki/CamelCase) i.e.  Temp, !TempSet and TempRB 

# Macros

All records should start `$(P)` for prefix which can be substituted at load time. Diamond have `$(P)$(Q)` for added flexibility and we may want to use this too

# Top Level domain

Some suggested top level domains – we may not want to use them all
|Prefix| Function |
|...|...|
| AC    | ISIS Accelerator/synchrotron related parameter |
| CS    | Control system specific top level variables e.g. global IOC related variables |
| TG    | ISIS Target related parameter |
| IN    | Instrument related parameter |
| HA    | Experimental hall/building related parameter (e.g. cabin temperature) |
| TE    | Testing domain, used by local EPICS developers |
| ME    | Movable equipment, equipment not tied to a specific beamline |
| BL    | Beamline – used if multiple instruments are sharing a common set of equipment, such as on the muon beamlines pre kicker. |

# AC Domain
| TG:TS1:MOD:H2:TEMP    | TS1 hydrogen moderator temperature |
| TG:TS1:MOD:H2:TC01:TEMP   | Alternative to above as there may be more than one temperature value! Using TC for “thermocouple” |

# TE Domain
Mostly free format - have developers fedid as second part, then whatever required. In many cases would want to suffix with above scheme to make final integration easier e.g.

```
TE:FAA59:TG:TS1:MOD:H2:TEMP
```


# BL Domain
This needs to be followed by information about which beamline. For neutron instruments could use the MCR shutter port identifier (N1, N2, N3 etc.) – need to find out what they call the Muon beamline.

# HA Domain
Should be followed by the hall identifier. We could use `HA:TS1:*` etc, or be more general for possible  use with any building e.g. `HA:R55:* `

# IN Domain
Sub domain is full instrument name e.g GEM. If we wish to distinguish the instrument “front end” from the rest, could use `*:FE` subdomain

| IN:GEM:*  | Prefix for all variables related to GEM instrument |
| IN:GEM:SB:*  | Where to record short SECI block (short/friendly) names if we use them |
| IN:GEM:MOT:*  | Motion control equipment - see below |
| IN:GEM:VAC:*  | Vacuum equipment |
| IN:GEM:CS:*   | Variables related to instrument control system software - see below |
| IN:GEM:PS:*   | Power supply |
| IN:GEM:CHOP:FERMI:*   | |
| IN:GEM:SE:*   | Sample environment not covered elsewhere |
| IN:GEM:DET:*  | Detector related variables |
| IN:GEM:FE:*   | Instrument “front end” equipment |
| IN:GEM:DAE:*  | Data acquisition electronics related PVs |

# The IN:{INST}:CS sub domain

| IN:{INST}:CS:IOC:*    | Variables describing running IOCs provided by the IOC themselves |
| IN:{INST}:CS:IOC:{IOCNAME}:AS:*   | Austosave PVs for IOC {IOCNAME} |
| IN:{INST}:CS:IOC:{IOCNAME}:DEVIOS:*   | DevIOStats PVs for IOC {IOCNAME} |
| IN:{INST}:CS:IOC:{IOCNAME}:MOT:*  | Motion specific PVs e.g. allstop from motorUtils  | 
| IN:{INST}:CS:IOC:{IOCNAME}:PS:*   | ProcServCtrl PVs for IOC {IOCNAME} |
| IN:{INST}:CS:GATEWAY:EXTERNAL:*   | Gateway special PVs for the external gateway |
| IN:{INST}:CS:GATEWAY:BLOCKSERVER:*    | Gateway special PVs for the blockserver gateway |
| IN:{INST}:CS:SCAN:ACTIVE  | where to put scan related variables? |
| IN:{INST}:CS:PS:{IOCNAME}:*   | variables created by PROCSERVCTRL IOC for starting/stopping IOCs via procServ |

# The IN:{INST}:MOT:* sub domain

| IN:{INST}:MOT:MTRccmm | Epics motor records for motor on controller number cc, motor number mm. These numbers are zero padded to two digits and star from 1 e.g. MTR0101 is the first motor on the first controller |
| IN:{INST}:MOT:JAWSmm  | First set of jaws e.g. JAWS01 |
| IN:{INST}:MOT:DMCcc   | Galil specific controller variables for controller cc |
| IN:{INST}:MOT:STOPALL | stop all motion |

# Standard signal names

If a value can fluctuate, these refer to the current measured value of a quantity and the suffixes SP and RBV are used to indicated the desired value software requested (setpoint) and the desired value being used in the hardware (RBV)

| Signal Name   | Meaning   | Valid Units |
|...|...|...|
| POS   | Position |    M, mm, cm |
| STAT  | Status, State | Open, Closed, On, Off, Ok, Error |
| CURR  | Current | A, mA, uA |
| VOLT  | Voltage | kV, V |
| CMD   | Device command e.g. write to this to perform an action, such as start/stop a run | |  
| SEL   | Select mode or position | |
| TEMP  | Temperature   | |
| COUNT | Counter value, neutron counts | |
| COUNTD    | Counter value as a distribution, i.e. divided by bin width - so neutron counts per microsecond for example | |
| P, I, D |     P, I, D values on e.g. eurotherm | |
| TOF | Time of flight axis for a spectrum  | |
| TIME | An absolute timestamp , preferably in ISO8601 format | |



# Purpose

Remote IOCs are used when:
- There is a piece of equipment that is mobile (i.e. not a permanent part of any beamline)
- Diagnostics from the equipment are useful even when it is not connected to any beamline
- The kit is physically capable of running an IOC

The first piece of equipment to use this is likely to be the Triton dilution fridges.

# Architecture:

### Setting configuration parameters (macros, pv sets, etc)

Local PC (NDX instrument control computer):
- User edits configuration in GUI. There is a new option to select the "remote pv prefix" - if non-empty, this signifies that the IOC will run remotely.
- The local blockserver recieves the configuration and saves it as normal. The "remote pv prefix" property is stored in the configuration XML.
- The blockserver does not stop/start/restart any local IOC if it is marked as having a remote PV prefix.

Remote PC:
- The remote PC is configured to monitor a given instrument. This configuration must be done locally (on the remote PC). Currently this is done by `caput -S %MYPVPREFIX%REMIOC:INSTRUMENT TE:NDW1799:` to monitor `NDW1799`'s configuration.
- The remote ioc server sets up an EPICS monitor on the blockserver of the configured instrument
- When the remote ioc server gets a monitor, it writes the parts of the config which have the same remote pv prefix as itself to file (in XML format, same as what the blockserver uses).
- After writing the config XML, it restarts all of the IOCs which it's looking after

### Instrument archive

To be done in https://github.com/ISISComputingGroup/IBEX/issues/4465

### Ioc running status

To be done in https://github.com/ISISComputingGroup/IBEX/issues/4467

### Interesting PVs

To be done in https://github.com/ISISComputingGroup/IBEX/issues/4468

### Alarms

To be done in https://github.com/ISISComputingGroup/IBEX/issues/4466

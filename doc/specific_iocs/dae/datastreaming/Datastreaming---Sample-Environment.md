# Sample environment forwarding

All IBEX instruments are currently forwarding their sample environment PVs into Kafka. This is done in two parts:

### BlockserverToKafka
This is a Python process that runs on each NDX (see code [here](https://github.com/ISISComputingGroup/EPICS-inst_servers/tree/master/BlockServerToKafka)) it monitors the blockserver config PVs and any time the config changes it pushes a new configuration to the forwarder, via a Kafka topic `forwarder_config`. This is a process written and managed by IBEX developers.

The instrument name for the BlockServerToKafka service is `BSKAFKA`. 

### Forwarder
This is a Python program responsible for taking the EPICS data and pushing into Kafka. ISIS currently has two instances of the forwarder running (one for the production and one for development). They are both running as services (Developer Forwarder and Production Forwarder) under `nssm` on NDADATASTREAM, which can be accessed via the `ibexbuilder` account. The configuration files and logs for these forwarders are located in `C:\Forwarder\dev_forwarder` and `C:\Forwarder\prod_forwarder`. The actual source lives in `C:\forwarder\fw_py`, updating it is a case of running `git pull` and re-installing the requirements. 

Source for the forwarder is available [here](https://github.com/ess-dmsc/forwarder)

On NDADATASTREAM the forwarder is run as a service with `nssm` - this is responsible for things like log file rotation and configuring which config files are used with the forwarder. To edit these services run `nssm edit ProdForwarder` or `nssm edit DevForwarder` which will open a GUI for doing so. 
To start/stop/restart the services use `nssm [start/stop/restart] [service name]` 

_NB: The forwarder was previously written in C++ but has now migrated to Python instead._
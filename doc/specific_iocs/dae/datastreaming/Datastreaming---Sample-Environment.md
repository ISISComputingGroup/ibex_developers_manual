# Sample environment forwarding

All IBEX instruments are currently forwarding their sample environment PVs into Kafka. This is done in two parts:

{#bskafka}
## BlockserverToKafka

This is a Python process that runs on each NDX (see code [here](https://github.com/ISISComputingGroup/EPICS-inst_servers/tree/master/BlockServerToKafka)) it monitors the blockserver config PVs and any time the config changes it pushes a new configuration to the forwarder, via a Kafka topic `forwarder_config`. This is a process written and managed by IBEX developers.

The `procserv` name for the BlockServerToKafka service is `BSKAFKA`. 

## Forwarder

Source for the forwarder is available [here](https://github.com/ess-dmsc/forwarder)

We don't currently run this for every instrument, and need to figure out topology ie. running a central forwarder, one per instrument and so on.

### Forwarder on HIFI

HIFI has an instance of the forwarder currently running under procserv within IBEX for the SuperMuSR project.

in `C:\Instrument\Apps\EPICS\utils\build_ioc_startups.py` we have hotfixed this line: 
`ioc_startups.add("FWDR", IocStartup(os.path.join("C:\\", "instrument", "dev", "forwarder"), description="forward epics to kafka", exe="forwarder_launch.bat", iocexe="procServ.exe"))`

to add a Procserv entry that runs it. 

HIFI also has a modified `ISIS/inst_servers/master/start_bs_to_kafka_cmd.bat` which points to the SuperMuSR Redpanda instance. 

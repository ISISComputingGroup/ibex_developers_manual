# Data streaming: Sample environment forwarding

All IBEX instruments are currently forwarding their sample environment PVs into Kafka. This is done in two parts:

{#bskafka}
## BlockserverToKafka

This is a Python process that runs on each NDX (see code [here](https://github.com/ISISComputingGroup/EPICS-inst_servers/tree/master/BlockServerToKafka)) it monitors the blockserver config PVs and any time the config changes it pushes a new configuration to the forwarder, via a Kafka topic `forwarder_config`. This is a process written and managed by IBEX developers.

The `procserv` name for the BlockServerToKafka service is `BSKAFKA`. 

## Forwarder

Source for the forwarder is available [here](https://github.com/ess-dmsc/forwarder)

As of IBEX version 25.8.0 we run this on every instrument under the `FWDR` `procserv` name.

### Forwarder on HIFI

HIFI uses a different broker currently, so we have changed the `KAFKA_BROKER` macro for `BSKAFKA` and `FWDR`. This is currently in `globals.txt`. 

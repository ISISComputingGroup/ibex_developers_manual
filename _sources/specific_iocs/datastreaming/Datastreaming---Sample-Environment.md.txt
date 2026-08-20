# Data streaming: Sample environment forwarding

All IBEX instruments are currently forwarding their sample environment PVs into Kafka.

This will be done in two parts:

{#bskafka}
## Kafka forwarder configurer

Repo [here](https://github.com/ISISComputingGroup/kafka_forwarder_configurer)

This is a Python process which monitors the blockserver config PVs and any time the config changes it pushes a new configuration to the forwarder, to its configuration topic.


## Forwarder

Source for the forwarder is available [here](https://github.com/ISISComputingGroup/forwarder)

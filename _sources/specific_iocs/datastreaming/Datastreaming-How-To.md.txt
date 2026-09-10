{#datastreaminghowto}
# Data streaming: how-to guide

This is a guide for basic operations using either the development or production Kafka clusters we use for data streaming at ISIS. 

Note that there are many ways to do the following, what is written here is the way commonly done at ISIS on our development and production clusters. [Redpanda Console](https://github.com/redpanda-data/console) allows for topic creation etc. which is a web-based application. 

## Topic operations

### Create a new topic

This can be done through Redpanda console or via a Kafka API call. 

### List topics

This can be done through Redpanda console or via a Kafka API call. 

### Viewing or "consuming" data from a topic 

[Saluki](https://github.com/ISISComputingGroup/saluki) can be used for de-serialising the flatbuffers-encoded blobs that are pushed into Kafka.


{#localredpanda}
## Run my own instance of Kafka/Redpanda

This is done easily by running [this](https://docs.redpanda.com/redpanda-labs/docker-compose/single-broker/#run-the-lab) `docker-compose` file.


## Stream event data from the ISISICP
The ICP on any instrument that is running in full event mode and with a DAE3 may stream neutron events into Kafka. This can also be done in simulation mode.

This is controlled using flags in the `isisicp.properties` file:

```
isisicp.kafkastream = true
# if not specified, topicprefix will default to instrument name in code
isisicp.kafkastream.topicprefix =
# FIA team run their kafka cluster on port 31092, not 9092
isisicp.kafkastream.broker = livedata.isis.cclrc.ac.uk:31092
isisicp.kafkastream.topic.suffix.runinfo = _runInfo
isisicp.kafkastream.topic.suffix.sampleenv = _sampleEnv
isisicp.kafkastream.topic.suffix.alarms = _alarms
```

In the same file, you will also need to ensure the following properties are set:

```
isisicp.incrementaleventnexus = true

# Event rate, can adjust up or down
isisicp.simulation.neventssim = 5000

# Ensure simulated data is switched on
isisicp.simulation.simulatedata = true
isisicp.simulation.simulatespec0 = true
isisicp.simulation.simulatebin0 = true
isisicp.simulation.spreadsimevents = true
```

You additionally need to ensure you are running in event mode. You can do this using the DAE tables `wiring_event_ibextest.dat`, `detector_ibextest.dat` & `spectra_ibextest.dat`. Copies of these tables can be found at:

```
\\isis\shares\ISIS_Experiment_Controls\event_mode_tables
```
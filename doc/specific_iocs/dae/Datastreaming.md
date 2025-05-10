# Datastreaming

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

datastreaming/*
```

The datastreaming system is being built as part of in-kind work to ESS. It will be the system that the ESS uses to take data and write it to file - basically their equivalent to the [ICP](/specific_iocs/DAE-and-the-ICP). The system may also replace the ICP at ISIS in the future.

In general the system works by passing both neutron and SE data into [Kafka](https://kafka.apache.org/) and having clients that either view data live (like Mantid) or write the data to file, additional information can be found [here](http://accelconf.web.cern.ch/AccelConf/icalepcs2017/papers/tupha029.pdf) and [here](https://iopscience.iop.org/article/10.1088/1742-6596/1021/1/012013). 

The datastreaming layout proposed looks something like this, not including the Mantid steps or anything before event data is collected:

![](ESSDSLayout.png)

## Datastreaming at ISIS

Part of our in-kind contribution to datastreaming is to test the system in production at ISIS. Currently it is being tested in the following way, with explanations of each component below:

![](ISISDSLayout.png)

## The Kafka Cluster

There is a Kafka cluster at `livedata.isis.cclrc.ac.uk`. Port 9092 is used for the primary Kafka broker. A web interface
is available on port 8080.

The production server auto-creates topics when those topics are produced to; consuming however does not create them.

Credentials for the cluster can be found in Keeper, under `ds streaming container user`. The machine is reachable by
SSH with these credentials.

### Deployment

Deployment is currently onto a machine running in the SCD cloud. Deployment instructions can be found
[in the `ds-containers` repository](https://github.com/isiscomputinggroup/ds-containers).

## Neutron Data

The ICP on any instrument that is running in full event mode and with a DAE3 may stream neutron events into Kafka.

This is controlled using flags in the `isisicp.properties` file:

```
isisicp.kafkastream = true
# if not specified, topicprefix will default to instrument name in code
isisicp.kafkastream.topicprefix =
isisicp.kafkastream.broker = livedata.isis.cclrc.ac.uk:9092
isisicp.kafkastream.topic.suffix.runinfo = _runInfo
isisicp.kafkastream.topic.suffix.sampleenv = _sampleEnv
isisicp.kafkastream.topic.suffix.alarms = _alarms
```

## SE Data

See [Forwarding Sample Environment](datastreaming/Datastreaming---Sample-Environment)

## Filewriting

See [File writing](datastreaming/Datastreaming---File-writing)

## System Tests

Currently system tests are being run to confirm that the start/stop run and event data messages are being sent into
Kafka and that a Nexus file is being written with these events. The Kafka cluster and filewriter are being run in docker
containers for these tests and so must be run on a Windows 10 machine. To run these tests you will need to
install [docker for windows and add yourself as a docker-user](https://docs.docker.com/docker-for-windows/install/#install-docker-desktop-on-windows).

## The future of streaming at ISIS

After the in-kind work finishes and during the handover, there are some proposed changes that affect the layout and
integration of data streaming at ISIS. This diagram is subject to change, but shows a brief overview of what the future
system might look like:

![](FUTUREISISDSLayout.png)

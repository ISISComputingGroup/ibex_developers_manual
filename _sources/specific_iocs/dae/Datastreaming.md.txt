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

## The Kafka Clusters
There are two Kafka clusters, production (`livedata.isis.cclrc.ac.uk:9092`) and development (`tenten.isis.cclrc.ac.uk:9092` or `sakura.isis.cclrc.ac.uk:9092` or `hinata.isis.cclrc.ac.uk:9092`). The development cluster is set up to auto-create topics and so when new developer machines are run up all the required topics will be created. However, the production server does not auto-create topics this means that when a new real instrument comes online corresponding topics must be created on this cluster, which is done as part of the install script. Credentials for both clusters can be found in the keeper shared folder.

### Grafana dashboard
A Grafana dashboard for the production cluster can be found at `madara.isis.cclrc.ac.uk:3000`. This shows the topic data rate and other useful information. Admin credentials can also be found in the sharepoint. 

### Deployment
Deployment involves the use of Ansible playbooks, the playbooks and instructions for using these can be found [here.](https://github.com/ISISComputingGroup/ansible-kafka-centos)

## Neutron Data
The ICP on any instrument that is running in full event mode and with a DAE3 is streaming neutron events into Kafka. 

## SE Data
See [Forwarding Sample Environment](datastreaming/Datastreaming---Sample-Environment)

## Filewriting

See [File writing](datastreaming/Datastreaming---File-writing)

## System Tests
Currently system tests are being run to confirm that the start/stop run and event data messages are being sent into Kafka and that a Nexus file is being written with these events. The Kafka cluster and filewriter are being run in docker containers for these tests and so must be run on a Windows 10 machine. To run these tests you will need to install [docker for windows and add yourself as a docker-user](https://docs.docker.com/docker-for-windows/install/#install-docker-desktop-on-windows).

## The future of streaming at ISIS

After the in-kind work finishes and during the handover, there are some proposed changes that affect the layout and integration of data streaming at ISIS. This diagram is subject to change, but shows a brief overview of what the future system might look like:

![](FUTUREISISDSLayout.png)
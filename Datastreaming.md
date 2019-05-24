> [Wiki](Home) > [The Backend System](The-Backend-System) > [Datastreaming](Datastreaming)

# The Datastreaming Project
The datastreaming system is being built as part of in-kind work to ESS. It will be the system that the ESS uses to take data and write it to file (basically their equivalent to the [ICP](DAE-and-the-ICP)). The system may also replace the ICP at ISIS in the future.

In general the system works by passing both neutron and SE data into [Kafka](https://kafka.apache.org/) and having clients that either view data live (like Mantid) or write the data to file, additional information can be found [here](http://accelconf.web.cern.ch/AccelConf/icalepcs2017/papers/tupha029.pdf) and [here](https://iopscience.iop.org/article/10.1088/1742-6596/1021/1/012013/pdf). 

# Datastreaming at ISIS
Part of our in-kind contribution to datastreaming is to test the system in production at ISIS. Currently it is being tested in the following way:

## The Kafka Clusters
There are two Kafka clusters, production (`livedata.isis.cclrc.ac.uk:9092`) and development (`tenten.isis.cclrc.ac.uk:9092` or `sakura.isis.cclrc.ac.uk:9092` or `hinata.isis.cclrc.ac.uk:9092`). The development cluster is set up to auto-create topics and so when new developer machines are run up all the required topics will be created. However, the production server does not auto-create topics this means that when a new real instrument comes online corresponding topics must be created on this cluster, which is done as part of the install script.

## Neutron Data
The ICP on any instrument that is running in full event mode and with a DAE3 is streaming neutron events into Kafka. 

## SE Data
All IBEX instruments are currently forwarding their sample environment PVs into Kafka. This is done in two parts:

### BlockserverToKafka
This is a Python process that runs on each NDX (see code [here](https://github.com/ISISComputingGroup/EPICS-inst_servers/tree/master/BlockServerToKafka)) it monitors the blockserver config PVs and any time the config changes it pushes a new configuration to the forwarder, via a Kafka topic `forwarder_config`. This is a process written and managed by IBEX developers.

### Forwarder
This is a C++ program responsible for taking the EPICS data and pushing into Kafka. ISIS currently has two instances of the forwarder running (one for the production and one for development). They are both running as services (Developer Forwarder and Production Forwarder) on NDADATASTREAM, which can be accessed via the `ibexbuilder` account. The logs for these forwarders are located in `C:\Forwarder\dev_forwarder` and `C:\Forwarder\prod_forwarder`.
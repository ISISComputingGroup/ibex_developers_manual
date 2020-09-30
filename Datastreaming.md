> [Wiki](Home) > [The Backend System](The-Backend-System) > [Datastreaming](Datastreaming)

# The Datastreaming Project
The datastreaming system is being built as part of in-kind work to ESS. It will be the system that the ESS uses to take data and write it to file - basically their equivalent to the [ICP](DAE-and-the-ICP). The system may also replace the ICP at ISIS in the future.

In general the system works by passing both neutron and SE data into [Kafka](https://kafka.apache.org/) and having clients that either view data live (like Mantid) or write the data to file, additional information can be found [here](http://accelconf.web.cern.ch/AccelConf/icalepcs2017/papers/tupha029.pdf) and [here](https://iopscience.iop.org/article/10.1088/1742-6596/1021/1/012013). 

The datastreaming layout proposed looks something like this, not including the mantid steps or anything before event data is collected:

![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/ESSDSLayout.png)

# Datastreaming at ISIS
Part of our in-kind contribution to datastreaming is to test the system in production at ISIS. Currently it is being tested in the following way, with explanations of each component below:

![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/ISISDSLayout.png)

## The Kafka Clusters
There are two Kafka clusters, production (`livedata.isis.cclrc.ac.uk:9092`) and development (`tenten.isis.cclrc.ac.uk:9092` or `sakura.isis.cclrc.ac.uk:9092` or `hinata.isis.cclrc.ac.uk:9092`). The development cluster is set up to auto-create topics and so when new developer machines are run up all the required topics will be created. However, the production server does not auto-create topics this means that when a new real instrument comes online corresponding topics must be created on this cluster, which is done as part of the install script. Credentials for both clusters can be found in the sharepoint.

### Grafana dashboard
A Grafana dashboard for the production cluster can be found at `madara.isis.cclrc.ac.uk:3000`. This shows the topic data rate and other useful information. Admin credentials can also be found in the sharepoint. 

### Deployment
Deployment involves the use of Ansible playbooks, the playbooks and instructions for using these can be found [here.](https://github.com/ScreamingUdder/ansible-kafka-centos)

## Neutron Data
The ICP on any instrument that is running in full event mode and with a DAE3 is streaming neutron events into Kafka. 

## SE Data
All IBEX instruments are currently forwarding their sample environment PVs into Kafka. This is done in two parts:

### BlockserverToKafka
This is a Python process that runs on each NDX (see code [here](https://github.com/ISISComputingGroup/EPICS-inst_servers/tree/master/BlockServerToKafka)) it monitors the blockserver config PVs and any time the config changes it pushes a new configuration to the forwarder, via a Kafka topic `forwarder_config`. This is a process written and managed by IBEX developers.

The instrument name for the BlockServerToKafka service is `BSKAFKA`. 

### Forwarder
This is a C++ program responsible for taking the EPICS data and pushing into Kafka. ISIS currently has two instances of the forwarder running (one for the production and one for development). They are both running as services (Developer Forwarder and Production Forwarder) on NDADATASTREAM, which can be accessed via the `ibexbuilder` account. The logs for these forwarders are located in `C:\Forwarder\dev_forwarder` and `C:\Forwarder\prod_forwarder`.

## Filewriting
The [filewriter](https://github.com/ess-dmsc/kafka-to-nexus) is responsible for taking the neutron and SE data out of Kafka and writing it to a nexus file. When the ICP ends a run it sends a config message to the filewriter, via kafka, to tell it to start writing to file.

### Notes for trying to get the filewriter working on windows: 
#### trying to run filewriter natively:
- hdf5 conan library does not seem to build under windows, however it's falling over in the conan step
- ess takes ownership of the library 
- did not get any further than this as the conan step failed, the rest of the libraries built
- not sure what is falling over but the hdf5 library can probably be fixed

#### trying to run a docker instance of the filewriter
- DATASTREAM is potentially a VM and recursive hyper-v may not work - confirmed
- Docker desktop does not run on build 14393 which is what it's on
- I don't think this will work as we need hyper v for a windows build
- will continue trying to install docker but so far no luck 
- windows containers are a bit weird and we may just end up with the same problems as #1

following [this link](https://blog.couchbase.com/setup-docker-windows-server-2016/)
1.enabled containers and restarted 
1. installed docker - weird error but seemed to install:
```
Start-Service : Failed to start service 'Docker Engine (docker)'.
At C:\Users\ibexbuilder\update-containerhost.ps1:393 char:5
+     Start-Service -Name $global:DockerServiceName
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OpenError: (System.ServiceProcess.ServiceController:ServiceController) [Start-Service],
   ServiceCommandException
    + FullyQualifiedErrorId : StartServiceFailed,Microsoft.PowerShell.Commands.StartServiceCommand
```

Docker service then does not start and gives this error in logs:
`fatal: Error starting daemon: Error initializing network controller: Error creating default network: HNS failed with error : The object already exists.`

A quick google leads to [this](https://github.com/moby/moby/issues/34018#issuecomment-313790817)

After deleting `hns.data` from `C:\ProgramData\Microsoft\Windows\HNS` and restarting HNS it still does not work and gives the same error.

#### Verdict

The best option here would be to try and get it running natively, as DATASTREAM is a Virtual Machine itself and Docker appears to not work. As well as this, we can then run it with `nssm` which is how we run the forwarder as well, which makes for consistent service management. We could also probably use the log rotation that the forwarder is using which is build into NSSM. 

## System Tests
Currently system tests are being run to confirm that the start/stop run and event data messages are being sent into Kafka and that a Nexus file is being written with these events. The Kafka cluster and filewriter are being run in docker containers for these tests and so must be run on a Windows 10 machine. To run these tests you will need to install [docker for windows and add yourself as a docker-user](https://docs.docker.com/docker-for-windows/install/#install-docker-desktop-on-windows).

## The future of streaming at ISIS

After the in-kind work finishes and during the handover, there are some proposed changes that affect the layout and integration of data streaming at ISIS. This diagram is subject to change, but shows a brief overview of what the future system might look like:

![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/FUTUREISISDSLayout.png)
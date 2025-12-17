# File writing

The [filewriter](https://github.com/ess-dmsc/kafka-to-nexus) is responsible for taking the neutron and SE data out of Kafka and writing it to a nexus file. When the ICP ends a run it sends a config message to the filewriter, via Kafka, to tell it to start writing to file.

There is also a [filewriter written for the SuperMuSR project](https://github.com/ISISNeutronMuon/digital-muon-pipeline/tree/main/nexus-writer) which we may choose to use. This will be decided in [this ticket](https://github.com/ISISComputingGroup/DataStreaming/issues/2) 

We are currently figuring out topology on how to run this, ie one-per-instrument or centrally. This is being done as part of the `MNeuData` project generally, but for HRPD-X we will decide this in [this ticket](https://github.com/ISISComputingGroup/DataStreaming/issues/4)

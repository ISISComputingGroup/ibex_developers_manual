# File writing

The [filewriter](https://github.com/ess-dmsc/kafka-to-nexus) is responsible for taking the neutron and SE data out of Kafka and writing it to a nexus file. When the ICP ends a run it sends a config message to the filewriter, via Kafka, to tell it to start writing to file.

## ISIS-filewriter
https://github.com/ISISComputingGroup/isis-filewriter has been created for an easy setup of the filewriter using docker-compose. it is hardcoded currently and requires the `file_writer_config.ini` file to be changed to point at the `_runInfo` topics manually. To begin with we ran it just pointing at `ZOOM_runInfo`, and it successfully wrote files containing event data. 
Steps to run the docker-compose script can be found in the `README` of the project. 

The isis-filewriter repository also contains some utility scripts for Kafka operations, as well as some test `nexus_structure` files which were used to write files using the filewriter at ISIS. `add_data_to_runinfo` was used to write the config for all of the streams on MERLIN and successfully wrote events, histograms and some sample environment data.


***

## Log of changes and updates to the filewriter deployment and configuration messages
### Notes for trying to get the filewriter working on windows server 2016: 
#### trying to run filewriter natively:
- hdf5 Conan library does not seem to build under windows, however it's falling over in the Conan step
- ess takes ownership of the library 
- did not get any further than this as the Conan step failed, the rest of the libraries built
- not sure what is falling over but the hdf5 library can probably be fixed

#### trying to run a docker instance of the filewriter
- DATASTREAM is potentially a VM and recursive hyper-v may not work - confirmed
- Docker desktop does not run on build 14393 which is what it's on
- I don't think this will work as we need hyper v for a windows build
- will continue trying to install docker but so far no luck 
- windows containers are a bit weird and we may just end up with the same problems as #1

following [this link](https://blog.couchbase.com/setup-docker-windows-server-2016/)

1. Enabled containers and restarted 
1. Installed Docker - weird error but seemed to install:
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

##### Verdict

The best option here would be to try and get it running natively, as DATASTREAM is a Virtual Machine itself and Docker appears to not work. As well as this, we can then run it with `nssm` which is how we run the forwarder as well, which makes for consistent service management. We could also probably use the log rotation that the forwarder is using which is build into NSSM. 

#### Update - 07/10/20
The filewriter is now running in a docker-compose script on NDHSPARE62, this is with Docker desktop rather than the enterprise edition and is not using the LCOW framework. We should think about a more permanent solution, however Docker clearly works on server 2019 and not 2016. NDADATASTREAM is running 2016 so may make sense to update that if we want the filewriter running on it as well. 


#### combine-runinfo (not used)
https://github.com/ISISComputingGroup/combine-runinfo has also been created to workaround the filewriter only being able to point at one configuration topic, so we can use the filewriter for all instruments. combine-runinfo's purpose is to run a [Kafka Stream Processor](https://kafka.apache.org/10/documentation/streams/developer-guide/processor-api.html) to forward all new configuration changes into the `ALL_runInfo` topic to be used with a single instance of the filewriter. 

This project is written in Kotlin and then compiled with Gradle to create a runnable `.jar` file. This is flexible, and we could re-write it in Java if it's used permanently and maintaining another language is an issue. 
#### Update - 08/10/2020
`combine-runinfo` didn't work with the messages from all topics, running the `.jar` gave these errors: 
```
to topic ALL_runInfo due to org.apache.kafka.common.errors.RecordTooLargeException: The message is 3146528 bytes when serialized which is larger than the maximum request size you have configured with the max.request.size configuration.
        at org.apache.kafka.streams.processor.internals.RecordCollectorImpl.recordSendError(RecordCollectorImpl.java:138)
        at org.apache.kafka.streams.processor.internals.RecordCollectorImpl.access$500(RecordCollectorImpl.java:50)
        at org.apache.kafka.streams.processor.internals.RecordCollectorImpl$1.onCompletion(RecordCollectorImpl.java:201)
        at org.apache.kafka.clients.producer.KafkaProducer.doSend(KafkaProducer.java:930)
        at org.apache.kafka.clients.producer.KafkaProducer.send(KafkaProducer.java:856)
        at org.apache.kafka.streams.processor.internals.RecordCollectorImpl.send(RecordCollectorImpl.java:167)
        at org.apache.kafka.streams.processor.internals.RecordCollectorImpl.send(RecordCollectorImpl.java:102)
        at org.apache.kafka.streams.processor.internals.SinkNode.process(SinkNode.java:89)
        at org.apache.kafka.streams.processor.internals.ProcessorContextImpl.forward(ProcessorContextImpl.java:201)
        at org.apache.kafka.streams.processor.internals.ProcessorContextImpl.forward(ProcessorContextImpl.java:180)
        at org.apache.kafka.streams.processor.internals.ProcessorContextImpl.forward(ProcessorContextImpl.java:133)
        at org.apache.kafka.streams.processor.internals.SourceNode.process(SourceNode.java:87)
        at org.apache.kafka.streams.processor.internals.StreamTask.process(StreamTask.java:366)
        ... 5 more
Caused by: org.apache.kafka.common.errors.RecordTooLargeException: The message is 3146528 bytes when serialized which is larger than the maximum request size you have configured with the max.request.size configuration.
```
The `combine-runinfo` was updated to use bytes rather than strings, however this did not solve the message size issue. 
After this it was decided that as we were going to use a python script to modify the runinfo messages anyway to contain sample environment data and so on we may as well just forward the modified run info messages directly into `ALL_runInfo` instead. 

#### Adding ISIS data to the filewriter configuration 
To add static data to the filewriter configuration without directly modifying the ICP's output to the `runInfo` topics a script will be used. Things like instrument name and other fields that do not change between instruments can be added here but there are a few gaps that will need to be streamed:
- Stuff in root of file - things like inst name that can be derived from topic are ok, things that cannot be, like experiment identifier, DAE modes etc 
- Events in `detector1_events` - currently not being forwarded
- Sample environment is tricky - we need to know what blocks to put in the file template, it's not as simple as just going "anything with the PV prefix of IN:ZOOM" although we could add to the script to look at the forwarder status and check in the currently forwarded PVs
- Fields derived from detector events such as `total_counts`

The general structure of the file can be written as this will likely not differ between instruments (at least not much) so this will be added in by the script that forwards to `ALL_runInfo` 

NB. I couldn't use the NeXus-Constructor for this as it no longer takes a NeXus file as an input, the version on master doesn't allow top-level fields or arbitrary groups, and there aren't many things in the ZOOM file for example that are in `/raw_data_1/instrument` which is where the NeXus constructor puts components by default. Because of events also being stored in the entry (`raw_data_1`), the NeXus-Constructor crashes when trying to output to a JSON file as it tries to write the events out which cannot be worked around unless you modify the source code to ignore that particular group. Even with this done the constructor is still quite unresponsive because of the amount of data in the in-memory NeXus file. 

#### Update - 23/10/2020 (end of cycle) 

We managed to get the filewriter to work and output _a_ file containing one of each type of stream (`hs00`, `f142`, `ev42`) on MERLIN, which proved that the data streaming stack could be used at ISIS on a very basic level. For some reason when trying to output all events, histograms and sample environment the filewriter refused to write any sample environment data. at first we thought this was because the forwarder had crashed, which it had, however even with it up and running again the filewriter did not write any `f142` streams. Besides this it did manage to write histograms from 9 monitors at once as well as events from MERLIN. these can be seen in the files on NDHSPARE62. 
Metadata such as start time and other ISIS-specific static data was not added to the file but this could be added easily in the future by the ICP. 



# File writing

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

## Update - 07/10/20
The filewriter is now running in a docker-compose script on NDHSPARE62, this is with Docker desktop rather than the enterprise edition and is not using the LCOW framework. We should think about a more permanent solution, however Docker clearly works on server 2019 and not 2016. NDADATASTREAM is running 2016 so may make sense to update that if we want the filewriter running on it as well. 

### isis-filewriter
https://github.com/ISISComputingGroup/isis-filewriter has been created for an easy setup of the filewriter using docker-compose. it is hardcoded currently and requires the file_writer_config.ini` file to be changed to point at the `_runInfo` topics manually. To begin with we ran it just pointing at ZOOM_runInfo, and it successfully wrote files containing event data. 
Steps to run the docker-compose script can be found in the `README` of the project. 

### combine-runinfo
https://github.com/ISISComputingGroup/combine-runinfo has also been created to workaround the filewriter only being able to point at one configuration topic, so we can use the filewriter for all instruments. combine-runinfo's purpose is to run a [Kafka Stream Processor](https://kafka.apache.org/10/documentation/streams/developer-guide/processor-api.html) to forward all new configuration changes into the `ALL_runInfo` topic to be used with a single instance of the filewriter. 

This project is written in Kotlin and then compiled with Gradle to create a runnable `.jar` file. This is flexible, and we could re-write it in Java if it's used permanently and maintaining another language is an issue. 

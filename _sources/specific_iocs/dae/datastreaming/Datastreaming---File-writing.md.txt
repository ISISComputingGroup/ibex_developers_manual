# File writing

The [filewriter](https://github.com/ess-dmsc/kafka-to-nexus) is responsible for taking the neutron and SE data out of Kafka and writing it to a nexus file. When the ICP ends a run it sends a config message to the filewriter, via Kafka, to tell it to start writing to file.

There is also a [filewriter written for the SuperMuSR project](https://github.com/STFC-ICD-Research-and-Design/supermusr-data-pipeline/tree/main/nexus-writer) which we may choose to use.  

We are currently figuring out topology on how to run this, ie one-per-instrument or a central one. For now it is not deployed or running anywhere.

#### Adding ISIS data to the filewriter configuration 
To add static data to the filewriter configuration without directly modifying the ICP's output to the `runInfo` topics a script will be used. Things like instrument name and other fields that do not change between instruments can be added here but there are a few gaps that will need to be streamed:
- Stuff in root of file - things like inst name that can be derived from topic are ok, things that cannot be, like experiment identifier, DAE modes etc 
- Events in `detector1_events` - currently not being forwarded
- Sample environment is tricky - we need to know what blocks to put in the file template, it's not as simple as just going "anything with the PV prefix of IN:ZOOM" although we could add to the script to look at the forwarder status and check in the currently forwarded PVs
- Fields derived from detector events such as `total_counts`

The general structure of the file can be written as this will likely not differ between instruments (at least not much) so this will be added in by the script that forwards to `ALL_runInfo` 

NB. I couldn't use the NeXus-Constructor for this as it no longer takes a NeXus file as an input, the version on master doesn't allow top-level fields or arbitrary groups, and there aren't many things in the ZOOM file for example that are in `/raw_data_1/instrument` which is where the NeXus constructor puts components by default. Because of events also being stored in the entry (`raw_data_1`), the NeXus-Constructor crashes when trying to output to a JSON file as it tries to write the events out which cannot be worked around unless you modify the source code to ignore that particular group. Even with this done the constructor is still quite unresponsive because of the amount of data in the in-memory NeXus file. 

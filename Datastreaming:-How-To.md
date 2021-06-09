# Data streaming how-to guide
This is a guide for basic operations using either the development or production Kafka clusters we use for data streaming at ISIS. 

Note that there are many ways to do the following, what is written here is the way commonly done at ISIS on our development and production clusters. Something like `kafka-tool` is a nice GUI that will list topics, brokers, etc and create or delete topics. You may have more luck running things like `kafkacat`, `kafkacow` or any of the official Kafka scripts under the [Windows subsystem for linux](https://docs.microsoft.com/en-gb/windows/wsl/install-win10)

## Topic operations

Pushing to one topic does not necessarily mean that the other topics in the cluster receive the data and replicate it, so use with caution. If you need to create a topic that is replicated through all of the topics you should probably follow [this guide](https://coralogix.com/blog/create-kafka-topics-in-3-easy-steps/) by `ssh` on the actual server machines themselves. 

### Create a new topic
There is a script in the [isis-filewriter](https://github.com/ISISComputingGroup/isis-filewriter/tree/master/scripts) repository which will create a script for you. It takes a broker, topic name, and number of partitions (usually 1 partition is fine for a basic topic, more for concurrent streams)

### List topics
To list topics on a broker you need to use the metadata API. GUIs such as offset-explorer can do this quite easily, or you can use [Kafkacat](https://github.com/edenhill/kafkacat) or [Kafkacow](https://github.com/ess-dmsc/kafkacow)

### Viewing or "consuming" data from a topic 
Like above, the best way of doing this programmatically is by using the API in your given language. [Kafkacow](https://github.com/ess-dmsc/kafkacow) does this and de-serialises from the relevant flatbuffers schema the data has been pushed in such as `ev42` for event data. 

# Data streaming how-to guide

This is a guide for basic operations using either the development or production Kafka clusters we use for data streaming at ISIS. 

Note that there are many ways to do the following, what is written here is the way commonly done at ISIS on our development and production clusters. Something like `kafka-tool` is a nice GUI that will list topics, brokers, etc and create or delete topics. You may have more luck running things like `kafkacat`, `kafkacow` or any of the official Kafka scripts under the [Windows subsystem for linux](https://docs.microsoft.com/en-gb/windows/wsl/install-win10)


## Topic operations

### Create a new topic

This can be done through Redpanda console or via a Kafka API call. 

### List topics

This can be done through Redpanda console or via a Kafka API call. 

### Viewing or "consuming" data from a topic 

[Saluki](https://github.com/rerpha/saluki) can be used for deserialising the flatbuffers-encoded blobs that are pushed into Kafka.


{#localredpanda}
## Run my own instance of Kafka/Redpanda

This is done easily by running [this](https://docs.redpanda.com/redpanda-labs/docker-compose/single-broker/#run-the-lab) `docker-compose` file.

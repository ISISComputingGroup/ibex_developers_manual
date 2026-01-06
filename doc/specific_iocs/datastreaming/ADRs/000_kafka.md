# 0 - Kafka

## Status

Accepted

## Context

We need to decide on a technology through which we are going to do data streaming. 

There are several options here: 
- Kafka or kafka compatible solutions such as Redpanda
- Redis
- ZeroMQ/RabbitMQ/ActiveMQ

Within each of these options we need to decide on a serialization format.
Options are: 
- protobuffers
- flatbuffers with ESS schemas
- JSONB
- msgpack
- Avro
- encoded JSON/BSON  


## Decision

We have decided to use a Kafka compatible broker as a streaming platform. This may be either Kafka or Redpanda.

This is because we can lean on the ESS experience in using this technology and may be able to collaborate with them and use shared tools. 
Flatbuffers encoding was performance tested during the in-kind project and showed good performance versus the alternatives at the time. 

We have also decided to serialize the data using the [ESS flatbuffers schemas](https://github.com/ess-dmsc/streaming-data-types) with ISIS additions where necessary. 

Kafka is a broker-based streaming technology - as opposed to brokerless systems which do not keep messages. This allows a Kafka-based system to replay messages or for a consumer to catch up with the 'history' of a stream. We will not retain events in Kafka indefinitely - retention will be tuned to keep a suitable number of messages for our use-cases versus hardware constraints.

## Consequences

What becomes easier or more difficult to do because of this change?

Kafka is indisputably harder to set up than some other simpler alternatives. This is somewhat mitigated by its scaling and redundancy benefits. 
We don't intend to do a large amount in Kafka itself (ie. transforms or stream processors)

The advantage of using Kafka is that we keep much more closely aligned to the ESS, CLF, ANSTO and other facilities who are all using Kafka with Flatbuffers schemas.  

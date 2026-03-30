# Data streaming: topics

We have a number of topics per-instrument on `livedata`, the {ref}`Kafka cluster<kafkacluster>` we use. 

Partition numbers are listed below. For variable partitions this will depend on the throughput requirements of the specific instrument. 

## `_runInfo`

partitions: 1 

This contains run start and run stop flatbuffers blobs. 

Flatbuffers schemas in this topic: 
- [`pl72` - Run start](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/pl72_run_start.fbs)
- [`6s4t` - Run stop](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/6s4t_run_stop.fbs)

## `_rawEvents`

Partitions: variable

This contains _raw_ events (`ev44` schema) and metadata (`pu00`) schema, as emitted by
the streaming control board and the individual detector modules.

Flatbuffers schemas in this topic:
- [`ev44` - Events](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/ev44_events.fbs)
- [`pu00` - Pulse metadata](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/pu00_pulse_metadata.fbs)

## `_events`

partitions: variable

This contains _aggregated_ event data. "Aggregated data" means that the metadata for each frame has been merged,
and events concatenated from a large number of small messages to a smaller number of larger messages.

When sorted by `message_id`, this stream will contain, for each frame:
- One `pu00` message (containing vetos, period number, protons-per-pulse)
- Zero or more `ev44` messages containing the events

See documentation of `kafka-event-aggregator` for more details about precise format of the `_events` stream.

Flatbuffers schemas in this topic:
- [`ev44` - Events](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/ev44_events.fbs)
- [`pu00` - Pulse metadata](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/pu00_pulse_metadata.fbs)

{#topics_sampleenv}
## `_sampleEnv`
 
partitions: 1

This contains sample environment data forwarded from EPICS.
In a `.nxs` file this should end up in `raw_data_1/selog/`

Flatbuffers schemas in this topic: 
- [`f144` - All CA and Scalar PVA data](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/f144_logdata.fbs)
- [`se00` - PVA Arrays](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/se00_data.fbs)
- [`al00` - EPICS alarms](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/al00_alarm.fbs)
- [`ep01` - EPICS connection status](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/ep01_epics_connection.fbs)
- [`un00` - EPICS units](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/un00_units.fbs)

## `_runLog`

partitions: 1 

This contains run metadata forwarded from the ICP. 
In a `.nxs` file this should end up in `raw_data_1/runlog/`

Schemas in this topic match the ones in {ref}`topics_sampleenv`

## `_monitorHistograms`

partitions: variable

This contains monitor histograms.
Flatbuffers schemas in this topic: 
- [`hs01` - Histograms](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/hs01_event_histogram.fbs)

## `_detSpecMap`

partitions: 1

This contains details of the detector-spectrum mapping.
Flatbuffers schemas in this topic: 
- [`df12` - Detector-spectrum mapping](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/df12_det_spec_map.fbs)

## `_areaDetector`

partitions: variable

This is raw `areaDetector` data. It's sent by [this line in `ISISDAE`](https://github.com/ISISComputingGroup/EPICS-ioc/blob/716aada58c972cf0661ab6cebc41fba34d29b806/ISISDAE/iocBoot/iocISISDAE-IOC-01/liveview.cmd#L8)

## `_forwarderConfig`

partitions: 1 

This is the forwarder configuration, sent by {ref}`bskafka`.
Flatbuffers schemas in this topic: 
- [`fc00` - Forwarder configuration](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/fc00_forwarder_config.fbs)

## `_forwarderStatus`

partitions: 1

This is the forwarder status topic which contains details about what PVs the forwarder is forwarding. 
Flatbuffers schemas in this topic: 
- [`x5f2` - General status](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/x5f2_status.fbs)

## `_forwarderStorage`

partitions: 1 

This is the last known forwarder configuration, sent by {ref}`bskafka`. This is for if the forwarder crashes, then it can quickly retrieve its last configuration.
Flatbuffers schemas in this topic: 
- [`fc00` - Forwarder Configuration](https://github.com/ISISComputingGroup/streaming-data-types/tree/master/schemas/fc00_forwarder_config.fbs)

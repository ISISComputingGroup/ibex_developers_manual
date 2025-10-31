# Data streaming topics

We have a number of topics per-instrument on `livedata`, the {ref}`Kafka cluster<kafkacluster>` we use. 

## `_runInfo`

This contains run start and run stop flatbuffers blobs. 

Flatbuffers schemas in this topic: 
- [`pl72` - Run start](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/pl72_run_start.fbs)
- [`6s4t` - Run stop](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/6s4t_run_stop.fbs)

## `_events`

This contains data from event-mode events.

Flatbuffers schemas in this topic:
- [`ev44` - Events](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/ev44_events.fbs)

{#topics_sampleenv}
## `_sampleEnv`

This contains sample environment data forwarded from EPICS.
In a `.nxs` file this should end up in `raw_data_1/selog/`

Flatbuffers schemas in this topic: 
- [`f144` - All CA and Scalar PVA data](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/f144_logdata.fbs)
- [`se00` - PVA Arrays](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/se00_data.fbs)
- [`al00` - EPICS alarms](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/al00_alarm.fbs)
- [`ep01` - EPICS connection status](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/ep01_epics_connection.fbs)
- [`un00` - EPICS units](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/un00_units.fbs)

## `_runLog`

This contains run metadata forwarded from the ICP. 
In a `.nxs` file this should end up in `raw_data_1/runlog/`

Schemas in this topic match the ones in {ref}`topics_sampleenv`

## `_monitorHistograms`

This contains monitor histograms.
Flatbuffers schemas in this topic: 
- [`hs01` - Histograms](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/hs01_event_histogram.fbs)

## `_detSpecMap`

This contains details of the detector-spectrum mapping.
Flatbuffers schemas in this topic: 
- [`df12` - Detector-spectrum mapping](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/df12_det_spec_map.fbs)

## `_areaDetector`

This is raw `areaDetector` data. It's sent by [this line in `ISISDAE`](https://github.com/ISISComputingGroup/EPICS-ioc/blob/716aada58c972cf0661ab6cebc41fba34d29b806/ISISDAE/iocBoot/iocISISDAE-IOC-01/liveview.cmd#L8)

## `_forwarderConfig`

This is the forwarder configuration, sent by {ref}`bskafka`.
Flatbuffers schemas in this topic: 
- [`fc00` - Forwarder configuration](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/fc00_forwarder_config.fbs)

## `_forwarderStatus`

This is the forwarder status topic which contains details about what PVs the forwarder is forwarding. 
Flatbuffers schemas in this topic: 
- [`x5f2` - General status](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/x5f2_status.fbs)

## `_forwarderStorage`

This is the last known forwarder configuration, sent by {ref}`bskafka`. This is for if the forwarder crashes, then it can quickly retrieve its last configuration.
Flatbuffers schemas in this topic: 
- [`fc00` - Forwarder Configuration](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/fc00_forwarder_config.fbs)

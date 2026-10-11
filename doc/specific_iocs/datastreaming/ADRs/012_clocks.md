# 12 - Clocks & Kafka timestamping

## Status

- Accepted

## Context

The streaming system contains many systems with independent clocks. These clocks might not be synchronised with each other.

These include:

**GPS clock** - This clock is plugged into the streaming control board, fanned out to each detector module. It is used
to timestamp the signal indicating the start of a frame (which may come from ISIS or a chopper). It is nominally high
resolution, but operational experience has shown that under failure conditions it can be incorrect by tens of years.

**Streaming server clock** - Local clock on the streaming server. Synchronized only via NTP. Used wherever processes on
the streaming server generate timestamps. In future, this may be multiple clocks, if processes are distributed across
multiple machines.

**NDX clock** - Local clock on the NDX virtual machine. Synchronized only via NTP. Historically has high drift (tens of
seconds) due to running in a VM. Used for EPICS timestamps for sample-environment IOCs.

**Kafka server clock** - Local clock on Kafka server. Used as the Kafka message timestamp if any Kafka topics are
configured to use `LogAppendTime`. This may be *multiple* clocks if the Kafka cluster is distributed across machines.
Synchronized only via NTP.

**Detector-local clocks** - for instruments like SANDALS2 which will stream direct to Kafka from embedded Linux boards,
each board represents another clock, which would be used if Kafka `CreateTime` is used local to that board.

None of the above clocks are guaranteed to be monotonic; NTP may correct time backwards, and GPS time may jump backwards
under foreseeable failure conditions.

### Problem statement

Various consumers need information such as:
- Where in a stream do I seek to for data corresponding to the start of run {math}`R`.
- Is event {math}`E` part of run {math}`R`?
- Is sample environment data {math}`S` part of run {math}`R`?

This information needs to be resilient against foreseeable failure modes, such as:
- GPS time badly wrong (in either direction)
- GPS time discontinuities
- Single-event timestamps badly wrong (in either direction)
- NTP time being corrected forwards/backwards

We must also be able to have run start and stop messages that do not correspond to "now", to support re-writing
yesterday's data with a different filewriter or configuration.

## Decision

We will add infrastructure to ensure that we never need to compare a GPS timestamp against an NTP timestamp for data
collection purposes. We may compare the two timestamp sources for monitoring/diagnostic/alerting purposes.

It is not currently seen as viable to disentangle the possible sources of different NTP timestamps. Instead, we will
set up monitoring and alerting on all relevant servers to monitor the NTP time drift relative to each other. All
servers will be set up with the same upstream NTP servers.

Where appropriate, `LogAppendTime` should be preferred for streams that will need to be seeked later. Unlike
`CreateTime`, `LogAppendTime` ensures Kafka timestamps are monotonic, which is a requirement for seeking streams
reliably.

### Run starts / stops

Run starts and stops will be modified to contain **both** a local timestamp according to the streaming server, and a
GPS timestamp according to the streaming control board. This will require changes to the SCB firmware and
`kafka_dae_control`.

### `event_udp_to_kafka`, `kafka_event_aggregator`

Both processes and their corresponding output streams (`_rawEvents` and `_events`) will be modified to use either Kafka
`CreateTime` or `LogAppendTime` as the Kafka message timestamp. For avoidance of doubt, the timestamp *inside* the
schemas will still be the GPS timestamp.

### Forwarder

The forwarder should use `CreateTime` or `LogAppendTime` as it's _Kafka_ message timestamp, and the EPICS timestamp of
the PV update as the timestamp _inside_ the flatbuffers schemas.

### `kafka_file_writer`

The file-writer will seek streams to offsets based on the Kafka message timestamp (either `CreateTime` or
`LogAppendTime`) of each stream - i.e. an NTP synchronised timestamp. The timestamp to seek *to* is taken from the
payload of the run start/stop message. On run end, it will continue writing up to the Kafka offsets
corresponding to the NTP timestamp in the payload of the run stop message, plus a configurable number of seconds, to
account for latency introduced in `event_udp_to_kafka`, `kafka_event_aggregator`, or in message transmission. This
offset may be relatively generous; it's only negative effect is to delay creation of the final data file, so a number
of seconds is acceptable.

The file-writer will ignore events where the GPS timestamp of the event falls outside the GPS timestamps in the run
start and stop messages.

For sample-environment data, the filewriter will seek the streams according to the Kafka timestamps and write the EPICS
timestamps _inside_ the flatbuffers schemas "as seen". For sample-environment data, over-inclusion is risk-free whereas
under-inclusion may make analysis of the data impossible later.

In the NeXus file, we will need to document whether `start_time` and `stop_time` represent NTP time or GPS time. This
will require discussions with consumers such as Mantid, to ensure that mantid will accept event data that falls outside
the `start_time`-`stop_time` range. We may choose to write additional datasets describing the "other" timestamp.

### `kafka_dae_diagnostics` and other consumers

`kafka_dae_diagnostics` will be modified to look at the new GPS run start/stop timestamps and ignore events with GPS
timestamps falling outside those bounds.

## Risks

- If two NTP-based systems get out of sync with each other, neutron or sample-environment data might be wrongly excluded
from a run.
  - Mitigation: monitoring/alerting of time drift across all relevant NTP-based systems.
- If the GPS timestamp of a run-start is badly wrong, and the event-mode data later corrects itself, the data may be
ignored as falling outside the run.
  - This seems correct behaviour.
  - `kafka_dae_control` may choose to warn or fail to begin the run if the GPS timestamp is very different from it's
local NTP timestamp.
- If GPS timestamps jump, data that is part of a run may be excluded based on the GPS run start/stop times.
  - We will include a metric in the filewriter for rate of events excluded by start/stop time filters. This metric can
then be used to trigger alerts in the monitoring system
  - `kafka_dae_diagnostics` will also exclude the relevant events, leading to a `PROCESSING` state making it obvious
that there is a data-collection problem.
- If latency introduced by `event_udp_to_kafka` or `kafka_event_aggregator` is too high, some events at the end of a run
may be lost. `kafka_dae_diagnostics` will report this latency, as a comparison between the GPS time embedded in the
message and the NTP time that message is processed in `kafka_dae_diagnostics`. This comparison is only used for
monitoring/alerting and user feedback.

## Consequences

- The system is resilient against GPS time desyncing from NTP time
- The system is *not* resilient against large mismatches in NTP time across multiple NTP-based systems - this is
considered a failure condition that will require manual intervention to fix.
  - The system is tolerant of "small" NTP drifts (configurable in filewriter, assumed to be a number of seconds).
- Messages with erroneous GPS timestamps from the distant past are not immediately eligible for Kafka time-based
deletion.

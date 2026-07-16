# 7 - Periods

## Status

Accepted. 

## Context

Periods are used to split up runs. This may be because a scientist wants to scan over several points and keep events separated before data analysis, or it may be for other arbitrary reasons.

In the previous system, periods are 1-indexed to a user. This means that a dashboard can display things like `1/1 periods` if using a single period, or for example `9/12` periods to show a run that is in progress and currently collecting data to period 9. This means that PVs that interface the client and/or `genie_python` need to display as 1-indexed. NeXus files, specifically the `/raw_data_1/framelog/period_log/value` dataset, follow this logic. Conversely, the hardware was 0-indexed, so the ICP had to subtract/add 1 from the served PVs.

## Decision

We will use 0-indexing everywhere internal and 1-indexing for user facing period controls and readbacks:
- The streaming hardware will use zero-indexed periods.
- UDP messages from detectors will use zero-indexed periods.
- Flatbuffers messages, both before and after event_aggregator, will be zero-indexed
- `kafka_dae_control` will use zero-indexed periods everywhere except user-facing PVs (PVs that have no component starting/ending with a `_`), where it will need to do a conversion
- `kafka_dae_diagnostics` will use zero-indexed periods everywhere except user-facing PVs(see above), where it will need to do a conversion
- The filewriter will need to do a conversion internally to remain consistent with old format, such that flatbuffers messages saying "period 0" end up in a frame log called "period 1".

There was a consideration to reserve period 0 as an "unknown" period, similar to how traditionally the 0th detector was reserved for malformed data, however this doesn't make sense in the streaming world and an event without a period should just be discarded by the hardware or UDP to Kafka layer.

## Consequences
- We can use 0-indexed periods as a standard for everything that isn't user facing (and NeXus files which _are_ user facing) which means dealing with arrays is much simpler
- We need to be careful to make sure that the user is shown 1-indexed periods when viewing and setting periods

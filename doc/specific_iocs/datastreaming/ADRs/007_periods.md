# 7 - Periods

## Status

Accepted. 

## Context

Periods are used to split up runs. This may be because a scientist wants to scan over several points and keep events separated before data analysis, or it may be for other arbitrary reasons.

In the previous system, periods are 1-indexed to a user. This means that a dashboard can display things like `1/1 periods` if using a single period, or for example `9/12` periods to show a run that is in progress and currently collecting data to period 9. This means that PVs that interface the client and/or `genie_python` need to display as 1-indexed. Conversely, the hardware was 0-indexed, so the ICP had to subtract 1 from the served PV.

As well as hardware, periods in a NeXus file were previously 0-indexed, which made array slicing more straightforward as most programming languages similarly index starting at 0.

## Decision

We will use 0-indexing everywhere (in hardware, udp format, flatbuffers, nexus files) other than the period PVs served by `kafka_dae_control` and `kafka_dae_diagnostics` which will subtract and add one respectively to set and display period numbers. 

There was a consideration to reserve period 0 as an "unknown" period, similar to how traditionally the 0th detector was reserved for malformed data, however this doesn't make sense in the streaming world and an event without a period should just be discarded by the hardware or UDP to Kafka layer.

## Consequences
- We can use 0-indexed periods as a standard for everything that isn't user facing (and NeXus files which _are_ user facing)
- We need to be careful to make sure that the user is shown 1-indexed periods when viewing and setting periods

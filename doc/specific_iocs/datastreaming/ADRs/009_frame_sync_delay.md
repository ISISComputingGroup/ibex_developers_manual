# 9 - Frame sync delay handling

## Status

Provisional until implemented in firmware & `event_udp_to_kafka`.

## Context

Some instruments use a frame sync delay to shift their data acquisition window, relative to the time of the ISIS pulse.

For example, on HRPD, a typical configuration is:
- SMP timing is used with a 10Hz chopper to achieve a 100ms frame time
- That 100ms window can be shifted in time-of-flight, using a frame sync delay, to cover different time-of-flight ranges, for example:
  - `30_000 - 130_000` μs
  - `100_000 - 200_000` μs
  - `180_000 - 280_000` μs

What the streaming hardware currently emits is:
- The GPS time in the header is the time of the *delayed* frame sync. This means that the GPS time in the header is not the time of the ISIS (or chopper) pulse.
- The individual event timestamps are offsets from the GPS time.

This means that what the streaming hardware emits over UDP is:
- Self-consistent, in the sense that you can _add_ the GPS time in the header with the neutron time to get the correct absolute timestamp for each neutron.
- Not consistent with time-of-flight since the neutron was emitted, since the event time in the UDP data is an offset from some arbitrarily-delayed start time.
- The GPS timestamps in the UDP are not the time of the ISIS (or chopper) timing pulse.

## Decision

The decision is:
- The hardware will emit an additional `frame_sync_delay` field in the UDP header to tell consumers how long the frame sync
was delayed by, relative to the original timing signal which may have been either the ISIS timing pulse or an SMP (chopper) timing pulse.
- `event_udp_to_kafka` will transform timestamps from delayed-frame coordinates into pulse-relative coordinates for this frame sync delay, between when `event_udp_to_kafka` receives the UDP data and when it forms the `_rawData` stream:
  - The reference time as emitted in an `ev44` schema should be `udp_gps_time - frame_sync_delay`
  - The timestamp of each individual neutron event should be `event_timestamp + frame_sync_delay`

---

- `frame_sync_delay` may be greater than one frame period.

## Alternatives rejected

- Make every consumer of the event-stream implement frame sync delay corrections
  - Rejected because it would be easy to forget to do
  this, leading to subtly incorrect data: data would appear shifted in time-of-flight, would be a small shift for small frame sync delays.
- Implement corrections in hardware/firmware - larger firmware change, hardware has limited resources/ability to do this.

## Consequences

- Streaming firmware can keep its existing implementation of frame sync delay, only changing to emit an additional `frame_sync_delay` field in the UDP header.
- `event_udp_to_kafka` will gain additional complexity in applying 'corrections' for frame-sync delay, as part of decoding the
UDP data.
- The event timestamps emitted in `ev44`s from `event_udp_to_kafka` will be time-of-flight offsets from the original ISIS or chopper timing pulse, which is what scientists will expect to see in their event data.
- Adding together the `reference_time` and an individual neutron event timestamp from an `ev44` will still give a correct *absolute* time-of-arrival for that neutron.

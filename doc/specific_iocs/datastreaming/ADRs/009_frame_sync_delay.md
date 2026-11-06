# 9 - Frame sync delay handling

## Status

Accepted.

## Context

Some instruments use a frame sync delay to shift their data acquisition window, relative to the time of the ISIS pulse.

For example, on HRPD, a typical configuration is:
- SMP timing is used with a 10Hz chopper to achieve a 100ms frame time
- That 100ms window can be shifted in time-of-flight, using a frame sync delay, to cover different time-of-flight ranges, for example:
  - `30_000 - 130_000` μs
  - `100_000 - 200_000` μs
  - `180_000 - 280_000` μs

What the streaming hardware currently emits is:
- The GPS time in the header is the time of the *original* frame sync (in other words, the GPS time in the header is the time of the ISIS or chopper timing pulse).
- The individual event timestamps are offsets from `(gps_time + frame_sync_delay)`.

This means that what the streaming hardware emits over UDP is not self-consistent: adding the absolute pulse timestamp
with the neutron event timestamps will not produce correct absolute timestamps for individual neutron events.

## Decision

The decision is:
- The hardware will emit an additional `frame_sync_delay` field in the UDP header to tell consumers how long the frame sync
was delayed by, relative to the original timing signal which may have been either the ISIS timing pulse or an SMP (chopper) timing pulse.
- `event_udp_to_kafka` will transform neutron event timestamps by adding the `frame_sync_delay` to each neutron event's timestamp, which makes these timestamps relative to the pulse time.
- `event_udp_to_kafka` does *not* need to perform any manipulation on the GPS timestamps in the UDP headers of streamed packets; those headers already contain the correct pulse times.

---

- `frame_sync_delay` may be greater than one frame period.

## Alternatives rejected

- Make every consumer of the event-stream implement frame sync delay corrections
  - Rejected because it would be easy to forget to do
  this, leading to subtly incorrect data: data would appear shifted in time-of-flight, would be a small shift for small frame sync delays.
- Implement per-event corrections in hardware/firmware - larger firmware change, hardware has limited resources/ability to do this.

## Consequences

- Streaming firmware can keep its existing implementation of frame sync delay, only changing to emit an additional `frame_sync_delay` field in the UDP header.
- `event_udp_to_kafka` will gain additional complexity in applying 'corrections' for frame-sync delay, for each neutron event, as part of decoding the
UDP data.
- The event timestamps emitted in `ev44`s from `event_udp_to_kafka` will be time-of-flight offsets from the original ISIS or chopper timing pulse, which is what scientists will expect to see in their event data.
- Adding together the `reference_time` and an individual neutron event timestamp from an `ev44` will give a correct *absolute* time-of-arrival for that neutron.

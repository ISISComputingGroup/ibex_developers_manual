# 6 - Event aggregator

## Status

Accepted

## Context

Data (neutron events) and metadata (in particular vetos, period number and protons-per-pulse) may be emitted by
both individual detector modules and by the streaming control board:
- Events will be emitted by each detector module (which has no knowledge of events on other modules)
- Protons-per-pulse and period number will be emitted once per frame by the streaming control board
- Vetos may be emitted by both the streaming control board (global vetos) and each individual detector modules (e.g. local over-count vetos).

To avoid complex logic in every downstream consumer 'zipping' together these disparate pieces of information, we
require some form of 'aggregation' process, which emits 'complete' neutron frames with appropriate (merged) metadata
and the neutron events.

The SuperMuSR project has a comparable requirement, for which they have implemented [`digitizer-aggregator`](https://github.com/ISISNeutronMuon/digital-muon-pipeline/tree/main/digitiser-aggregator).

## Decision

We will satisfy this requirement using [`kafka_event_aggregator`](https://github.com/isisComputingGroup/kafka_event_aggregator).

We considered using the SuperMuSR aggregator directly, however it makes several assumptions that are not valid for
neutron use cases:
- Its event representation is Muon-specific
- It assumes exactly one event message will arrive from each detector in each frame. This is not true in the neutron
case, where we may get zero or one or more messages per frame.
- Some details of metadata formats are different between Neutron & Muon use cases.

## Consequences

- DSG hardware (detectors & streaming control board) will stream to a `_rawEvents` stream
  - This stream will have short, e.g. minutes/hours retention
- [`kafka_event_aggregator`](https://github.com/isisComputingGroup/kafka_event_aggregator) will forward events from `_rawEvents` to the `_events` stream (after combining the metadata and combining events into logical frames)
- Downstream consumers will subscribe to the `_events` stream
  - This stream will have longer retention

{#001_histograms}
# 1 - Histograms and event mode

## Status

Accepted

## Context

**Histogram mode**

In histogram mode, over the course of a run, counts are accumulated into a running histogram, binned by user-specified
time channel boundaries.

**Event mode**

In event mode, over the course of a run, each individual neutron event's detection time and detector ID is recorded.
Event mode data can be later binned to form a histogram, but a histogram cannot be recovered to individual events. In
other words, histogramming is lossy. The advantage of histogram mode is that it typically produces smaller data volumes.

Histogram mode has historically been used because:
- Hardware limitations in DAE2/3 preventing event-mode acquisition at high rates
- Analysis routines in Mantid which may perform poorly on event-mode data

## Decision

For HRPD-x, we will initially stream all data, including data from neutron monitors, in event mode. The Kafka streams will only contain event-mode data.

We will write event-mode Nexus files, however HRPD-X also require histogram-mode Nexus files (not containing neutron events) for their analysis routines.

## Consequences

- Data volumes on HRPD-x will be higher running in event mode compared to histogram mode. This includes both data in-flight
during networking and Kafka processing, as well as final event-mode Nexus file sizes. The histogram file size is independent of number of events.
- Only considering events will simplify components of the HRPD-x data streaming implementation.
- There may be two separate files generated per run, `_event.nxs` and `_histogram.nxs`. The exact naming is to be determined.

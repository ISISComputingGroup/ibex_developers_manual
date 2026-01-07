{#001_histograms}
# 1 - Histograms and event mode

## Status

Current, but may be superseded after HRPD-X.

## Context

**Histogram mode**

In histogram mode, over the course of a run, counts are accumulated into a running histogram, binned by user-specified
time channel boundaries.

**Event mode**

In event mode, over the course of a run, each individual neutron event's detection time and detector ID is recorded.
Event mode data can be later binned to form a histogram, but a histogram cannot be recovered to individual events. In
other words, histogramming is lossy. The advantage of histogram mode is that it typically produces smaller data volumes.

Histogram mode has historically been used due to hardware limitations in many cases.

## Decision

For HRPD-x, we will collect all data, including data from neutron monitors, in event mode only. HRPD-x will not support
histogram mode.

## Consequences

- Data volumes on HRPD-x will be higher running in event mode compared to histogram mode. This includes both data in-flight
during networking and kafka processing, as well as final Nexus file sizes.
- Only considering events will simplify components of the HRPD-x data streaming implementation.

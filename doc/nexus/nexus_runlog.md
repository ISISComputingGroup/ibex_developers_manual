# `raw_data_1/runlog`

This has an `NX_class` of `IXrunlog`; this is not a class specified by upstream NeXus definitions.

Each subgroup is an {external+nexus_manual:doc}`classes/base_classes/NXlog`.

The datasets written are:
- `count_rate` (float32, units="counts")
  - The count rate reported by the DAE, in Millions of events per hour (despite the units attribute)
- `dae_beam_current` (float32, units="uAh")
  - The beam current reported by the DAE
- `good_frames` (int32, units="frames")
  - The cumulative number of good frames so far in this run
- `good_uah_log` (float32, units="uAh")
  - The cumulative number of good uAh so far in this run
- `icp_event` (string, no units)
  - See {doc}`nexus_runlog/nexus_runlog_icpevent` for details about this dataset
- `is_running` (int32, units="none")
  - `1` if the DAE was in the `RUNNING` state, `0` otherwise
- `is_waiting` (int32, units="none")
  - `1` if the DAE was in the `WAITING` state, `0` otherwise
- `monitor_sum_1` (int32, units="counts")
  - Cumulative monitor sum so far in this run
- `np_ratio` (float32, units="none")
  - neutron-proton ratio
- `period` (int32, units="none")
  - The current period
- `raw_frames` (int32, units="frames")
  - The cumulative number of raw frames so far in this run
- `raw_uah_log` (float32, units="uAh")
  - The cumulative number of raw uAh so far in this run
- `run_status` (int32, units="none")
  - The run status as an integer, where
    - `0` is PROCESSING
    - `1` is SETUP
    - `2` is RUNNING
    - `3` is PAUSED
    - `4` is WAITING
    - `5` is VETOING
    - `6` is ENDING
    - `7` is SAVING
- `total_counts` (int32, units="counts")
  - The cumulative number of counts so far in this run

{#nexus_runlog_value}
### `raw_data_1/runlog/<name>/value`

This contains the data for the given parameter.

Attributes:
- `units`: Units specified in the list above

{#nexus_runlog_time}
### `raw_data_1/runlog/<name>/time`

This contains float32 timestamps of the values.

It is written approximately every 30 seconds, and is relative to the start of the run.

Attributes:
- `start`: the start time of the run, for example `"2026-09-09T16:16:57"`
- `units`: `second`

```{toctree}
:hidden:
:glob:

nexus_runlog/*
```

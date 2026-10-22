# `raw_data_1/framelog`

This is an {external+nexus_manual:doc}`classes/base_classes/NXcollection` which contains a set of time-series arrays
with equal sizes, indexed by the frame number. It is only written if event-mode is enabled.
Each subgroup is an {external+nexus_manual:doc}`classes/base_classes/NXlog`.

The datasets written are:
- `events_log` (int32, units="events")
  - The number of events in this frame
- `frame_log` (int32, units="frame_number")
  - The frame number (this will always monotonically increase by 1 for each frame)
- `good_frame_log` (int32, units="is_good")
  - `1` if the frame was a good frame, `0` otherwise
- `period_log` (int32, units="period_number")
  - The period number for each frame
- `proton_charge` (float32, units="uAh")
  - The proton charge delivered by this frame
- `raw_events_log` (int32, units="events")
  - The number of raw events (good+bad) in this frame

{#nexus_framelog_value}
### `raw_data_1/framelog/<name>/value`

This contains the data for the given parameter.

Attributes:
- `units`: Units specified in the list above

{#nexus_framelog_time}
### `raw_data_1/framelog/<name>/time`

This contains float32 timestamps of the values, relative to the start of the run.

It is written once per raw frame.

Attributes:
- `start`: the start time of the run, for example `"2026-09-09T16:16:57"`
- `units`: `second`
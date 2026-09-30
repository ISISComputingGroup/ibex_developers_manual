# `raw_data_1/selog/<name>/value_log`

This is an {external+nexus_manual:doc}`classes/base_classes/NXlog`.

{#nexus_selog_valuelog_name}
### `raw_data_1/selog/<name>/value_log/name`

Under IBEX, this is written as an empty string.

{#nexus_selog_valuelog_value}
### `raw_data_1/selog/<name>/value_log/value`

This is a time-series log of block values. For scalar blocks, this will be a 1-D dataset. For array blocks,
this will be a 2D dataset where the outermost dimension is time.

The datatype may be string or float32, depending on the type of the underlying EPICS block.

Attributes:
- `units`: Units as per the `.EGU` field of the EPICS PV.

{#nexus_selog_valuelog_time}
### `raw_data_1/selog/<name>/value_log/time`

This is a float32 log of the timestamps, relative to the start of the run, when the {ref}`value <nexus_selog_valuelog_value>`
readings were taken. A negative time is used to indicate that the block update happened before the run started.

Attributes:
- `units`: `"second"`
- `start`: Timestamp of the run start, for example `"2026-09-09T08:33:04"`

{#nexus_selog_valuelog_valuevalid}
### `raw_data_1/selog/<name>/value_log/value_valid`

This is a mask, written as an int32, which indicates whether a logged value was 'valid' according to EPICS at the
time it was logged. It is `1` if the value was valid, or `0` otherwise. Values may be invalid due to disconnected
hardware, corrupt responses from hardware, or misconfigurations - an invalid value should not be trusted by downstream
analysis programs.

A value is invalid if it's EPICS severity (per the `.SEVR` field) was greater or equal to 3.

{#nexus_selog_valuelog_alarmtime}
### `raw_data_1/selog/<name>/value_log/alarm_time`

This logs the timestamps of EPICS alarm status or severity changes.

The timestamps here are not necessarily the same as those in {ref}`time <nexus_selog_valuelog_time>`; new entries
in this dataset are only created when the EPICS `.STAT` or `.SEVR` fields change.

Attributes:
- `units`: `"second"`
- `start`: Timestamp of the run start, for example `"2026-09-09T08:33:04"`

{#nexus_selog_valuelog_alarmseverity}
### `raw_data_1/selog/<name>/value_log/alarm_severity`

This logs the string value of the EPICS severity (`.SEVR`) field. This dataset uses the timestamps from
{ref}`alarm_time <nexus_selog_valuelog_alarmtime>`.

{#nexus_selog_valuelog_alarmstatus}
### `raw_data_1/selog/<name>/value_log/alarm_status`

This logs the string value of the EPICS status (`.STAT`) field. This dataset uses the timestamps from
{ref}`alarm_time <nexus_selog_valuelog_alarmtime>`.

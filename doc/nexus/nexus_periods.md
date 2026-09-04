# `raw_data_1/periods`

This has an `NX_class` of `IXperiods`; this is not a class specified by upstream NeXus definitions.

Periods are a way of segregating a run into discrete subcomponents during data acquisition. The run may switch between
periods using a number of hardware or software mechanisms, and may return to a previous period later.

For example, periods may represent spin-up and spin-down measurements, or may be used to separate points during the scan
of a motion axis.

{#nexus_periods_number}
## `raw_data_1/periods/number`

The number of periods configured in the data-acquisition system for this measurement, as an int32.

{#nexus_periods_highest_used}
## `raw_data_1/periods/highest_used`

The maximum period number into which the data acquisition system collected data, as an int32. This is 1-indexed.

For example:
- If five periods were configured and all were used during the data acquisition, `highest_used` would be `5`.
- If five periods were configured, but only the first period was used, `highest_used` would be `1`.

{#nexus_periods_total_counts}
## `raw_data_1/periods/total_counts`

The total number of events counted into each period. This is an array of float32, in units of `Mev` (millions of events).

:::{caution}
The array does **NOT** necessarily have length {ref}`nexus_periods_number`; it instead has a length corresponding to
the number of configured DAQ periods. This may be smaller than or equal to {ref}`nexus_periods_number`. Dwell periods
are omitted from this array.
:::

Attributes:
- `units`: `Mev`

{#nexus_periods_good_frames}
## `raw_data_1/periods/good_frames`

The total number of good frames counted into each period. This is an array of int32.

The array has length {ref}`nexus_periods_number`

{#nexus_periods_raw_frames}
## `raw_data_1/periods/raw_frames`

The total number of raw frames (including both good and vetoed frames) counted into each period. This is an array of int32.

The array has length {ref}`nexus_periods_number`

{#nexus_periods_proton_charge}
## `raw_data_1/periods/proton_charge`

The 'good' proton charge (corresponding to {ref}`nexus_periods_good_frames`) counted into each period. This is an array of float32.

The array has length {ref}`nexus_periods_number`

Attributes:
- `units`: `uAh`

{#nexus_periods_proton_charge_raw}
## `raw_data_1/periods/proton_charge_raw`

The 'raw' proton charge (corresponding to {ref}`nexus_periods_raw_frames`) counted into each period. This is an array of float32.

The array has length {ref}`nexus_periods_number`

Attributes:
- `units`: `uAh`

{#nexus_periods_good_frames_daq}
## `raw_data_1/periods/good_frames_daq`

The total number of good frames counted into each DAQ period. This is an array of int32.

:::{caution}
The array does **NOT** necessarily have length {ref}`nexus_periods_number`; it instead has a length corresponding to
the number of configured DAQ periods. This may be smaller than or equal to {ref}`nexus_periods_number`. Dwell periods
are omitted from this array.
:::

{#nexus_periods_sequences}
## `raw_data_1/periods/sequences`

The total number of period sequences completed. This is an array of int32.

**In software period mode**, this means the number of times each period was changed into. Beginning a run counts as changing
into the initial period.

**In hardware period mode**, this means the number of 'period sequences' - loops of the period sequence - that have completed.
If the run was allowed to reach its maximum configured hardware period sequences, the number of sequences completed will
be that number plus one.

The array has length {ref}`nexus_periods_number`

Examples:
- `[17, 17, 17, 17]`, for a run with 4 hardware periods (DAQ, Dwell, DAQ, Dwell) and configured to run for 16 hardware
period sequences.
- `[1, 3, 0, 0]`, for running in software-period mode with 4 periods and the control sequence:
```
g.begin()
g.pause()
g.change_period(2)
g.change_period(2)
g.change_period(2)
g.resume()
g.end()
```

{#nexus_periods_frames_requested}
## `raw_data_1/periods/frames_requested`

The number of frames that were requested in each period, as an array of int32. **This is only meaningful in hardware period mode**; in software
period mode this may contain arbitrary, non-meaningful, data.

The array has length {ref}`nexus_periods_number`

{#nexus_periods_type}
## `raw_data_1/periods/type`

The number of frames that were requested in each period, as an array of int32. **This is only meaningful in hardware period mode**; in software
period mode this may contain arbitrary, non-meaningful, data.

The period types are:
- `0`: Unused
- `1`: DAQ
- `2`: Dwell

The array has length {ref}`nexus_periods_number`

{#nexus_periods_output}
## `raw_data_1/periods/output`

The binary output configured for each hardware period, as an array of int32. **This is only meaningful in hardware period mode**; in software
period mode this may contain arbitrary, non-meaningful, data.

The array has length {ref}`nexus_periods_number`

{#nexus_periods_labels}
## `raw_data_1/periods/labels`

This is the string 'label' assigned to each hardware period, concatenated together with a `;` character into a single string.
**This is only meaningful in hardware period mode**; in software period mode this may contain arbitrary, non-meaningful, data.

Examples:
- `";;;"` for a run with 4 periods, each having the empty string as a label.
- `"label1;label2;label3;label4"`, for a run with 4 periods, each with a non-empty label.

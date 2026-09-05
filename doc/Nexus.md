# NeXus Files

IBEX writes out scientific data as {external+nexus:doc}`NeXus files <index>`. The NeXus format documents the *general*
layout of a NeXus file; this documentation documents the *specific* datasets written in practice by IBEX,
including any quirks or facility-specific details of their interpretation.

The NeXus files conform, where possible, to the {external+nexus:doc}`TOFRaw` definition.

## Data types

Except where otherwise noted:
- Strings are ASCII-encoded, null terminated.
- Little-endian data types are used.
- 32-bit signed integers or 32-bit floats are used

{#nexus_raw_data_1}
## `raw_data_1`

An ISIS NeXus file always contains a top-level `raw_data_1` group, which is an {external+nexus_manual:doc}`classes/base_classes/NXentry`.
It may contain the datasets and groups listed below:

{#nexus_definition}
### `raw_data_1/definition`

**On a Neutron instrument**: ASCII string containing `TOFRAW`. See {external+nexus_manual:doc}`classes/applications/NXtofraw` for the application
definition this references.

Attributes:
- `version`: `"1.0"`
- `url`: `"http://definition.nexusformat.org/instruments/TOFRAW?version=1.0"`

**On a Muon instrument**: ASCII string containing `pulsedTD`.

Attributes:
- `version`: `"2.0"`
- `url`: `"http://definition.nexusformat.org/instruments/pulsedTD?version=2.0"`

{#nexus_definition_local}
### `raw_data_1/definition_local`

`"ISISTOFRAW"`. See {external+nexus_manual:doc}`classes/applications/NXtofraw` for the application
definition this references.

Attributes:
- `version`: `"1.0"`
- `url`: `"http://svn.isis.rl.ac.uk/instruments/ISISTOFRAW?version=1.0"`

**This dataset is not written on a Muon instrument**.

{#nexus_program_name}
### `raw_data_1/program_name`

`"ISISICP.EXE"` on a DAE2/DAE3 instrument, or the name of the file-writer executable on a data-streaming instrument.

{#nexus_run_number}
### `raw_data_1/run_number`

The run number, as a 32-bit signed integer. For example, for run `POLREF12345`, the run number is `12345`.

{#nexus_run_cycle}
### `raw_data_1/run_cycle`

The ISIS cycle identifier, as a string. For example `24_5` for cycle 2024/05.

{#nexus_title}
### `raw_data_1/title`

The user-provided run title as a string.

For example `"Quiet Counts after DAE fix 24/5"`.

{#nexus_notes}
### `raw_data_1/notes`

The user-provided notes as a string. Commonly empty and written as a zero-length string in that case. Set in IBEX via
Experiment Details -> Sample -> Comments.

{#nexus_name}
### `raw_data_1/name`

The instrument name, for example `POLREF` or `MERLIN`.

Attributes:
- `short_name`: a shortened, typically 3-character, representation of the instrument name. For example, `MERLIN`'s short
name is `MER`.

{#nexus_beamline}
### `raw_data_1/beamline`

The instrument name, for example `POLREF` or `MERLIN`. The instrument name is identical to the {ref}`nexus_name` dataset.
Unlike {ref}`nexus_name`, this dataset does **not** contain a `short_name` attribute.

{#nexus_start_time}
### `raw_data_1/start_time`

The time when data collection started, as an ISO8601 string. For example `2025-03-27T10:56:13`.

Attributes:
- `units`: `"ISO8601"`

{#nexus_end_time}
### `raw_data_1/end_time`

The time when data collection ended, as an ISO8601 string. For example `2025-03-27T10:56:13`.

Attributes:
- `units`: `"ISO8601"`

{#nexus_duration}
### `raw_data_1/duration`

The duration of the measurement, as a float32. Identical to {ref}`nexus_collection_time`. This is not necessarily equal to the difference between {ref}`nexus_start_time` and
{ref}`nexus_end_time`, because time spent paused or under run control is not included.

Attributes:
- `units`: `"second"`

{#nexus_collection_time}
### `raw_data_1/collection_time`

The duration of the measurement, as a float32. Identical to {ref}`nexus_duration`. This is not necessarily equal to the difference between {ref}`nexus_start_time` and
{ref}`nexus_end_time`, because time spent paused or under run control is not included.

Attributes:
- `units`: `"second"`

{#nexus_proton_charge}
### `raw_data_1/proton_charge`

Accumulated "good" proton charge (i.e. the proton charge corresponding to {ref}`nexus_good_frames`) during the run, as a float32.

Attributes:
- `units`: `"uAh"`

{#nexus_proton_charge_raw}
### `raw_data_1/proton_charge_raw`

Accumulated total proton charge (i.e. the proton charge corresponding to {ref}`nexus_raw_frames`) during the run, as a float32.

Attributes:
- `units`: `"uAh"`

{#nexus_good_frames}
### `raw_data_1/good_frames`

Number of good frames during the run, as an int32.

{#nexus_raw_frames}
### `raw_data_1/raw_frames`

Number of good and vetoed frames during the run, as an int32.

{#nexus_experiment_identifier}
### `raw_data_1/experiment_identifier`

RB number of the run, formatted as a string. For example `"12345678"`

{#nexus_seci_config}
### `raw_data_1/seci_config`

This represents the **IBEX** configuration loaded at the time of the run. The name `seci_config` is historical, as
SECI was the previous control system used before IBEX. IBEX configuration names are user-specified, within a set of rules.
For example, `"Horizontal_HCM_with_Helmholtz_coils"`


### `raw_data_1/measurement_id`

A copy of {ref}`nexus_measurement_id`.

### `raw_data_1/measurement_subid`

A copy of {ref}`nexus_measurement_subid`.

### `raw_data_1/measurement_type`

A copy of {ref}`nexus_measurement_type`.

### `raw_data_1/measurement_first_run`

A copy of {ref}`nexus_measurement_first_run`.

### `raw_data_1/measurement_label`

A copy of {ref}`nexus_measurement_label`.

### `raw_data_1/script_name`

This is user-settable string metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Script Name.

---

The top-level {ref}`nexus_raw_data_1` {external+nexus_manual:doc}`classes/base_classes/NXentry` also contains the following groups,
which are documented on their own pages:

```{toctree}
:glob:
:titlesonly:

nexus/*
```

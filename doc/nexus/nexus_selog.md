{#nexus_selog}
# `raw_data_1/selog`

This has an `NX_class` of `IXselog`; this is not a class specified by upstream NeXus definitions. Each block is
a group with an `NX_class` of `IXseblock`, which is also not a standard NeXus class.

The list of blocks to be written is defined by the IBEX configuration, and is user-editable in IBEX.

In addition to the list of blocks from IBEX, the following logs are written:
- `EPICS_PUTLOG`: a string log containing the EPICS channel access put log, with each put operation as a string.
- `ICP_DAE_TD`: This describes the difference between the DAE's internal clock and a *monotonic* software clock
- `IDP_SYS_TD`: This describes the difference between the *monotonic* software clock and an (NTP-corrected) system clock

Each `IXseblock` contains the following datasets:

{#nexus_selog_viname}
### `raw_data_1/selog/<name>/vi_name`

Under IBEX, this is always written as an empty string. It was previously used to refer to the
filepath of a LabVIEW VI responsible for serving this data.

{#nexus_selog_readcontrol}
### `raw_data_1/selog/<name>/read_control`

Under IBEX, this is always written as an empty string. It was previously used to refer to the
path to this data within a LabVIEW VI.

{#nexus_selog_setcontrol}
### `raw_data_1/selog/<name>/set_control`

Under IBEX, this is always written as an empty string. It was previously used to refer to the
path to this data within a LabVIEW VI.

{#nexus_selog_value}
### `raw_data_1/selog/<name>/value`

The latest value of the block **in each period**, as an array.
This is written with a datatype corresponding to the underlying EPICS type.

For example, the array `[12.34, 56.78]` means that the most recent value while the instrument was in period 1 was `12.34`,
and the most recent value while the instrument was in period 2 was `56.78`

Attributes:
- `units`: Engineering units of the block, as per EPICS `.EGU` field.

{#nexus_selog_valuespread}
### `raw_data_1/selog/<name>/value_spread`

The difference between the minimum recorded value and maximum recorded value for a block **in each period**, as an array.
This dataset is only written if the underlying EPICS type is numeric.

For example, the array `[1.23, 0]` means that:
- The difference between the min and max values recorded *while the instrument was in period 1* was `1.23`
- The difference between the min and max values recorded *while the instrument was in period 2* was zero.

Attributes:
- `units`: Engineering units of the block, as per EPICS `.EGU` field.

{#nexus_selog_setpoint}
### `raw_data_1/selog/<name>/setpoint`

The latest setpoint value of a block **in each period**, as an array.
This is written with a datatype corresponding to the underlying EPICS type.

Attributes:
- `units`: Engineering units of the block, as per EPICS `.EGU` field.

{#nexus_selog_setpointspread}
### `raw_data_1/selog/<name>/setpoint_spread`

The difference between the minimum recorded value and maximum setpoint values for a block **in each period**, as an array.
This dataset is only written if the underlying EPICS type is numeric.

Attributes:
- `units`: Engineering units of the block, as per EPICS `.EGU` field.

---

The selog group also contains the following groups:

```{toctree}
:glob:
:titlesonly:

nexus_selog/*
```

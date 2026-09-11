{#nexus_instrument_dae_vetos}
# `raw_data_1/instrument/dae/vetos`

This is an `IXvetos` class, which is a non-standard NeXus class.

### `raw_data_1/instrument/dae/<veto_name>`

There are one or more of these datasets, each describing a single veto called `<veto_name>`.

The dataset contains the number of frames in the run vetoed by this specific veto, as an int32.

Attributes:
- `enabled` (int32) - `1` if the veto was enabled, or `0` if it was disabled at the end of the run. Note that veto enablement may have changed mid-run.

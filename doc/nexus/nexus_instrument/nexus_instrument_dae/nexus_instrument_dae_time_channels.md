# `raw_data_1/instrument/dae/time_channels_<N>`

This is an `IXtime_channels` class, which is a non-standard NeXus class.

{#nexus_instrument_dae_time_channels_tof}
### `raw_data_1/instrument/dae/time_channels_<N>/time_of_flight`

Bin-edges used by histogramming for time channel set N, as a float32. This histogramming may have been performed either in hardware or
in software. This is only written on a Neutron instrument.

Attributes:
- `units`: `"microsecond"`
- `axis`: `1`
- `primary`: `1`

{#nexus_instrument_dae_time_channels_tofraw}
### `raw_data_1/instrument/dae/time_channels_<N>/time_of_flight_raw`

Bin-edges used by histogramming for time channel set N, as an int32. For ICP-written files, this represents a multiple of the DAE clock frequency,
and the underlying binning as passed to hardware.
This dataset is **not** necessarily in cycles of a 32 MHz clock as the `frequency` attribute would indicate.

This is only written on a Neutron instrument.

Attributes:
- `units`: `"pulses"`
- `frequency`: `"32 MHz"`

{#nexus_instrument_dae_time_channels_rawtime}
### `raw_data_1/instrument/dae/time_channels_<N>/raw_time`

Bin-edges used by histogramming for time channel set N, as a float32. This histogramming may have been performed either in hardware or
in software. This is only written on a Muon instrument.

Attributes:
- `units`: `"microsecond"`

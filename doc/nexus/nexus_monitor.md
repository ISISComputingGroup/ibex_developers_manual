# `raw_data_1/monitor_<N>`

This is an {external+nexus_manual:doc}`classes/base_classes/NXmonitor`.

Monitors are numbered from 1; the groups are called `monitor_1`, `monitor_2`, and so on.

{#nexus_monitor_data}
### `raw_data_1/monitor_<N>/data`

An int32 array with dimensions (number of DAQ periods, number of time channels) containing the histogrammed counts
for this monitor.

Attributes:
- `axes`:
  - `period_index,spectrum_index,raw_time` on a neutron instrument
  - `period_index,spectrum_index,time_of_flight` on a muon instrument
- `long_name`: `"positron counts"` (only written on a muon instrument)

{#nexus_monitor_monnum}
### `raw_data_1/monitor_<N>/monitor_number`

An int32 monitor number.

The `raw_data_1/monitor_<N>/monitor_number` dataset always has value `N`.

{#nexus_monitor_period_index}
### `raw_data_1/monitor_<N>/period_index`

This is a NeXus link to {ref}`nexus_instrument_dae_period_index`.

{#nexus_monitor_spectrum_index}
### `raw_data_1/monitor_<N>/spectrum_index`

This is a scalar int32 dataset describing which spectrum this monitor corresponds to.

{#nexus_monitor_tof}
### `raw_data_1/monitor_<N>/time_of_flight`

This is a NeXus link to {ref}`nexus_instrument_dae_time_channels_tof`.

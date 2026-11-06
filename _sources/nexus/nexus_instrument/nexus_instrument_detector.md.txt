# `raw_data_1/instrument/detector_<N>`

This is a {external+nexus_manual:doc}`classes/base_classes/NXdetector`.

Spectra are grouped into different `detector_<N>` groups based on the time-regime set they share. In other words,
`detector_N` contains data from all spectra configured to use time regime `N`.

{#nexus_instrument_detector_counts}
### `raw_data_1/instrument/detector_<N>/counts`

This is the histogram data for detector N, as int32 counts. It has dimensions `periods,spectra,time_channels`, where periods is the number
of DAQ periods (which may be different from the *total* number of periods).

This is written only if histograms were requested.

Attributes:
- `units`: `"counts"`
- `signal`: `1`
- `axes`: 
  - On a muon instrument: `"period_index,spectrum_index,raw_time"`
  - On a neutron instrument: `"period_index,spectrum_index,time_of_flight"`
- `long_name`: `"positron_counts"` (written on Muon instruments only)

{#nexus_instrument_detector_spectrum_index}
### `raw_data_1/instrument/detector_<N>/spectrum_index`

Mapping of array position in the {ref}`histogram array <nexus_instrument_detector_counts>` to spectrum IDs, as an int32.

### Muon-specific datasets

:::{caution}
TODO
:::

{#nexus_instrument_detector_period_index}
### `raw_data_1/instrument/detector_<N>/period_index`

This is a NeXus link to {ref}`nexus_instrument_dae_period_index`.

{#nexus_instrument_detector_tof}
### `raw_data_1/instrument/detector_<N>/time_of_flight`

This is a NeXus link to {ref}`nexus_instrument_dae_time_channels_tof`.

{#nexus_instrument_detector_tofraw}
### `raw_data_1/instrument/detector_<N>/time_of_flight_raw`

This is a NeXus link to {ref}`nexus_instrument_dae_time_channels_tofraw`.

It is only written on Neutron instruments.

{#nexus_instrument_detector_sourcedetdist}
### `raw_data_1/instrument/detector_<N>/source_detector_distance`

This is user-settable float32 metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Detector Distance

:::{caution}
The parameter name in the NeXus file is the *source*-detector distance, whereas in IBEX it is called the *sample*-detector distance.
This is only consistent it one interprets the "source" of the scattered radiation as being the sample.
:::

{#nexus_instrument_detector_polarangle}
### `raw_data_1/instrument/detector_<N>/polar_angle`

This is the average polar angle (two-theta) of a spectrum, as a float32. It is an average because a spectrum may be
made from multiple detector pixels.

Attributes:
- `units`: `"degree"`

{#nexus_instrument_detector_distance}
### `raw_data_1/instrument/detector_<N>/distance`

This is the L2 flight path of a spectrum, as a float32. It is an average because a spectrum may be
made from multiple detector pixels.

Attributes:
- `units`: `"metre"`

{#nexus_instrument_detector_delt}
### `raw_data_1/instrument/detector_<N>/delt`

This is the "hold-off time" of a spectrum, as a float32. It is an average because a spectrum may be
made from multiple detector pixels. It is in `us`, but a units attribute is not written.

{#nexus_instrument_detector_azangle}
### `raw_data_1/instrument/detector_<N>/azimuthal_angle`

This is the azimuthal angle of a spectrum, as a float32. It is an average because a spectrum may be
made from multiple detector pixels.

Attributes:
- `units`: `"degree"`

{#nexus_instrument_detector_usertable}
### `raw_data_1/instrument/detector_<N>/user_table<N>`

These are arbitrary user-specified tables for each detector, as a float32. It is an average because a spectrum may be
made from multiple detector pixels.

User tables start from `user_table01`.

`user_table01` is always equivalent to {ref}`nexus_instrument_detector_azangle`.

{#nexus_instrument_detector_eventframenumber}
### `raw_data_1/instrument/detector_<N>/event_frame_number`

This is the frame number corresponding to each entry in {ref}`nexus_detevents_eventtimezero`, as an int32. It always
increments by 1 for each frame.

This is only written in event mode. See also {external+nexus_manual:doc}`classes/base_classes/NXevent_data`.

{#nexus_instrument_detector_eventid}
### `raw_data_1/instrument/detector_<N>/event_id`

This is the *spectrum* (not *detector*) that each event was detected on.

This is only written in event mode. See also {external+nexus_manual:doc}`classes/base_classes/NXevent_data`.

{#nexus_instrument_detector_eventindex}
### `raw_data_1/instrument/detector_<N>/event_index`

The index into the event_time_offset, event_id pair for the pulse occurring at the matching entry in event_time_zero.

This is only written in event mode. See also {external+nexus_manual:doc}`classes/base_classes/NXevent_data`.

{#nexus_instrument_detector_eventtimezero}
### `raw_data_1/instrument/detector_<N>/event_time_zero`

This is the time that each pulse started, as float32 microseconds, with respect to the offset which is the beginning
of a run.

This is only written in event mode. See also {external+nexus_manual:doc}`classes/base_classes/NXevent_data`.

Attributes:
- `offset`: The start of run timestamp, for example `"2025-03-27T13:38:28"`
- `units`: `"second"`

{#nexus_instrument_detector_eventtimeoffset}
### `raw_data_1/instrument/detector_<N>/event_time_offset`

This is the timestamp of each event, as float32 microseconds, with respect to the offset in {ref}`nexus_instrument_detector_eventtimezero`.

This is only written in event mode. See also {external+nexus_manual:doc}`classes/base_classes/NXevent_data`.

Attributes:
- `units`: `"second"`

{#nexus_instrument_detector_eventtimeoffsetshift}
### `raw_data_1/instrument/detector_<N>/event_time_offset_shift`

This dataset contains the string `"random"` if event time offsets have been assigned a randomised position within the
time bin given by {ref}`nexus_detevents_eventtimebins`.

This randomisation is needed to avoid artefacts in downstream reduction software when using event-mode hardware with a
low resolution clock (for example DAE2/3).

This is only written in event mode. 

{#nexus_instrument_detector_totalcounts}
### `raw_data_1/instrument/detector_<N>/total_counts`

This dataset contains the total number of event-mode events, as an int64. It is equal to the length of the
{ref}`event_time_offset <nexus_instrument_detector_eventtimeoffset>` or {ref}`event_id <nexus_instrument_detector_eventid>` datasets.

This is only written in event mode. 

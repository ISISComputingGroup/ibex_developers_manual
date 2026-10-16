# 2 - Wiring and Spectra mapping

## Status

Partially accepted (wiring table format and file locations still TBD) - revised in October 2026.

## Context

Wiring tables were traditionally used for configuring the acquisition hardware, previously DAE2/3, by mapping physical detector cards to a detector (or pixel) ID.

This is a concept that still exists in the streaming pipeline however the format is now different (`.csv` as opposed to the old wiring table format). 

The options that we're considering are:
- change `.csv` to align with the old format
- write a service/script to convert to/from `.csv`
- keep the two formats separate, acknowledging that they will not be backwards or forwards compatible

Spectra are an abstraction on top of the detector ID numbering - see {ref}`daespectra` for more information.

Spectra files share the above considerations as they also use a different file format.

Grouping spectra in hardware was primarily used to get around limitations of DAE hardware. However, there are some other uses cases:
- reducing the size of histograms
- mapping out detectors which are not useful for the particular experiment/run 
- grouping several detector pixels together to create one region

The last two points apply to event mode. We are not planning on streaming histogram mode data, but will histogram in the file writer (see {ref}`001_histograms`).

Previously both files used a `.dat` extension, which were loaded by the ICP which would error if they were not valid.


## Decision

We are not going to support the old-style spectra files at runtime.

We will use JSON to map detector IDs to spectra numbers, as this means we can use an industry-standard file format and its surrounding tools. A JSON schema will be written for validation, and loading into `kafka_dae_control` should be trivial.

`kafka_dae_control` will send this information once at run start, as part of the [`detector_spectrum_map`](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/pl72_run_start.fbs#L28) field, to be used by downstream consumers (`event_aggregator`, `file_writer` and `kafka_dae_diagnostics`). This information will only be sent at the start of the run - we do not support changing this mapping during in a run in any way.

We may write a converter script to convert from the old file format if a use case shows up that requires it - this should be very simple.

For wiring tables this is TBD in https://github.com/ISISComputingGroup/DataStreaming/issues/27.

We are deferring where beamline-specific files such as these and application configuration lives in a further ADR. This ADR should be updated when it is created.

## Consequences
- `kafka_dae_control` will need to load and validate files
- `kafka_dae_control` will need some logic to find the largest spectrum number, add 1 to it (to cater for spectrum 0) and use this for the `n_spectra` field of the [`df12_det_spec_map` schema](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/df12_det_spec_map.fbs).
  - There may be missing spectra from the `spectrum` array - this will need to be dealt with by consumers to fill in the blank spectra for histogram spectra dimension and datasets within files.
- Whoever is responsible for writing the spectra mapping files can validate them externally before they are loaded in to `kafka_dae_control`
- downstream consumers will require changes: 
  - `event_aggregator` - this will need to do the mapping during aggregation from the `rawEvents` stream so that any event messages have their `pixel_id` filled out as the **Spectrum number**, not the detector ID. 
    - the alternative to this is that you stream detector IDs and have to perform the mapping in all of your consumers. We considered this but ultimately chose to do it once as that seemed more efficient and consistent among consumers. They can also backtrack using the run-start detector spectrum mapping. 
  - `kafka_dae_diagnostics` - this will need create it's n-dimensional array, whose length is based on the `n_spectra` field, on a run start. it will then need to treat `pixel_id` as the spectrum number for events when indexing that array.
  - `file_writer` - this will need to fill in the spectra mapping in order to write the events, particularly the `event_id` field of a  [`NXevent_data`](https://manual.nexusformat.org/classes/base_classes/NXevent_data.html). 

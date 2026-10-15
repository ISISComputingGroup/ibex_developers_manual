# 2 - Wiring and Spectra mapping

## Status

Partially accepted (wiring table format still TBD)

## Context

Wiring tables were traditionally used for configuring the acquisition hardware, previously DAE2/3, by mapping physical detector cards to a detector (or pixel) ID.

This is a concept that still exists in the streaming pipeline however the format is now different (`.csv` as opposed to the old wiring table format). 

The options that we're considering are:
- change `.csv` to align with the old format
- write a service/script to convert to/from `.csv`
- keep the two formats separate, acknowledging that they will not be backwards or forwards compatible

Spectra are an abstraction on top of the detector ID numbering - see {ref}`daespectra` for more information.

Spectra files share the above considerations as they also use a different file format.

Grouping spectra in hardware was primarily used to get around limitations of DAE hardware. However, we need to support histogram mode, which can use spectra mapping for:
- reducing the size of histograms
- mapping out detectors which are not useful for the particular experiment/run 
- grouping several detector pixels together to create one region

The last two points apply to event mode too.

Previously both files used a `.dat` extension, which were loaded by the ICP which would error if they were not valid.


## Decision

We are not going to support the old-style spectra files at runtime.

We will use JSON to map detector IDs to spectra numbers, as this means we can use an industry-standard file format and its surrounding tools. A JSON schema will be written for validation, and loading into `kafka_dae_control` should be trivial.

`kafka_dae_control` will send this information once at run start, as part of the [`detector_spectrum_map`](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/pl72_run_start.fbs#L28) field, to be used by downstream consumers. This information will only be sent at the start of the run - we do not support changing this mapping during in a run in any way.

We may write a converter script to convert from the old file format if a use case shows up that requires it - this should be very simple.

For wiring tables this is TBD in https://github.com/ISISComputingGroup/DataStreaming/issues/27.

## Consequences
- `kafka_dae_control` will need to load and validate files
- `kafka_dae_control` will need some logic to find the largest spectrum number, add 1 to it (to cater for spectrum 0) and use this for the `n_spectra` field of the [`df12_det_spec_map` schema](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/df12_det_spec_map.fbs).
  - There may be missing spectra from the `spectrum` array - this will need to be dealt with by consumers to fill in the blank spectra for histogram spectra dimension and datasets within files.
- Whoever is responsible for writing the spectra mapping files can validate them externally before they are loaded in to `kafka_dae_control`

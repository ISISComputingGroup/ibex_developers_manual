# `raw_data_1/instrument/dae`

This has an `NX_class` of `IXdae`; this is not a class specified by upstream NeXus definitions.

{#nexus_instrument_dae_detector_table_file}
### `raw_data_1/instrument/dae/detector_table_file`

This is a filepath to a 'detector table', from a location accessible by the data acquisition system. A detector table
specifies metadata, for example flight path length or two theta, for each detector pixel.

For example, `"C:/Instrument/Settings/config/DEMO/configurations/tables/RCPTT_detector128.dat"`

NeXus consumers should treat this as metadata, and should not assume that they will be able to read the file pointed at.

{#nexus_instrument_dae_spectra_table_file}
### `raw_data_1/instrument/dae/spectra_table_file`

This is a filepath to a 'spectra table', from a location accessible by the data acquisition system. A spectra table
defines the mapping between a physical hardware pixel, and a 'spectrum', which may represent one or more pixels grouped
together.

For example, `"C:/Instrument/Settings/config/DEMO/configurations/tables/RCPTT_spectra128.dat"`

NeXus consumers should treat this as metadata, and should not assume that they will be able to read the file pointed at.

{#nexus_instrument_dae_wiring_table_file}
### `raw_data_1/instrument/dae/wiring_table_file`

This is a filepath to a 'wiring table', from a location accessible by the data acquisition system. A wiring table
defines a mapping between an electronics channel/crate/card/location, to a pixel identifier.

For example, `"C:/Instrument/Settings/config/DEMO/configurations/tables/RCPTT_wiring128.dat"`

NeXus consumers should treat this as metadata, and should not assume that they will be able to read the file pointed at.

{#nexus_instrument_dae_type}
### `raw_data_1/instrument/dae/type`

A string identifying the type of data acquisition hardware in use; for example:
- `"ISIS_DAE3"`
- `"ISIS_DAE2"`

Future acquisition systems may use different type identifiers; this list should not be treated as exhaustive.

---

The `raw_data_1/instrument/dae` group also contains the following groups:

```{toctree}
:glob:
:titlesonly:

nexus_instrument_dae/*
```

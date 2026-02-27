# 2 - Wiring and Spectra mapping

## Status

pending

## Context

Wiring tables is a concept that still exists however the format is now different (`.csv` as opposed to the old wiring table format). 

The options that we're considering are:
- change `.csv` to align with the old format
- write a service/script to convert to/from `.csv`
- keep the two formats separate, acknowledging that they will not be backwards or forwards compatible

Spectra files share the above considerations as they also use a different file format.

Grouping spectra in hardware was primarily used to get around limitations of DAE hardware. In event mode there is no advantage to grouping spectra in hardware. 

## Decision

We are not going to support the old-style spectra files or any spectrum mapping/grouping in general 

For wiring tables this is TBD in https://github.com/ISISComputingGroup/DataStreaming/issues/27.

## Consequences

- If HRPD-x previously grouped spectra in hardware, they will now need to be grouped in software (e.g. Mantid) instead.
- Our data streaming software will not need to support spectrum grouping.

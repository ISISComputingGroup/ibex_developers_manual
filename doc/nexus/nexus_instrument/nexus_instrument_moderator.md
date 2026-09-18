# `raw_data_1/instrument/moderator`

This is a {external+nexus_manual:doc}`classes/base_classes/NXmoderator`.

## `raw_data_1/instrument/moderator/distance`

This is written as the **negative** of the L1 flight path distance, as a float32. It is set in IBEX
under Experiment Details -> Beamline Parameters -> Primary Flight Path (L1)

For an instrument with an L1 of 12.3 m, this dataset would be written as `-12.3`.

Attributes:
- `units`: `"metre"`
# `raw_data_1/user_1`

This is an {external+nexus_manual:doc}`classes/base_classes/NXuser` group, containing the following data:

{#nexus_user_affiliation}
## `raw_data_1/user_1/affiliation`

In principle, this represents the affiliations (institutes) of the beamline users specified in {ref}`nexus_user_name`.
However, this is not currently populated by IBEX and the ICP, and so is written as an empty string.

{#nexus_user_name}
## `raw_data_1/user_1/name`

Users of the beamline. This is a comma-separated list of surnames, as a single string. For example `"Bloggs,Smith,Jones,Williams"`.

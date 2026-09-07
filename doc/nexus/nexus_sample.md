# `raw_data_1/sample`

This is an {external+nexus_manual:doc}`classes/base_classes/NXsample`.

{#nexus_sample_name}
## `raw_data_1/sample/name`

This is user-settable string metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Name

{#nexus_sample_distance}
## `raw_data_1/sample/distance`

This is unconditionally written as `0.0`, **as a float64**.

:::{note}
No units attribute is written by the ISISICP, which is invalid as per the NeXus standard.
:::

{#nexus_sample_id}
## `raw_data_1/sample/id`

This is user-settable string metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample ID

{#nexus_sample_thickness}
## `raw_data_1/sample/thickness`

This is user-settable float32 metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Thickness

:::{note}
It is in units of `mm`, but no units attribute is written by the ISISICP, which is invalid as per the NeXus standard.
:::

{#nexus_sample_width}
## `raw_data_1/sample/width`

This is user-settable float32 metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Width

It is in units of `mm`, but no units attribute is written.

{#nexus_sample_height}
## `raw_data_1/sample/height`

This is user-settable float32 metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Height

It is in units of `mm`, but no units attribute is written.

{#nexus_sample_type}
## `raw_data_1/sample/type`

This is user-settable string metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Type

:::{note}
{external+nexus_manual:doc}`classes/base_classes/NXsample` defines that this can only be one of a defined set of values.
Our files impose no such restriction and will write the arbitrary user-specified string.
:::

{#nexus_sample_shape}
## `raw_data_1/sample/shape`

This is user-settable string metadata. It is set in IBEX under Experiment Details -> Sample Parameters -> Sample Geometry

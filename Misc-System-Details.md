> [Wiki](Home) > [Project overview](Project-overview) > [Misc System Details](Misc-System-Details)

### `Max_array_bytes`

The `Max_array_bytes` constant is used throughout ibex to specify the size of the largest waveform (which is usually produced by the dae). Large objects are need especially for (Live View)[DAE-Live-View]. Currently the largest know version of this is on POLREF who want to see their linear detector with a time of flight 2D view. This has the size of:

    5001 (time channels) * 640 * 8 ~ 20M

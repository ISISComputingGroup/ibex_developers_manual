{#dsrunstartstops}
# Data streaming: run starts/stops

Run starts and stops will be dealt with by [`kafka_dae_control`](https://github.com/ISISComputingGroup/kafka_dae_control) and the flatbuffers blobs will be constructed in this process. It may need to be hooked onto by `ISISDAE` for older instruments using DAE2/DAE3 and the ISISICP. 

Run starts will contain static and streamed data in the `nexus_structure`, including things like `run_number`, `instrument_name` and so on which will get written to a file. 

Run starts will _also_ contain metadata used by `kafka_dae_diagnostics`, in a json schema defined by https://github.com/ISISComputingGroup/DataStreaming/issues/29 - this is so `kafka_dae_diagnostics` does not have to try and parse the `nexus_structure` as it doesn't know or care about NeXus files. 


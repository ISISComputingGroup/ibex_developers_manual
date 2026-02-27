{#dseventshistos}
# Data streaming: Neutron events and histograms

## For DAE2/DAE3 instruments
The ICP (communicated to via the ISISDAE IOC) is responsible for communicating with the DAE2/DAE3 in terms of setting configuration, as well as streaming events and histograms from both.


## For new instruments using FPGA-based acquisition electronics
`kafka_dae_control` is responsible for communicating with the electronics and sending run starts/stops. It will have a similar interface to `ISISDAE` so we can drop-in replace it in the GUI.(?)


## Live view, spectra plots etc. 
These will be provided by a soft IOC (`kafka_dae_diagnostics`) which effectively consumes from event and histogram topics (and possibly run starts?) which will serve areaDetector and other PVs. 

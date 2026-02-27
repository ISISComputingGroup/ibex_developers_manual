# Data Streaming

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

datastreaming/*
```

The data streaming system is being built as a requirement for HRPD-X and possibly SANDALS-II, separate (and complementary) to the `MNeuData` project. HRPD-X, SANDALS-II and other future instruments will not have a traditional DAE2/DAE3 as they are now obsolete. It is architecturally similar to the system that the ESS uses to take data (neutron events, sample environment, and anything else that we can throw into a streaming platform) and write it to file. Previously ISIS aided development to the ESS' streaming pipeline as part of an in-kind project. The system will replace the ICP at ISIS. Note that all documentation here is applicable to the HRPD-X upgrade and may change in the future. 

In general this works by producing both neutron events and histograms, sample environment data, and other diagnostic data into a [Kafka](https://kafka.apache.org/) cluster and having clients (consumers in Kafka lingo!) that either view data live and act on it or write the data to a nexus file. Additional information can be found [here](http://accelconf.web.cern.ch/AccelConf/icalepcs2017/papers/tupha029.pdf) and [here](https://iopscience.iop.org/article/10.1088/1742-6596/1021/1/012013). 

All data is serialised into [Flatbuffers](https://flatbuffers.dev/) blobs using [these schemas](https://github.com/ess-dmsc/streaming-data-types) - we have a tool called [saluki](https://github.com/ISISComputingGroup/saluki) which can deserialise these and make them human-readable after they've been put into Kafka. 

Overall architecture is as follows:

![](datastreaming/ISISDSLayout.drawio.svg)

This comprises of a few different consumers and producers: 
- [`kafka_dae_diagnostics`](https://github.com/ISISComputingGroup/kafka_dae_diagnostics) - This is a soft IOC which provides `areaDetector` views, spectra plots and so on by consuming events from the cluster and displaying them over EPICS CA/PVA.
- [`kafka_dae_control`](https://github.com/ISISComputingGroup/kafka_dae_control) - This is also a soft IOC which is more or less a drop-in replacement for the ISISDAE. It provides an interface that several clients (ie. [genie](https://github.com/ISISComputingGroup/genie), [ibex_bluesky_core](https://github.com/ISISComputingGroup/ibex_bluesky_core), [ibex_gui](https://github.com/ISISComputingGroup/ibex_gui)) talk to to start/stop runs and configure streaming electronics. `kafka_dae_control` will send UDP packets to the streaming electronics to configure it. 
- [`kafka_forwarder_configurer`](https://github.com/ISISComputingGroup/kafka_forwarder_configurer) - This configures the `forwarder` with the blocks that are in an instrument's current configuration, as well as other PVs which will either get written to a file or archived for e.g. the log plotter. 
- `forwarder` - See [Forwarding Sample Environment](datastreaming/Datastreaming---Sample-Environment)
- `filewriter` - See [File writing](datastreaming/Datastreaming---File-writing)

{#kafkacluster}
## The Kafka Cluster

There is a (non-production!) [Redpanda](https://www.redpanda.com/) Kafka cluster at `livedata.isis.cclrc.ac.uk:31092`.
A web interface is available [here](https://reduce.isis.cclrc.ac.uk/redpanda-console/overview).

:::{important}
It was decided that we no longer maintain the Kafka cluster, and it will be handled by the Flexible Interactive
Automation team. See `\\isis\shares\ISIS_Experiment_Controls\On Call\autoreduction_livedata_support.txt` for their
support information.
:::

## How to/FAQs
See {ref}`datastreaminghowto`

## Run starts/stops
See {ref}`dsrunstartstops`

## SE Data

See [Forwarding Sample Environment](datastreaming/Datastreaming---Sample-Environment)

## Neutron events and histograms
See {ref}`dseventshistos`

## Filewriting

See [File writing](datastreaming/Datastreaming---File-writing)

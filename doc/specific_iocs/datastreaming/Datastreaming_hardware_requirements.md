# Data streaming server hardware requirements

This page aims to set a standard for the hardware requirements for the HRPD-X, SANDALS-II, WISH and VESUVIO instrument upgrades.

The specifications listed below are for a single node, however for very high data rate instruments further benchmarking will be required.

## Hardware Requirements

### Network interface(s)

We will require 2x 10Gigabit interfaces for each node.
1 of these will be used for direct data transfer from detectors.
1 of these will be used for connections to other nodes in the kafka cluster and connection to the wider ISIS network.

Standard DRAC interfaces are also being assumed (meaning a total of 3 links from each node to a switch)

### CPU

This server will be running a Redpanda node which scales over multiple cores. It will also run a number of other processes (our software and possibly DSGs) each of which may also be multi-threaded.

We tested on the ESS streaming cluster which has 8 physical cores per node. With the full stack of streaming software, although at the time these were prototypes, this was approaching performance limits of the system.

SuperMuSR has experience running a cluster and streaming system on Dell Poweredge R6715s with AMD EPYC 9355Ps.
The advantages of mirroring their machines are that we may be able to provide spares for SuperMuSR or vice versa, and they are well tested already.

### RAM

Redpanda requirements state that [machines must have at least 2GB of memory per core](https://docs.redpanda.com/current/deploy/redpanda/manual/production/requirements/#cpu-and-memory) - this implies at least 64GB of RAM.
On the test cluster 32GB of RAM became a limiting factor.
Alongside Redpanda/Kafka we need to host containers which suggests that 128GB would give reasonable overhead to do so. 

### Storage

Data drive should be [NVME as per the Redpanda requirements](https://docs.redpanda.com/current/deploy/redpanda/manual/production/requirements/#storage)

The storage requirements are based on having at least a single run's worth of events in Kafka at a given time, as well as being able to write that file out to storage before it's moved off the machine.

HRPD-X has notably lower requirements than SANDALS-II. There are two options:

1. keep machines for both exact copies, which means a like-for-like can be swapped in in case of a hardware failure. This means that for HRPD-X we may be able to up retention rates of events and diagnostic data.
2. keep machines baseline specifications the same except for storage which is tailored towards that instrument.

For HRPD-X: 

Worst case sustained count rate estimate is 50Mbps. There is a requirement to be able to keep 1 run's amount of events in a kafka instance along with the same amount of space for a nexus file to be written (until it is ultimately moved off this machine)

We then need other space for slower streams such as sample environment and run info. 

While commissioning we may also need additional space to store low-level diagnostic information such as streaming extra information from the streaming boards. 

On this basis we will specify these machines with 4TB of storage along with a separate boot disk to be used for the base OS and software deployments. The latter can be 500GB-1TB. This leaves headroom for diagnostics and foreseeable future needs over the next 3-5 years. 

## Notes

- From dell consumer prices, we worked out that our baseline versus the SuperMuSR specifications was about 16% - with the differences being half the CPU cores and RAM.
- The NDHes could be an option, but their chassis do not support NVME storage which is a Redpanda requirement. With a specification adjusted to allow this and a CPU upgraded to the lower bound of what is considered reasonable the SuperMuSR machines are +~60% more expensive. These were also out of stock on dell's website so may be about to be discontinued.
- For HRPD-X, a single node will likely suffice. For SANDALS-II, it will not - performance tests showed that Repanda or Apache Kafka scale much more with multiple nodes. A single node was maxing out at ~350MB/s with kafka's built in `kafka-producer-perf-test.sh` (Exact arguments were ` ./kafka-producer-perf-test.sh --topic perf-test --record-size 1047576 --num-records 100000 --throughput -1 --print-metrics --producer-props linger.ms=50 batch.size=1048576 bootstrap.servers=localhost:9092`)

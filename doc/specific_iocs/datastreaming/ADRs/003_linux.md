# 3 - Linux

## Status

Accepted. 

## Context

Historically we have used Windows for running most of our software due to LabVIEW support when migrating from SECI.
This often means software is not natively supported as most of the wider experiment controls community at comparable facilities run Linux instead, so we regularly have to port software designed for Linux to run on Windows.

Streaming software is linux-centric and running Kafka itself natively on Windows is not natively supported by either [confluent Kafka](https://www.confluent.io/blog/set-up-and-run-kafka-on-windows-linux-wsl-2/#:~:text=Windows%20still%20isn%E2%80%99t%20the%20recommended%20platform%20for%20running%20Kafka%20with%20production%20workloads) or [redpanda](https://docs.redpanda.com/current/get-started/quick-start/#:~:text=If%20you%E2%80%99re,Linux%20%28WSL%29%2E). In addition, a number of tools developed both externally and at ISIS for data streaming only currently run on Linux.

Running software under WSL is an option, but is not [built for production use.](https://learn.microsoft.com/en-us/windows/wsl/faq#can-i-use-wsl-for-production-scenarios-) It also adds several layers of complexity with networking, file systems and so on. Container networking configuration is difficult and limited using WSL.

We would ideally like to run the data streaming software in containers as they offer security, deployment and repeatability benefits and are extremely popular in the software development industry. HRPD-X coming online with a new detector technology means that we will need to be able to easily apply new versions of data-streaming software at short notice. Containers give us an easy, repeatable path to be able to do this.

Docker Desktop _is_ supported on Windows, but uses the WSL with a strict licensing agreement which does not suit our needs. Other alternatives also use the WSL. Many container configuration options (e.g. host networking, volume mounting options) cannot be supported with containers on Windows (whether via Docker desktop or another solution). 

One of the long-term goals on the Experiment Controls road-map is to revisit our operating system choice. It is very likely this will be a distribution of Linux.

For HRPD-X specifically, the NDX and NDH is unsuitable for deploying data streaming software, as it will remain using Windows (in the short term).

Additionally, Windows Licensing costs have recently changed significantly (as of January 2026). If we chose to use a Linux distribution, even with support ie. in the style of Red Hat Enterprise Linux, it is likely it would cost less.

ISIS has made it clear that Linux support will be provided in the medium term.

## Decision

New or repurposed hardware, running Linux, will be used to run the streaming software as shown {ref}`here<ds_hardware_architecture>`.

Wherever possible, software will be deployed in containers, which will minimise the amount of Linux systems administration knowledge required. The aim will be for the Linux machine to 'only' have a container engine (such as docker or podman) installed, and very little else.

## Consequences

- We are able to use Linux-centric technologies and tools, without needing to spend large amounts of time inventing workarounds for Windows.
- The OS will be different. Developers will need _some_ understanding of Linux to maintain these servers.
  * Mitigation: do as little as possible on the host, ideally limit it to just having a container engine installed via a configuration management tool such as Ansible.
- Data-streaming infrastructure will not be on the NDH/NDX machine with the rest of IBEX. This is fine - EPICS is explicitly designed to run in a distributed way.
- We will need to carefully consider the system specification of the Linux server in order to ensure it is adequate for expected data rates (including data rates from e.g. noisy detectors, to a point). In particular we expect to need to carefully consider:
  * Disk write performance (for the Kafka broker and the filewriter)
  * Network interface speeds (both from the electronics into this server, and from this server onwards to consumers such as Mantid)
  * Memory (for any processes which need to histogram the data - must be able to keep a histogram in memory)
 - The data streaming stack will be unaffected by a restart of the NDX system, and will keep running in the background.
 - We will configure the relevant containers for data streaming software to automatically start on reboot of the data streaming Linux server.

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

There are a few different options with associated risks and benefits:

### 1 - Running natively on the (Windows) NDX machines

This has the benefit that everything runs along with the rest of IBEX, though we would have to spend extra development effort trying to port software to Windows which we may undo in the future if moving to Linux anyway. 

The NDX already exists so doesn't add any system administration requirements to be able to run the software. 

The main drawbacks for this approach are that: 
- the NDXes do not have sufficient resources for the software currently
- Windows is different to everyone else running the streaming software, and we may waste effort porting software to Windows
- Kafka itself will not run on Windows
- Deployment and patching will become difficult for a system which will need to be patched frequently and will interfere with the rest of the control system. As an example, we do not use virtual environments in python, so updating a python depdendency for the `forwarder` runs the risk that it may break something in user scripts and/or the block server, which would be very bad. 
- Task scheduling/service management can be difficult on Windows, we could use `procserv` but in most cases we don't require an interactive terminal for processes.
- Moving away from Windows is on the roadmap - we would be creating more work for ourselves when we migrate over eventually. 


### 2 - Running natively on a separate Linux machine

This adds another machine in the data streaming stack which _could_ fail and stop data collection. 

Running the streaming software (which is designed to be run on Linux) natively would be the most performant of all the approaches. 

The main benefit to this is that we can specify the hardware requirements independently so they are suitable for the streaming software, with enough overhead to run Kafka on if needed. 

Tooling is generally more available for deployment and patching than Windows, however this is not something we are familiar with as a team. 

The downside is that if the setup of this machine isn't entirely automated it could be very difficult to maintain and/or reproduce if a hardware failure occurred. 

As well as this, more Linux system administration knowledge is required by the team. 

Operating system updates could inadvertently affect the processes running on the machine, which could cause issues if we set the system to install unattended upgrades.

### 3 - Running in containers on the NDX machines

The benefit of doing this is that all services can be brought up and down together with the rest of the control system. It is also one less link in the data streaming chain to fail. 

This would require the use of the WSL which is not specifically designed for production use and has limited functionality with containers due to host-network mode issues and so on. 
NDXes are virtualised and have _very_ limited resources. 

Another drawback is that we currently the current IBEX deployment method makes it difficult to patch these services as easily - moving these services elsewhere means we do not have to interrupt e.g. sample environment scripts to restart/redeploy new versions of DAE processes.

We are unable to use Docker desktop, required for docker engine on Windows, without paid licensing. An alternative is Rancher Desktop or podman. These both use underlying VMs. 

### 4 - Running in containers on a Linux VM on the NDH 

This has the same benefits as above but would allow us to run a Linux VM alongside the NDX which lets us avoid WSL oddities.
Additionally, there should be more flexibility in deployment and patching, and less interference with the rest of IBEX.

NDHes are currently very limited on resources, much like the NDXes which run on them. This is the main sticking point for this approach. 

Alongside this, virtual machines do generally introduce a performance penalty - the exact figure for this depends on several factors but it will never be as fast as a native application or a container which shares the kernel. For fast processes such as live histogramming and event processing we may require high performance which could be limited by a virtual machine. 

### 5 - Running in containers on a separate Linux machine

This adds another machine in the data streaming stack which _could_ fail and stop data collection. 
As well as this, it will rely on the instrument's local network switch, which could also fail (though this is applicable to any of the options as the WLSF boards will be streaming over this switch)

Another downside, which affects the above approach, is that some system administration knowledge will be required to keep the operating system alive and secure. If we are using containers this should be very minimal. 

This shares the benefit of being able to specify suitable hardware requirements as approach 2.

Containers are much more easily reproducible than native software. The wider industry is moving towards them generally because of this amongst other reasons. 

Deployment, patching and orchestration is also very widely supported by several frameworks with containers. We should decide exactly what we're doing at a later point, but if we started with [`docker-compose`](https://docs.docker.com/compose/) as a simple first step, it is straightforward to move towards something like [Kubernetes](https://kubernetes.io/) instead if we decide we need the features it offers. 

Containers also provide a cyber-security benefit in that the processes are isolated individually. 

DSG already have some container-based software to convert UDP streams to Flatbuffers blobs - we could quite easily host this for them if we have container infrastructure. This applies to any of the approaches that offer it.

If we end up being responsible for running the Kafka instance for HRPD-x, adding this is straightforward - Redpanda and the other Kafka implementations all offer production-ready container images. 

## Decision

New hardware, running Linux, will be used to run the streaming software as shown {ref}`here<ds_hardware_architecture>`.

Wherever possible, software will be deployed in containers, which will minimise the amount of Linux systems administration knowledge required. The aim will be for the Linux machine to 'only' have a container engine (such as docker or podman) installed, and very little else. Containers will use health checks and auto-restarting to ensure reliability. We will decide on exact deployment and orchestration methods later on, but there are several approaches to choose from.

Exact specifications will depend on data rates and prototype testing. 

## Consequences

- We are able to use Linux-centric technologies and tools, without needing to spend large amounts of time inventing workarounds for Windows.
- The OS will be different. Developers will need _some_ understanding of Linux to maintain these servers.
  * Mitigation: do as little as possible on the host, ideally limit it to just having a container engine installed via a configuration management tool such as Ansible. Some Linux distributions come with this out of the box such as [Fedora CoreOS](https://docs.fedoraproject.org/en-US/fedora-coreos/) or [RancherOS](https://rancher.com/docs/os/v1.x/en/)
- Data-streaming infrastructure will not be on the NDH/NDX machine with the rest of IBEX. This is fine - EPICS is explicitly designed to run in a distributed way.
- We will need to carefully consider the system specification of the Linux server in order to ensure it is adequate for expected data rates (including data rates from e.g. noisy detectors, to a point). In particular we expect to need to carefully consider:
  * Disk write performance (for the Kafka broker and the filewriter)
  * Network interface speeds (both from the electronics into this server, and from this server onwards to consumers such as Mantid)
  * Memory (for any processes which need to histogram the data - must be able to keep a histogram in memory)
 - The data streaming stack will be unaffected by a restart of the NDX system, and will keep running in the background.
 - We will configure the relevant containers for data streaming software to automatically start on reboot of the data streaming Linux server.

The above will be impacted if we are required to run a Kafka instance on the streaming machine - this is unclear as of January 2026. Redpanda provides [some documentation on hardware requirements](https://docs.redpanda.com/current/deploy/redpanda/manual/production/requirements/) which we should consider. 

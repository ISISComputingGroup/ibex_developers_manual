The EPICS Archiver Appliance is principally targeted to run on a Linux host and there are some issues when attempting to run it under Windows.
[Ticket #8438](https://github.com/ISISComputingGroup/IBEX/issues/8438) was to investigate and document whether the Archiver Appliance can be run in a container on a Windows host. Particular interest is its ability to run on a NDX Windows virtual machine.

A new EPICS gateway has been configured to make localhost PVs available to the container - In C:\Instrument\Apps\EPICS\gateway (https://github.com/ISISComputingGroup/EPICS.git), new files have been added:

| File | Description |
| ---- | ----------- |
| gwcontainer.acf | Container gateway security |
| gwcontainer.pvlist | Container gateway PV list |
| start_gwcontainer.bat | Container gateway start script, called from start_gateways.bat |
| stop_gwcontainer.bat | Container gateway stop script, called from stop_gateways.bat |

A new git repository has been created (git@github.com:ISISComputingGroup/isis-aa-config.git). This contains all the code required to build a Archiver Appliance image and run a container instance.

| File | Description |
| ---- | ----------- |
| Containerfile | Defines the content to build into the image |
| aa-compose.yaml | Used by `nerdctl compose` to marshall building the image and running the container  |
| docker-compose.yaml | This was used as an experimental compose file to test various networking options to try to circumvent Windows lack of 'host' container networking. Retained as there is some useful info and techniques |
| containerdata  | This directory is mounted by the container and facilitates data persistence  |

Due to complications and uncertainties of licencing of Docker Desktop, it has been decided to adopt an open source alternative, a number of which are freely available, such as Rancher Desktop, Podman, etc. For the purpose of this exercise, [Rancher](https://rancherdesktop.io/) was chosen.

## Rancher Desktop Installation
Non-windows Containers on Windows hosts need Windows System for Linux (WSL2) to be installed on the host machine. If not already present, this is installed as part of the Rancher Desktop installation process. Rancher Desktop will create its own necessary distributions (rancher-desktop-data and rancher-desktop) on WSL and it there is no need to manually install anything else.

Download the Installation MSI file for Windows (x64). At the time of writing, it is: `Rancher.Desktop.Setup.1.15.1.msi`

Run the msi file, you will need admin access at some point. Under testing, an error message was presented: "Rancher Desktop Setup Wizard ended prematurely. Your system has not been modified...", but on the second attempt, the installation completed successfully. 

## Observations and present limitations

# **This page is currently not in use**


## Setting Up a Development Environment on Windows

WSL, or Windows Subsystem for Linux, allows the use of a Linux/GNU environment from a Windows machine.

### Check Your Windows Version

WLS2 is only available in Windows 11 or Windows 10, Version 1903, Build 18362 or later.

The Windows version of your machine can be checked by pressing `Win + R`, typing `winver` and pressing Enter.

### Installing WSL

To install WSL, open a PowerShell or CMD window in Administrator mode, and enter the following: 

`wsl --install`

Note: This method only works if WSL is not installed. If you run `wsl --install` and see the WSL help text, please try running `wsl --list --online` to see a list of available distribution and run `wsl --install -d <DistroName>` to install a distribution.

### Uninstalling Legacy WSL Versions

If you wish to uninstall the legacy version of WSL, instructions of how can be found [here](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#uninstall-legacy-version-of-wsl)

### Additional Resource

Further information on the WSL installation process can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command)

## Rancher Desktop Installation

Rancher Desktop is an application provides container management and `Kubernetes` on the desktop. Rancher Desktop provides the ability to build, push, and pull container images along with the ability to run containers.

Rancher Desktop can be installed [here](https://docs.rancherdesktop.io/getting-started/installation/).

Once the .exe file has been downloaded, follow the steps to complete the installation process.

Ensure the `dockerd` is selected as the runtime during the installation or within the Rancher Desktop settings. 

## Creating a Container

1. Create a folder in which all container file will be stored i.e. `C:\Instrument\App\Epics\Container`.

2. Within the folder, create a `test.db` file:

	`record(ao, "TESTTEST:FOO") {}`

3. A `Dockerfile` should be added as this is the set of 'instructions' from which Docker builds images. Below is an example which creates a container with a simple IOC: 
```
    FROM python:3.11-slim
    RUN apt-get update && \
        apt-get install -y \
        build-essential \
        wget \
        git \
        && rm -rf /var/lib/apt/list/*
	
    RUN pip install --upgrade pip
    RUN pip install epicscorelibs
	
    ENV EPICS_BASE=/epics
    ENV EPICS_HOST_ARCH=linux-x86_64
    ENV EPICS_CA_SERVER_PORT 5066
	
    WORKDIR /app
    COPY . /app
	
    ENTRYPOINT ["python", "-m", "epicscorelibs.ioc", "-d", "test.db"]

```

4. To build the container from the `Dockerfile`, cd into the folder within a CMD window, ensure that Rancher Desktop is running and enter:

	`docker build -t <container_name> .`

        docker build: Tells Docker to create a new image.
     
        -t: Specifies a name for the image you're building.

        <container_name>: The name you're giving to the new image.

        .: Tells Docker to use the current folder for the build.

5. To run the container, enter the following (replace the path with your own folder location):

	`docker run --rm -it --net=host -v <path_to_folder>:/usr/src/app <container_name>`

    `EXAMPLE: docker run --rm -it --net=host -v /c/Instrument/Apps/EPICS/isis-ioc-container:/usr/src/app ioc_container`

        docker run: Starts a container.

        --rm: Deletes the container when done.

        -it: Lets you interact with the container.

        --net=host: Uses your computer’s network.

        -v <path_to_folder>:/usr/src/app: Shares a folder from your computer with the container.

        <container_name>: The image to use for the container.

	After this, the container should be running within the Python Environment within the CMD window.

6. To test if the PV is readable within the container, a EPICS terminal window is needed. For this, open another CMD window and enter:

	`C:\Instrument\Apps\Epics\config_env.bat`
	
	If `Warning: "Identical process variable name on multiple servers"` appears within the EPICS Terminal , enter the following to set the CA address to that of the container:
	
	`set EPICS_CA_ADDR_LIST=127.0.0.1:5066`

7. Now that both terminals are running, the value from the PV can be retrieve by entering the following command into the EPICS terminal:

    `caget TESTTEST:FOO` 

    To which the response should be `TESTTEST:FOO    0`

    `caput <PV_name>` can also be used to set the value of the PV.


### Network Connections

The following command entered within the EPICS terminal allows users to check for network connections that are being used by a specified port, in this example the port 5066 is being checked:

`netstat -a -n -o |findstr 5066`


## Observations and Present Limitations

It would appear that both IBEX and the network=host wish to use port 5064, and the container is being blocked whilst the IBEX server is running.

A solution as been found, which is already included within the `Dockerfile`, where another port has been bound which enables the container's IOC to be communicated with whilst the IBEX server is running. However, it has been found that each IOC will need it's own port, which can lead to issues as the number IOC increases.

## Further Exploration

In the above example, an approach similar to [epics-containers](https://epics-containers.github.io/main/index.html) was attempted, however there are a couple of alternative methods that could be explored.

[SnowSignal](https://github.com/ISISNeutronMuon/SnowSignal/tree/main) is a possible alternative to UDP communication between localhost and the container. SnowSignal is designed to create a mesh network between instances of the program that will listen for UDP broadcasts received on one node of the network and rebroadcast on all other nodes.

WLS on Windows 11 22H2 and higher introduced ['Mirror mode networking'](https://learn.microsoft.com/en-us/windows/wsl/networking#mirrored-mode-networking). This changes WSL to an entirely new networking architecture which has the goal of 'mirroring' the network interfaces that you have on Windows into Linux, to add new networking features and improve compatibility.

## WSL2 on a Windows 11 Virtual Machine

There can be an issue with running a VM on a Windows 11 VM, which may result in the following error:

["Error: 0x80370102 The virtual machine could not be started because a required feature is not installed."](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#error-0x80370102-the-virtual-machine-could-not-be-started-because-a-required-feature-is-not-installed) 


The command is as below, if you run it directly on the right server you can skip the "-Computername HOSTSERVERNAME" bit.
 
`PS C:\> Set-VMProcessor -ComputerName HOSTSERVERNAME -VMName GUESTMACHINENAME -ExposeVirtualizationExtensions $true`

## Setting Up a Development Environment on Windows

WSL, or Windows Subsystem for Linux, allows the use of a Linux/GNU environment from a Windows machine.

### Check Your Windows Version

WLS2 is only available in Windows 11 or Windows 10, Version 1903, Build 18362 or later.

The Windows version of your machine can be checked by pressing `Win + R`, typing `winver` and pressing Enter.

### Installing WSL

To install WSL, open a PowerShell or CMD window in Administrator mode, and enter the following: 

`wsl --install`

Note: This method only works if WSL is not installed. If you run `wsl --install` and see the WSL help text, please try running `wsl --list --online` to see a list of available distros and run `wsl --install -d <DistroName>` to install a distro.

### Uninstalling Legacy WSL Versions

If you wish to uninstall the legacy version of WSL, instructions of how can be found [here](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#uninstall-legacy-version-of-wsl)

### Additional Resource

Further information on the WSL installation process can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command)

## Rancher Desktop Installation

Rancher Desktop is an application provides container management and Kubernetes on the desktop. Rancher Desktop provides the ability to build, push, and pull container images along with the ability to run containers.

Rancher Desktop can be installed [here](https://docs.rancherdesktop.io/getting-started/installation/).

Follow the steps to complete the installation process.

Ensure the `dockerd` is selected as the runtime during the installation or within the Rancher Desktop settings. 

## Creating a Container

1. Create a folder in which all container file will be stored i.e. C:\Instrument\App\Epics\Container

2. Within the folder, create a test.db file:

	`record(ao, "TESTTEST:FOO") {}`

3. Additionally, a Dockerfile should be added as this is the set of 'instructions' from which Docker builds images. Below is an example which creates a container with a simple IOC: 

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
	
	    ENTRYPOINT ["python", "-m", "epicscorelibs.ioc", "-d", "testdup.db"]


4. To build the container from the Dockerfile, cd into the folder within a CMD window

	`docker build -t ioc_container .`

5. To run the container, enter the following (replace the path with your own folder location)

	`docker run --rm -it --net=host -v C:\Instrument\Apps\EPICS\isis-ioc-container:/usr/src/app ioc_container`

	The container should be running, this can be seen now by the python environment running within the CMD window

6. Within another  CMD window, a EPICS terminal window is needed:

	`C:\Instrument\Apps\Epics\config_env.bat`
	
	If `Warning: "Identical process variable name on multiple servers"` appears within the EPICS Terminal , enter the following to set the CA address to that of the container:
	
	`set EPICS_CA_ADDR_LIST=127.0.0.1:5066`

BONUS:

The following command within the EPICS terminal allows the ports which are specified to be checked, in this example the port 5066 is being checked:

`netstat -a -n -o |findstr 5066`

To get the PV value, enter:

`caget TESTTEST:FOO`

`caput` can also be used to set the value of the PV:


## Observations and Present Limitations

It would appear that both IBEX and the network=host wish to use port 5064, and the container is being blocked whilst the IBEX server is running.

A solution as been found, which is already included within the Dockerfile, where another port has been bound which enables the container's IOC to be communicated with whilst the IBEX server is running. However, it has been found that each IOC will need it's own port, which can lead to issues as the number IOC increases.

## Further Exploration

Talk about snowsignal
Talk about WLS2 on Windows 11
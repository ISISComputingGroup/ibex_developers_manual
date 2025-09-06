# Adding Jenkins nodes

These are instructions for adding a new Windows machine as a node to be used by Jenkins.

## Hardware Prerequisites

A useful build server will need roughly the following specifications:
- Processor:
  - Not a virtual machine (we have tried VMs in the past, but the performance penalty is too high for a 
build server)
  - Semi-modern processor. Most of our builds are _primarily_ single-threaded, so single-core performance
is more important than multi-core at present.
- Memory:
  - 32GB or more of RAM (16GB may be possible to use, but will be substantially slower to build). Extra RAM 
can be acquired relatively cheaply, if the machine has spare memory slots (check compatibility carefully).
- Storage
  - **Must be an SSD**. PCIe (M.2) preferred but not required. Do not use a spinning hard disk as a build drive - it will be painfully slow.
  - Doesn't need to be the primary OS drive - a separate drive also works and can generally be acquired relatively cheaply, if the machine has a spare M.2 or SATA port.
  - **For an EPICS build node**: 1TB capacity minimum. This capacity is needed because multiple builds' workspaces will be present at once.
  - **For a system tests build node**: 500GB capacity minimum.
- Location
  - The machine should be located in a suitable place, ideally in a room with air-conditioning. Many of our
build servers are in the R55 server room for this reason.

## Software Prerequisites

It is possible to follow the "full" first-time install guide to get all the components necessary for build jobs:

* First set up the machine so it can be used to build the back-end system manually by following these [instructions](/overview/First-Time-Build)
* After you have registered the ISISICP go into `c:\Instrument\Apps\EPICS\ICP_Binaries\isisdae` and read `README_isisicp_reg.txt` in particular you will probably need to add the the account running jenkins to the windows group mentioned 
* Delete the EPICS subdirectory that was created in the previous step (maintaining C:\Instrument\Apps)

### EPICS build node

The bare minimum requirements for an EPICS/GUI/Uktena build node are:

- Visual Studio
  * C++
  * ATL
  * MFC
  * .NET targeting pack
- Perl
- Java
- Maven
- Doxygen
- git
- TwinCAT bits
- `symstore` (`\\isis\inst$\Kits$\CompGroup\ICP\winsdk`)

### System tests node

The bare minimum requirements for a system tests node are:

- Create directories:
  * `c:\Instrument\Apps`
  * `c:\Instrument\var\autosave`
  * `c:\Instrument\var\logs`
  * `c:\Instrument\var\tmp`
- Java
- git
- Latest MySQL (use `upgrade_mysql` script in `ibex_utils`)
- Ensure there is a config directory for this instrument, in `C:\Instrument\Settings\config\<machine name>`
  * Must be checked out onto an instrument branch
- Ensure there is a calibrations directory for this instrument, in `C:\Instrument\Settings\config\common`
  * Must be a git checkout, on `master` branch

## Adding to Jenkins

* Go to [our jenkins instance](https://epics-jenkins.isis.rl.ac.uk/computer/) and log in to Jenkins
* Create a `New Node` with the Node Name as the computer name, select 'Permanent Agent'
* Set a root directory of `C:\Jenkins`
  * The root directory may need to be on a different drive, if the `c:\` drive is small. See hardware prerequisites
above, for minimum hardware requirements of this drive.
* Set labels
  - For an EPICS build node, create **two** build nodes in Jenkins
    * One called `<computer_name>`, with the following labels: `ConfigCheck genie gui isisicp`, with 4 executors.
    * One called `<computer_name>_epics`, with the `epics_build` label, with a single executor.
  * For a system tests build node, create a single Jenkins node, with label `system_tests`, with a single executor.
* Select the `Launch agent by connecting it to the controller`
* Save
* Select the slave that has just been created and make a note of secret. For an initial test make a note of the curl and java commands from `Run from agent command line: (Windows)`
* In a command window in c:\jenkins run the curl and java commands. These can be put into a bat file for interactive running.

## Setup as service

We use https://github.com/jenkinsci/windows-slave-installer-module and https://github.com/winsw/winsw the relevant files are in 
`\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions\builderserver` to copy to `c:\Jenkins`   

Copy `jenkins-agent.exe` and `jenkins-agent.xml` into same directory on the target machine e.g. `c:\jenkins`

Edit `jenkins-agent.xml` and change  https://epics-jenkins.isis.rl.ac.uk/computer/COMPUTER/jenkins-agent.jnlp and the SECRET field to the same as they are from the Jenkins' Node page, add `-workDir` argument of `c:\jenkins`
COMPUTER should be capitalised in same way as written on Jenkins.

Open an admin cmd window and run `jenkins-agent.exe install` and then `servies.msc`

Find the jenkins service in the Service Manager window on the machine, and change it to run as `isis\ibexbuilder` rather than local service account, you'll need to enter `ISISBuilder` password.

Then run start service from the Service Manager window.

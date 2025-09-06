# Build Servers

## EPICS/GUI build server

### Prerequisites

A useful build server will need roughly the following hardware:
- Not a virtual machine (we have used VMs in the past, but the performance penalty is quite high for a windows build server)
- 32GB or more of RAM (16GB may be possible to use, but will be substantially slower to build). Extra RAM can be acquired relatively cheaply if needed, if the machine has spare slots (check compatibility carefully)
- 1TB SSD (this capacity is needed because multiple builds' workspaces will be present at once). This does not need to be the primary OS drive - a separate drive also works and can generally be acquired relatively cheaply, if the machine has a spare M.2 or SATA port.
- A semi-modern processor. Most of our builds are _primarily_ single-threaded at present, so single-core performance is more important than multicore. This may change if we change to using `make -j <processors>` by default at some point in future.

### Software to install

In order to set up a new build server, capable of running GUI, Uktena, and EPICS builds, you need to install the following software:
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
- symstore (`\\isis\inst$\Kits$\CompGroup\ICP\winsdk`)

### Connecting to Jenkins

Use the given URL _without_ the `-websocket` flag.

Set up two executors in Jenkins, one for EPICS with a single slot (suffixed with `_epics`, and with workspace `workspace_epics`), the other for gui/config checker/uktena and other builds, which can have multiple executors in the default workspace.

Add the `epics_build` label to the epics executor, and the `gui`, `genie`, `ConfigCheck` labels to the other executor.

## System tests build server

```{note}
This applies to the IOC tests & system tests jobs, not Squish system tests.
```

A useful build server for system tests will need roughly the following hardware:
- 32GB or more of RAM preferred, 16GB may be possible. Extra RAM can be acquired cheaply if needed, if the machine has spare slots (check compatibility carefully)
- 500GB SSD

Things to be installed manually:
- Create directories:
  * `c:\Instrument\Apps`
  * `c:\Instrument\var\autosave`
  * `c:\Instrument\var\logs`
  * `c:\Instrument\var\tmp`
- Install latest java
- Install latest mysql (use `upgrade_mysql` script in `ibex_utils`)
- Ensure there is a config directory for this instrument, in `C:\Instrument\Settings\config\<machine name>`
  * Must be checked out onto an instrument branch
- Ensure there is a calibrations directory for this instrument, in `C:\Instrument\Settings\config\common`
  * Must be a git checkout, on `master` branch
- 

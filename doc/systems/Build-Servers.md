# Build Servers

In order to set up a new build server, capable of running GUI, Uktena, and EPICS builds, you need to install:
- Visual Studio
- Perl
- Java
- Maven
- Doxygen
- git
- TwinCAT bits

## Connecting to Jenkins

Use the given URL _without_ the `-websocket` flag.

The node needs adding in Jenkins, configuring with a number of executors, and labels `epics_build`, `gui`, `genie` adding to it.

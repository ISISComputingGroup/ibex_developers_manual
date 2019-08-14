> [Wiki](Home) > [Processes](Processes) > [Dependency Update](Dependency-updates)

After a release all of the dependencies of the system should be considered for update. This will ensure that we do not get too far out of date and any upgrade will, hopefully, be small and not require much effort. In general we do not want to be on the bleeding edge but at the last stable release so use your judgement. The list of dependency will get shipped with the release notes and should be kept up-to-date with any notes. This page documents the process of updating and any complexities.

1. Update GUI Java JRE to the latest version (See [Jenkins Build Server `Jenkins builds will bundle the JRE with the client`](Jenkins-Build-Server) for more information)
2. Looks at the [the dependencies on the dev release notes](https://github.com/ISISComputingGroup/IBEX/wiki/ReleaseNotes_Dev#dependencies) for each item check if there is an update (as long as it is not listed below) and update it.

# GUI Dependencies

## PyDev plugin

### eclipse 3
The pydev plugin in eclipse 3 version is stuck at the current version because pydev later than this need eclipse 4 I think.

### eclipse 4

The different versions of the plugins are found at [http://www.pydev.org/update_sites/](http://www.pydev.org/update_sites/)

## General Procedure

### GUI

  - Remove old library file
  - Add library to `/lib`
  - Remove old lib and add new lib in the `Manifest` on the `Runtime` tab in the `Classpath` part.
  - If the old library was marked on order and export tick the box to export it for other projects

### IN module

  - Update the jar in `EPICS\ISIS\IocLogServer\master\LogServer\lib`
  - Update the `pom.xml` and `.classpath` to include the new version number  

## Active MQ

To update activeMQ in epics:
  - Add the activeMQ directory to `...\EPICS\ISIS\ActiveMQ\master`
  - Remove the old activeMQ directory
  - Update the config to include anything new in the new version
  - Update `start-jms-server.bat` to point at the new version of apache
  - Update the Log server modules in `EPICS\ISIS\IocLogServer\master\LogServer`

Update activeMQ in the GUI in `base/uk.ac.stfc.isis.ibex.activemq` (you need to export the library)

## MYSql Connector/J

- To update IOCLog in EPICS `EPICS\ISIS\IocLogServer\master\LogServer`
- To update GUI in `base/uk.ac.stfc.isis.ibex.databases`

## Joda Time

- To update IOCLog in EPICS `EPICS\ISIS\IocLogServer\master\LogServer`
- To update GUI in `base/uk.ac.stfc.isis.ibex.epics`

# CS-Studio

### GUI

Our CS-Studio GUI dependencies are located on a share at `\\shadow.isis.cclrc.ac.uk\icp_p2$\css_gui_dependencies` (which is accessible via a webpage at `http://shadow.nd.rl.ac.uk/ICP_P2/css_gui_dependencies/`. To update the CS-Studio components that the GUI uses:
- `git clone --recursive https://github.com/ISISComputingGroup/isis_css_top.git`
- Make relevant changes to the code, make sure submodules get pinned to new versions using same workflow as in EPICS top.
- Trigger a build on Jenkins
- After the build is complete go to the build server and copy the entire isis_css_top tree to the share
- Subsequent GUI builds will pick up the new dependencies
- Test that your changes work correctly!

### Archive engines / alarm servers

- The build uses the same process as above
- Once build is done, the products are in `org.csstudio.sns\repository\products`
- Copy the zip files for alarm server, alarm config tool, archive engine and archive config tool to `\\shadow.isis.cclrc.ac.uk\icp_binaries$\CSS`, renaming the directories to match the existing names if necessary
- The changes will be picked up after doing `create_icp_binaries` and then `css\master\setup_css.bat`



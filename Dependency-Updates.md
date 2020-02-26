> [Wiki](Home) > [Processes](Processes) > [Dependency Update](Dependency-updates)

After a release all of the dependencies of the system should be considered for update. This will ensure that we do not get too far out of date and any upgrade will, hopefully, be small and not require much effort. In general we do not want to be on the bleeding edge but at the last stable release (i.e. prefer LTS versions when they are available). The list of dependency will get shipped with the release notes and should be kept up-to-date with any notes. This page documents the process of updating.

**Any dependencies which should not be updated should be listed with a reason [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Unupdated-dependencies)**

# GUI

The GUI has multiple mechanisms for pulling in dependencies, all of which may potentially need updates. You should aim to do one dependency update at a time, testing each update both under the eclipse IDE and maven and committing before moving onto the next update.

### `.jar` files

The following `.jar` files may need updating. Check for new versions in maven central or on the vendor website, and update if new versions are available:

```
./base/uk.ac.stfc.isis.ibex.activemq/lib/activemq-all-5.15.11.jar
./base/uk.ac.stfc.isis.ibex.databases/lib/mysql-connector-java-8.0.19.jar
./base/uk.ac.stfc.isis.ibex.epics/lib/commons-codec-1.14-javadoc.jar
./base/uk.ac.stfc.isis.ibex.epics/lib/commons-codec-1.14-sources.jar
./base/uk.ac.stfc.isis.ibex.epics/lib/commons-codec-1.14.jar
./base/uk.ac.stfc.isis.ibex.epics/lib/joda-time-2.10.5.jar
./base/uk.ac.stfc.isis.ibex.logger/lib/log4j-api-2.13.0.jar
./base/uk.ac.stfc.isis.ibex.logger/lib/log4j-core-2.13.0.jar
./base/uk.ac.stfc.isis.ibex.nicos/lib/jeromq-0.5.2.jar
./base/uk.ac.stfc.isis.ibex.ui/lib/opal-1.0.0.jar
```

### Target platform

This is defined in the file `./base/uk.ac.stfc.isis.ibex.targetplatform/uk.ac.stfc.isis.ibex.targetplatform.target
`

General update process:
- Look for newer versions of the repository. E.g. if the repository url is `http://some.website/releases/1.23`, try visiting `http://some.website/releases` to see whether the releases are listed. If so, point the target platform at the new releases.
- Some repositories are updated "in-place". Do upgrade these, simply delete and then re-add them to the target platform, when they are re-added they will pick up the latest versions.

**Note: when updating the eclipse framework itself, you also need to update `client.tycho.parent` - see below for details.**

### Parent POM

Tycho and eclipse framework versions are defined in the file `./base/uk.ac.stfc.isis.ibex.client.tycho.parent/pom.xml`. Note that the eclipse framework version *must* correspond with the version defined in the target platform, otherwise the maven build will fail with mismatched framework versions.

### Client JRE

The GUI builds copy a JRE from `\\isis\inst$\Kits$\CompGroup\ICP\ibex_client_jre`. Replace this with the latest JRE and check that things still work.

# Python

## Python itself

- Check on Python.org for newer versions of python itself
- If a newer version is available, download the "windows installer".
- Install python to a location of your choice (not `c:\instrument\apps\python`).
- Zip up the resulting directory and add it to the share at `\\isis\inst$\Kits$\CompGroup\ICP\genie_python_dependencies_python_3` as `python_clean_<version>.zip`
- Edit `package_builder\common_build_python_3.bat` to use the new python version and test that all dependencies work correctly

## Python packages

Check on PyPi for any package updates, then edit `requirements.txt` to install new versions where needed.

# System

### MySQL
Download the latest MySQL version as a zip file and put in the share `\\isis\inst$\Kits$\CompGroup\ICP\MySQL` and remove the old one.

In the upgrade script `https://github.com/ISISComputingGroup/ibex_utils/tree/master/installation_and_upgrade/ibex_install_utils` edit `install_tasks.py` to point at the new version.

Update the one in your local machine by running `upgrade_mysql.bat`. 

### Java
- Get the latest AdoptOpen JDK 8 from `https://adoptopenjdk.net/` and put it in `\\isis\shares\ISIS_Experimental_Controls_Public\third_party_installers\latest_versions`.
- Copy the older version onto the `\\isis\shares\ISIS_Experimental_Controls_Public\third_party_installers\old_versions`. 
- Uninstall the older version from control Panel and install the new version.
- Test the following IOCs start correctly
  * ARBLOCK
  * ARINST
  * ALARM
  * IOCLOG
  * CSS studio IDE is loaded correctly

### Maven

### Make

- Download the latest make sources from `https://ftp.gnu.org/gnu/make/`
- In the downloaded source tree, open a command prompt
- Run `config_env.bat` (this runs a correct `vcvarsall.bat` for the current system)
- Run `build_w32.bat`
- Copy the built binary in `./WinRel/gnumake.exe` to `C:\instrument\apps\epics\utils_win32\master\bin\make.exe`

### git

Git upgrade is handled by install scripts.

# CS-Studio

## GUI

Our CS-Studio GUI dependencies are located on a share at `\\shadow.isis.cclrc.ac.uk\icp_p2$\css_gui_dependencies` (which is accessible via a webpage at `http://shadow.nd.rl.ac.uk/ICP_P2/css_gui_dependencies/`. To update the CS-Studio components that the GUI uses:
- `git clone --recursive https://github.com/ISISComputingGroup/isis_css_top.git`
- Make relevant changes to the code, make sure submodules get pinned to new versions using same workflow as in EPICS top.
- Trigger a build on Jenkins
- After the build is complete go to the build server and copy the entire isis_css_top tree to the share
- Subsequent GUI builds will pick up the new dependencies
- Test that your changes work correctly!

## Archive engines / alarm servers

- The build uses the same process as above
- Once build is done, the products are in `org.csstudio.sns\repository\products`
- Copy the zip files for alarm server, alarm config tool, archive engine and archive config tool to `\\shadow.isis.cclrc.ac.uk\icp_binaries$\CSS`, renaming the directories to match the existing names if necessary
- The changes will be picked up after doing `create_icp_binaries` and then `css\master\setup_css.bat`

# ActiveMQ

To update activeMQ in epics:
  - Add the activeMQ directory to `...\EPICS\ISIS\ActiveMQ\master`
  - Remove the old activeMQ directory
  - Update the config to include anything new in the new version
  - Update `start-jms-server.bat` to point at the new version of apache
  - Update the Log server modules in `EPICS\ISIS\IocLogServer\master\LogServer`

# IOCLogServer

The IOC log server has a similar build process to the main GUI, and includes several `.jar` files in it's repository. These may have new versions and need to be updated.

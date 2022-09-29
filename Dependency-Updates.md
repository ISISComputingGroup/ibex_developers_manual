> [Wiki](Home) > [Processes](Processes) > [Dependency Update](Dependency-updates)

After a release all of the dependencies of the system should be considered for update. This will ensure that we do not get too far out of date and any upgrade will, hopefully, be small and not require much effort. In general we do not want to be on the bleeding edge but at the last stable release (i.e. prefer LTS versions when they are available). The list of dependency will get shipped with the release notes and should be kept up-to-date with any notes. This page documents the process of updating.

**Any dependencies which should not be updated should be listed with a reason [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Unupdated-dependencies)**

**When updating dependencies add the new dependencies to the upcoming release notes**

# GUI

The GUI has multiple mechanisms for pulling in dependencies, all of which may potentially need updates. You should aim to do one dependency update at a time, testing each update both under the eclipse IDE and maven and committing before moving onto the next update.

### `.jar` files

We now only reference a single `.jar` file (`opal`) from the GUI. This is not currently being updated as the project has moved to nebula visualisation widgets and no new versions are being produced.

### Target platform

This is defined in the file `./base/uk.ac.stfc.isis.ibex.targetplatform/targetplatform.target`

General update process:
- Look for newer versions of the repository. E.g. if the repository url is `http://some.website/releases/1.23`, try visiting `http://some.website/releases` to see whether the releases are listed. If so, point the target platform at the new releases.
- Some repositories are updated "in-place". Do upgrade these, simply delete and then re-add them to the target platform, when they are re-added they will pick up the latest versions.
- For maven dependencies referenced in target platform, look up latest version on maven central then update the version number in target platform to correspond. If the version numbers are hardcoded in `feature.xml` or `MANIFEST.MF` for individual plugins, update it there too.

**Note: when updating the eclipse framework itself, you also need to update `client.tycho.parent` - see below for details.**

### Parent POM

Tycho and eclipse framework versions are defined in the file `./base/uk.ac.stfc.isis.ibex.client.tycho.parent/pom.xml`. Note that the eclipse framework version *must* correspond with the version defined in the target platform, otherwise the maven build will fail with mismatched framework versions.

### Client JRE

The GUI builds copy a JRE from `\\isis\inst$\Kits$\CompGroup\ICP\ibex_client_jre`. Replace this with the latest JRE and check that things still work.

### Pydev

To update the version of Pydev on shadow, git clone --recurse-submodules the latest version and run mvn install in its base directory. After a successful build, upload the repo to shadow.

# Python

## Python itself

- Check on Python.org for newer versions of python itself
- If a newer version is available, download the "windows installer".
- Install python to a location of your choice (not `c:\instrument\apps\python3`).
- Zip up the resulting directory and add it to the share at `\\isis\inst$\Kits$\CompGroup\ICP\genie_python_dependencies_python_3` as `python_clean_<version>.zip`
- Edit `package_builder\common_build_python_3.bat` to use the new python version and test that all dependencies work correctly
- Edit SUPPORTED_PYTHON_VERSION in `genie_python\genie.py`

## Python packages

Check on PyPi for any package updates, then edit `requirements.txt` to install new versions where needed. Note that since we decided [all python projects should use virtual environments](Python-dependencies#how-python-dependencies-should-be-handled-in-the-future) there will be `requirements.txt`files for all Python projects using the new import mechanism, ensure these are also updated.

### Lewis
To update Lewis, merge upstream to our fork: https://github.com/ISISComputingGroup/lewis - This should get picked up automatically by the build server as it installs from the `main` branch of our fork. 

If the version of Lewis is updated the version should be changed in individual support modules in the `lewis_emulators\lewis_versions.py` file. This should also be done for the IOC Generator templates for future IOCs. 
 
# System

### MySQL
Download the latest MySQL version as a zip file and put in the share `\\isis\inst$\Kits$\CompGroup\ICP\MySQL` and remove the old one.

In the upgrade script `https://github.com/ISISComputingGroup/ibex_utils/tree/master/installation_and_upgrade/ibex_install_utils` edit `install_tasks.py` to point at the new version.

Update the one in your local machine by running `upgrade_mysql.bat`. 

### Java
- Get the latest AdoptOpen JDK 8 from `https://adoptium.net/releases.html?variant=openjdk8&jvmVariant=hotspot` and put it in `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions`.
- Copy the older version onto the `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\old_versions`. 
- Uninstall the older version from control Panel and install the new version.
- Test the following IOCs start correctly
  * ARBLOCK
  * ARINST
  * ALARM
  * IOCLOG
  * CSS studio IDE is loaded correctly

### Maven
- Download the latest maven from `https://maven.apache.org/download.cgi#`
- Delete the older version of the maven
- unzip and copy the content to `\\shadow.isis.cclrc.ac.uk\ICP_Binariesw$\maven`


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

Our CS-Studio GUI dependencies are located on a share on shadow, a read only version `\\shadow.isis.cclrc.ac.uk\ICP_P2$\css_gui_dependencies` (which is accessible via a webpage at `http://shadow.nd.rl.ac.uk/ICP_P2/css_gui_dependencies/` and a writable version `\\shadow.isis.cclrc.ac.uk\ICP_P2W$\css_gui_dependencies`. To update the CS-Studio components that the GUI uses:
- `git clone --recursive https://github.com/ISISComputingGroup/isis_css_top.git`
- Make relevant changes to the code, make sure submodules get pinned to new versions using same workflow as in EPICS top.
- Trigger a build on Jenkins
- After the build is complete go to the build server and copy the entire isis_css_top tree to the share (`\\shadow.isis.cclrc.ac.uk\ICP_P2W$`)
- Subsequent GUI builds will pick up the new dependencies
- Test that your changes work correctly!
- if you cannot write to the `ICP_P2W$` share on shadow, your fed id account will need adding to the `icp` local group on shadow itself. This just requires somebody to run the `vigr` command on shadow and then possibly `service smb restart` too 

## Archive engines / alarm servers

- The build uses the same process as above
- Once build is done, the products are in `org.csstudio.sns\repository\products`
- Copy the zip files for alarm server, alarm config tool, archive engine and archive config tool to `\\shadow.isis.cclrc.ac.uk\icp_binaries$\CSS`, renaming the directories to match the existing names if necessary
- The changes will be picked up after doing `create_icp_binaries` and then `css\master\setup_css.bat`
- Ensure scripts to launch Archivers and alarm server [1](https://github.com/ISISComputingGroup/EPICS-CSS/blob/master/AlarmServer/run_alarm_server.bat) [2](https://github.com/ISISComputingGroup/EPICS-CSS/blob/master/ArchiveEngine/start_block_archiver.bat) [3](https://github.com/ISISComputingGroup/EPICS-CSS/blob/master/ArchiveEngine/start_inst_archiver.bat) point at correct executables after running `create_icp_binaries.bat` and `setup_css.bat`.

# ActiveMQ

To update activeMQ in epics:
  - Create a vendor branch on `...\EPICS\ISIS\ActiveMQ\master`
  - Put the latest ActiveMQ version (from https://activemq.apache.org/) on this branch
  - Create a PR to merge this in (this PR will be merged as part of the update dependencies ticket)
  - Update the config to include anything new in the new version
  - Update the Log server modules in `EPICS\ISIS\IocLogServer\master\LogServer`

# IOCLogServer

The IOC log server has a similar build process to the main GUI, and includes several `.jar` files in it's repository. These may have new versions and need to be updated.

# Cygwin Tools

`procServ`, `conserver` and `console` are cygwin applications, compiled copies of which are kept centrally in `ICP_Binaries\EPICS_Tools` and then copied into subdirectories of `tools/master` of the EPICS distribution during a build. Their source code is located in the https://github.com/ISISComputingGroup/EPICS-tools repository and they are built by the EPICS_tools Jenkins job which places new versions in `kits$\EPICS_Tools`. The Jenkins job only runs when requested.

If you update the source code of procServ/conserver the following applies too, but we should also update `cygwin` and rebuild the binaries periodically even if the source code is unchanged. To publish new binaries:
- determine the host running the Jenkins job, look at the LABEL parameter of the build (this is currently ndw1757)
- log onto the machine and update cygwin - goto https://www.cygwin.com/ in a web browser from the machine and download and run `setup-x86_64.exe`
- We need to stop it upgrading `libcrypt-devel` from 2.1 to 4.1 so locate `libcrypt-devel` in the pending package list shown and chose "keep" in the dropdown menu next to it.
- (if you forget to do the above, you can always re-run `setup-x86_64.exe` and downgrade `libcrypt-devel` from 4.1 to 2.1)
- let it update packages
- now start the jenkins EPICS_Tools job
- when it has finished, copy new files from `kits$\EPICS_Tools` to `ICP_Binaries\EPICS_Tools`

# NICOS
[Nicos Dependency update steps](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Developing-NICOS).

**Note:**
We are using a fork of NICOS. If updating NICOS, ensure that the protocol versions defined in the client and the server match. The server version is specified in `C:\Instrument\Apps\EPICS\ISIS\ScriptServer\master\nicos\protocols\daemon\classic.py` and the client version in `/uk.ac.stfc.isis.ibex.nicos/src/uk/ac/stfc/isis/ibex/nicos/messages/ReceiveBannerMessage.java`. If these do not match, the script server connection will fail.
    
# Updates to consider

- PCRE (https://github.com/ISISComputingGroup/EPICS-pcre)
- procServ
- EPICS base
- Support modules e.g. StreamDevice, asyn, Lua etc.

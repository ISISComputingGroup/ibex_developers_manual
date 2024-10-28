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

**Note: when updating the eclipse framework itself, you will need to download the same eclipse IDE with the same version number or else some jars may not be found. You also need to update `client.tycho.parent` - see below for details. Make sure you update the [gui build wiki page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-the-GUI) to ensure new starters get the correct version.**

### Parent POM

Tycho and eclipse framework versions are defined in the file `./base/uk.ac.stfc.isis.ibex.client.tycho.parent/pom.xml`. Note that the eclipse framework version *must* correspond with the version defined in the target platform, otherwise the maven build will fail with mismatched framework versions.

### Client JRE

The GUI builds copy a JRE from `\\isis\inst$\Kits$\CompGroup\ICP\ibex_client_jdk<jdk_version>`. Copy the latest jdk to ICP, rename to follow the same format, and then update `ibex_gui\build\build.bat` to point at the new JRE location.

### Pydev

- git clone --recurse-submodules the latest version of [our fork](https://github.com/ISISComputingGroup/Pydev) and create a new dependency update branch off of master. 
- git clone --recurse-submodules the latest version of [the upstream](https://github.com/fabioz/Pydev) on to a vendor branch and merge this branch into the dependency update branch.
- Run `mvn install` in the dependency update branch base directory. 
- After a successful build, create a PR to merge the changes into master, and upload the updated repo to `\\shadow.isis.cclrc.ac.uk\ICP_P2W$`, this latest version should be named 'Pydev'.
- Remove and re-add the Pydev target platform dependency in the GUI

# Python

## Python itself

- Check on Python.org for newer versions of python itself
- If a newer version is available, download the "windows installer".
- Select custom install, install python to a location of your choice (not `c:\instrument\apps\python3`).
- During the python installation process, **ensure that you tick the box asking whether you want to install TCL/TK support** in optional features. This is needed for independent matplotlib plots in standalone genie_python windows.
- Also during the python installation process, in advanced options screen select both `download debugging symbols` and `download debug binaries`
- Zip up the resulting directory and add it to the share at `\\isis\inst$\Kits$\CompGroup\ICP\genie_python_dependencies_python_3` as `python_clean_<version>.zip`
- Edit `package_builder\common_build_python_3.bat` to use the new python version and test that all dependencies work correctly
- Edit SUPPORTED_PYTHON_VERSION in `genie_python\genie.py`

## Python packages

Check on PyPi for any package updates, then edit `requirements.txt` to install new versions where needed. Note that since we decided [all python projects should use virtual environments](Python-dependencies#how-python-dependencies-should-be-handled-in-the-future) there will be `requirements.txt`files for all Python projects using the new import mechanism, ensure these are also updated.

### ODE

ODE is handled separately from other packages and is installed from a wheel on `\\isis\inst$\Kits$\CompGroup\ICP\genie_python_dependencies_python_3` if moving to a new python version i.e. 3.10 to 3.11 this wheel will need to be replaced. 
* First check [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ode) for a matching version of ODE, if one is not present one will need to be built, to do so:
    * Make a note of the latest release tag from the [ODE Bitbucket](https://bitbucket.org/odedevs/ode/downloads/?tab=tags)
    * open a cmd window and cd to e.g. `c:\devel`
    * run `git clone https://bitbucket.org/odedevs/ode.git`
    * If `0.16.4` is your version to build then `cd ode && git checkout 0.16.4`
    * type `set "CMAKE=c:\Instrument\Apps\EPICS\ICP_Binaries\CMake\bin\cmake.exe"`
    * type `mkdir ode-build && cd ode-build`
    * run `"%CMAKE%" -G"Visual Studio 16 2019" -A x64 ..`
    * type `start ode.sln`
    * change to `Debug` to `Release` configuration at top, it should already say x64, and from menu build -> build solution
    * now cd to the `bindings\python directory`
    * open ode.pyx, change definition of `collide_callback` to add `noexcept` i.e. `cdef void collide_callback(void* data, dGeomID o1, dGeomID o2):` to `cdef void collide_callback(void* data, dGeomID o1, dGeomID o2) noexcept:`
    * Navigate to `bindings/python` and open the `setup.py`
    * Add `from wheel.bdist_wheel import bdist_wheel` to the imports at top.
    * remove the whole try/except clause that calls `pkg-config` from `Popen`, instead just set the variables explicitly e.g. `ode_cflags = [r'-IC:\devel\ODE\include', r'-IC:\devel\ODE\ode-build\include']` and `ode_libs = [r'C:\devel\ODE\ode-build\Release\ode_double.lib']`
    * in main() Update the version number to match the version of ode used, and set the name to `ode`.
    * run `%python3% setup.py build_ext` and then `%python3% setup.py bdist_wheel`
    * copy the wheel generated in `dist` to `\\isis\inst$\Kits$\CompGroup\ICP\genie_python_dependencies_python_3`
    * copy `ode_double.dll` from `C:\devel\ODE\ode-build\Release` to the same place
* Edit `common_build_python.bat` in `package_builder` to point to the most recent wheel file.
* Test by running `python run_all_tests.py` in `inst_servers`, which contains collision avoidance monitor tests
   
### Lewis
To update Lewis, merge upstream to our fork: https://github.com/ISISComputingGroup/lewis - This should get picked up automatically by the build server as it installs from the `main` branch of our fork. 

If the version of Lewis is updated the version should be changed in individual support modules in the `lewis_emulators\lewis_versions.py` file. This should also be done for the IOC Generator templates for future IOCs. 
 
# System

### MySQL
Download the latest stable MySQL version as a zip file and put in the share `\\isis\inst$\Kits$\CompGroup\ICP\MySQL` and remove the old one.

In the upgrade script `https://github.com/ISISComputingGroup/ibex_utils/tree/master/installation_and_upgrade/ibex_install_utils` edit `install_tasks.py` to point at the new version.

Update the one in your local machine by running `upgrade_mysql.bat`.

In `create_icp_binaries.bat`, update the unpacked version of MySQL used during the build to the new version added on the share.

In `c:\instrument\apps\epics\support\mysql\master\MySQLCppApp\src\mysql-connector-c++`, update the vendor submodule to a recent version, then rebuild `mysql`, `pvdump`, and then all IOCs, in that order.

### Java
- Get the latest AdoptOpen JDK msi file from `https://adoptium.net/releases.html?jvmVariant=hotspot` and put it in `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions`.
  * Only upgrade major versions to another LTS version.
- Copy the older version onto the `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\old_versions`. 
- Uninstall the older version from control Panel and install the new version.
- Test that running `start_ibex_server.bat` completes successfully, and ensure there are no obvious errors in the IOC log files for:
  * ARBLOCK
  * ARINST
  * ALARM
  * IOCLOG
- Check that CS Studio IDE is loaded correctly

### Maven
- There are two versions of maven, this is to update the one following the format `maven-X.x.x`
- Download the latest maven from `https://maven.apache.org/download.cgi#`
- Delete the older version of the maven
- unzip and copy the content to `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Binaries`
- Update `copy_in_maven.bat` in `\ibex_gui\build\` to point at the new maven version 


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

Our CS-Studio GUI dependencies are located on a share on shadow, a read only version `\\shadow.isis.cclrc.ac.uk\ICP_P2$\` (which is accessible via a webpage at `http://shadow.nd.rl.ac.uk/ICP_P2/` and a writable version `\\shadow.isis.cclrc.ac.uk\ICP_P2W$\`.

CS-Studio requires a version of jdk11 to build that it gets from `C:\Program Files\AdoptOpenJDK` or `C:\Program Files\Eclipse Adoptium`.
- Install the latest jdk11, and ensure `isis_css_top\build.bat` points at the correct jdk location.
- You will need JavaFX binaries. These can be patched onto the AdoptOpenJDK/Eclipse Temurin installation. Download the Windows SDK from \\isis\inst$\Kits$\CompGroup\ICP\Java_utils\openjfx-19_windows-x64_bin-sdk\javafx-sdk-19 (originally from [gluon](https://gluonhq.com/products/javafx/)) and copy the bin, lib, and legal directories over the corresponding directories in the jdk. Note that the JavaFX version does not necessarily need to match your java installation, as long as the versions are compatible. For example we can use JavaFX 19 on a Java 11 installation. Please check that the license is still appropriate before you install.

To update the CS-Studio components that the GUI uses:
- `git clone --recursive https://github.com/ISISComputingGroup/isis_css_top.git`
- Make relevant changes to the code, make sure submodules get pinned to new versions using same workflow as in EPICS top.
- Trigger a build on Jenkins
- After the build is complete go to the build server and copy the entire isis_css_top tree to the share (`\\shadow.isis.cclrc.ac.uk\ICP_P2W$`) rename the folder to `css_gui_dependencies_<year_month_day>`.
- Updated the gui target platform to point at the new folder, i.e. `http://shadow.nd.rl.ac.uk/ICP_P2/css_gui_dependencies_<year_month_day>/p2repo/`
- Reload the target platform and rebuild the gui.
- Test that your changes work correctly!
- if you cannot write to the `ICP_P2W$` share on shadow, your fed id account will need adding to the `icp` local group on shadow itself. This just requires somebody to run the `vigr` command on shadow and then possibly `service smb restart` too 

## Archive engines / alarm servers

- The build uses the same process as above
- Once build is done, the products are in `org.csstudio.sns\repository\products`
- Copy the zip files for alarm server, alarm config tool, archive engine and archive config tool to `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Binaries\CSS`, renaming the directories to match the existing names if necessary (The existing ones should be backed up).
- The changes will be picked up after doing `create_icp_binaries` and then `css\master\setup_css.bat`
- Ensure scripts to launch Archivers and alarm server [1](https://github.com/ISISComputingGroup/EPICS-CSS/blob/master/AlarmServer/run_alarm_server.bat) [2](https://github.com/ISISComputingGroup/EPICS-CSS/blob/master/ArchiveEngine/start_block_archiver.bat) [3](https://github.com/ISISComputingGroup/EPICS-CSS/blob/master/ArchiveEngine/start_inst_archiver.bat) point at correct executables after running `create_icp_binaries.bat` and `setup_css.bat`.

# ActiveMQ

To update ActiveMQ in epics:
  - Create a new branch on `...\EPICS\ISIS\ActiveMQ\master`.
  - Put the latest ActiveMQ version (from https://activemq.apache.org/) on the vendor branch that already exists on the repo.
  - Merge the vendor branch into your new branch
  - Create a PR to merge this in to master (this PR will be merged as part of the update dependencies ticket).

# IOCLogServer

The IOC log server has a similar build process to the main GUI, and includes several `.jar` files in it's repository. These may have new versions and need to be updated.

Update `EPICS\ISIS\IocLogServer\master\LogServer\pom.xml` with new dependency version numbers.

# Cygwin Tools

`procServ`, `conserver` and `console` are cygwin applications, compiled copies of which are kept centrally in `ICP_Binaries\EPICS_Tools` and then copied into subdirectories of `tools/master` of the EPICS distribution during a build. Their source code is located in the https://github.com/ISISComputingGroup/EPICS-tools repository and they are built by the EPICS_tools Jenkins job which places new versions in `kits$\EPICS_Tools`. The Jenkins job only runs when requested.

If you update the source code of procServ/conserver the following applies too, but we should also update `cygwin` and rebuild the binaries periodically even if the source code is unchanged. To publish new binaries:
- determine the host running the Jenkins job, look at the LABEL parameter of the build (this is currently ndhspare53)
- log onto the machine and update cygwin - goto https://www.cygwin.com/ in a web browser from the machine and download and run `setup-x86_64.exe`
- let it update packages

There are two cygwin distributions on the computer in `c:\cygwin64` and `c:\mini_cygwin64`, the one in `cygwin64` is used to build programs and the one in `mini_cygwin64` is a minimal distribution that is copied to the instrument along with the built procServ/conserver programs to provide a runtime environment. Both of these need to be updated, so you will **need to run the above setup twice** changing the installation directory between runs. when you update `c:\mini_cygwin64` there will likely be very few packages and nothing additional needs to be done other than update it. After you update the main `cygwin64` you will need to disable ASLR on cygwin1.dll     

- now start the jenkins EPICS_Tools job, this will build and update `kits$\Binaries\EPICS_Tools` 

# NICOS
[Nicos Dependency update steps](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Developing-NICOS).

**Note:**
We are using a fork of NICOS. If updating NICOS, ensure that the protocol versions defined in the client and the server match. The server version is specified in `C:\Instrument\Apps\EPICS\ISIS\ScriptServer\master\nicos\protocols\daemon\classic.py` and the client version in `/uk.ac.stfc.isis.ibex.nicos/src/uk/ac/stfc/isis/ibex/nicos/messages/ReceiveBannerMessage.java`. If these do not match, the script server connection will fail.
    
# Updates to consider

- PCRE (https://github.com/ISISComputingGroup/EPICS-pcre)
- procServ
- EPICS base
- Support modules e.g. StreamDevice, asyn, Lua etc.
- Google test for EPICS (`gtest`) (https://github.com/epics-modules/gtest)


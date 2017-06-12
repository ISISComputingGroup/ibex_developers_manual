> [Wiki](Home) > [The Backend System](The-Backend-System) > First time installing and building (Windows)

*You can get more information on the development workflow [here](Git-workflow)*.

# Things to know as a developer
See https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Things-to-know-as-a-developer

# Install Perl
Download and install [Strawberry Perl](http://strawberryperl.com/)

# Install WiX toolset (used for building MSI installer files)
Latest stable version from http://wixtoolset.org/releases/

# Install Visual Studio

See  [Install Visual Studio](Install-Visual-Studio)

# Install CMake
Install [CMake](https://cmake.org/download/) 

# Install Java SDK
Install the [Java SDK for Windows x64](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

# Install Maven 
Install [Maven](https://maven.apache.org/download.cgi) and follow the 'Windows tips' in [these instructions ](https://maven.apache.org/install.html) to set environment variables for the SDK with JAVA_HOME and maven in PATH
It is recommended to install Maven into `C:\Tools\`

# Install Git 
Install Git [Getting-started-with-Git-and-GitHub](Getting-started-with-Git-and-GitHub)

# Recursive clone from git

In `C:\Instrument\Apps\` run:

`git clone --recursive https://github.com/ISISComputingGroup/EPICS.git`

# Install MySQL

See [Installing and upgrading MySQL](Installing-and-Upgrading-MySQL)

# Install genie_python

Run the `genie_python_install.bat` batch file located in `\\isis\inst$\Kits$\CompGroup\ICP\genie_python\BUILD-<highest number>` 

# Build EPICS back-end
`cd` to `C:\Instrument\Apps\EPICS\` and run `build.bat`
Note that take some time and should end with building the documentation.

Certain items will not be built when using VS2013, these are:
*  Mk3Chopper support module and IOC - only builds with VS2010

If you see `Error 2: file not found`, you may not have installed the correct windows SDK or visual studio version. Check for `rc.exe` in `C:\Program Files (x86)\Windows Kits\10\bin\x86\` (as appropriate for your system). If you don't have `rc.exe`, try installing the windows SDK appropriate for your operating system.

# Set up the CS-Studio archiver
In `C:\Instrument\Apps\EPICS\CSS\master` run `setup_css.bat`
this will create directories for the archive engine. in `.\css-win.x86_64`

# Setting up a configurations directory

* Create the following folder structure: `C:\Instrument\Settings\config`

* Navigate to the config folder

* Via a git client clone the repository from 'http://spudulike@control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git' to a directory with your machine name, like so:
```
git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git NDWXXX
```
* Confirm that you now have the config file structure in place (components, configurations and synoptics directories)

* Create a branch from master with the machine name (if on an instrument) or your fedid if on a dev machine:
```
cd NDXXX/
git checkout -b NDXXXX
rename 'Python\init_inst_name.py' to 'Python\init_<Inst name>.py'
git add Python\init_<Inst name (lowercase e.g. iristest1)>.py
git rm Python\init_inst_name.py
git commit -m"create initial python"
git push --set-upstream origin NDWXXXX
```
Any configs created through IBEX will now be stored on this branch (they will only be pushed remotely if you do a manual push first e.g. the last line above)

These repositories can be web browsed via [http://control-svcs.isis.cclrc.ac.uk/git/](http://control-svcs.isis.cclrc.ac.uk/git/)

* It is possible to access the configurations of another developer or of an instrument by fetching the correct branch and switching to it, like so:
```
git fetch
git checkout NDXALF
```
Note: The developer branch has been created to store useful configurations that may be shared amongst all developers.

Note that if this is not a new instrument, or that if the instrument already has a branch in the configs git that rather than the steps above, the following should be undertaken, as the branch should already exist:
```
cd C:\Instrument\Settings\config
git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git NDXXXX
cd NDXXXX
git checkout NDXXXX
```

# Setting up a calibrations directory

Run the following command from a Git-enabled command prompt (or modify target to run with Git Bash):

```
git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git C:\Instrument\Settings\config\common
```

The purpose and function of the calibration files are described [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Calibration-Files).

# Configure DAE for simulation mode on developer's computer

* Open an administrator command prompt (right click on command prompt in start menu and click "run as administrator")
* cd to     c:\Instrument\Apps\EPICS\ICP_Binaries\isisdae\x64\Release
* Type:
```
    isisicp.exe /RegServer
    isisdatasvr.exe /RegServer
```
Unfortunately the /RegServer registration process doesn't report either success or failure. If, on later starting the ISISDAE IOC, you see lots of errors of the form "CoCreateInstanceEx (ISISICP) : Class not registered" then it means the /RegServer flag did not work. Try registering it again in case you were not Administrator when you tried it the first time. 

# Setting up nicos

Nicos needs some local passwords setting; to do this look at:

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/ISIS-Proxy#security

# Building the GUI

After following the above instructions please see [Building the GUI](Building-the-GUI).
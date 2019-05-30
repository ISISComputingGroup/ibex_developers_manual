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

# Install Java JDK

Install **OpenJDK 8 hotspot** from https://adoptopenjdk.net/releases.html#x64_win (the MSI installer is fine, tick all the boxes when it asks you which components to install)

Do not install an Oracle JDK.

You may wish to install some optional java components [as detailed here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Upgrade-Java#additional-optional-steps-for-developer-installations-not-required-on-instruments).

# Install Maven 
Install [Maven](https://maven.apache.org/download.cgi) and follow the 'Windows tips' in [these instructions ](https://maven.apache.org/install.html) to set environment variables for the SDK with JAVA_HOME and maven in PATH
It is recommended to install Maven into `C:\Tools\`

# Install Git 
Install Git [Getting-started-with-Git-and-GitHub](Getting-started-with-Git-and-GitHub)

# Recursive clone from git

Navigate to `C:\Instrument\Apps\` and check whether the EPICS directory already exists. If so, remove the EPICS directory before continuing.
  
In `C:\Instrument\Apps\` run:

`git clone --recursive https://github.com/ISISComputingGroup/EPICS.git`

# Install MySQL

See [Installing and upgrading MySQL](Installing-and-Upgrading-MySQL)

# Install genie_python

See [Building and installing genie_python](Building-and-Installing-genie_python)

# Build EPICS back-end
`cd` to `C:\Instrument\Apps\EPICS\` and run `build.bat`
Note that this will take some time and should end with building the documentation.

Certain items will not be built when using VS2013, these are:
*  Mk3Chopper support module and IOC - only builds with VS2010

If you see `Error 2: file not found`, you may not have installed the correct windows SDK or visual studio version. Check for `rc.exe` in `C:\Program Files (x86)\Windows Kits\10\bin\x86\` (as appropriate for your system). If you don't have `rc.exe`, try installing the windows SDK appropriate for your operating system.

Whilst this is building you can independently start [Building the GUI](Building-the-GUI).

# Set up the CS-Studio archiver
In `C:\Instrument\Apps\EPICS\CSS\master` run `setup_css.bat`
this will create directories for the archive engine. in `.\css-win.x86_64`

# Setting up the configurations & scripting directory

* Create the following folder structure: `C:\Instrument\Settings\config`

* Navigate to the config folder

* Enable git credential store and set a username, on a developer machine use your own name rather than "spudulike" of course, on a developer machine replace NDXXXX with the name of your computer, on an instrument use the real instrument name  
```
git config --global core.autocrlf true
git config --global credential.helper wincred
git config --global user.name "spudulike"
git config --global user.email "spudulike@ndxxxx.isis.cclrc.ac.uk"
```

* Enable default recursive check
```
git config --global push.recurseSubmodules check
```

* Via a git client clone the repository from 'http://spudulike@control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git' to a directory with your machine name, like so:
```
git clone http://spudulike@control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git NDXXXX
```
 (when prompted, give spudulike password)

* Confirm that you now have the config file structure in place (components, configurations and synoptics directories)

* Create a branch from master with the machine name (if on an instrument) or your fedid if on a dev machine:
```
cd NDXXXX/
git checkout -b NDXXXX
rename Python\init_inst_name.py Python\init_<Inst name (lowercase e.g. iristest1)>.py
git add Python\init_<Inst name (lowercase e.g. iristest1)>.py
git rm Python\init_inst_name.py
git commit -m"create initial python"
git push --set-upstream origin NDXXXX
```

(Note, the init_inst_name python file should have underscores rather than dashes if the machine name contains dashes. So `NDWTEST-BLAH` would have the init file `init_ndwtest_blah.py`).

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

If the `C:\Instrument\Settings\config\common` directory already exists, cd into it and do a `git pull` on master. Else run the following command from a Git-enabled command prompt (or modify target to run with Git Bash):

```
git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git C:\Instrument\Settings\config\common
```

The purpose and function of the calibration files are described [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Calibration-Files).

# Configure DAE for simulation mode on developer's computer / Register ISISICP

* Make sure **ISISDAE-IOC-01.exe** and **ISISICP.exe** processes are not running
* run    **create_icp_binaries.bat**   in  **c:\Instrument\Apps\EPICS**   to get the latest version 
* Open an administrator command prompt (right click on command prompt in start menu and click "run as administrator")
* cd to     **c:\Instrument\Apps\EPICS\ICP_Binaries\isisdae\x64\Release**
* Type:
```
    isisicp.exe /RegServer
    isisdatasvr.exe /RegServer
```
Unfortunately the /RegServer registration process doesn't report either success or failure. If, on later starting the ISISDAE IOC, you see lots of errors of the form "CoCreateInstanceEx (ISISICP) : Class not registered" then it means the /RegServer flag did not work. Try registering it again in case you were not Administrator when you tried it the first time. If you get messages about missing method/functions etc. it may mean a previous isisicp.exe registered successfully, but the newer one didn't - just try again as administrator

# Building the GUI

After following the above instructions please see [Building the GUI](Building-the-GUI).

# VNC

If you are supporting instruments it may be useful to download a VNC client. We have not settled on one that we all use but we have used:

 - tighVNC (just the client) which is available [here](http://www.tightvnc.com/)
 - VNC Viewer (just the client) which is available [here](https://www.realvnc.com/en/connect/download/viewer/)

# Utilities

Git clone (usually in c:\Instrument\Dev) the following utilities:

```
git clone https://github.com/ISISComputingGroup/IBEX_device_generator.git
git clone https://github.com/ISISComputingGroup/ibex_utils.git
git clone https://github.com/ISISComputingGroup/ConfigChecker.git
```

# NI DAQ

Some IOCs depends on DAQMX binaries from national instruments. Go to http://sine.ni.com/psp/app/doc/p/id/psp-268 and download the latest DAQMX drivers. When installing, ensure you check the box to install DAQMX.

If you do not do this step, you will be unable to run certain IOCs (e.g. riken power supplies, muon separator), and consequently some of their tests will fail.

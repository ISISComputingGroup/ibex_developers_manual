### Create directory structure
Create these directories from the command line: C:\Instruments\Apps\

### Install Perl
Download and install [Strawberry Perl](http://strawberryperl.com/)

### Install Visual Studio 2010
Install Visual Studio 2010 
Install SDK 7.1 
-The SDK may fail if you have these installed: 
* Microsoft Visual C++ 2010 x86 Redistributable
* Microsoft Visual C++ 2010 x64 Redistributable

If these do exist on your computer you need to uninstall them before installing the SDK.

Install: 
* Visual Studio 2010 SP1
* Visual C++ 2010 SP1 Compiler Update for the Windows SDK 7.1

### Install CMake
Install [CMake](https://cmake.org/download/) 

### Install Java SDK
Install the [Java SDK for Windows x64](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

### Install Maven 
Install [Maven](https://maven.apache.org/download.cgi) and follow the 'Windows tips' in [these instructions ](https://maven.apache.org/install.html) to set environment variables for the SDK with JAVA_HOME and maven in PATH

### Install Git 
Install Git from [here](https://git-scm.com/download/win). Optionally you may wish to install [Tortoise Git](https://tortoisegit.org/) too, which provides useful tools for diffs and merging. 

### Install MySQL
Install MySQL 5.6 from [here](https://dev.mysql.com/downloads/windows/installer/5.6.html)

Select "server only"/"server machine" on first page of install wizard and change the data path to `c:\instrument\var\mysql` 

Make sure you use the agreed password for the root directory. If you don't know what that password is you should be able to find it in `/Instrument/Apps/EPICS/CSS/master/ArchiveEngine/setup_mysql_database.txt`.

Do leave TCP/IP access enabled.

Once installed run the `config_mysql.bat` batch file in `EPCIS/SystemSetup/`.

Note: For running tests locally, make sure that you have run `Create test account.bat` from `EPICS/SystemSetup/` as well.

### Recursive clone from git
`git clone --recursive https://github.com/ISISComputingGroup/ibex_gui.git`

### Install genie_python

Run the `genie_python_install.bat` batch file located in `\\isis\inst$\Kits$\CompGroup\ICP\Client\genie_python`

### Install Python modules

In a command window run:
`install_python_modules.bat`

If mysql-connector-python fails, download it from ​[here](http://dev.mysql.com/downloads/connector/python/). The Windows installers don't seem to work, instead select "Platform Independent" and download the source zip, then unpack and run the usual `python setup.py install`

### Run build.bat
`cd` to `\Instrument\Apps\EPICS\` and run `build.bat`

### Run setup_css.bat
In `Instrument\Apps\EPICS\CSS\master` run `setup_css.bat`
this will create directories for the archive engine. in `.\css-win.x86_64`

### Setting up a configurations directory

* Create the following folder structure: `C:\Instrument\Settings\config`

* Navigate to the config folder

* Via a git client clone the repository from 'http://spudulike@control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git' to a directory with your machine name, like so:
```
git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git NDWXXX
```
* Confirm that you now have the config file structure in place (components, configurations and synoptics directories)

* Create a branch from master with an identifiable name (e.g. name or fed-id):
```
cd NDWXXX/
git checkout -b myfedid
```
Any configs created through IBEX will now be stored on this branch

* It is possible to access the configurations of another developer or of an instrument by fetching the correct branch and switching to it, like so:
```
git fetch
git checkout NDXALF
```
Note: The developer branch has been created to store useful configurations that may be shared amongst all developers.

### Building the GUI

After following the above instructions please see [Building the GUI](Building-the-GUI).
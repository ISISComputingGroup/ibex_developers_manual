### Create directory structure
Create these directories from the command line: C:\Instruments\Apps\

### Install Perl
Download and install [Strawberry Perl ](http://strawberryperl.com/)

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
Install Git from [here](https://git-scm.com/download/win)

### Install MySQL
Install mySQL 5.6 [here](https://dev.mysql.com/downloads/windows/installer/5.6.html)

Select "server only"/"server machine" on first page of install wizard and change the data path to `c:\instrument\var\mysql` 

Make sure you use the agreed password for the root directory. If you don't know what that password is you should be able to find it in `/Instrument/Apps/EPICS/CSS/master/ArchiveEngine/setup_mysql_database.txt`.

Do leave TCP/IP access enabled.

### Recursive clone from git
`git clone --recursive https://github.com/ISISComputingGroup/ibex_gui.git` 

### Run build.bat
`cd` to `\Instrument\Apps\EPICS\` and run `build.bat`

### Run setup_css.bat
In `Instrument\Apps\EPICS\CSS\master` run `setup_css.bat`
this will create directories for the archive engine. in `.\css-win.x86_64`

### 



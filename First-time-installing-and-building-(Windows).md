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

### Install maven (set environment variables for the SDK with JAVA_HOME and maven in PATH)
Install [Maven](https://maven.apache.org/download.cgi) and follow the 'Windows tips' in [these instructions ](https://maven.apache.org/install.html)

### Install Git 
Install Git from [here](https://git-scm.com/download/win)

### Recursive clone from git
`git clone --recursive https://github.com/ISISComputingGroup/ibex_gui.git` 

### Run build.bat
`cd` to `\Instrument\Apps\EPICS\` and run `build.bat`

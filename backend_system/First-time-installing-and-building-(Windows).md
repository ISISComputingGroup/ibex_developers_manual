> [Wiki](Home) > [The Backend System](The-Backend-System) > First time installing and building (Windows)

*You can get more information on the development workflow [here](Git-workflow)*.

# Install Perl
Download and install [Strawberry Perl](http://strawberryperl.com/)

# Install Visual Studio 2010
Install Visual Studio 2010 

Install SDK 7.1 
-The SDK may fail if you have these installed: 
* Microsoft Visual C++ 2010 x86 Redistributable
* Microsoft Visual C++ 2010 x64 Redistributable

If these do exist on your computer you need to uninstall them before installing the SDK.

Install: 
* Visual Studio 2010 SP1
* Visual C++ 2010 SP1 Compiler Update for the Windows SDK 7.1

# Install Visual Studio 2013
Windows SDK 7 has compatibility issues with newer versions of Windows. In this case, Visual Studio 2013 may be used instead.

During the installation of VS2013, under "Optional Features" make sure to include Microsoft Foundation Classes for C++.

Additionally, download and install the [Multibyte MFC Library](https://www.microsoft.com/en-us/download/details.aspx?id=40770).

# Install CMake
Install [CMake](https://cmake.org/download/) 

# Install Java SDK
Install the [Java SDK for Windows x64](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

# Install Maven 
Install [Maven](https://maven.apache.org/download.cgi) and follow the 'Windows tips' in [these instructions ](https://maven.apache.org/install.html) to set environment variables for the SDK with JAVA_HOME and maven in PATH

# Install Git 
Install Git [Getting-started-with-Git-and-GitHub](Getting-started-with-Git-and-GitHub)

# Recursive clone from git

In `C:\Instrument\Apps\` run:

`git clone --recursive https://github.com/ISISComputingGroup/EPICS.git`

# Install MySQL
Install MySQL 5.6 from [here](https://dev.mysql.com/downloads/windows/installer/5.6.html)

For "Choosing a Setup Type," select "Server only"
On the next page, set the Data Directory to `C:\Instrument\Var\mysql`

After it installs you will get to the "Type and Networking" page, for the "Config Type" choose "Server Machine".

Leave TCP/IP access enabled.

On the "Accounts and Roles" page make sure you use the agreed password for root. 
If you don't know what that password is you should be able to find it in `C:\Instrument\Apps\EPICS\CSS\master\ArchiveEngine\setup_mysql_database.txt`. Do not follow the instructions in this file.

Under "Windows Service" make sure "Start the MySQL Server at System Startup" is **checked**

Once installed run the `config_mysql.bat` batch file in `C:\Instrument\Apps\EPICS\SystemSetup\`.

Note: For running tests locally, make sure that you have run `create_test_account.bat` from `C:\Instrument\Apps\EPICS\SystemSetup\` as well.

# Install genie_python

Run the `genie_python_install.bat` batch file located in `\\isis\inst$\Kits$\CompGroup\ICP\Client\genie_python`

# Build EPICS back-end
`cd` to `C:\Instrument\Apps\EPICS\` and run `build.bat`
Note that take some time and should end with a build complete message, if it hasn't seek help!

Certain items will not be built when using VS2013, these are:
*  Mk3Chopper support module and IOC - only builds with VS2010

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

* Create a branch from master with an identifiable name (e.g. name or fed-id):
```
cd NDWXXX/
git checkout -b myfedid
```
Any configs created through IBEX will now be stored on this branch

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

Now create the common configuration with
```
git clone http://spudulike@control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git C:\Instrument\Settings\config\common
```

### Configure DAE for simulation mode on developer's computer

* Open an administrator command prompt (right click on command prompt in start menu and click "run as administrator")
* cd to     c:\Instrument\Apps\EPICS\ICP_Binaries\isisdae\x64\Release
* Type:
```
    isisicp.exe /RegServer
    isisdatasvr.exe /RegServer
```
Unfortunately the /RegServer registration process doesn't report either success or failure. If, on later starting the ISISDAE IOC, you see lots of errors of the form "CoCreateInstanceEx (ISISICP) : Class not registered" then it means the /RegServer flag did not work. Try registering it again in case you were not Administrator when you tried it the first time. 

### Building the GUI

After following the above instructions please see [Building the GUI](Building-the-GUI).
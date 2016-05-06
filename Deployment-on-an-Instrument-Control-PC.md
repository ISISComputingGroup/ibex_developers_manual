#Installing IBEX on an Instrument Control PC

This document describes the steps necessary to install IBEX on an Instrument control PC.  In due course some, or all, of the steps may be superseded by an automated installation process (e.g. a .msi file).  Until then, this document is a useful reference.

## Preparatory Steps

- Check that 7-Zip is installed on the PC.  If not, download the latest version from the 7-Zip web-site (http://www.7-zip.org/) and install it.
- Check that Java is installed on the PC.  If not, download the latest JRE from the Java web-site (http://www.java.com/en/) and install it.  Make sure you choose the 64-bit version of Java.
- Create directories on the local hard drive as follows:

    mkdir C:\Instrument\Apps\EPICS
    mkdir C:\Instrument\Apps\Python
    mkdir C:\Instrument\Apps\Client
    mkdir C:\Instrument\Settings\config
    cd C:\Instrument

- Checkout Config Directory

    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-configurations-directory)

- Check that MySQL v5.6 is installed on the PC.  If not,
    - download the MySQL installer `mysql-installer-community-5.6.16.0` from `\\isis\inst$\Kits$\External\BuildServer(ndwvegas)` and install it.
    - during the MySQL installation process,
        - use the password `isis@instdb99`
        - select a "server only" installation
        - change the data path to `C:\Instrument\var\mysql`
        - choose "server machine" during configuration
        - leave TCP/IP enabled
    - You may need to re-boot after installing MySQL

## Install EPICS

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use pushd instead of cd):

    `cd \\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_CLEAN_win7_x64`

- Inside the `EPICS_CLEAN_win7_x64` folder you will see a number of folders with names of the form `BUILD-nnn`, where `nnn` is a 3 digit number.  Change directory to the build folder which contains the most recent successful clean build.  

- Inside the `BUILD-nnn` folder you will find a file called `install_to_inst.bat`.  Run the command `install_to_inst.bat`.  This will copy the contents of the above directory to `C:\Instrument\Apps\EPICS`.

- Configure the archive engine:

    cd c:\Instrument\Apps\EPICS\SystemSetup
    config_mysql

Note: If you run the `config_mysql.bat` script on an existing system YOU MAY LOSE HISTORICAL LOG DATA.


## Install IBEX Client

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use pushd instead of cd):

    cd \\isis\inst$\Kits$\CompGroup\ICP\Client

- Inside this folder you will see a number of folders with names of the form `BUILDmmm`, where `mmm` is a 3 digit number.  Change directory to the build folder which contains the most recent successful clean build.  

- Run the command `install_client.bat`.  This will copy the contents of the above directory to `C:\Instrument\Apps\Client`.  It will also install genie_python.

- You might find it convenient to create a desktop shortcut to use to launch the IBEX client.


## Start the Instrument

To start the instrument, open a command prompt and type the following:

    cd c:\Instrument\Apps\EPICS
    start_inst
    
Allow the `start_inst` script a few moments to complete before starting the IBEX client.


## Stop the Instrument

To stop the instrument, exit from the IBEX client (if you are running it), then open a command prompt and type the following:

    cd c:\Instrument\Apps\EPICS
    stop_inst
    
Allow the `stop_inst` script a few moments to complete.


Further Information

There is further installation related information on the following pages:

- `Initial Setup <https://trac.isis.rl.ac.uk/ICP/wiki/InitialSetup>`_
- `Setup Motion Set Points <https://trac.isis.rl.ac.uk/ICP/wiki/SetupMotionSetPoints>`_
- `Installation Troubleshooting <https://trac.isis.rl.ac.uk/ICP/wiki/InstallTroubleshoot>`_


}}}
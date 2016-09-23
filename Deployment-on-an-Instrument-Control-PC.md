> [Wiki](Home) > [Deployment](Deployment) > Deployment on an Instrument Control PC

This document describes the steps necessary to install IBEX on an Instrument control PC.  In due course some, or all, of the steps may be superseded by an automated installation process (e.g. a .msi file).  Until then, this document is a useful reference. If you are upgrading a release some steps will not be needed.

## Preparatory Steps

- If needed take screen shots of running instrument (then got list of blocks, configurations, synoptics etc.).
- Stop running instrument and GUI.
- Backup old directories
    * Consider deleting old backups.
    * Create `D:\data\old\ibex_backup_YYYY_MM_DD` e.g. `ibex_backup_2016_02_22`
       * **Note:** always create the backup folder in `D:\data\old`.  This makes it easy to delete the backup and recover the disk space when the backup is no longer required.
    * **_Move_** `EPICS`, `Python` and `Client` directories from `C:\instrument\apps` to backup directory
    * **_Copy_** the following directories to backup directory:
        1. `C:\instrument\settings`
        1. `C:\instrument\var\autosave`
        1. `C:\instrument\var\mysql`
- If you are using any serial devices with the system, don't forget to check that nport is installed, and configure the COM settings as standard (moxa 1 starts at COM5, moxa 2 at COM21, etc.)
- Check that 7-Zip is installed on the PC.  If not, download the latest version from the 7-Zip web-site (http://www.7-zip.org/) and install it.
- Check that git is installed on the PC.  If not, download the latest version from the Git web-site (https://git-scm.com/download/win) and install it.
- Check that Java is installed on the PC.  If not, download the latest JRE from the Java web-site (http://www.java.com/en/) and install it.  Make sure you choose the 64-bit version of Java.
- If the PC is running the Windows Classic theme, switch it to a modern theme (e.g. Windows 7 Theme); the IBEX GUI looks better when using a modern theme.  To change the theme see [Change Windows Theme](Change Windows Theme).
- Check that the LabVIEW modules are installed in `C:\labview modules`.  If the LabVIEW modules are not installed you can proceed, but there some extra steps you need to perform (see below)

- Checkout Config Directory

    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-configurations-directory)

- Checkout Calib Directory

    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-calibrations-directory)



- Create directories on the local hard drive as follows:
```
mkdir C:\Instrument\Apps\EPICS
mkdir C:\Instrument\Apps\Client
mkdir C:\Instrument\Settings\config
mkdir C:\scripts
cd C:\Instrument
```

- Check that MySQL v5.6 is installed on the PC.
   - If a different version of MySQL is already installed, you should consider removing it and installing MySQL v5.6.
   - If MySQL v5.6 is already installed, you might wish to consider removing it and doing a clean re-install.
   - If you decide to remove a previous installation of MySQL (v5.6 or otherwise), please ensure you fully remove it before installing MySQL v5.6.
      - use the MySQL uninstaller from the Programs & Features control panel to remove MySQL
      - after uninstalling, confirm that no MySQL features remain listed in the Programs & Features control panel
   - If MySQL v5.6 is not already installed, or you are doing a clean re-install:
      - download the MySQL installer `mysql-installer-community-5.6.16.0` from `\\isis\inst$\Kits$\External\BuildServer(ndwvegas)` and install it.
      - during the MySQL installation process,
         - use the password `isis@instdb99`
         - select a "server only" installation
         - change the data path to `C:\Instrument\var\mysql`
         - choose "server machine" during configuration
         - leave TCP/IP enabled
      - You may need to re-boot after installing MySQL

## Install EPICS

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use `pushd` instead of `cd`):

    `cd \\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_CLEAN_win7_x64`

- Inside the `EPICS_CLEAN_win7_x64` folder you will see a number of folders with names of the form `BUILD-nnn`, where `nnn` is a 3 digit number.  Change directory to the build folder which contains the most recent successful clean build.  

- Inside the `BUILD-nnn` folder you will find a file called `install_to_inst.bat`.  Run the command `install_to_inst.bat`.  This will copy the contents of the above directory to `C:\Instrument\Apps\EPICS`.

- Configure the archive engine:

```
    cd C:\Instrument\Apps\EPICS\SystemSetup
    config_mysql
```

Note: **BE CAREFUL.**  If you run the `config_mysql.bat` script on an existing system **YOU MAY LOSE HISTORICAL LOG DATA**.

- Make changes documented in Release notes between previous version and current version; You may wish to update the GUI before doing this (see [Releases](https://github.com/ISISComputingGroup/IBEX/wiki#releases))

- Record the release to the instrument (add to list in [Instrument Releases](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information))

- Make sure these [tests are performed](server-release-tests), these are items we have missed in the past.

## Install IBEX Client

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use `pushd` instead of `cd`):

    `cd \\isis\inst$\Kits$\CompGroup\ICP\Client`

- Inside this folder you will see a number of folders with names of the form `BUILDmmm`, where `mmm` is a 3 digit number.  Change directory to the build folder which contains the most recent successful clean build.  

- Run the command `install_client.bat`.  This will copy the contents of the above directory to `C:\Instrument\Apps\Client`.  It will also install genie_python.

- You might find it convenient to create a desktop shortcut to use to launch the IBEX client.

- Make changes documented in Release notes between previous version and current version (see [Releases](https://github.com/ISISComputingGroup/IBEX/wiki#releases)). 

- If releasing to an instrument record the release to the instrument (add to list in [Instrument Releases](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information))

- Make sure these [tests are performed](client-release-tests), these are items we have missed in the past.

## Extra step for machines with no LabVIEW modules directory

On most instruments there will be a `C:\labview modules` directory containing sample environment plus DAE programs. If you are installing EPICS on a non-instrument and need to start the DAE in simulation mode, then you need to  

    cd C:\Instrument\Apps\EPICS
    create_icp_binaries
    
## Register DAE

Register the `isisicp.exe` program (either in `C:\labview modules\dae\...` or `ICP_Binaries\...`) as per developer setup instructions

## If upgrading an existing instrument

Step through the TODO list in the release notes.

## Start the Instrument

To start the instrument, open a command prompt and type the following:

    cd C:\Instrument\Apps\EPICS
    start_ibex_server
    
Allow the `start_ibex_server` script a few moments to complete before starting the IBEX client.


## Stop the Instrument

To stop the instrument, exit from the IBEX client (if you are running it), then open a command prompt and type the following:

    cd C:\Instrument\Apps\EPICS
    stop_ibex_server
    
Allow the `stop_ibex_server` script a few moments to complete.

## Add instrument to list of known instruments

If the instrument is not on the list of known instruments already (i.e. for switching the GUI), follow the instructions [here](Making an Instrument Available from the GUI).

## Set up motion set points 

The details of the individual set points for any given device will depend on that device and how it is used on an instrument, but the general principles described here will apply.

### Background
Most devices on ISIS instruments are moved using motors controlled by Galil motion controllers, therefore, configuring motion set points is largely a matter of configuring the Galils correctly.

Key directories on the control server on the control server include

* ``C:\Instrument\Settings\config\NDXxxxxx\configurations\galil``, which includes 
    * ``README_galil_cmd.txt``, a documentation file describing how to configure a Galil controller
    * ``galil1.cmd - galil<N>.cmd``, where `<N>` is the total number of Galil controllers on the instrument
    * ``axes.cmd``, which relates the Sample Stack axes to Galil ports
    * ``jaws.cmd``, which relates the axes of jaw sets to Galil ports
    * ``motionsetpoints.cmd``, which relates the axes of moveable devices to Galil ports and to lookup tables (which define the set positions for the devices)
    * ``sampleChanger.cmd``, which defines positions for the sample changer (the type used on LARMOR).
* ``C:\Instrument\Settings\config\NDXxxxxx\configurations\motionSetPoints``, which includes 
    * ``analyser.txt``, lookup file of x-y coordinates of set-points for LARMOR analyser
    * ``beamstop.txt``, lookup file of x-y coordinates of set-points for LARMOR moving beamstop
    * ``monitor3.txt``, lookup file of y coordinates of set-points for LARMOR analyser
    * ``monitor4.txt``, lookup file of y coordinates of set-points for LARMOR analyser
    * ``pinhole_selector.txt``, lookup file of x-y coordinates (in degrees) of set-points for IMAT pinhole device
    * ``polariser.txt``, lookup file of x-y coordinates of set-points for LARMOR polariser
    * ``sample.txt``, lookup file of x-y coordinates of set-points for LARMOR sample rack.
    * ``sample_x.txt``, lookup file of x coordinate of set-points for LARMOR sample rack.
    * ``sample_y.txt``, lookup file of y coordinate of set-points for LARMOR sample rack.
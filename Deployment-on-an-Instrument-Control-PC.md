> [Wiki](Home) > [Deployment](Deployment) > Deployment on an Instrument Control PC

This document describes the steps necessary to install/upgrade IBEX on an Instrument control PC.  In due course some, or all, of the steps may be superseded by an automated installation process (e.g. a .msi file).  Until then, this document is a useful reference. Steps for upgrading only are marked **upgrade**, streps for inital install are marked **install** other steps should be done for both.

## Preparatory Steps for Client and Server

- As early as possible email the group to let us know of the upgrade. This includes starting point (e.g. v2.2.0) and what is going to be released. This will allow people to comment or add special instructions for various machines if they have forgotten to add them to the IBEX page.

- Inform the instrument scientist that you are going to upgrade the instrument in 5 minutes so that they are not suprised when you remote desktop to the instrument.

- **install** Check that Java is installed on the PC.  If not, download the latest JRE from the Java web-site (http://www.java.com/en/) and install it.  Make sure you choose the 64-bit version of Java.
- **install** If the PC is running the Windows Classic theme, switch it to a modern theme (e.g. Windows 7 Theme); the IBEX GUI looks better when using a modern theme.  To change the theme see [Change Windows Theme](Change Windows Theme).

## Preparatory Steps for Server

- **upgrade** Note the current version number of the instrument (Help->About)

- **upgrade** Take screen shots of running instrument. This ensures it is restarted as it was found and enables you easily to spot changes in config. Items to include: blocks, each perspective, configuration each tab, running ioc's available configs, components and synoptics

- **upgrade** Stop running instrument `ibex_stop_server.bat`.

- **upgrade** Backup old directories
    * Delete backups older than the last backup.
    * Create `C:\data\old\ibex_backup_YYYY_MM_DD` e.g. `ibex_backup_2016_02_22`
    * **_Move_** `EPICS`, `EPICS_utils`, `Python` and `Client` directories from `C:\instrument\apps` to backup directory
    * **_Copy_** the following directories to backup directory:
        1. `C:\instrument\settings`
        1. `C:\instrument\var\autosave`
    * Consider copy db files (check the size >5GB don't bother, unless the database is going to be changed). If you decide to then 
        1. Stop the mysql service (run in admin mode services.msc, find the mysql56 service and stop it)
        1. Copy `C:\instrument\var\mysql` to backup directory
        1. Start the service

- **upgrade** Update the Common Calibration directory.
    1. Do a git status to find out if files have been added or changed (if they have querry why this is and take appropriate action)
    1. Git pull the latest version onto the system (if any file changes make a note so it can be sent to the instrument scientists so they know things have been changed) 

- **install** If you are using any serial devices with the system, don't forget to check that nport is installed, and configure the COM settings as standard (moxa 1 starts at COM5, moxa 2 at COM21, etc.)

- **install** Check that 7-Zip is installed on the PC.  If not, download the latest version from the 7-Zip web-site (http://www.7-zip.org/) and install it.

- **install** Check that git is installed on the PC.  If not, download the latest version from the Git web-site (https://git-scm.com/download/win) and install it.

- **install** Check that the LabVIEW modules are installed in `C:\labview modules`.  If the LabVIEW modules are not installed you can proceed, but there some extra steps you need to perform (see below)

- **install** Create directories on the local hard drive as follows:
    ```
    mkdir C:\Instrument\Settings\config
    mkdir C:\scripts
    ```
- **install** Checkout Common Calibration Directory

    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-calibrations-directory)

- **install** Checkout Config Directory
    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-configurations-directory)

- **install** Check that MySQL v5.6 is installed on the PC.
   - If MySQL is already installed, locate the current data directory and make sure that any pre-existing data is backed up.
   - If a different version of MySQL is already installed, you should remove it and install MySQL v5.6.
   - If MySQL v5.6 is already installed, it is recommended that you remove it and do a clean re-install.
   - If you decide to remove a previous installation of MySQL (v5.6 or otherwise), please ensure you fully remove it before installing MySQL v5.6.
      - use the MySQL uninstaller from the Programs & Features control panel to remove MySQL
      - after uninstalling, confirm that no MySQL features remain listed in the Programs & Features control panel
   - If MySQL v5.6 is not already installed, or you are doing a clean re-install:
      - download the MySQL installer `mysql-installer-community-5.6.16.0` from `\\isis\inst$\Kits$\External\BuildServer(ndwvegas)` and install it.
      - during the MySQL installation process,
         - use the password specified on the passwords page
         - select a "server only" installation
         - change the data path to `C:\Instrument\var\mysql`
         - choose "server machine" during configuration
         - leave TCP/IP enabled
      - You may need to re-boot after installing MySQL

## Install EPICS

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use `pushd` instead of `cd`): `cd \\isis\inst$\Kits$\CompGroup\ICP\Releases\X.x.m\EPICS` where `X.x.m` is the version you wish to install.
    * If this doesn't connect use:
    * `net use Z: \\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Releases  /user:CLRC\<fed id>`
    * Z:
    * cd X.x.m\EPICS
- Run `install_to_inst.bat` This will copy the contents of the above directory to `C:\Instrument\Apps\EPICS`.
- **install** Configure the database schemas engine. 
    * Note: **BE CAREFUL.**  If you run the `config_mysql.bat` script on an existing system **YOU WILL LOSE ALL HISTORICAL DATA**.:

    ```
    cd C:\Instrument\Apps\EPICS\SystemSetup
    config_mysql
    ```


- **upgrade** reapply any hotfixes which are not included in the current release but have been made to the instrument [see notes column in instrument releases table](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)

- **install** If the machine has no LabVIEW modules directory (c:\LabVIEW Modules) containing sample environment plus DAE programs. Install that now with:

    If you are installing EPICS on a non-instrument and need to start the DAE in simulation mode, then you need to (in an epics terminal):  
	
        cd C:\Instrument\Apps\EPICS
        create_icp_binaries
		
    Register the DAE `isisicp.exe` program (either in `C:\labview modules\dae\...` or `ICP_Binaries\...`) as per developer setup instructions

		
- **install** If the instrument is not on the list of known instruments already (i.e. for switching the GUI), follow the instructions [here](Making an Instrument Available from the GUI).
- **install** To add a new EPICS instrument to the web dashboard you will need to remote desktop into NDAEXTWEB1 with your fedID credentials (you may need to request admin rights on your credentials) and do the following:
    * Add the instrument hostname to NDX_INSTS or ALL_INSTS within JSON_bourne\webserver.py
    * Add a link to the main page of the dataweb to IbexDataweb/default.html?instrument=_instname_. This can be done in the C:\inetpub\wwwroot\DataWeb\Dashboards\redirect.html
    * Restart JSON_bourne on extweb (It is running as a service).
	
## Install IBEX Client

- Stop the client if it is running

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use `pushd` instead of `cd`): `cd \\isis\inst$\Kits$\CompGroup\ICP\Releases\X.x.m\Client` where `X.x.m` is the version you wish to install.
    * If this doesn't connect use:
    * `net use Z: \\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Releases  /user:CLRC\<fed id>`
    * Z:
    * cd X.x.m\Clients

- Run the command `install_client.bat`.  This will copy the contents of the above directory to `C:\Instrument\Apps\Client`.  It will also install genie_python.

- Create a desktop shortcut to use to launch the IBEX client.

- Make changes documented in Release notes (see [Releases](https://github.com/ISISComputingGroup/IBEX/wiki#releases)). NB these are for *both* server and client and may be pertinent for a new install.

## Deployment tests

- Make sure these [client tests are performed](client-release-tests), these are items we have missed in the past.

- Make sure these [server tests are performed](server-release-tests), these are items we have missed in the past. Theses are different from the client tests.

- **install** Check that the DAE is logging EPICS block (especially if this is the first time epics has been installed). See  [DAE troubleshooting](DAE-Trouble-Shooting) "No log files are produced ..."

- **upgrade** Ensure that the screens shots you take match the updates system

## Release documentation

- Send release notes and actions that you have performed to the instrument scientist so they know what has been updated/installed. This includes any updates to common configuration/calibration files.

- Record the release to the instrument (add to list in [Instrument Releases](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)).

## Start and stop

* Start, open a command prompt and type the following:

    cd C:\Instrument\Apps\EPICS
    start_ibex_server
    
   Allow the `start_ibex_server` script a few moments to complete before starting the IBEX client.


* Stop the Instrument

	Exit from the client
    Open a command prompt and type the following:

    cd C:\Instrument\Apps\EPICS
    stop_ibex_server
    
    Allow the `stop_ibex_server` script a few moments to complete.

	
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
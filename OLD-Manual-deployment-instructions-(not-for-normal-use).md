# Steps using Manual Steps 

Note: These should not normally be used to do a "standard" deployment but may be useful if you are doing a strange deployment on a non-standard machines. These instructions may not have been kept up to date with the latest deployment script. If possible, use the instructions here instead: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Deployment-on-an-Instrument-Control-PC

## Preparatory Steps for Client and Server

- Inform the instrument scientist that you are going to upgrade the instrument in 5 minutes so that they are not surprised when you remote desktop to the instrument.

- **install** Check that Java is installed on the PC.  If not, download the latest JRE from the Java website (http://www.java.com/en/) and install it.  Make sure you choose the 64-bit version of Java.  See also [Upgrade Java](Upgrade-java). The version should be that based on the release notes.

- **install** If the PC is running the Windows Classic theme, switch it to a modern theme, Windows 7 Theme + Grey Background (220,220,220 in RGB); the IBEX GUI looks better when using a modern theme.  To change the theme see [Change Windows Theme](Change-Windows-Theme).

## Preparatory Steps for Server

- **upgrade** Note the current version number of the instrument (Help->About)

- **install** Check that the following hardware requirements are fulfilled:
  - The hardware has 8GB of RAM.
  - The hardware has at least 30GB of free disk space.

- **upgrade** Check that the hardware has 8GB of RAM.

- **upgrade** Take screenshots of running instrument. This ensures it is restarted as it was found and enables you easily to spot changes in config. Items to include: 
    1. blocks
    1. each perspective 
    1. current configuration each tab
    1. running IOC's available configs
    1. other configurations and components and synoptics

- **upgrade** Record any open LabVIEW VI which are running.

- **upgrade** Stop running instrument `stop_ibex_server.bat`.

- **upgrade** Backup old directories
    * Delete backups older than the last backup.
    * Create `C:\data\old\ibex_backup_YYYY_MM_DD` e.g. `ibex_backup_2016_02_22`
    * **_Move_** `EPICS`, `EPICS_utils`, `Python` and `Client` directories from `C:\instrument\apps` to backup directory
    * **_Copy_** the following directories to backup directory:
        1. `C:\instrument\settings`
        1. `C:\instrument\var\autosave`
    * Clear up database using [Database Troubleshooting Reducing database disc space](Database-Troubleshooting#Reducing-database-disc-space)
    * Back up db if db is changing: 
        1. Stop the mysql service:
             1. `mysql -u root -p --execute="SET GLOBAL innodb_fast_shutdown=0"`
             1. `mysqladmin -u root -p shutdown` (stops down service)
        1. Copy `C:\instrument\var\mysql` to backup directory
        1. Start the service "MySQL57" in services.

- **upgrade** Update the Common Calibration directory.
    1. Do a git status to find out if files have been added or changed (if they have a query why this is and take appropriate action)
    1. Git pull the latest version onto the system (if any file changes make a note so it can be sent to the instrument scientists so they know things have been changed) 

- **install** If you are using any serial devices with the system, don't forget to check that nport is installed, and configure the COM settings as standard (moxa 1 starts at COM5, moxa 2 at COM21, etc.)

- **install** Check that git is installed on the PC.  If not, download the latest version from the Git website (https://git-scm.com/download/win) and install it.

- **install** Check that the LabVIEW modules are installed in `C:\labview modules`.  If the LabVIEW modules are not installed you can proceed, but there some extra steps you need to perform (see below)

- **install** Create directories on the local hard drive as follows:
    ```
    mkdir C:\Instrument\Settings\config
    mkdir C:\scripts
    ```
- **install** Checkout Common Calibration Directory

    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-calibrations-directory)
    <br>**NOTE** If updating a mini-inst there may be a directory here which is not linked to git, the contents of the globals.txt are likely to be helpful in configuring the system under IBEX and should be noted before undertaking the checkout.

- **install** Checkout Config Directory
    [See the back-end getting started guide](First-time-installing-and-building-(Windows)#setting-up-a-configurations-directory)

- **install** Check that the version of MySQL installed corresponds to the version required for the release
   - If MySQL is already installed, locate the current data directory and make sure that any pre-existing data is backed up. (See [Installing and upgrading MySQL](Installing-and-Upgrading-MySQL))
   - If a different version of MySQL is already installed, you should upgrade to the correct version of MySQL (See [Installing and upgrading MySQL](Installing-and-Upgrading-MySQL))
   - If MySQL is not installed then install it. (See [Installing and upgrading MySQL](Installing-and-Upgrading-MySQL))

## Install EPICS

- **install**, **upgrade** and **mini-inst** From a command prompt type the following (if your command prompt doesn't support UNC paths, use `pushd` instead of `cd`): `cd \\isis\inst$\Kits$\CompGroup\ICP\Releases\X.x.m\EPICS` where `X.x.m` is the version you wish to install.
   * If this doesn't connect use:
      ```
      net use Z: \\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Releases  /user:CLRC\<fed id>
      Z:
      cd X.x.m\EPICS
      ```
- **mini-inst** take a backup of the current EPICS directory
- **install**, **upgrade** and **mini-inst** Run `install_to_inst.bat` This will copy the contents of the above directory to `C:\Instrument\Apps\EPICS`.
- **install**, **upgrade** and **mini-inst** If using the net user command delete the directory with `net use Z: /delete`
- **install** Configure the database schemas engine. 
    * Note: **BE CAREFUL.**  If you run the `config_mysql.bat` script on an existing system **YOU WILL LOSE ALL HISTORICAL DATA**.:

    ```
    cd C:\Instrument\Apps\EPICS\SystemSetup
    config_mysql
    ```
- **upgrade** mysql is upgraded using the these [instructions](Installing-and-Upgrading-MySQL#upgrade-56x-to-56x-or-57x-to-57x-where-5x-is-the-same-version)

- **upgrade** reapply any hotfixes which are not included in the current release but have been made to the instrument [see notes column in instrument releases table](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)

- **install** and **upgrade** upgrade the configuration (in case the initial ones created are out of date)
    1. check the configuration directory in git (git status) sort out any changes
    1. run in an epics terminal `python misc\upgrade\master\upgrade.py`
    1. check the changes to the configuration using git (git status) commit the changes.

- **install** If the machine has no LabVIEW modules directory (c:\LabVIEW Modules) containing sample environment plus DAE programs. Install that now with:
	
        cd C:\Instrument\Apps\EPICS
        create_icp_binaries
		
    Register the DAE as per the instructions in [the getting started guide](First-time-installing-and-building-(Windows)#configure-dae-for-simulation-mode-on-developers-computer).

		
- **install** If the instrument is not on the list of known instruments already (i.e. for switching the GUI), follow the instructions [here](Making-an-Instrument-Available-from-the-GUI).

- **install** Close the original terminal from which you installed. If you try to boot IBEX from this terminal it will not be able to find python.

## Update the web dashboard

- **install** Add the instrument hostname to NDX_INSTS or ALL_INSTS within webserver.py on the master branch of (https://github.com/ISISComputingGroup/JSON_bourne)

- **install** Remote desktop into the external web server (see password page for username and password)

- **install** Update the code at C:\JSON Bourne to be the same as that in the repository

- **install** Add a link to the main page of the dataweb to `IbexDataweb/default.html?instrument=_instname_`. This can be done in the `C:\inetpub\wwwroot\DataWeb\Dashboards\redirect.html`

- **install** Restart JSON_bourne on extweb (It is running as a service).
	
## Install IBEX Client

- Stop the client if it is running

- From a command prompt type the following (if your command prompt doesn't support UNC paths, use `pushd` instead of `cd`): `cd \\isis\inst$\Kits$\CompGroup\ICP\Releases\X.x.m\Client` where `X.x.m` is the version you wish to install.
    * If this doesn't connect use:
    * `net use Z: \\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Releases  /user:CLRC\<fed id>`
    * `Z:`
    * `cd X.x.m\Clients`

- Run the command `install_client.bat`.  This will copy the contents of the above directory to `C:\Instrument\Apps\Client`.  It will also install genie_python.

- Create a desktop shortcut to use to launch the IBEX client.

- Pin the IBEX client to the taskbar
    * Unpin any previous IBEX icon.
    * Open IBEX and wait until it has fully started
    * Pin IBEX to the taskbar (right click on the IBEX client in the taskbar -> Pin to taskbar)
    * Check that you can't open multiple clients by clicking on the taskbar icon again once IBEX is open
    * Check that if you open multiple client instances by right-clicking on the taskbar icon and selecting "ibex-client", then the icons for each instance of the client stack on top of each other.

- Make changes documented in Release notes (see [Releases](https://github.com/ISISComputingGroup/IBEX/wiki#releases)). NB these are for *both* server and client and may be pertinent for a new install.

## Install Wiring Tables

- *Migrating an instrument:* 
   * Move (as distinct from copy) wiring tables from `C:\Instrument\Tables` and `C:\labview modules\dae` to `C:\Instrument\Settings\config\NDXxxxxx\configurations\tables`
   * If the scientist wishes to continue to use SECI for a period, inform the scientist that wiring tables have moved.  SECI can browse to the new location.

- *New instrument:* Install the wiring tables in  `C:\Instrument\Settings\config\NDXxxxxx\configurations\tables`

## Post-release actions
- Run the script in `C:\Instrument\Apps\EPICS\misc\upgrade\master\install_scripts\instrument_upgrade.bat`. Follow any prompts which are given.

## Deployment tests

- Check that [Java Auto Update](https://www.java.com/en/download/help/java_update.xml#sched) is disabled (i.e. make sure the "Check for Updates Automatically" checkbox is unchecked).

- **upgrade** Restart any VIs which were running

- Make sure these [client tests are performed](client-release-tests), these are items we have missed in the past.

- Make sure these [server tests are performed](server-release-tests), these are items we have missed in the past. These are different from the client tests.

- **install** Check that the DAE is logging EPICS block (especially if this is the first time epics has been installed). See  [DAE troubleshooting](DAE-Trouble-Shooting) "No log files are produced ..."

- **upgrade** Ensure that the screens shots you take match the updates system

## Release documentation

- Send release notes and actions that you have performed to the instrument scientist so they know what has been updated/installed. This includes any updates to common configuration/calibration files.

- Record the release of the instrument (add to list in [Instrument Releases](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information)).

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

**(install)** 

The details of the individual setpoints for any given device will depend on that device and how it is used on an instrument, but the general principles described here will apply.

### Background
Most devices on ISIS instruments are moved using motors controlled by Galil motion controllers, therefore, configuring motion set points is largely a matter of configuring the Galils correctly.

Key directories on the control server on the control server include

* ``C:\Instrument\Settings\config\NDXxxxxx\configurations\galil``, which includes 
    * ``README_galil_cmd.txt``, a documentation file describing how to configure a Galil controller
    * ``galil01.cmd - galil<N>.cmd``, where `<N>` is the total number of Galil controllers on the instrument
    * ``axes.cmd``, which relates the Sample Stack axes to Galil ports
    * ``jaws.cmd``, which relates the axes of jaw sets to Galil ports
    * ``motionsetpoints.cmd``, which relates the axes of movable devices to Galil ports and to lookup tables (which define the set positions for the devices)
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

## Adding Nagios checks

nagios is the instrument monitoring system, this will not affect operation but adding the instrument to Nagios will generate notifications of issues. This requires editing configuration files on the "varanus" server, but the procedure is probably going to be simplified when it moves to a new system. For the moment contact Freddie    


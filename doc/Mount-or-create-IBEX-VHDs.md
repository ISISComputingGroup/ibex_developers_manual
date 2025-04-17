> [Wiki](Home) > [Deployment](Deployment) > [Mount or create IBEX VHDs](Mount-or-create-IBEX-VHDs)

# Deployment

The new architecture for deployment is to deploy onto VHDs which will be copied to the desired places and linked in; this was a result of [discussions of making deployment quicker](Plan-how-to-deploy-automatically-on-30-instruments).

## Part of the system
### System VHD

There needs to be a system VHD, this has been created by Chris and will be detailed *CHRIS TODO*. This contains windows and user level programs (probably including labview).

### App VHD

IBEX applications need to be placed on a disk and these should be generic for all instruments. In practice hot fixes will make them different, we record hotfixes and these are reapplied on upgrade of needed. 

### Configuration Settings VHD

IBEX settings are placed on a setting VHD, these will be created once when the instrument is converted to use VHDs and after that this will be persisted through IBEX and Windows upgrades. On Upgrade, the configuration will need to be upgraded and the common calibration files need to be updated.

### Var VHD

These contain part of the system which change often. We are undecided what to do on upgrade:

- *Either:* Create the VHD when migrated and on upgrade truncate the database, move old log files and old autosave files. Then upgrade the database.
- *Or:* Every upgrade use a new common VHD copy across autosave files (maybe these should live in settings), dump the data schema for interesting tables and reimport it.

For the test system I have gone with the first approach because it was easy. I like the second approach better.

# VHD Creation

## Create empty VHDs

1. Copy the three empty vhdx files (`empty_apps.vhdx`, `empty_var.vhdx`,`empty_settings.vhdx`) to a local disk (from CompGroup\chris) and rename to
`apps.vhdx`, `var.vhdx` and `settings.vhdx`.
2. These are pre-configured to be 30GB each.

## Mount a VHD

1. Open a command prompt as administrator
1. `diskmgmt.msc`
1. Click Action -> Attach VHD
    - I had to click help first
1. Select location of VHD
  1. Mount `Apps.vhdx` to `C:\Instrument\Apps` by creating a directory junction from `c:\instrument\apps` to the drive letter of the VHD you mounted
  1. Mount `Settings.vhdx` to `C:\Instrument\Settings\config` as above
  1. Mount `Var.vhdx` to `C:\Instrument\var` as above

## Dismounting VHD

1. Close the VHD and copy back
    1. Right click on drive on left at the bottom
    1. Detach VHD
    1. Copy file back to the source

# VHD Creation Jenkins Job
## 

There is an [automated job in jenkins](http://epics-jenkins.isis.rl.ac.uk/job/Create_VHD/) which builds VHDs from the latest IBEX server/client/python versions.

### Build server setup

To set up a computer to be able to run the [automated VHD creation script](https://github.com/ISISComputingGroup/ibex_utils/tree/master/installation_and_upgrade):
- Hyper-V must be enabled on the computer which will be running the script. It can be turned on by searching for "turn windows features on or off" from the start menu and then selecting the entire Hyper-V tree. If hyper-v wasn't already turned on this will require a restart. If you are on Windows 2012, enable it from the Server Manager (by the start button on the desktop) then select Manage -> Add Roles and Features and check the entire Hyper-V tree.
- Powershell must be upgraded to at least version 5 to support the commands we are using.
- Set up an environment variable called `MYSQL_PASSWORD` containing the MySQL root user password.
- In the admin documents area, create an (empty) folder at `C:\Users\Administrator\Documents\fake_release_dir\1.0.0`
- A local python must be installed in `C:\Users\Administrator\Documents`. Note: we do not use the python from the network share here as we are running as Admin.
- The machine you're installing this on must be listed in genie_logger.py in the vhd_builder list to avoid writing logs to `C:\Instrument\Var\logs` before Var is mounted

These items cannot be automated by jenkins as they need to be the admin user.

### Mounting and dismounting VHDs automatically

Because VHD mounting and dismounting requires admin rights, this is done by a scheduled task running as the admin user. The code run by these scheduled tasks is checked out to `C:\Users\Administrator\Documents\ibex_utils\installation_and_upgrade`, and the bat file which is run is `vhd_scheduled_task.bat`.

The scheduled tasks run every minute and look for a file which is created by the install script. If this file exists, the tasks will mount/dismount the vhds and then delete the file. Otherwise the tasks do nothing.

### Build artefacts

Empty VHDs are currently taken from:
```
\\isis\inst$\Kits$\CompGroup\Chris
```

Once filled with IBEX files, the VHDs are copied to:
```
\\isis\inst$\Kits$\CompGroup\ICP\VHDS
```

# Upgrade IBEX Version on a VM By Copying VHD

 - The VM set up, running an older version of IBEX, has been located within Hyper-V manager.
 - If you wish, a 'Checkpoint' (Right Click -> Checkpoint) can be capture of the current system to allow a way to restore the VM to a functioning state, if required.
 - Ensure that the VM is switched OFF (Right Click -> Turn Off...).
 - Once the State has changed to 'Off', Right Click the VM and select 'Settings...'.
 - Under Hardware -> SCSI Controller, Select the Hard Drive for '/apps'.
 - Select 'Browse...' and locate the '/apps' drive containing the latest IBEX build.
 - Select 'Open', and double check this is the correct drive.
 - Select 'Apply' and then 'OK'.
 - To test that the IBEX has been updated, double click the VM or right click and press 'Start'.
 - Once the IBEX server has been start, you can check the version within 'Help' -> 'About' on the toolbar within the IBEX GUI.


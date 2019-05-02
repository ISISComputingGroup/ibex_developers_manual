> [Wiki](Home) > [Deployment](Deployment) > [Create IBEX VHDs](Create-IBEX-VHDs)

# Deployment

The new archicheture for deployment is to deploy onto VHDs which will be copied to the desired places and linked in; this was a result of [discussions of making deployment quicker](Plan-how-to-deploy-automatically-on-30-instruments).

## Part of the system
### System VHD

There needs to be a system VHD, this has been created by Chris and will be detailed *CHRIS TODO*. This contains windows and user level programs (probably including labview).

### App VHD

IBEX applications needs to be placed on a disk these should be generic for all instruments. In practice hot fixes will make them different, we record hotfixes and these are reapplied on upgrade of needed. 

### Configuration Settings VHD

IBEX settings are placed on a setting VHD, these will be created once when the instrument is converted to use VHDs and after that this will be persited through IBEX and Windows upgrades. On Upgrade the configuration will need to be upgrades and the common calibration files need to be updated.

### Var VHD

These contain part of the system which change often. We are undecided what to do on upgrade:

- *Either:* Create the VHD when migrated and on upgrade truncate the database, move old log files and old autosave files. Then upgrade the database.
- *Or:* Every upgrade use a new common VHD copy across autosave files (maybe these should live in settings), dump the data schema for intersting tables and reimport it.

For the test system I have gone with the first approach because it was easy. I like the second approach better.

### Cross disks

There are some things which are cross disks, e.g. the database is a service but is stored on the apps. Do these instructions live in an upgrade script? How do we unmount and mount the disks during upgrade? The upgrade process needs thinking about.

# VHD Creation

## Create empty VHD

- TODO Chris

## Mount a VHD

1. Open `cmd` in `O3` mode
1. `diskmgmt.msc`
1. Click Action -> Attach VHD
    - I had to click help first
1. Select location of VHD

## Dismounting VHD

1. Close the VHD and copy back
    1. Right click on drive on left at the bottom
    1. Detach VHD
    1. Copy file back to the source

## VHD Contents

### IBEX Apps to VHD

1. Mount the VHD (see [above](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Create-IBEX-VHDs/_edit#mount-a-vhd))
1. Open the mapped drive and copy the following:
    1. Copy EPICS
    1. Copy Client
    1. Copy EPICS UTILS
    1. Copy Python
    1. Copy ICP Binaries into EPICS
    1. Copy MySql

### IBEX Settings VHD

Either:
1. Copy current settings to VHD

Or:
1. Follow instructions to create config and common config from the developer's setup

### IBEX Var VHD

Either:
1. Copy current var to VHD

Or:
1. Follow instructions to create a blank database and copy that to the disk
1. Add other directories meant to be in var from the developer's setup e.g. log, autosave

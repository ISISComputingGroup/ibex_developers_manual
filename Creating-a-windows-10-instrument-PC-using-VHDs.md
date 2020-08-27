Note: these instructions are only partially complete as https://github.com/ISISComputingGroup/IBEX/issues/5489 was de-prioritized. There are still likely to be issues with this process at this time.

# Creating the initial system

To begin assembling a system, you need to build a new clone. The process to build a new clone uses the microsoft deployment toolkit. It is easiest to build the clone "in-place" on the NDH which it will eventually run on - it is a bad idea to attempt to build the clone on one machine and later transfer it.

The configuration files for MDT are not currently available as they are stored on a special server; these should be made available generally as it currently means we are unable to build a new machine easily.

The current build process creates a windows 10 image which should have the operating system + required software other than ibex installed (e.g. labview, nport, 7-zip). It also creates empty folders for Apps, Settings and Var - these are **unused placeholders** for where the VHDs are mounted, so **they need to be deleted as they will be replaced by the IBEX VHDs**. 

# Adding IBEX VHDs to the system

- Remote desktop into the NDH host computer and launch Hyper-V manager.
- In Hyper-V manager, right click the machine and ensure it is shut down.
- Copy a recent set of IBEX VHDS (Apps, Settings, Var) from `inst$\kits$\compgroup\icp\VHDs` onto the NDH host machine.
- In Hyper-V manager, add the VHDs as disks for the virtual machine. You do not need to specify a mount point, just make the disks available.
- Power on the NDX virtual machine by right clicking on it in Hyper-V manager and selecting "power on".
- Inside the NDX machine, on the desktop there will be a script called `makeinst.ps1`. Run this script in an admin powershell prompt.
  * This script looks for volumes with the right label and mounts them into `C:\volumes`, and then creates directory junctions from `c:\instrument\apps` to `c:\volumes\Apps`.
  * If the script fails due to directories being more/less nested than it expects, ensure you have the latest version of the `makeinst.ps1` script.
- You should now have an ibex installation on the NDX virtual machine

Note that the IBEX VHDs are never mounted with a drive letter (unlike on the jenkins build server). They can only be reached via `c:\volumes` and directory junctions which point there.

# Setting up IBEX before first use

- Start the MYSQL server by adding it as a service (as per install script)
- Change the settings folder name from `NDHSPARE70` (which is the build server) to the machine you are building
- Inside the settings folder, do a git checkout to the correct config branch and pull
- See also any manual steps listed at https://github.com/ISISComputingGroup/IBEX/issues/5437

# Starting IBEX

- At this stage you should be able to start IBEX. Make sure you start it as a standard user, not admin, otherwise all of the log files and directories will be created with the wrong permissions.
  * It seems that the Var and Settings VHDs in particular are very sensitive to getting into a state where the files are "owned" by admin but admin can't delete them, and a reboot does not fix this. To fix this, install fresh settings/var vhds by following the "upgrade/change vhd" instructions below.

# Upgrading/changing IBEX VHDs

If you need to upgrade/change IBEX VHDS, the process is as follows:
- Power off the NDX machine
- Go into hyper-V and remove the three IBEX VHDS from the VM (Apps, Settings, Var)
- Replace the VHDS on the filesystem on the NDH with the new versions you wish to install
- Add these back in to the VM via Hyper-V manager
- Boot the VM
- Re-run the `makeinst.ps1` script in an admin powershell prompt
- Ensure that the filesystem looks sensible e.g. that `Apps/` contains EPICS and a client, `Settings` contains a settings directory, and `Var/` contains the expected file structure.

Note: you can not simply replace the VHDs on the NDH by name. This is because Hyper-V sets some attributes on the VHDs when they are explicitly added; if these attributes are not set, you will get an error on attempting to boot the VM.


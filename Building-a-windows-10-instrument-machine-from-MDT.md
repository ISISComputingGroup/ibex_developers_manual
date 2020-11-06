# Building a new instrument virtual machine from MDT

Note: this page documents the process of building a windows 10 **system**. This page does not focus on deploying IBEX itself, and if you are converting an instrument from SECI to IBEX you will generally not need to perform this process as a suitable NDX machine will already exist.

### Find a suitable physical host

- Find a suitable physical host server. The server will need a minimum of 14GB of memory and 256GB of hard disk space free
  * If you are building a real instrument machine, this will usually be `NDHINST`, and the virtual machine that you're building will usually be `NDXINST`

### Copy needed files onto physical host

- Copy the set of IBEX VHDs you wish to install from the share onto the `NDH` host computer, ensuring that you are copying onto a disk with a suitable amount of free space.
- In Hyper-V manager, add the VHDs as disks for the virtual machine. You do not need to specify a mount point, just make the disks available.
  * Note: if you are replacing existing disks, you **still need to delete and re-add them in Hyper-V for them to be recognised!**
- Find the latest windows 10 ISO file from `\\isis\inst$\mdt$\dev1\MDTDeploymentShare\Boot\LiteTouchPE_x64_Hyper-V.iso` and copy this ISO onto the `NDH` machine
  * *Note: This ISO is not really a windows PE iso, it is instead an ISO which has been built by MDT. You cannot just use a version downloaded from microsoft.com*

### Configure the VM

- Go into hyper-v manager on the MDT server host and select new machine. Default settings are mostly ok other than:
  * Set the name to the intended hostname of the NDXMDTSERVPROD machine
  * Make sure VM files are stored on a disk with adequate space (often `D:\` or `E:\` on NDH machines)
  * Set startup memory to 14GB.
  * Set it to connect to ISIS network if you get the option, otherwise it will be ok on the default.
  * Set virtual hard disk size to 128GB
  * Install OS later
- Add the VHDs that you copied over earlier as "SCSI" disks in hyper-v manager
  * Note you do not need to map them anywhere at this stage, they merely need to be attached to the VM
- Tell Hyper-V to boot from the windows PE ISO you copied earlier by adding it as the "DVD" drive in hyper-v
- Boot the machine
- Select "Build thick updated windows 10 image"
- Computer name - set it to `NDXINST` (same as name in Hyper-V)
- Join the default ISIS workgroup (found on passwords page if you are unsure)
- Don't restore settings or data
- When asked for admin password, refer to passwords page and add the new password there if necessary.

### Setting up IBEX before first use

- Run the script `c:\makeinst.cmd`. This should create `Apps`, `Settings` and `Var` folders with the contents of the VHDs you mounted
  * Check that this step has worked before proceeding! The `makeinst.cmd` script is flaky and may appear to have worked while actually leaving the system in an invalid state.
- Start the MYSQL server by adding it as a service. MDT will have cloned `ibex_utils` into `C:\instrument`, from there run `windows_10_vhd_deploy.bat`
- Change the settings folder name from `NDHSPARE70` (which is the build server) to the machine you are building
- Inside the settings folder, do a git checkout to the correct config branch and pull
- See also any manual steps listed at https://github.com/ISISComputingGroup/IBEX/issues/5437

### Starting IBEX

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
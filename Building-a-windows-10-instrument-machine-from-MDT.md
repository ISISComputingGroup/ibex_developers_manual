# Building a new instrument virtual machine from MDT

Note: this page documents the process of booting and building a windows 10 **system** in an empty virtual machine. This page does not focus on deploying IBEX itself, and if you are converting an instrument from SECI to IBEX you will generally not need to perform this process as a suitable NDX machine will already exist.

### Find a suitable physical host

- Find a suitable physical host server. The server will need a minimum of 14GB of memory and 256GB of hard disk space free. You can use hyperv on your own Windows 10 desktop if your machine is powerful enough.
  * If you are building a real instrument machine, this will usually be `NDHINST`, and the virtual machine that you're building will usually be `NDXINST`

### Copy needed files onto physical host

Think of a virtual machine name <VMname> to use later - this name will need to be unique on the network.

Make a copy of a boot ISO from `\\isis\inst$\Kits$\CompGroup\ICP\W10Clone\Boot` on your local computer. You may see several ISOs in here, see the `README.txt` and choose the appropriate one. This iso does an initial boot and the loads the rest off a network share embedded within it, thus the iso itself doesn't need to change often, it is just poining you to the appropriate location to install from.   

Next make a local copy of the VHD disks from `\\isis\inst$\Kits$\CompGroup\ICP\W10Clone\VHDS` - choose either an appropriate IBEX release or latest Jenkins build. Youy will need to copy the `apps`, `var` and `settings` VHDS. If you plan to have several local VMs, you may wish to rename these to `<VMname>-settings.vhdx` etc. Make a copy of the `var` disk name rename it to `scratch.vhdx` or `<VMname>-scratch.vhdx` as appropriate.

Now we create <VMname>. Don't use hyperv quick create, start hyperv manager as your admin account.
in hyperv settings (right click on your computer name in hyperv) - adjust hyperv paths for where to create machines and disks if you want a non-default location. Make sure disk path is somewhere with lots of space.
in virtual switch manager - there will probably be a default switch there connected to "internal network". You need to create a new virtual switch of type "external" and attach it to the correct ISIS network adapter. If you have several network interfaces, you may need to look at you system network setting to get the right adapter name.

Now select new -> virtual machine. Create a generation 2 VM, 12GB mem = 12288mb is ample, less may be fine. Select use dynamic memory. 
chose "external network" switch for the VM, create a new virtual hard disk (the default), choose install os from iso for booting, select above iso file saved above

right click on VM, in firmware/bios settings of VM, put hard disk/network/dvd as boot order, this helps on booting, initially giving you some time (while it is failking to netrok boot) to get ready to press key to boot from dvd. After initial dvd boot you don't want to boot from iso again. 
 
increase number of processors say to 4
add scsi hard drives and attach vhds, add scratch first and then add rest in any order. 
go to checkpoints of VM and disable automatic checkpoints
now create a checkpoint before you start - this lets you revert back (apply) and re-run a boot without having to recreate the VM
start vm and connect to screen of vm

After iso boot it will go into MDT install, choose reclone full system (thick w10) as install type
change computer name to your unique VM name from above











- Copy the set of IBEX VHDs you wish to install from the share onto the `NDH` host computer, ensuring that you are copying onto a disk with a suitable amount of free space.
  - These should be `apps.vhdx`, `var.vhdx`, `settings.vhdx` and `scratch.vhdx`. You **MUST** mount `scratch.vhdx` as the first SCSI drive in the VM as it gets formatted and partitioned during the MDT task sequence (into `Data` and `Scratch`). `scratch.vhdx` is actually a blank VHDX so an empty one called something different will work as well (or a copy of one of the others)
  * Note: ensure the VHDs are not corrupt first by mounting them on your local machine - if they fail to mount, they may be corrupt and you should select a different set of VHDs. After mounting each VHD should contain some files, e.g. the Apps VHD should contain an EPICS installation and a client.
- Find the latest windows 10 ISO file from `<mdt PRODUCTION deployment share location>\Boot\LiteTouchPE_x64.iso` and copy this ISO onto the Hyper-V host (`NDH`) machine
  * *Note: This ISO is not really a windows PE iso, it is instead an ISO which has been built by MDT. You cannot just use a version downloaded from microsoft.com*
  * The MDT deployment share location and credentials can be found on the passwords page if you are unsure

### Configure the VM

- Go into hyper-v manager on the MDT server host and select new machine. Default settings are mostly ok other than:
  * Set the name to the intended hostname of the NDX machine
  * Make sure VM files are stored on a disk with adequate space (often `D:\` or `E:\` on NDH machines)
  * Set startup memory to 14GB (in hyper-v set to NUMA architecture limit which is usually just below 14gb).
  * Set it to connect to ISIS network if you get the option, otherwise it will be ok on the default.
  * Set virtual hard disk size to 128GB
  * Install OS later
- In Hyper-V manager, add the VHDs as disks for the virtual machine. You do not need to specify a mount point, just make the disks available.
  * Note: if you are replacing existing disks, you **still need to eject and re-add them in Hyper-V on the NDH for them to be recognized!**
  * Note: This may cause bluescreening and it may be better to do the install first and then manually mounting the VHDs afterwards before running `make_inst.cmd` and so on. 
- Tell Hyper-V to boot from the windows PE ISO you copied earlier by adding it as the "DVD" drive in hyper-v
- Boot the virtual machine from hyper-v
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
- Shutdown the NDX machine (gracefully)
- Go into hyper-V and remove the three IBEX VHDS from the VM (Apps, Settings, Var)
- Replace the VHDS on the filesystem on the NDH with the new versions you wish to install
- Add these back in to the VM via Hyper-V manager
- Boot the VM
- Ensure that the filesystem looks sensible e.g. that `Apps/` contains EPICS and a client, `Settings` contains a settings directory, and `Var/` contains the expected file structure.

Note: you can not simply replace the VHDs on the NDH by name. This is because Hyper-V sets some attributes on the VHDs when they are explicitly added; if these attributes are not set, you will get an error on attempting to boot the VM.
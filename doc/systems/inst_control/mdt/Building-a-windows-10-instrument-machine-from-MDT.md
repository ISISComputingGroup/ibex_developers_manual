# Building a new instrument virtual machine from MDT

Note: this page documents the process of booting and building a windows 10 **system** in an empty virtual machine. This page does not focus on deploying IBEX itself.
 - if you do not see hyper-v on your windows desktop, you just need to enable it via `turn windows feature on or off` , Select `Hyper-V` and sub items.

**Note**: boot and build can take a while, 3 hours on an NDH with SSDs, longer of you have spinning disks.

### Find a suitable physical host

- Find a suitable physical host server. The server will need a minimum of 14GB of memory and 256GB of hard disk space free. You can use hyper-v on your own Windows 10 desktop if your machine is powerful enough.
  * If you are building a real instrument machine, the hyper-v host will usually be `NDHINST`, and the virtual machine <VMname> that you're building will usually be `NDXINST`

### Copy needed files onto physical host

Choose a virtual machine name <VMname> to use later - this name will need to be unique on the network (for an instrument this is the NDX name). For developing, choose a name with an `NDXTEST` prefix followed by a number. Choose a free number and record your choice in the spreadsheet called `w10_test_machines.xslx` in the General channel of Teams.  

- Make a copy of a boot ISO from `<Kits>\CompGroup\ICP\W10Clone\Boot` on your local computer. You may see several ISOs in here, see the `README.txt` and choose the appropriate one. This iso does an initial boot and the loads the rest off a network share name embedded within it, thus the iso itself doesn't need to change often, it is just pointing to the appropriate location to install from.   
  * *Note: This ISO is not really a windows PE iso, it is instead an ISO which has been built by MDT. You cannot just use a version downloaded from `microsoft.com`*
- Next make a local copy of the VHD disks from `<Kits>\CompGroup\ICP\W10Clone\VHDS` - choose either an appropriate IBEX release or latest Jenkins build. You will need to copy the `apps`, `var` and `settings` VHDS. If you plan to have several local VMs, you may wish to rename these to `<VMname>-settings.vhdx` etc. Make a copy of the `var` disk name rename it to `scratch.vhdx` or `<VMname>-scratch.vhdx` as appropriate. Make sure you are copying them to a disk with enough free space. 
  * Note: you can check the VHDs are not corrupt by mounting them on your local machine (right click on file) if they fail to mount, they may be corrupt and you should select a different set of VHDs. After mounting each VHD should contain some files, e.g. the Apps VHD should contain an EPICS installation and a client.

### Configure the VM <VMname>

- Don't use hyper-v quick create, start hyper-v manager as your admin account.
- in hyper-v settings (right click on your computer name in hyper-v) - adjust hyper-v paths for where to create machines and disks if you want a non-default location. Make sure disk path is somewhere with lots of space.
- in virtual switch manager: there will probably be a default switch there connected to "internal network". You need to create a new virtual switch of type "external" and attach it to the correct ISIS network adapter. If you have several network interfaces, you may need to look at you system network setting to get the right adapter name.

- Now select new -> virtual machine. Create a generation 2 VM, 12GB memory = 12288mb is ample, less may be fine. Select use dynamic memory. 
chose "external network" switch for the VM, create a new virtual hard disk (the default, 128GB), choose install os from iso for booting, select above iso file saved above
  - (note: in hyper-v set to NUMA architecture limit which is usually just below 14gb).

right click on VM
- in firmware/bios settings of VM, put hard disk/network/dvd as boot order, this helps on booting, initially giving you some time (while it is failing to network boot) to get ready to press key to boot from dvd. After initial dvd boot you don't want to boot from dvd iso again. 
- increase number of processors say to 4
- add scsi hard drives and attach vhds, add scratch first and then add rest in any order. You do not need to specify a mount point, just make the disks available.
  - These should be `apps.vhdx`, `var.vhdx`, `settings.vhdx` and `scratch.vhdx`. You **MUST** mount `scratch.vhdx` as the first SCSI drive in the VM as it gets formatted and partitioned during the MDT task sequence (into `Data` and `Scratch`). `scratch.vhdx` is actually a blank VHDX so an empty one called something different will work as well (or a copy of one of the others)
  * Note: if you are replacing existing disks, you **still need to eject and re-add them in Hyper-V for them to be recognized!**

go to checkpoints of VM and disable automatic checkpoints, but create a checkpoint before you start - this lets you revert back (apply) and re-run a boot without having to recreate the VM

start vm and connect to screen of vm
 - If it blue screens try the boot again. I've seen this occasionally on windows 10 hyper v, not on the windows server hyper-v. 

After iso boot it will go into MDT install
- choose reclone full system (thick w10 image) as install type
- change computer name to your unique <VMname> from above, other defaults should be fine (join ISISWG, Don't restore settings or data)
- When asked for admin password, refer to passwords page and add the new password there if necessary for NDX. If this is your own desktop, change it to whatever you like - this is just the password for the `Administrator` account after boot. 
- now leave it installing, it will reboot several times and may look like it is doing nothing at times. Wait until you see the final dialogue box displayed on the screen that says the `installation has completed with 0 warnings and 0 errors` 

### Setting up IBEX before first use

- Check settings folder name - it should have been renamed during install to correct <VMname>
- (NDX instrument) Inside the settings folder, do a git checkout to the correct config branch and pull

### Starting IBEX

- At this stage you should be able to start IBEX. Make sure you start it as our **standard user**, not `Administrator` that you are probably still logged in as, otherwise all of the log files and directories will be created with the wrong permissions. It is probably easiest if you now remote desktop into your new VM rather than use the hyper-v console
  * It seems that the Var and Settings VHDs in particular are very sensitive to getting into a state where the files are "owned" by admin but admin can't delete them, and a reboot does not fix this. To fix this, install fresh settings/var vhds by following the "upgrade/change vhd" instructions below.
- Start ibex client, initially you will have no configuration loaded so not everything will start. Go to `configuration -> edit current configuration -> save as` and save it as something like `test` and switch to this configuration. This should now start DAE processes and you should end up in `SETUP` rather than `UNKNOWN` runstate after everything restarts. This seems to take a while for some reason, be patient.
- to be able to start a run with `Begin` you need to set some DAE parameters:
  * in `experiment setup -> time channels` set first row of time regime 1 to be   10, 10000, 100, dT=C
  * in `data acquisition` select the dropdown next to wiring, detector and spectra tables - choose the only option offered that is an `ibextest` table
  * now apply changes
 
## Upgrading/changing IBEX VHDs

If you need to upgrade/change IBEX VHDS, the process is as follows:
- Shutdown the NDX machine (gracefully)
- Go into hyper-V and remove the three IBEX VHDS from the VM (Apps, Settings, Var)
- Replace the VHDS on the filesystem on the NDH with the new versions you wish to install
- Add these back in to the VM via Hyper-V manager
- Boot the VM
- Ensure that the filesystem looks sensible e.g. that `Apps/` contains EPICS and a client, `Settings` contains a settings directory, and `Var/` contains the expected file structure.

Note: you can not simply replace the VHDs on the NDH by name. This is because Hyper-V sets some attributes on the VHDs when they are explicitly added; if these attributes are not set, you will get an error on attempting to boot the VM.
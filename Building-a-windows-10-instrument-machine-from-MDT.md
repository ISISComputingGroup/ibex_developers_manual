# Building a new instrument virtual machine from MDT

Note: this page documents the process of building a windows 10 **system**. This page does not focus on deploying IBEX itself, and if you are converting an instrument from SECI to IBEX you will generally not need to perform this process as a suitable NDX machine will already exist.

### Find a suitable physical host

- Find a suitable physical host server. The server will need a minimum of 14GB of memory and 256GB of hard disk space free
  * If you are building a real instrument machine, this will usually be `NDHINST`, and the virtual machine that you're building will usually be `NDXINST`

### Copy VHDs onto physical host

- Copy the set of IBEX VHDs you wish to install from the share onto the `NDH` host computer.

### Configure the VM

- Go into hyper-v manager on the MDT server host and select new machine. Default settings are mostly ok other than:
  * Set the name to the intended hostname of the NDXMDTSERVPROD machine
  * Make sure VM files are stored on a disk with adequate space (often `D:\` or `E:\` on NDH machines)
  * Set startup memory to 14GB.
  * Set it to connect to ISIS network if you get the option, otherwise it will be ok on the default.
  * Set virtual hard disk size to 128GB
  * Install OS later
- Find the latest windows 10 ISO file from `\\isis\inst$\mdt$\dev1\MDTDeploymentShare\Boot\LiteTouchPE_x64_Hyper-V.iso` and copy this ISO onto the `NDH` machine
  * *Note: This ISO is not really a windows PE iso, it is instead an ISO which has been built by MDT. You cannot just use a version downloaded from microsoft.com*
- Add the VHDs that you copied over earlier as "SCSI" disks in hyper-v manager
  * Note you do not need to map them anywhere at this stage, they merely need to be attached to the VM
- Tell Hyper-V to boot from this ISO
- Boot the machine
- Select "Build thick updated windows 10 image"
- Computer name - set it to `NDXINST` (same as name in Hyper-V)
- Join the default ISIS workgroup (found on passwords page if you are unsure)
- Don't restore settings or data
- When asked for admin password, refer to passwords page and add the new password there if necessary.
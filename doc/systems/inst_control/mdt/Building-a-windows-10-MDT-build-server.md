# Building an MDT build server

This wiki page documents the process for setting up a new MDT (microsoft deployment toolkit) build server to create new windows 10 clones.

The central source of truth for MDT configuration files is the MDT deployment share location, which can be found on the usual passwords page.

## Mental model

- `NDXINST` - this is the windows 10 virtual machine to be built. This is a usual NDX in the sense that it runs IBEX.
- `NDHINST` - this is the physical host on which the NDX virtual machine executes
- `NDXMDTSERVPROD` - This is an MDT server which contains instructions which the NDX can execute to install standard operating systems and/or software. This server can be either real or virtual as convenient. It never hosts a VM itself - it only contains the configuration files and setup for MDT. A new machine will need to be called something different (e.g. `NDXMDTSERVDEV`)

This wiki page describes the process for setting up a new `NDXMDTSERVPROD` machine (NOT an `NDHINST` or `NDXINST` machine).

## How to build a new MDT server

- If you are creating `NDXMDTSERVPROD` as a virtual machine, you need to find a physical host for the MDT server.
  * Ideally use same specifications as for an instrument machine (14GB memory, 256GB free disk space) 
  * If memory or disk space are tight, an MDT server can probably get by with ~6GB of memory and ~100GB of free disk space.
  * __NB: if you are considering using your local machine as a host while working from home the VPN can cause issues where NDHBUILD cannot be found. We haven't found an easy fix for this so it's probably best to use an on-site host machine.__
- If you are creating `NDXMDTSERVPROD` as a virtual machine, go into hyper-v manager on the MDT server host and select new machine. Default settings are mostly ok other than:
  * Set the name to the intended hostname of the `NDXMDTSERVPROD` machine
  * You'll need to create it on a disk which has enough space (will need ~256GB free)
  * Set startup memory to 14GB (or less - see above)
  * Set it to connect to ISIS network if you get the option, otherwise it will be ok on the default.
  * Set virtual hard disk size to 128GB (or a bit less - see above)
  * Install OS later
- Copy the windows 10 ISO file from `\\isis\inst$\mdt$\dev1\MDTDeploymentShare\Boot\LiteTouchPE_x64_Hyper-V.iso` and copy in onto the host server for `NDXMDTSERVPROD`.
  * This ISO is not really a windows PE iso, it is instead an ISO which has been built in the past by a different MDT server machine, and this will have configured the menus which are available when booting this ISO. This is **not** substitutable for e.g. a version downloaded from microsoft.com
- Tell Hyper-V to boot from this ISO by adding it as a disk in the virtual disk drive (right click on the machine in hyper-v and select "settings")
- You might choose to increase number of processors available to the VM
- Boot the machine
- This will boot into a "Microsoft Deployment Wizard", which will then launch a set of menus embedded within the ISO.
- Select "Build thick updated windows 10 image"
  * Thin image == Just windows 10
  * Thick image == windows 10 + software such as labview, nport, notepad++, 7-zip, IBEX (if you have access to the existing MDT build server you may wish to disable the IBEX installation as it won't be required for this machine)
- Computer name - set it to the hostname (same as name in Hyper-V)
- Join the default ISIS workgroup (the name of this workgroup can be found on the passwords page)
- Don't restore settings or data
- When asked for an administrator password generate a secure random password following STFC password guidance, and then add this to the usual passwords page alongside hostname.
- Don't capture any image
- Set it off, it will now take ~1 hour and will install everything unattended
- After it has finished installing, it is wise to take a hyper-v snapshot so that you can roll back to this point if needed
- Create a new account to use and remove unneeded accounts (e.g. the default ones created for instrument machines). You can use `lusrmgr.msc` to access these settings quickly, or click through from the control panel.
  * Add the account as `mdtbuilder`, set a password conforming to STFC password policy and add it to the usual passwords page
  * Add the ability to remote desktop as this account by adding it to group `Remote Desktop Users`
  * Add `mdtbuilder` to `Administrators` group (this is important for later)
- Now log out of the admin account and log back in as `mdtbuilder`
- Copy the following files from `\\isis.cclrc.ac.uk\inst$\kits$\CompGroup\ICP\MDT` into `NDXMDTSERVPROD`(if it asks for credentials use your fed id, **do not save these to the machine**):
  * `adksetup.exe` - a utility for measuring performance of machines ("assessment and deployment toolkit")
  * `MicrosoftDeploymentToolkit_x64.exe` - this is MDT itself
  * `adkwinpsetup.exe` - this may not be necessary?
- Run `adksetup.exe`
- When asked which features to install remove "windows performance toolkit", "user experience virtualisation", "microsoft application virtualisation", "Media experience analyzer"
- Run `adkwinpsetup.exe`, accept defaults
- Run `MicrosoftDeploymentToolkit_x64.exe`
- Open an **administrator** command prompt and type `net use <deployment share location> /USER:<account on passwords page`
- Go to start -> MDT -> Deployment workbench and **run it as admin**
- Right click "deployment shares" -> "open" -> MDT deployment share location (found on passwords page) -> next -> finish
  * If MDT complains that the directory does not exist, check you did the `net use` above correctly.
- Make changes to MDT process as required
- Right click "MDT Deployment Share" -> Properties
- Set "Network (UNC) path" to the MDT deployment share location (found on passwords page). Note that this **cannot** be a DFS filesystem, it must point to a real server. DFS shares are not supported by MDT.
- If this is a new share, under "Rules" tab you will need to set the following (these may already be set if using an existing share):
  * You will need to set paths: `SLShare` to `<logging_location>`, `SLShareDynamicLogging` to `<logging_location>\dynlogs` and `BackupShare` to `<logging_location>`. These are directories where logs will be written during the MDT build process, so that you can debug any failures. `<logging_location>` can be found on the passwords page.
  * Ensure user details in this file match the MDT account detailed on the passwords page
- Click `Edit bootstrap.ini`
  * Set `DeployRoot` to the MDT deployment share location (found on passwords page)
  * Ensure user details in this file match the MDT account detailed on the passwords page
- Right click "MDT Deployment Share" -> update deployment share

Congratulations! You should now have a working MDT build server. See [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/MDT-(Microsoft-deployment-toolkit)) for details about how to *use* MDT.
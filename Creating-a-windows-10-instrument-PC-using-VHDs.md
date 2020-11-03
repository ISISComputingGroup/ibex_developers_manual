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


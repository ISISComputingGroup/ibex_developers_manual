> [Wiki](Home) > [Deployment](Deployment) > [Create IBEX VHDs](Create-IBEX-VHDs)

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

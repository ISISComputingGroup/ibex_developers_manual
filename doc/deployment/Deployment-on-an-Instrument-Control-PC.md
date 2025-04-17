# Deploy to an instrument machine

This document describes the steps necessary to install/upgrade IBEX on an Instrument control PC. Be sure to login as `spudulike` when deploying on instruments instead of `gamekeeper`.

## Preparatory Steps for Client and Server

- Inform the instrument scientist that you are going to upgrade the instrument in 5 minutes so that they are not surprised when you remote desktop to the instrument, include a link to the release notes of the latest release in this email. Wait 5 minutes.
- Visit each instrument on which code will be released and check for changes which have been made which are not summarised on the [IBEX wiki](https://github.com/ISISComputingGroup/IBEX/wiki#tocInstrumentInfo). Do this by running `git status` in the EPICs directory and looking at the diff and comparing with those changes.
- Make sure that the public share has the most recent version of `ibex_utils` from Git (i.e. do git pull).

## Notes on network share access
The install will need to access both `<public share>\ibex_utils` (where the install script is located) and `kits$` (where the ibex release and a genie python instance is kept). As we will be updating python, we cannot use the locally installed python for the deploy. 

On an instrument NDX computer the D: and O: drives will be mapped to the instrument archive and have sufficient access rights, however they can sometimes become disconnected and then things don't work. So before starting look in windows explorer and if D: and/or O: are showing as Disconnected click on them to reconnect.

If you do not have either a D: or O: network drive, then you will need to specify network credentials to map the drive via the `net use` command.    

## Upgrading IBEX to the latest version
1. If an instrument, check D: network drive status as per above _Notes on network share access_
1. Ensure the instrument is running and in a setup state
1. Take screenshots of blocks, motors, running VIs, etc. to allow later comparison
1. Ensure all command lines to EPICS or windows accessing the EPICS path are closed (though there is no need to stop the IBEX Server)
1. Run `<public share>\ibex_utils\installation_and_upgrade\instrument_deploy.bat` (or for 32-bit releases run with the parameter `x86`)
    - you can double click on this, but usually better to drag the path into a new empty cmd window so you don't miss any errors on abort  
    - It will look for the highest version number in the release folder as a source.
    - If you want to install a non-default release you need to set the `SUFFIX` variable in the batch file. For example with `x.y.z` being the current release and `hotfix` being the suffix, it will look for the folder `Releases/x.y.z-hotfix`
    - Apart from the below points, just follow instructions
    - Be warned the upgrade runs in 3 steps and so will claim to have finished the upgrade 3 times
    - Do not remove any SECI icons from the task list if this is not the first time install
1. Compare screenshots taken earlier to current state

## Install IBEX for the first time
_Note this is unlikely to happen now we've migrated most instruments, and SECI instruments should have a copy of IBEX at the least._
<details>
<summary> Click to expand</summary>

- If an instrument, check D: network drive status as per above _Notes on network share access_
- Run `<public share>\ibex_utils\installation_and_upgrade\instrument_install.bat` (if you are on a test machine you may have to enter the full DNS path rather than the shorthand)
    - you can double click on this, but usually better to drag the path into a new empty cmd window so you don't miss any errors on abort  
    - It will look for the highest version number in the release folder as a source.
    - If you want to install a non-default release you need to set the `SUFFIX` variable in the batch file. For example with `x.y.z` being the current release and `hotfix` being the suffix, it will look for the folder `Releases/x.y.z-hotfix`
    - Follow the instructions on the command line. 
- If needed, shutdown IBEX and [upgrade the ISISICP](Upgrade-ISISICP). Remember to run the journal parser installation (Step 8 of upgrading ICP) - this can take some time.
- After the script has successfully finished and the IBEX server has been started, run `instrument_test.bat` in the same folder and follow the instructions.
</details>

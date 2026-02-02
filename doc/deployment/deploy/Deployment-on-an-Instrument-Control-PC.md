# Deploy to an instrument machine

This document describes the steps necessary to install/upgrade IBEX on an Instrument control PC. Be sure to login as `spudulike` when deploying on instruments.

## Preparatory Steps for Client and Server

Before the group starts any manual deployments, one developer should run the [`instrument_deploy.yaml` ansible playbook](https://github.com/ISISComputingGroup/ansible-playbooks/tree/main?tab=readme-ov-file#instrument_deployyaml) which currently installs the JDK on instruments. This should be run on the relevant deploy group - the playbook will prompt for the hosts to run it on to avoid accidentally deploying to all instruments. As an example, to deploy to the winter group, enter `winter_deploy` (as specified in the [inventory file](https://github.com/ISISComputingGroup/ansible-playbooks/blob/main/hosts.yaml)).
This playbook has been designed so it is idempotent, ie. if a step has already occurred such as deploying the JDK it will not be repeated.

- Inform the instrument scientist that you are going to upgrade the instrument in 5 minutes so that they are not surprised when you remote desktop to the instrument, include a link to the release notes of the latest release in this email. Wait 5 minutes.
- Make sure that `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils` is pointing at `master` and is up to date (i.e. do git pull).

:::{note}
If the Git Bash window is not pointing to the 'master' branch, you need to register the repository path as a safe directory. Run `git config --global --add safe.directory '%(prefix)///isis/shares/ISIS_Experiment_Controls_Public/ibex_utils` in Git Bash to resolve this.

:::{note}
The install will need to access both `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils` (where the install script is located) and `\\isis\inst$\kits$` (where the ibex release and a genie python instance is kept). As we will be updating python, we cannot use the locally installed python for the deploy. 

On an instrument NDX computer the D: and O: drives will be mapped to the instrument archive and have sufficient access rights, however they can sometimes become disconnected and then things don't work. So before starting look in windows explorer and if D: and/or O: are showing as Disconnected click on them to reconnect.

If you do not have either a D: or O: network drive, then you will need to specify network credentials to map the drive via the `net use` command.    
:::

## Upgrading IBEX to the latest version
1. Ensure the instrument is running and in a setup state
1. Take screenshots of blocks, motors, running VIs, etc. to allow later comparison
1. Ensure all command lines to EPICS or windows accessing the EPICS path are closed (though there is no need to stop the IBEX Server)
1. Run `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\instrument_deploy.bat` (or for 32-bit releases run with the parameter `x86`)
    - you can double click on this, but usually better to drag the path into a new empty cmd window so you don't miss any errors on abort  
    - It will look for the highest version number in the release folder as a source.
    - If you want to install a non-default release you need to set the `SUFFIX` variable in the batch file. For example with `x.y.z` being the current release and `hotfix` being the suffix, it will look for the folder `Releases/x.y.z-hotfix`
    - Apart from the below points, just follow instructions - most options should be answered `Y` (yes) to, but if you are unsure on a particular machine ask on technical.
    - Be warned the upgrade runs in 3 steps and so will claim to have finished the upgrade 3 times
1. Compare screenshots taken earlier to current state


### Notes on steps

#### Hotfixes

The script runs `git status` in `C:\Instrument\Apps\EPICS` for uncommitted changes on an instrument.
These _should_ be documented on [this page](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information--hotfixes) and should hopefully all be submitted upstream. If not, ask on technical what to do - we may need to re-patch them after the release has been deployed. 

#### Python virtual environments

The script will set up virtual environments for anything that uses the mechanism documented in the {ref}`Dependency updates notes. <dep_update_venvs>`

It does this by searching for `requirements-frozen.txt` recursively in the top of EPICS, then uses `uv` to set virtual environments up and install dependencies.

## Restore IBEX from backup(s)

As part of the deployment script, backup zip files will be created in `C:\data\old\ibex_backup_<date>`. 
If you need to go back to a previous backup, you can restore a full backup using the `tar` command, which
is available in any `cmd` window. 

For example, to restore `c:\Instrument\Apps\Python3` from a backup, run the following in a `cmd` window:

```
mkdir c:\Instrument\Apps\Python3
tar -xf c:\data\old\ibex_backup_<date>\Python3.zip -C c:\Instrument\Apps\Python3
```

If the `mkdir` step fails with the target directory already existing, delete or move it elsewhere
before restoring the backup.

If you instead wish to just restore/check the contents of a single file, the backups are standard `.zip`
archives which can be browsed using any zip tool - for example `7-zip` is relatively convenient and widely
installed on NDX computers.

## Install IBEX for the first time
:::{note}
This is unlikely to happen now we've migrated all instruments from SECI.
:::
<details>
<summary> Click to expand</summary>

- If an instrument, check D: network drive status as per above _Notes on network share access_
- Run `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\instrument_install.bat` (if you are on a test machine you may have to enter the full DNS path rather than the shorthand)
    - you can double click on this, but usually better to drag the path into a new empty cmd window so you don't miss any errors on abort  
    - It will look for the highest version number in the release folder as a source.
    - If you want to install a non-default release you need to set the `SUFFIX` variable in the batch file. For example with `x.y.z` being the current release and `hotfix` being the suffix, it will look for the folder `Releases/x.y.z-hotfix`
    - Follow the instructions on the command line. 
- If needed, shutdown IBEX and [upgrade the ISISICP](Upgrade-ISISICP). Remember to run the journal parser installation (Step 8 of upgrading ICP) - this can take some time.
- After the script has successfully finished and the IBEX server has been started, run `instrument_test.bat` in the same folder and follow the instructions.
</details>

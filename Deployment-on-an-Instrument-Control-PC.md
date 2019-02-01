> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC)

This document describes the steps necessary to install/upgrade IBEX on an Instrument control PC.  Most of these steps are superseded by the install script (but we are not quite ready to commit to this).  This document is the reference for deployment. 
Steps are marked with **bold** prefixes to indicate the following:
- **deploy** step to be done when using the deploy script
- **upgrade** steps to be done when upgrading 
- **install** steps should be done only for install
- **mini-inst** only these steps should be done for installation of a mini inst server. After installation [configure](Configure-Mini-Inst) it in the appropriate manner.
- unlabelled steps should be done except for installing a mini inst.

# Steps using the install/deployment script
## Preparatory Steps for Client and Server

- Inform the instrument scientist that you are going to upgrade the instrument in 5 minutes so that they are not surprised when you remote desktop to the instrument. Wait 5 minutes.
- Look in `C:\Program Files\MySQL` if `MySQL Server 5.7` and `MySQL Server 5.6` exists and `MySQL Server 5.6` is empty apart from bin then delete the directory `MySQL Server 5.6`
- Make sure that the public share has the most recent version of the install and upgrade information from Git (i.e. do git pull).

#### install
- Run `<public share>\ibex_utils\installation_and_upgrade\instrument_install.bat` (if you are on a test machine you may have to enter the full DNS path rather than the shorthand)
    - It will look for the highest version number in the release folder as a source.
    - If you want to install a non-default release you need to set the `SUFFIX` variable in the batch file. For example with `x.y.z` being the current release and `hotfix` being the suffix, it will look for the folder `Releases/x.y.z-hotfix`
    - Follow the instructions on the command line. 
- If needed, shutdown IBEX and [upgrade the ISISICP](Upgrade-ISISICP). Remember to run the journal parser installation (Step 8 of upgrading ICP) - this can take some time.
- After the script has successfully finished and the IBEX server has been started, run `instrument_test.bat` in the same folder and follow the instructions.
- If not already set, change the Windows theme to "Windows 7" in the "Aero Themes" section.  Also change the background to solid light grey.

#### upgrade
- Ensure the instrument is running and in a setup state (e.g. so you can take screenshots of blocks, motors, running VIs, etc.)
- Ensure all command lines to EPICS are closed
- Upgrade the ISISICP (Do not do this step (shurdown or install) for release 5.2)
  - Shutdown IBEX GUI (server should remain running)
  -  Run [Upgrade the ISISICP](Upgrade-ISISICP)
- Run `<public share>\ibex_utils\installation_and_upgrade\instrument_deploy.bat` **for 5.2.1** use `instrument_deploy_5.2.X.bat`
    - It will look for the highest version number in the release folder as a source.
    - If you want to install a non-default release you need to set the `SUFFIX` variable in the batch file. For example with `x.y.z` being the current release and `hotfix` being the suffix, it will look for the folder `Releases/x.y.z-hotfix`
    - Apart from the below points, just follow instructions
    - Be warned the upgrade runs in 3 steps and so will claim to have finished the upgrade 3 times
    - Do not remove any SECI icons from the task list if this is not the first time install
    - Ignore the section about copying ibex_system_boot.bat to ProgramData and so the step below instead
    - Answer `y` to everything apart from start GUI.
    - Python issues mean we should exit the script before install IBEX server and move the python directory to old and restart
    - The upgrade config part of the script will not run you should do this after the install
After install:
    1. Run the E4 client and pin the icon
    1. Run the upgrade config script in admin mode

## Creating IBEX auto-startup 
- Go to the `Startup` folder (which is contained inside the user's `AppData\Roaming\Microsoft\Windows\Start Menu\Programs` folder).
- In this directory do new -> shortcut and browse to c:\instrument\apps\epics and choose ibex_system_boot.bat


# Manual deploy instructions

Moved to https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/OLD-Manual-deployment-instructions-(not-for-normal-use)

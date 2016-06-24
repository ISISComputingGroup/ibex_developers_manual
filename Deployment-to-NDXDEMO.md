> [Wiki](Home) > Deployment to NDXDEMO

This document describes the steps necessary to install IBEX on NDXDEMO. There is a similar page on installation to a generic instrument control PC [here](Deployment-on-an-Instrument-Control-PC).

Notably this process is different for two reasons:

1. It focuses on the process from a developer point of view so includes the build steps in Jenkins
1. Users usually log into NDXDEMO as the local user via remote desktop and so don't have access to the `//isis` shared drive.

Note that the release process for IBEX is currently in flux and so some of these steps may change soon but the broad outline should stay the same.

## Jenkins builds

We are going to be using the following Jenkins builds:

- [genie_python](http://epics-jenkins.isis.rl.ac.uk/job/genie_python/)
- [EPICS](http://epics-jenkins.isis.rl.ac.uk/job/EPICS_IOC_Windows7_x64/2472/)
- [IBEX](http://epics-jenkins.isis.rl.ac.uk/job/ibex_gui/)

Before proceeding, ensure all changes have been incorporated into these builds.

## Client

1. Go to `\\isis\Kits$\CompGroup\ICP\Client\`
1. Copy the following folders to your local machine:
    - genie_python
    - EPICS_UTILS
    - BUILDnnn where `nnn` corresponds to the build of IBEX you want to deploy
1. Create a zip file containing the 3 folders. Zipping files is not mandatory to this process but will improve file transfer speeds dramatically.
1. Remote desktop to NDXDEMO
1. Copy the zip file to the folder `C:\Installers` **on NDXDEMO**. Clipboards are shared with remote desktop sessions so normal copy paste operations can be used.
1. Unzip the archive
1. Delete\move `C:\Instrument\Apps\Python` and `C:\Instrument\Apps\Client`
1. From `C:\Installers\Buildnnn` run `install_client.bat`

## Install EPICS
** This will install genie_python and IBEX **

1. Go to `\\isis\Kits$\CompGroup\ICP\EPICS\EPICS_win7_x64`
1. Find the folder corresponding to the build you want to deploy
1. Create a zip file of that folder on your local disk. Zipping files is not mandatory to this process but will improve file transfer speeds dramatically.
1. Remote desktop to NDXDEMO
1. Copy the zip file to the folder `C:\Installers` **on NDXDEMO**. Clipboards are shared with remote desktop sessions so normal copy paste operations can be used.
1. Unzip the EPICS archive
1. Delete C:\Instrument\Apps\EPICS (or at least move/rename it)
1. From `C:\Installers\EPICS` run `install_to_inst.bat`

## Start the Instrument

To start the instrument, open a command prompt and type the following:

    cd c:\Instrument\Apps\EPICS
    start_inst
    
Allow the `start_inst` script a few moments to complete before starting the IBEX client.

## Record Release

1. Record the release to the instrument (add to list in [Instrument Releases](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information))

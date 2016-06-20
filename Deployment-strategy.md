> [Wiki](Home) > [Deployment](Deployment) > Deployment Strategy

## TODO

1. Does Genie python belong in the back end.

## Versioned Components

All component should be versioned and released together under a single version number. 

### Version Numbers

Component will be version using

    major.minor.patch.build 

For example 1.2.3.678 is major version 1, minor version 2,  patch version 3, build number 678. The various parts are:

| What  | Description | Limitations on software |
| ---   | ----------- | ----------------------- |
| Major | Major incompatible releases of the software | Components should not work with each other, a warning should be issued. E.g. Block server PV name changed |
| Minor | Minor changes to the API which are back compatible, e.g. adding extra PVs | Items with the same minor version should work with each other |
| Patch | Changes which fix bugs in the system without changing functionality | E.g. Performance improvement |
| Build | The build server reference for this build | This is ignored but is a useful reference to find exact builds |

## Components

We are going to keep the list of components as small as possible to allow easier versioning and more coherent releases but if we find the versioning gets in the way of release we can split down the components more. Currently Components:

### 1. IBEX GUI

The IBEX GUI is likely to be installed by users and so its version is dependent on when user update. On connection to an instrument it should check the current version and encourage users to update to the latest version.

### 2. Genie Python

Genie Python is a standalone product which is used with the IBEX GUI and backend.

### 3. Back End

All the processes that start or must be running when the start-inst script is run.

1. IOCs
1. Block Server
1. Configuration Files
1. Databases (MySql) 
    1. alarms
    1. archive data
    1. experiment details
    1. message logs

The likely deployment is:
* Most instrument will be running a previous release. 
* Instrument which need the newest functionality, will be running the latest release.
* Instruments that need to be patched mid-cycle will be running a [patch release], (https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release#patch-release). The patch release has just enough in it over an above a standard release that the instrument can run. 

Ideally instruments are updated each time they have down time.

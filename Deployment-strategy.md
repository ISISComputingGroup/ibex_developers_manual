# Deployment Strategy

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

# Creating a Release

## Standard Release

Project is ready to be released not for a specific event, e.g. at the end of a sprint.

1. Look at the released features in this branch [IBEX/wiki/ReleaseNotes_Dev](https://github.com/ISISComputingGroup/IBEX/wiki/ReleaseNotes_Dev) and find the most severe change.
1. Start a release branch so that the code is frozen
1. Update the version number in the files ()
1. Commit you changes and push.
1. Create a released version in the [releases table](https://github.com/ISISComputingGroup/IBEX/wiki/Releases) (including link to release notes)
1. Move the changes which have been merged into master from the dev page to the new release notes page for the version.
1. Test
1. Record and fix any bugs
1. Create a tag of the form  VX.x.p `git tag -a vX.x.p -m "Release version X.x.p"`
1. Push tags and branch
1. Merge release branch back into master to capture any changes

## Patch Release

The is a release when a change needs to be made between standard releases; i.e. a standard release is inappropriate because it includes lots of code which has not been through a code freeze and test. 

1. Start a branch from the tag for the released version
1. Is the code for the bug/enhancement already written?
    * No: Make the changes on the branch.
    * Yes: Cherry pick commits needed from the branch with the written code
1. Test
1. Release as per a standard release but 
    1. Use this branch instead of master
    1. Only include the change you have made in the release notes
    1. Copy the release notes issues into the development page
1. Merge the new code back into master

# TODO

1. Does Genie python belong in the back end.
1. How do we create the build in Jenkins?

# Creating a release

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

release/*
```

## Standard Release

Project is ready to be released not for a specific event, e.g. at the end of a sprint. Script Generator version number always differs to the client's.

{#creating_release_pre_testing_steps}
### Pre Testing

1. Find out anything that needs to be in the release that isn't and mark with `for release` label. (This does not prevent a release)
1. Ensure the version of `cs-studio` [referenced in the GUI's target platform](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.targetplatform/targetplatform.target)
is recent enough to include the most recent changes in the
[`isis_css_top` repository](https://github.com/ISISComputingGroup/isis_css_top).
1. Update the [upgrade script](https://github.com/ISISComputingGroup/EPICS-upgrade/blob/master/upgrade.py) to include the latest version (this is done on master). Steps to do this are in [Config Upgrader in section *creating a production upgrade script*](/tools/Config-Upgrader) 
    1. After committing these changes to `master` on the `EPICS-upgrade` submodule, don't forget to push the new submodule version to `master` on the top `EPICS` branch. This is needed to make sure you changes appear on the release branch created in the next step. 
1. For packages which are published on `PyPI`, in particular `genie_python` and `ibex_bluesky_core`, create PyPI releases if needed.
    1. These packages are released by performing a `git tag x.y.z` on a checkout of `main`, where `x.y.z` is the new version you want to release. Push the tag using `git push origin tag x.y.z`. They will then build in github actions, and prompt to "approve" the release pipeline to PyPI. 
    1. `genie` should be released with a version number matching the main IBEX version number. The release takes around 15 minutes in GHA.
    1. `ibex_bluesky_core` should generally have a minor/patch version incremented for now until we reach v1. The release takes a couple of minutes in GHA.
    1. **Ensure these releases were successful** by checking on [pypi](https://pypi.org/) for the new release number before proceeding.
1. Start the Github Actions pipeline [`create-release-branches`](https://github.com/ISISComputingGroup/ibex_utils/actions/workflows/create-release-branches.yml).
    - Click on 'Run workflow'
    - Set `VERSION` to the new release version (e.g. `X.x.m`).
    - Set `TAG` if you wish to branch off a commit other than the latest top level `HEAD`. If you do branch off an earlier commit, also set `REMOTE` to `false` as it now does not make sense to verify if you are on the latest submodule versions.
    - The script will then (as selected):
        - Create the release branches (named `Release_X.x.m` except `Release_Script_Gen_X.x.m` for script generator) for:
            - `EPICS` and submodules.
            - `IBEX GUI`.
            - `Script Generator`.
            - `Uktena`.
        - Update or add version numbers:
            - In `ioc/master/INSTETC/INSTETC-IOC-01App/Db/svn-revision.db.tmpl` for `EPICS`.
            - In `/uk.ac.stfc.isis.ibex.e4.client/pom.xml` and `/uk.ac.stfc.isis.ibex.e4.client/META-INF/MANIFEST.mf` for `IBEX GUI`.
            - In `/uk.ac.stfc.isis.scriptgenerator.client/pom.xml` and `/uk.ac.stfc.isis.scriptgenerator.client/META-INF/MANIFEST.mf` for `Script Generator`.
            - Note: `genie_python` library version numbers are set automatically from the git tag, and no longer need manually updating.
        - Push these changes to remote release branch.
1. Start all of [these builds](https://epics-jenkins.isis.rl.ac.uk/view/Release/) in Jenkins.
1. Copy the new version's release notes (copy & paste) into a new blank `Release Notes "X.x.m"` (where `X.x.m` is the upcoming version) file and clear the contents: Check that all of the merged tickets have also had their [release notes merged](https://github.com/ISISComputingGroup/IBEX/pulls). Check that the release notes are as understandable as possible. 
1. Create a released version entry in the [releases table](https://github.com/ISISComputingGroup/IBEX/blob/master/docs/all-releases.md) (including link to release notes) and commit to master.
1. Update the "Latest Stable Release" and "Upcoming release" links on the [IBEX wiki homepage](https://github.com/ISISComputingGroup/IBEX) to be the new release and commit to master.
1. If applicable, update the dependencies since the last release and add them to the bottom of the release notes. To find the python dependencies list, run a `pip freeze` on a cleanly released `uktena`. Note that you will need to specify the scripts directory to run pip commands. i.e. `C:\Instrument\Apps\Python3\Scripts\Pip.exe freeze`
1. copy the release to the `git$` share on `control-svcs` (see Keeper for the username and password for this), this is so we can set git remotes for hotfixes etc. as part of the deploy. So if release is number 1.2.3
    - `robocopy "\\isis\inst$\Kits$\CompGroup\ICP\Releases\1.2.3\EPICS\.git" "\\control-svcs.nd.rl.ac.uk\git$\releases\1.2.3\EPICS.git" /mir /nfl /ndl`
    - edit `EPICS.git\config` on the control-svcs version (you can browse straight to the `\\control-svcs` share above)
        - change `bare = false` to `bare = true`
        - Add an extra section at end of file
```
[http]
        receivepack = true
```

1. Do the same for the `EPICS32` 32-bit build, replacing `EPICS` with `EPICS32` everywhere in the commands above.
1. Check release is now listed in [`https://control-svcs.isis.cclrc.ac.uk/git/?a=project_list;pf=releases`](https://control-svcs.isis.cclrc.ac.uk/git/?a=project_list;pf=releases)
1. Run the [`instrument_deploy.yaml` ansible playbook](https://github.com/ISISComputingGroup/ansible-playbooks/tree/main?tab=readme-ov-file#instrument_deployyaml) which currently installs the JDK on instruments. 


{#creating_release_testing_steps}
### Testing

Update `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils` - this is so the most recent install script will be used for testing and install. You should:
* do a `git branch` and check it is on `master` and not e.g. a test or ticket branch
* do a `git status` and check for any changes, if there are post on Teams
* do a `git pull` so you are on the latest `master` branch with no local changes

One or more people should do [manual system tests, using this page](Manual-System-Tests).

{#creating_release_post_testing_steps}
### Post Testing

These steps should only be done once all changes to a release have been made and we are ready to deploy. Here we are creating a tag
which will become inconsistent if further changes are made to the release branch. Hence it is important to delete
the relevant release branch after it has been tagged.
    
1. Create a release tag in the EPICS, ibex_gui and uktena repositories. For each repo
    1. Go to `[REPO_URL]/releases`, e.g. `https://github.com/ISISComputingGroup/ibex_gui/releases`
    1. Click `Draft a new release`
    1. Enter the tag version in the format `vX.x.p` and target the release branch
    1. Enter the title `Release version X.x.p`
    1. Add a link to the release notes in the description
    1. **Delete the release branch** once the release and tag has been created. 
1. Create release tag from the release branch for each submodules in EPICS, then delete the release branch. To do this, run the following two git commands in top level EPICS (replace `X.x.x` with the release number): 
    1. `git submodule foreach --recursive "git fetch && git tag Release_ibex_X.x.x origin/Release_X.x.x || exit 0"` // Create tag
    1. `git submodule foreach --recursive "git push origin tag Release_ibex_X.x.x && git push --delete origin Release_X.x.x || exit 0"` // Push tags and delete release branch

    _Note: you may need to run `git config fsck.badEmail ignore` for the above step_
1. Make sure any changes on the release branch are merged back onto master for EPICS, ibex_gui, and uktena (except version numbering)
1. Consider which instruments need this release:
    * Breaking release: upgrade everyone
    * Big improvement:  upgrade everyone if there is a big improvement that everyone will benefit from
    * Standard release: upgrade instruments that need updates, i.e. they need a newly released feature, and all those that are in the current release group, see [column in instruments table](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information). Note on the release ticket which instruments need to be released to using checkboxes (one for start and one for finish).
1. [Create repository for recording instrument changes post release](release/Release-based-repository) the deploy script automatically puts the instrument onto a branch of this repository
## Partial Release
For any release in which GUI version increments but server version does not, ensure the previous server version is added to the release folder via symbolic links or junctions, [see this ticket](https://github.com/ISISComputingGroup/IBEX/issues/7250).

## Patch Release

The is a release when a change needs to be made between standard releases; i.e. a standard release is inappropriate because it includes lots of code which has not been through a code freeze and test. 

1. Follow all Pre Testing steps above except:
    * For step 4 (creating the release branch) instead of creating from master create it from the latest release tag
    * Update GUI Java JRE
    * Finding the most significant change
    * Updating the MySQL and Java being deployed
1. Is the code for the bug/enhancement already written?
    * No: Make the changes on the branch.
    * Yes: Cherry pick commits needed from the branch with the written code
1. Test
1. Release as per a standard release but 
    1. Use this branch instead of master
    1. Only include the change you have made in the release notes
    1. Copy the release notes issues into the development page
1. Merge the new code back into master


## Adding late commits to the release Branch for EPICS

1. Test and merge the change into master
1. Create a release branch in the submodule (if it doesn't exist)
    1. Navigate to EPICS in github
    1. navigate to the submodule
    1. Create new branch (this means it will be branched from the release point)
1. Switch the branch of the submodule:  `git checkout Release_X.x.m`
1. Pull the latest release branch:  `git pull`
1. Merge in the ticket `git merge XXX`
1. push that branch
1. cd to EPICS
1. checkout release branch and pull
1. update submodule reference, commit and push.

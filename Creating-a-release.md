> [Wiki](Home) > [Deployment](Deployment) > Creating a release

## Understanding Java Licensing
Make sure you [understand how Java is licensed](Understanding-Java-Licensing), so that we do not inadvertently make ISIS liable for licensing fees.

## Release tickets

Text for release ticket:

    As a developer I want an IBEX release so I can install it on the instrument machines for the start of machine physics on 26th.
    
    Acceptance Criteria:
    
    - [ ] [Pre Testing Steps](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release#pre-testing)
    - [ ] [Testing steps](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release#testing)
    - [ ] [Post Testing](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release#post-testing)
    - [ ] [Create a ticket to update dependencies to latest versions and test](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Dependency-updates)
    - [ ] [Create a ticket to give instrument demos](https://github.com/ISISComputingGroup/IBEX/wiki/Timetable-for-Instrument-Demos)
    - [ ] Distribute release notes via email [Instrument scientist release email](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Updating-Instrument-Machines#a-new-release)

## Standard Release

Project is ready to be released not for a specific event, e.g. at the end of a sprint. Script Generator version number always differs to the client's.

### Pre Testing

1. Contact computing group to let us know of the upgrade. Find out anything that needs to be in the release that isn't and mark with `for release` label. (This does not prevent a release)
1. Look at the released features in this branch [Upcoming Changes](https://github.com/ISISComputingGroup/IBEX/blob/master/release_notes/ReleaseNotes_Upcoming.md) and find the most significant level of change (i.e. is this cumulatively a major change, a minor change, or a patch?).
1. Update the [upgrade script](https://github.com/ISISComputingGroup/EPICS-upgrade/blob/master/upgrade.py) to include the latest version (this is done on master). Steps to do this are in [Config Upgrader in section *creating a production upgrade script*](Config-Upgrader#creating-a-production-upgrade-script) 
    1. After committing these changes to `master` on the `EPICS-upgrade` submodule, don't forget to push the new submodule version to `master` on the top `EPICS` branch. This is needed to make sure you changes appear on the release branch created in the next step. 
1. For packages which are published on `PyPI`, in particular `genie_python` and `ibex_bluesky_core`, create PyPI releases if needed.
    1. These packages are released by performing a `git tag x.y.z` on a checkout of `main`, where `x.y.z` is the new version you want to release. Push the tag using `git push origin tag x.y.z`. They will then build in github actions, and prompt to "approve" the release pipeline to PyPI. 
    1. `genie` should be released with a version number matching the main IBEX version number. The release takes around 15 minutes in GHA.
    1. `ibex_bluesky_core` should generally have a minor/patch version incremented for now until we reach v1. The release takes a couple of minutes in GHA.
    1. **Ensure these releases were successful** by checking on [pypi](https://pypi.org/) for the new release number before proceeding.
1. Start the Jenkins pipeline [Release Branches](https://epics-jenkins.isis.rl.ac.uk/job/Release_branches/).
    - Click on 'Build with Parameters'.
    - Set `VERSION` to the new release version (e.g. `X.x.m`).
    - Set `TAG` if you wish to branch off a commit other than the latest top level `HEAD`. If you do branch off an earlier commit, also set `REMOTE` to `false` as it now does not make sense to verify if you are on the latest submodule versions. 
    - Check `REMOTE` if the `EPICS` submodules should be checked for later versions on their remote - the script will fail if there are submodule commits unpushed to top level. For a normal release you will be expecting all submodules to be on the latest version. If you want the currently pinned (not necessarily latest) versions, do not check REMOTE. If you should/expect to be using the latest versions of all dependent submodules, check REMOTE box to verify this. If there are unpushed submodules the `EPICS repo checks` Jenkins build will likely be in error already.
    - The script will then (as selected):
        - Create the release branches (named `Release_X.x.m` except `Release_Script_Gen_X.x.m` for script generator) for:
            - `EPICS` and submodules.
            - `IBEX GUI`.
            - `Script Generator`.
            - `Uktena`.
            - `JSON_bourne`. (not none by default as it does not often change and is also not directly deployed to instruments)
        - Update or add version numbers:
            - In `ioc/master/INSTETC/INSTETC-IOC-01App/Db/svn-revision.db.tmpl` for `EPICS`.
            - In `/uk.ac.stfc.isis.ibex.e4.client/pom.xml` and `/uk.ac.stfc.isis.ibex.e4.client/META-INF/MANIFEST.mf` for `IBEX GUI`.
            - In `/uk.ac.stfc.isis.scriptgenerator.client/pom.xml` and `/uk.ac.stfc.isis.scriptgenerator.client/META-INF/MANIFEST.mf` for `Script Generator`.
            - Note: `genie_python` library version numbers are set automatically from the git tag, and no longer need manually updating.
        - Push these changes to remote release branch.
        - Start the Jenkins builds (click `Scan Repository` on the ones that are multibranch pipelines):
            - `EPICS_release`. (Build will be in `Kits$\CompGroup\ICP\Releases\X.x.m\EPICS`)
            - `EPICS_release32`. (Build will be in `Kits$\CompGroup\ICP\Releases\X.x.m\EPICS32`)
            - `uktena_release_pipeline`. (Build will be in `Kits$\CompGroup\ICP\Releases\X.x.m\genie_python_3`)
            - `ibex_gui_releases_pipeline`. (Build will be in `Kits$\CompGroup\ICP\Releases\X.x.m\Client`)
            - `scriptgenerator_release`. (Build will be in `Kits$\CompGroup\ICP\Releases\script_generator_release\X.x.m`)
1. Move the `Upcoming Release Notes` page (copy & paste) into a new blank `Release Notes "X.x.m"` file: Check that all of the merged tickets have also had their [release notes merged](https://github.com/ISISComputingGroup/IBEX/pulls) then move the changes which have been merged into the new release from the [upcoming page](https://github.com/ISISComputingGroup/IBEX/blob/master/release_notes/ReleaseNotes_Upcoming.md) to a new release notes page for the version, and commit this change to the master branch. Check that the release notes are as understandable as possible. 
1. Create a released version entry in the [releases table](https://github.com/ISISComputingGroup/IBEX/blob/master/docs/all-releases.md) (including link to release notes) and commit to master.
1. Update the "Latest Stable Release" link on the [IBEX wiki homepage](https://github.com/ISISComputingGroup/IBEX) to be the new `"Release X.x.m"` and commit to master.
1. Remove all entries from `Upcoming Release Notes`, leaving a blank file with only the headers, e.g. "Instrument Specific Changes", etc. and commit to master.
1. If applicable, update the dependencies since the last release and add them to the bottom of the release notes. To find the python dependencies list, run a `pip freeze` on a cleanly released `genie_python`. Note that you will need to specify the scripts directory to run pip commands. i.e. `C:\Instrument\Apps\Python3\Scripts\Pip.exe freeze`
1. Update the [user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki) with any relevant changes
1. copy the release to `control-svcs`, this is so we can set git remotes for hotfixes etc. as part of the deploy. So if release is number 1.2.3
    - `robocopy "Kits$\CompGroup\ICP\Releases\1.2.3\EPICS\.git" "\\control-svcs.nd.rl.ac.uk\git$\releases\1.2.3\EPICS.git" /mir /nfl /ndl`
    - edit `EPICS.git\config` on the control-svcs version (you can browse straight to the `\\control-svcs` share above)
        - change `bare = false` to `bare = true`
        - Add an extra section at end of file
```
[http]
        receivepack = true
```
1. Check release is now listed in `https://control-svcs.isis.cclrc.ac.uk/git/?a=project_list;pf=releases` 

### Testing

Using GitBash, update the `experiment controls public share` has the most recent version of `ibex_utils` from Git (i.e. do git pull) - this is so the most recent install script will be used for testing and install. In git bash you can do a `cd` with the windows path but just change `\` to `/` e.g. `cd //isis/somewhere`. When you do a git operation it may warn about directory ownership, just follow the command it suggests to add an exception and then git try again. You should:
* do a `git branch` and check it is on `master` and not e.g. a test or ticket branch
* do a `git status` and check for any changes, if there are post on Teams
* do a `git pull` so you are on the latest `master` branch with no local changes

One or more people should do [manual system tests, using this page](Manual-system-tests).

### Post Testing

These steps should only be done once all changes to a release have been made and we are ready to deploy. Here we are creating a tag
which will become inconsistent if further changes are made to the release branch. Hence it is important to delete
the relevant release branch after it has been tagged.
    
1. Create a release tag in the EPICS, ibex_gui, genie_python and JSON_bourne repositories. For each repo
    1. Go to `[REPO_URL]/releases`, e.g. `https://github.com/ISISComputingGroup/ibex_gui/releases`
    1. Click `Draft a new release`
    1. Enter the tag version in the format `vX.x.p` and target the release branch
    1. Enter the title `Release version X.x.p`
    1. Add a link to the release notes in the description
    1. **Delete the release branch** once the release and tag has been created. 
1. Create release tag from the release branch for each submodules in EPICS, then delete the release branch. To do this, run the following two git commands in top level EPICS (replace `X.x.x` with the release number): 
    1. `git submodule foreach --recursive "git fetch && git tag Release_ibex_X.x.x origin/Release_X.x.x || exit 0"` // Create tag
    1. `git submodule foreach --recursive "git push --tags && git push --delete origin Release_X.x.x || exit 0"` // Push tags and delete release branch

    _Note: you may need to run `git config fsck.badEmail ignore` for the above step_
1. Make sure any changes on the release branch are merged back onto master for EPICS, ibex_gui, genie_python, and JSON_bourne (except version numbering)
1. Consider which instruments need this release:
    * Breaking release: upgrade everyone
    * Big improvement:  upgrade everyone if there is a big improvement that everyone will benefit from
    * Standard release: upgrade instruments that need updates, i.e. they need a newly released feature, and all those that are in the current release group, see [column in instruments table](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information). Note on the release ticket which instruments need to be released to using checkboxes (one for start and one for finish).
1. Deploy a new JSON_bourne if required see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Web-Dashboard)
1. Create repository for recording instrument changes post release https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Release-based-repository the deploy script automatically puts the instrument onto a branch of this repository
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

### Note: Minor upgrades to v11.0.0.
**WARNING:** If branching off the `v11.0.0` to make a release, you will need to re-add changes made in this [commit](https://github.com/ISISComputingGroup/EPICS-upgrade/commit/9b92ba915ca7cfdd1f711aff4945fe842972ee11). Otherwise, you will have problems with an incorrect number in the instrument's config area when deploying. 

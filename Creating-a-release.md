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
    1. Don't forget to push the changes to the associated submodule on the EPICS master branch before proceeding.
1. Start a release branch so that the code is frozen (e.g. `Release_1.1.0`). You will need a branch for
    1. [genie_python](https://github.com/ISISComputingGroup/genie_python)
    1. [ibex_gui](https://github.com/ISISComputingGroup/ibex_gui)
    1. [script_generator](https://github.com/ISISComputingGroup/ibex_gui)
        1. Script generator release branch should start with `Release_Script_Gen_X.x.m`

    1. [EPICS](https://github.com/ISISComputingGroup/EPICS)
    1. For EPICS submodules you should use:
        1. `git submodule update --init --recursive --remote` which sets all the repos to their pinned version
        1. `git submodule foreach "(git checkout -b Release_X.x.x; git push -u origin Release_X.x.x)||true"` this creates a branch at the current checked out version for each repo and pushes it.
    1. [JSON_bourne](https://github.com/ISISComputingGroup/JSON_bourne). First check if changes have been made as JSON_bourne is rarely edited.
1. Update the version numbers:
    1. GUI
        1. In `/uk.ac.stfc.isis.ibex.e4.client/plugin.xml` in `Overview` tab set `Version: ` to be `X.x.m`
        1. In `/uk.ac.stfc.isis.ibex.e4.client/pom.xml` edit the `<version>` tag (not in parent) content to be `X.x.m` (This tag may not be present and so will have to be added see as in [this](https://github.com/ISISComputingGroup/ibex_gui/compare/master...Release_5.2.1) example)
        1. Edit the `Bundle-Version` in `/uk.ac.stfc.isis.ibex.e4.client/META-INF/MANIFEST.mf` to be `X.x.m`
    1. Script generator
        1. In `/uk.ac.stfc.isis.scriptgenerator.client/plugin.xml` in `Overview` tab set `Version: ` to be `X.x.m`
        2. In `/uk.ac.stfc.isis.scriptgenerator.client/pom.xml` create a new `<version>` tag (not in parent) and give it content of be `X.x.m` (e.g. see [here](https://github.com/ISISComputingGroup/ibex_gui/compare/Release_Script_Gen_7.2.0))

    1. EPICS
        1. In `EPICS\ioc\master\INSTETC\INSTETC-IOC-01App\Db\svn-revision.db.tmpl` edit `field(VAL, "0.0.0.$WCREV$")` to be `field(VAL, "X.x.m.$WCREV$")`
        1. NB this has to be committed on a branch in IOC and then this submodule commit has to be added to the EPICS release branch
    1. Genie Python
        1. `...\Python\Lib\site-packages\genie_python\version.py` edit `VERSION = "0.0.0.qualifier"` to VERSION = "X.x.m"
1. Commit your changes and push.
1. For the builds `ibex_gui_release`, `genie_python_release`, `scriptgenerator_release` and `EPICS_release`, do the following:
    1. Find the release build pipeline in Jenkins
    1. Click "Scan repository". It should find the new release branch and queue a build.
    1. The release build for script generator will be created in `P:\Kits$\CompGroup\ICP\Releases\script_generator_release\X.x.m`
    1. The release builds for the rest will be created in `P:\Kits$\CompGroup\ICP\Releases\X.x.m`
   
1. Check that all of the merged tickets have also had their [release notes merged](https://github.com/ISISComputingGroup/IBEX/pulls) then move the changes which have been merged into the release from the [upcoming page](https://github.com/ISISComputingGroup/IBEX/blob/master/release_notes/ReleaseNotes_Upcoming.md) to a new release notes page for the version. Whilst doing this make sure that the release notes are as understandable as possible. 
1. Create a released version in the [releases table](https://github.com/ISISComputingGroup/IBEX#all-releases) (including link to release notes)
1. Find dependencies which have been updated since last release and add them to the bottom of the release notes. Particularly make sure that you run a `pip freeze` on a cleanly released `genie_python` to give you the python dependencies list.
1. Update the [user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki) with any relevant changes

### Testing
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
    1. *Delete the release branch* once the release and tag has been created. 
1. Create release tag from the release branch for each submodules in EPICS, then delete the release branch. To do this, run the following two git commands in top level EPICS (replace `X.x.x` with the release number): 
    1. `git submodule foreach --recursive "git fetch && git tag Release_ibex_X.x.x origin/Release_X.x.x || exit 0"` // Create tag
    1. `git submodule foreach --recursive "git push --tags && git push -d origin Release_X.x.x || exit 0"` // Push tags and delete release branch
1. Make sure any changes on the release branch are merged back onto master (except version numbering)
1. Consider which instruments need this release:
    * Breaking release: upgrade everyone
    * Big improvement:  upgrade everyone if there is a big improvement that everyone will benefit from
    * Standard release: upgrade instruments that need updates, i.e. they need a newly released feature, and all those that are in the current release group, see [column in instruments table](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information). Note on the release ticket which instruments need to be released to using checkboxes (one for start and one for finish).
1. Deploy a new JSON_bourne if required see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Web-Dashboard)

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

> [Wiki](Home) > [Deployment](Deployment) > Creating a release

## Standard Release

Project is ready to be released not for a specific event, e.g. at the end of a sprint.

1. Look at the released features in this branch [IBEX/wiki/ReleaseNotes_Dev](https://github.com/ISISComputingGroup/IBEX/wiki/ReleaseNotes_Dev) and find the most significant level of change (i.e. is this cumulatively a major change, a minor change, or a patch?).
1. Start a release branch so that the code is frozen (e.g. `Release_v1.1.0`). You will need a branch for
    1. EPICS
    1. genie_python
    1. ibex_gui
1. Update the version numbers:
    1. GUI
        1. In `ibex_gui/base/uk.ac.stfc.isis.ibex.product/META-INF/MANIFEST.MF` edit `Bundle-Version:...` to be `X.x.m.qualifier`
        1. In `ibex_gui/base/uk.ac.stfc.isis.ibex.product/pom.xml` edit the `<version>` tag content to be `X.x.m-SNAPSHOT`
        1. In `ibex_gui/base/uk.ac.stfc.isis.ibex.client.product/pom.xml` edit the `<version>` tag content (the one underneath `<modelVersion>`) to be `X.x.m-SNAPSHOT`
    1. EPICS
        1. In `EPICS\ioc\master\INSTETC\INSTETC-IOC-01App\Db\svn-revision.db.tmpl` edit `field(VAL, "1.0.0.$WCREV$")` to be `field(VAL, "X.x.m.$WCREV$")`
    1. Genie Python
        1. `genie_python\source\version.py` edit `CURRENT_VERSION = "2.0.0"` to CURRENT_VERSION = "X.x.m"
1. Commit you changes and push.
1. For the builds `ibex_gui_release`, `genie_python_release` and `EPICS_release`, do the following:
    1. Find the build in Jenkins
    1. Go into the build configuration (configure button in left-hand panel)
    1. Update the `Branches to build > Branch specifier` field to `*/Release_X.x.m` where `X.x.m` is the appropriate release number.
    1. Click `Build now`
    1. The release builds will be created in `P:\Kits$\CompGroup\ICP\Releases\X.x.m`
1. Create a released version in the [releases table](https://github.com/ISISComputingGroup/IBEX/wiki/Releases) (including link to release notes)
1. Move the changes which have been merged into the release from the dev page to the new release notes page for the version.
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

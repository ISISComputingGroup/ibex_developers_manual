# Jenkins Build Server

There is a Jenkins Build Server located at [http://epics-jenkins.isis.rl.ac.uk/](http://epics-jenkins.isis.rl.ac.uk/).

For information on configuring Jenkins see [Adding a new Windows machine to Jenkins](Adding-a-new-Windows-machine-to-Jenkins).

## What is built

### EPICS

* Builds EPICS itself and the IOCs
* Runs the unit tests for the BlockServer and the DatabaseServer
* Runs a Python script as a series of unit tests to check the units in all the EPICS db files
* If the above was successful the compiled binaries are made available at `\\isis\inst$\Kits$\CompGroup\ICP\EPICS`

### Client

* The [`ibex_gui`](http://epics-jenkins.isis.rl.ac.uk/job/ibex_gui_pipeline/) build uses the `master` branch for the [IBEX GUI](https://github.com/ISISComputingGroup/ibex_gui)
* The `ibex_gui_build_PRs` builds all the PRs for the `ibex_gui` branch
* The Tycho build is run, which is slightly different to building within Eclipse. This can be run locally by running the `build/build.bat` file that is checked out with the client.
* The Tycho build also runs the unit tests
* Jenkins additionally runs CheckStyle and shows a fail build if there is an increase
* Jenkins builds will bundle the JRE with the client. The version of the JRE bundled is located at `\\isis\inst$\Kits$\CompGroup\ICP\ibex_client_jre`. This should be updated occasionally.
* If successful The builds are output to `\\isis\inst$\Kits$\CompGroup\ICP\Client`, including an installer.

### genie_python

genie_python gets built and put at `\\isis\inst$\Kits$\CompGroup\ICP\Client\genie_python`. There is a batch file to do the installation.

## Setting up a Pipeline Build

Pipeline builds are created by adding a Jenkins file to you root directory and then pointing Jenkins at your repository.

### Jenkins File

Defines all the steps there is much documentation on line. Start from a previous file which does something similar and edit. Here is an example [in the ibex gui](https://github.com/ISISComputingGroup/ibex_gui/blob/master/Jenkinsfile). In it the label is the label of the node on which it is to run. The labels are set by editing the node configuration in jenkins.

Once this is set up create a new pipeline build in Jenkins.
 
1. In jenkins click "New Item"
2. Name the project and select Pipeline
3. Under pipeline from SCM select `Git`
    1. Then add the repository url in and the credentials as ISISBuildServer
    1. Set the branch if needed

This should now build.


## Setting up a Multi-branch pipeline

Jenkins Multi-branch Pipeline project type enables you to implement different Jenkinsfile for different
branches of the same project. Additionally, we can make Jenkins to only create and execute pipeline
for a specific branch.

1. Go to http://epics-jenkins.isis.rl.ac.uk/ and log in using your federal ID and password.
1. Click New Item on the top left corner of the dashboard.
1. Enter the name, select Multi-branch pipeline and click OK.
1. Add Display Name and Description (Not mandatory but would be useful)
1. Under `Branch Sources` tab click `Add source` and select `GitHub`
    1. Choose credentials User ISISBuilder
    1. Add Repository HTTPS URL (your git repo)
    1. Under `Behaviors` -> `Discover branches` select `Strategy` from the drop-down list to be
   `Exclude branches that are also filed as PRs` 
    1. Under `Behaviors` click `Add` and choose `Filter by name (with wildcards)` and fill the `Include` text field
       with `Release_*` or whatever is the release prefix for your release branch and remove the rest of the options.
    1. Under `Property Strategy`, click `Add property` and choose `Suppress automatic SCM triggering`.
1. Under `Build Configuration` tab, `Script Path` should match the name of your Jenkinsfile
1. Click Save

This will build now. To start the build again click `Scan Repository Now`

## Other

* [Jenkins trouble shooting](Jenkins-Trouble-Shooting)
* Jenkins builds use the office 365 connector plugin (https://github.com/jenkinsci/office-365-connector-plugin) to update the teams channel with build information. Examples of how this can be configured can be found in the Jenkins files of the top-level EPICS repository and the GUI repository.
There is a Jenkins Build Server located at [http://epics-jenkins.isis.rl.ac.uk/](http://epics-jenkins.isis.rl.ac.uk/).

## What is built

### Client

The [`ibex_gui`](http://epics-jenkins.isis.rl.ac.uk/job/ibex_gui_build_PRs/) build uses the `master` branch for the [IBEX GUI](https://github.com/ISISComputingGroup/ibex_gui).

The `ibex_gui_build_PRs` builds all the PRs for the `ibex_gui` branch.

For the client the Tycho build is run, which is slightly different to building within Eclipse. This can be run locally by running the `build/build.bat` file that is checked out with the client. The Tycho build builds the GUI and runs the unit tests. Jenkins additionally runs CheckStyle and some code coverage tools.

The builds are output to `\\isis\inst$\Kits$\CompGroup\ICP\Client`, including an installer.

### genie_python

genie_python gets built and put at `\\isis\inst$\Kits$\CompGroup\ICP\Client\genie_python`. There is a batch file to do the installation.






There is a Jenkins Build Server located at [http://epics-jenkins.isis.rl.ac.uk/](http://epics-jenkins.isis.rl.ac.uk/).

## What is built

### EPICS

* Builds EPICS itself and the IOCs
* Runs the unit tests for the BlockServer and the DatabaseServer
* Runs a Python script as a series of unit tests to check the units in all the EPICS db files
* If the above was successful the compiled binaries are made available at `\\isis\inst$\Kits$\CompGroup\ICP\EPICS`

### Client

* The [`ibex_gui`](http://epics-jenkins.isis.rl.ac.uk/job/ibex_gui_build_PRs/) build uses the `master` branch for the [IBEX GUI](https://github.com/ISISComputingGroup/ibex_gui)
* The `ibex_gui_build_PRs` builds all the PRs for the `ibex_gui` branch
* The Tycho build is run, which is slightly different to building within Eclipse. This can be run locally by running the `build/build.bat` file that is checked out with the client.
* The Tycho build also runs the unit tests
* Jenkins additionally runs CheckStyle and shows a fail build if there is an increase
* If successful The builds are output to `\\isis\inst$\Kits$\CompGroup\ICP\Client`, including an installer.

### genie_python

genie_python gets built and put at `\\isis\inst$\Kits$\CompGroup\ICP\Client\genie_python`. There is a batch file to do the installation.

### System Tests

The system test are set up to take copies of the other built artefacts and run GUI tests through RCPTT. They first remove the old genie_python and run `genie_python_install.bat`.

Next the EPICS build is copied over, the contents of `C:\Instrument\Settings\` and `C:\Instrument\Var\` removed and `start_inst.bat` is run. Finally the GUI is copied over, and `runner.cmd` is run to start the [RCP Testing Tool tests](System-Testing-with-RCPTT).




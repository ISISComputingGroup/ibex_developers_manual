# Manual system tests

Manual system tests should be performed as part of the release cycle and should be performed once a branch has been created. See [Creating-a-release](Creating-a-release)

1. Create a Github project to track the testing
    1. Go to [the group projects](https://github.com/orgs/ISISComputingGroup/projects?query=is%3Aopen)
    1. On the `...` menu alongside `Manual System Tests Template` select `Make a copy`.
    1. Check the `Draft Issues will be copied` checkbox
    1. Name the file as per `VXX.xx.xx Manual System Tests`
1. Choose an instrument to test on (local or remote) and install the test version
    1. Navigate to an `ibex_utils` folder (either locally or in the `ISIS_Experiment_Controls_Public` share) and pull the latest changes from git
    1. Run `installation_and_upgrade\instrument_deploy.bat`
    1. Follow the instructions on the command line interface. If you are unsure whether a step needs to performed, ask someone from the team.
    1. [DEMO only] run `create_icp_binaries.bat` in the EPICS directory. If the instrument never makes it out of "Processing" with the ISISDAE IOC throwing errors that read "CoCreateInstanceEx (ISISICP) : The system cannot find the path specified", this is how you fix it.
1. Run through the tests in the project. Set the status to `In Progress` as you start it, then `Pass`, `Fail`, `Change` as appropriate.
1. After the testing is complete review those shown on the Failures and Change tabs.
    1. If the issue can be fixed now (e.g. a documentation error) do so.
    1. If the issue doesn't need fixing, then it can be ignored.
    1. If the issue should be fixed, but requires a new release being built:
        1. Edit the title to read `FAILURE: VXX.x.x: [test title]` or `CHANGE: VXX.x.x: [test title]` as appropriate.
        1. Use the `Convert to Issue` option on the ticket and add it to the issues in IBEX. 
        1. If it's a failure and needs to be fixed immediately add it to the appropriate project boards (the PI board with the current sprint as the selected one, and the IBEX project board in the IBEX repo) with a `for release` label. 
    1. If the issue should be fixed, but can wait until the next release
        1. Edit the title to read `FAILURE: VXX.x.x: [test title]` or `CHANGE: VXX.x.x: [test title]` as appropriate.
        1. Use the `Convert to Issue` option on the ticket and add it to the issues in IBEX.
        1. Add it to the PI board with the next sprint selected.
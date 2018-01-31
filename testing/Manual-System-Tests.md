> [Wiki](Home) > [Deployment](Deployment) > Manual system tests

Manual system tests should be performed as part of the release cycle and should be performed once a branch has been created. See [Creating-a-release](Creating-a-release)

1. Create a shared spreadsheet to record test results
    1. Copy the [manual system tests template](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/testing/manual_system_tests_template.xlsx) to a shared folder.
    1. Set the spreadsheet as shared (Review -> share workbook). This means people can work on it in parallel, save to update your sheet with other peoples changes.
1. Choose an instrument to test on (local or remote) and install the test version
    1. Navigate to the an `ibex_utils` folder and pull the latest changes from git
    1. Check `instrument_deploy.bat` contains the correct version number for the current release. If so, run it
    1. Follow the instructions on the command line interface. If you are unsure whether a step needs to performed, ask someone from the team.
    1. [DEMO only] run `create_icp_binaries.bat` in the EPICS directory. If the instrument never makes it out of "Processing" with the ISISDAE IOC throwing errors that read "CoCreateInstanceEx (ISISICP) : The system cannot find the path specified", this is how you fix it.
1. Run through the tests on the spreadsheet. Each line is a test with a description which should contain actions to perform and what should happen should be noted. If that is not in the test then add what did happen/or should have happened to that test.

    - If a bug is discovered:

        1. Record it on the bugs sheet. 
        1. If you know it is ticketed then add a ticket, record the ticket number and  if it needs to be fixed for the release then add label "for release". If you are not sure then wait. 

1. After testing is done consider all bugs and decide for each whether you should:

    1. Create a ticket - if the fix is needed for this release, then append the "for release" label to the ticket.
    1. Ignore - write why it is ok to ignore this
    1. Fix - if it is a documentation error and can be fixed now.
1. Once the tests are completed, add the spreadsheet containing the tests outcome [here](Manual-System-Tests-Results).
1. Remove all test results and update the new template.

> [Wiki](Home) > [Deployment](Deployment) > Manual system tests

Manual system tests should be performed as part of the release cycle and should be performed once a branch has been created.

The test description should be read and what should happen should be noted. If that is not in the test then add what did happen/or should have happened to that test.

If a bug is discovered:

1. Record it on the bugs sheet. 
1. If you know it is ticketed then add a ticket, record the ticket number and  if it needs to be fixed for the release then add label "for release". If you are not sure then wait. 

After testing is done consider all bugs and decide whether:
1. create a ticket - if so then append the label "for release" if for this release otherwise leave
1. ignore - write why it is ignorable
1. fix - if it is a documentation error and can be fixed now.

Use the [template for system testing](testing/manual_system_tests_template.xlsx). This is not an exhaustive list: if you can think of additional tests, or improve the description of the existing ones, please feel free to improve the template.

Note that the spreadsheet has a Bugs sheet where we can take note of any bugs found during the system tests session, before actually creating tickets.

When having multiple people running system tests in parallel we have found it useful to move the spreadsheet to a shared Google Sheet, so that multiple people can update it at the same time.

Once the tests are completed, please add the spreadsheet containing the tests outcome [here](Manual-System-Tests-Results).
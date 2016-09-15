> [Wiki](Home) > [Deployment](Deployment) > Manual system tests

Manual system tests should be performed as part of the release cycle and should be performed once a branch has been created.

If a bug is discovered:

1. Create a ticket (if there isn't one already)
1. Decide on how important/easy to fix this bug is
    1. If it is can be fixed for this cycle append the label "for current release"
    1. If it can not be fixed then add this bug to the release notes under Known Bugs

Use the [template for system testing](testing/manual_system_tests_template.xlsx). Note that the spreadsheet has a Bugs sheet where we can take note of any bugs found during the system tests session, before actually creating tickets.

When having multiple people running system tests in parallel we have found it useful to move the spreadsheet to a shared Google Sheet, so that multiple people can update it at the same time.

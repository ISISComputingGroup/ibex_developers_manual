# 2021-10-28

## Items from last retrospective

* IOC tests are better but still a bit flaky. Some fail on some servers but not others but down to only 4 failing
* We would rather not remove the failing tests but will propose a ticket to fix them
* JH has created a [ticket](https://github.com/ISISComputingGroup/IBEX/issues/6862) to avoid merge conflicts on release notes 

## Items from current retrospective

### Sprint Planning was Fast
* Likely due to good pre-planning

### Fridays/Tech-debt
* We are probably having too many of these so need to reduce the frequency
* People generally like having them for a full week but also find it hard to slot the Friday work into other things happening that week
* Could have a nominated number of points for Fridays over the whole sprint but this would be hard to manage
* It's hard to make it a "fun day" when remote and spread over a week
* ACTION: KB will think about ways to make it more fun

### Moving configs from control-svcs
* ACTION: DO to create [ticket](https://github.com/ISISComputingGroup/IBEX/issues/6863)

### Managing Squish License
* ACTION: LC to make spreadsheet to manage who has the license (is set up on teams)
* Discussed restarting the server every night but this will kick the CI off so will not do it
* There are instructions on the wiki for how to restart the license server if someone has taken the license
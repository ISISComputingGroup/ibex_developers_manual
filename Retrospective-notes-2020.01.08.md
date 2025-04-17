### Losing track of requirements

Some requirements of the system, especially those which are older might only be held in the memories of developers rather than written down. 

We concluded that all requirements must be covered with system tests. This would prevent any more requirements from only being honoured by the developers who know them.

To make sure that we haven't dropped any requirements, we should go through the IBEX requirements document (~70 pages) and use this to generate more system tests. We should not do this all at once.

### Statistics on sprints

It would be useful to see the stats on how many points we have completed in the previous sprint before the review.

These statistics are already made as part of managing the IBEX project. What would be distributed would probably be the number of completed tickets at the point the report was compiled.

### Do we list the support systems in the release schedule?

Some of our systems, such as DEMO, have ended up with out of date software, such as SQL. Are these support systems in the release schedule and maintained appropriately?

Created a ticket to make a decision about the best approach: https://github.com/ISISComputingGroup/IBEX/issues/5072

### Dev Release Notes

We are about to make a release but the release notes are missing a lot of the changes which have been made.

We should be more careful when starting and reviewing tickets, this process is documented on the [wiki](Tickets-and-their-Workflow#movement-of-tickets) (and also many PR templates).

### Config checker and systems tests caught several bugs
There was much rejoicing 🎉
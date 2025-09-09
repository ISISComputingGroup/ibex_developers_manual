# 2019-11-06

## How to handle non-critical but serious bugs

e.g. IOC is updated to fix bug. We know it could be used on other instruments but isn't being used now. What do we do?

The procedure we decided on is documented [here](/deployment/patch/Modifying-Code-on-an-instrument)

## Stop doing 0 point tickets

0-point tickets are skewing the analysis of our capacity to get work done in the sprint.

0-point tickets are often unplanned tickets such as support.

There were 2 possibilities:

- Recalibrate the pointing system to be sensitive and not include 0 points
- Allocate a block of points to multiple tickets that would be 0 points e.g. 5 points to support

We have decided on the first (recalibration). It has been noted it will take 3 to 4 sprints until we have calibrated ourselves to work with the new points system.

We need to understand that the points count for when a ticket is started to when it is truly finished and in the complete column.

Because the points system is now more sensitive to smaller tickets it means that we will get tickets with very high points. This highlights our need to split tickets more carefully, which is something we need to work on. It has also been noted that some tickets (e.g. writing an IOC) do not make sense to split. We need to be careful with how we handle these.

## What is our process for reviewing support tickets? Should we have a designated support reviewer as a helper to the person on support?

This question was noted because at one point there seemed to be a lot of support tickets in review that seemingly weren't being reviewed quickly enough.

Using the flash review process is recommended for support tickets that are small enough.

It has been noted that we could have a support reviewer that is responsible for ensuring support tickets are reviewed throughout a cycle, though no plan was put in place to do this.

It has also been noted that most people do, but that we should ensure when we finish a ticket and move onto a review, that review should be of the same complexity as the ticket we have just finished or we should do multiple reviews to match the complexity.

## We seem to sometimes have reflectometry, pending tasks and HIFI tickets on the IBEX board. Is this deliberate? We don't point and prioritize them the same, should they be on their own boards and not the IBEX board?

These tickets are also contributing to IBEX so should be in the IBEX board and pointed accordingly as well as their own board. Their own board is more used to track the progress of the sub-project.

Having these tickets in the IBEX board helps people working in those sub-projects to remain aware of what needs to be reviewed etc.

We should remove the review column from the reflectometry board.

## In sprint retrospective should we quickly discuss our progress on the last retrospectives notes and plans?

Yes.
 
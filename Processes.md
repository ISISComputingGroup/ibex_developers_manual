Various Processes for Tasks and quick info into how they should work

## What to do when you need to fix something on an Instrument

1. Fix the bug
1. Record the bug as a ticket; with solution done
1. Note the bug next to the instrument on the main IBEX page
1. If the bug is likely to effect other instruments inform the icp team using the group email
1. If the bug will seriously effect instrument scientists consult the PM

## Ticket Types

wf - means workflow and is how waffle decides on which column the ticket is in

Type   | Meaning
------ | -------
**awaiting** | Tickets where it is hard to determine when they will be done because they are awaiting hardware, access etc. These tickets should be left on the backlog and pulled into the current sprint when ready. **Not the same as impeded**.
**bug**    | A bug in the system reported by either a user or developer
**# (number)** | Estimate on how long in story points the ticket will take to develop not including review time
**rework** | Ticket has been through at least one review (with *ready* developer has changes to make, with *in progress* developer is working on it, with *review* developer has finished changes and they need re-reviewing
**under review** | Ticket is currently being reviewed
**urgent** | Ticket is urgent and should be rushed through the system
**wontfix** | Ticket will not be fixed, it is not needed or too complicated.
**duplicate** | Ticket is a duplicate of a different ticket and will not be fixed (usually other ticket is referenced)
**for current release** | Ticket is needed for the current release and should be prioritised (allows us to keep track of whether a release can be made)
**proposal** | It is proposed that the ticket should be in the next sprint (removed each sprint)
**ready (wf)** | Ticket is in the current sprint and can be worked on
**in progress (wf)** | Ticket is currently in progress
**review (wf)** | Ticket is done and should be review by someone
**completed (wf)** | Ticket is complete
**impeded (wf)** | Ticket is in progress but can not be completed because of something else. Reason for impediment should be added to the ticket. This should not be for long.
**fixed (wf)** | Ticket has been fixed (added at end of sprint only and by the person running the sprint)

## Creation of Tickets

Tickets should be created at need by developers as git issues using the waffle board. Initially they should *not* have a milestone attached to them unless they are needed for a definite date and this is the LATEST that they could possible be started. If you are doing this ensure that there is enough time for testing; bugs fixing etc. If the ticket is created for a scientist don't forget to note this in the ticket.

## Backlog Pruning

Before the backlog pruning meeting people should add the 'proposal' label to tickets they would like to see in the next sprint; all the tickets that must be in and a maximum of 2 per person. At the meeting we will look at these tickets as a priority and as many newly created tickets as we can. 'proposal' label will then be added or removed depending on the general consensus.

Filter for proposed tickets `is:open label:proposal`

Filter for other tickets `is:open -label:proposal -label:"in progress" -label:"ready" -label:"review" -label:"completed" -label:"impeded"`

## Sprint Planning

At sprint planning we will *only* look at tickets with 'proposal' label. These will be selected in and added to the ready column or milestone; estimates will be added. These will then be looked at to slim down to the number of points we usually manage in a sprint. After sprint planning all 'proposal' labels will be removed from all tickets.

## Movement of Tickets

Developers should pick up a ticket as close to the top of the Ready column as they can (i.e. don't pick a ticket assigned to someone else). Assign the ticket to yourself and move it to in progress. When the ticket is done move it to the top of the review column (unless it is high priority in that case move it to the bottom). Then pick a ticket to review from the bottom of the review column. Review the ticket and move it either to the review complete or add the rework label and move it back to the top of the ready column (it is a courtesy to inform the person you have done this).

## Adding tickets Mid Sprint

If you are adding a ticket to the ready column mid sprint. Please make sure it is added in priority order with estimates attached and unless there is a good reason clear it at standup.

## Regular Demos of IBEX to Scientists

The regular 4-week Sprint Review is not the ideal forum for demonstrating new developments in IBEX to scientists. Instead, we will demonstrate each new release of IBEX prior to its deployment to groups of instrument scientists (or, when appropriate, to individual instrument scientists).  Demos will be arranged as follows:
1. Developers pair off to demonstrate IBEX to each group of instrument scientists.  
1. One member of each pair takes the initiative to contact the scientists to arrange the demo.  
1. Ideally, arrange the the demo to happen out of cycle and near the end of a sprint (that’s what is most convenient to both scientists & developers), but demos can be held at other times, if necessary.
1. Choose a convenient location to perform the demo (e.g. in the instrument cabin or a scientist's office (if there is room), or a meeting room)
1. Demo all the changes since the last release (or previous demo), with emphasis on those items of most relevance to the instrument
1. Gather and share feedback (e.g. on instrument wiki pages)

Over time we can change the pairs, so that everybody gets exposed to different instruments & instrument scientists.

Use the [sprint/release demos](https://github.com/ISISComputingGroup/IBEX/wiki/Timetable-for-sprint-demos) page to plan each round of demos..

## Friday Quality Time

Developers like quality time, on Friday afternoon a developer may choose max 2 ticket that can be completed in a couple of hours. Good candidates are 0 time tickets from the backlog. NB These tickets are not a priority it is just for fun :-)

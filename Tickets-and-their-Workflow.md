> [Wiki](Home) > [Processes](Processes) > [Tickets and their Workflow](Tickets-and-their-Workflow)

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
**support** | Ticket has been generated in response to a support issue for an instrument scientist or instrument problem. These are unscheduled and reactive tickets, but it is useful to keep track of time spent.
**wontfix** | Ticket will not be fixed, it is not needed or too complicated.
**duplicate** | Ticket is a duplicate of a different ticket and will not be fixed (usually other ticket is referenced)
**for current release** | Ticket is needed for the current release and should be prioritised (allows us to keep track of whether a release can be made)
**proposal** | It is proposed that the ticket should be in the next sprint (removed each sprint)
**training** | Ticket is easy and not urgent, therefore suitable for new starters
**motion control** | Ticket may be of interest to the motion control hardware team. Tickets are relevant if they change how we interact with a motion control device or change the workflow for commissioning motion
**ready (wf)** | Ticket is in the current sprint and can be worked on
**in progress (wf)** | Ticket is currently in progress
**review (wf)** | Ticket is done and should be review by someone
**completed (wf)** | Ticket is complete
**impeded (wf)** | Ticket is in progress but can not be completed because of something else. Reason for impediment should be added to the ticket. This should not be for long.
**fixed (wf)** | Ticket has been fixed (added at end of sprint only and by the person running the sprint)

## Creation of Tickets

Tickets should be created at need by developers as git issues using the waffle board. Initially they should *not* have a milestone attached to them unless they are needed for a definite date and this is the LATEST that they could possible be started. If you are doing this ensure that there is enough time for testing; bugs fixing etc. If the ticket is created for a scientist don't forget to note this in the ticket.

## Backlog Pruning

Before the backlog pruning meeting people should move tickets to the 'proposal' column they would like to see in the next sprint; all the tickets that must be in and a maximum of 2 extras per person. At the meeting we will look at these tickets discuss what they are and then rank their importance.

Filter for proposed tickets `is:open label:proposal`

Filter for other tickets `is:open -label:proposal -label:"in progress" -label:"ready" -label:"review" -label:"completed" -label:"impeded"`

## Sprint Planning

At sprint planning we:

1. Look at any newly propose tickets and rank them
2. Estimate the top ticket on the list
3. Add its value to the current sprint (possibly by dragging)
4. If we have points left in the sprint go to 2

After sprint planning the ready column will be ordered.

## Movement of Tickets

Developers should pick up a ticket as close to the top of the Ready column as they can (i.e. don't pick a ticket assigned to someone else). Assign the ticket to yourself and move it to in progress. When the ticket is done move it to the top of the review column (unless it is high priority in that case move it to the bottom). Then pick a ticket to review from the bottom of the review column. Review the ticket and move it either to the review complete or add the rework label and move it back to the top of the ready column (it is a courtesy to inform the person you have done this). You must do a review when you move any ticket to the review column even if it is a rework. (A rework ticket review counts as a review).

Sometimes you may want to split a larger ticket into smaller tickets to do this see [Umbrella Tickets](Umbrella-Tickets).

## Adding tickets Mid Sprint

If you are adding a ticket to the ready column mid sprint. Please make sure it is added in priority order with estimates attached and unless there is a good reason clear it at standup.

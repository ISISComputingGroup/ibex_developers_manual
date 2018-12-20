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
**re-request** | Instrument scientist has requested a ticket and it has been request by another instrument scientist in the past. A comment should record who asked with a +1.
**Needs pair review** | If a ticket is complicated or has many changes, the ticket should be reviewed by a pair of developers not just one. This ticket can be added at any time. It may be ignored for review of rework unless otherwise stated. |
**Code Review** | Ticket that could be reviewed by a wider group in a code review session. For particularly large or unique additions. 

## Creation of Tickets

Tickets should be created at need by developers as git issues using the waffle board. Initially, they should *not* have a milestone attached to them unless they are needed for a definite date and this is the LATEST that they could possibly be started. If you are doing this ensure that there is enough time for testing; bugs fixing etc. If the ticket is created for a scientist don't forget to note this in the ticket.

## Movement of Tickets

Developers should pick up a ticket as close to the top of the Ready column as they can (i.e. don't pick a ticket assigned to someone else). 

1. Assign the ticket to yourself and move it to in progress. 
2. When the ticket is done.
    - Create a pull request
    - If the config needs updating either:
        - Add a change to the config updating script (usually if it effects multiple config/instruments)
        - Add a step to the upgrade script (usually when it is a simple change which effects a single instrument)
        - Go onto the instrument and add the change (be *very* sure it will not effect anything)
    - Add summary to the [Dev Release Notes](https://github.com/ISISComputingGroup/IBEX/wiki/ReleaseNotes_Dev) in the section `Changes in software but still on a branch`.
    - Move the ticket to the top of the review column (unless it is high priority in that case move it to the bottom). 
3. Pick a ticket to review from the bottom of the review column. Review the ticket and move it either to the review complete or add the rework label and move it back to the top of the ready column (it is a courtesy to inform the person you have done this). You must do a review when you move any ticket to the review column even if it is a rework. (A rework ticket review counts as a review).
4. If changes are merged into master, add the ticket to the [Dev Release Notes](https://github.com/ISISComputingGroup/IBEX/wiki/ReleaseNotes_Dev).

Sometimes you may want to split a larger ticket into smaller tickets to do this see [Umbrella Tickets](Umbrella-Tickets).

## Adding tickets Mid Sprint

If you are adding a ticket to the ready column mid sprint. Please make sure it is added in priority order with estimates attached and unless there is a good reason clear it at standup.

## Meeting where we manipulate tickets

    - [Backlog Preperation](Backlog-Preperation)
    - [Sprint Review](Sprint-Review)
    - [Sprint Planning](Sprint-Planning)
    - [Sprint Retrospective](Sprint-Retrospective)

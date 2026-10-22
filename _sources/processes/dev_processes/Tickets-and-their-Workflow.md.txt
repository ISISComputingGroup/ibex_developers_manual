# Ticket workflows

## Ticket Types

wf - means workflow and is how the IBEX Project Board decides on which column the ticket is in

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
**duplicate** | Ticket is a duplicate of a different ticket and will not be fixed (usually the other ticket is referenced)
**for current release** | Ticket is needed for the current release and should be prioritised (allows us to keep track of whether a release can be made)
**proposal** | It is proposed that the ticket should be in the next sprint (removed each sprint)
**training** | Ticket is easy and not urgent, therefore suitable for new starters
**motion control** | Ticket may be of interest to the motion control hardware team. Tickets are relevant if they change how we interact with a motion control device or change the workflow for commissioning motion
**ready (wf)** | Ticket is in the current sprint and can be worked on
**in progress (wf)** | Ticket is currently in progress
**review (wf)** | Ticket is done and should be review by someone
**completed (wf)** | Ticket is complete
**impeded (wf)** | Ticket is in progress but cannot be completed because of something else. The reason for impediment should be added to the ticket. This should not be for long.
**fixed (wf)** | Ticket has been fixed (added at end of sprint only and by the person running the sprint)
**re-request** | Instrument scientist has requested a ticket and it has been requested by another instrument scientist in the past. A comment should record who asked with a +1.
**Needs pair review** | If a ticket is complicated or has many changes, the ticket should be reviewed by a pair of developers, not just one. Ideally one of the reviewers will already be familiar with the affected area of the code (to help with knowledge sharing). This label can be added at any time. It may be ignored for review of rework unless otherwise stated. |
**Code Review** | Ticket that could be reviewed by a wider group in a code review session. For particularly large or unique additions. 
**Bucket** | Items that were proposed in the last proposal round, but were not high enough priority to make it into the sprint. If tickets in ready run out, these tickets should be picked up in preference to other tickets in the backlog. <br> If a "bucket" ticket is required in the next sprint, then add a `proposal` label before the bucket label is removed at the end of the current sprint.
**no_release_notes** | Items that do not need associated release notes, such as minor tasks that do not affect the code base.

## Creation of Tickets

Tickets should be created at need by developers as git issues using the IBEX Project Board. Initially, they should *not* have a milestone attached to them unless they are needed for a definite date and this is the LATEST that they could possibly be started. If you are doing this ensure that there is enough time for testing; bugs fixing etc. If the ticket is created for a scientist don't forget to note this in the ticket.

When creating a ticked put on appropriate labels. When adding a 'Proposal' label, also add the ticket to the 'Planning' project in 'Proposals' column.

## Movement of Tickets

Developers should pick up a ticket as close to the top of the Ready column as they can (i.e. don't pick a ticket assigned to someone else). 

1. Assign the ticket to yourself and move it to in progress. 
2. When the ticket is done.
    - Create a pull request. If the pull request is in a public repository the PR size bot will automatically assign a label to it based on the number of lines changed. For details see https://github.com/noqcks/pull-request-size#sizing . Note that these labels are purely informational for other developers and do not form part of the sprint process (in particular, they are not related to ticket sizes in any way).
    - If the config needs updating either:
        - Add a change to the config updating script (usually if it affects multiple config/instruments)
        - Add a step to the upgrade script (usually when it is a simple change which affects a single instrument)
        - Go onto the instrument and add the change (be *very* sure it will not affect anything)
    - Create a **pull request** modifying the release notes for the next release.
        - Edit the file using instructions included on the page (Change types are explained near bottom of the page)
        - Save your changes to a branch under same name as your ticket changes branch and add pull request
        - Include link to your ticket in pull request description
        - Link up your pull request in the ticket as a comment. It is helpful for the reviewer to have a comment clearly listing all of the relevant pull requests and documentation changes, including release notes, that they should review.
    - Try to get an informal review to check for glaring problems.
    - Either on the ticket under the Projects section use the drop-down menu to move the ticket to the review column or manually move the ticket to the bottom of the review column (unless it is of high priority, in that case, move it to the top). 
3. Pick a ticket to review from the top of the review column. Review the ticket and if it is good close it (this will move it to the review complete) and add the complete label. If it needs work then add the rework label and move it back to the top of the ready column (you should inform the assignee that it is back in rework so they know how to prioritise their work). You must do a review when you move any ticket to the review column even if it is a rework. (A rework ticket review counts as a review).
4. Make sure to check the associated [upcoming release notes](https://github.com/ISISComputingGroup/IBEX/blob/master/release_notes/ReleaseNotes_Upcoming.md) PR makes sense and merge it.

Sometimes you may want to split a larger ticket into smaller tickets to do this see [Umbrella Tickets](Umbrella-Tickets).

## Flash reviews

Some work is very small and doesn't warrant a full ticket and process e.g. fix a code comment, fix trivial Makefile error stopping build working. Such changes should have no potential side effects and take ~5 minutes to review. The procedure is:
* create a PR
* post PR into the flash-reviews Teams channel
* we are using emojis to indicate status and avoid creating a new line that a reply/comment would. We don't want tickets disappearing off the top of the screen. The emojis to use are:  
  * when somebody is looking at it, they add a "surprised" emoji
  * if you are done and merged, add a "happy"
  * if it is not a flash review and needs further changes, comment on github ticket and add a "sad" face
    
## Adding tickets Mid Sprint

If you are adding a ticket to the ready column mid-sprint. Please make sure it is added in priority order with estimates attached and unless there is a good reason clear it at standup.

## Meeting where we manipulate tickets

- [Program Increment Planning](../meetings/Program-Increment-Planning)
- [Backlog Preparation](../meetings/Backlog-Preparation)
- [Sprint Planning](../meetings/Sprint-Planning)
- [Sprint Review](../meetings/Sprint-Review-and-Retro)

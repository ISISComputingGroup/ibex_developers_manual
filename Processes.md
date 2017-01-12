Various Processes for Tasks and quick info into how they should work

## Ticket Types

wf - means workflow and is how waffle decides on which column the ticket is in

Type   | Meaning
------ | -------
bug    | A bug in the system reported by either a user or developer
# (number) | Estimate on how long in story points the ticket will take to develop (no review)
rework | ticket has been through at least one review (with ready developer has changes to make, with inprogress developer is working, with review developer has finished changes and they need reviewing
under review | ticket is currently being reviewed
urgent | ticket is urgent and should be rushed through the system
wontfix | ticket will not be fixed 
duplicate | this ticket is a duplicate of a different ticket and will not be fixed (usual other ticket is referenced)
fixed | Ticket has been fixed (added at end of sprint only)
for current release | Ticket is needed for the current release and should be prioritised (allows us to keep track of whether a release can be made)
proposal | It is proposed that the ticket should be in the next sprint (removed each sprint)
ready (wf) | ticket is in the current sprint and can be worked on
in progress (wf) | Ticket is currently in progress
review (wf) | Ticket is done and should be review by someone
completed (wf) | ticket is complete
impeded (wf) | ticket is in progress but can not be completed because of something else. Reason for impediment should be added to the ticket. This should not be for long.

## Creation of Tickets

Tickets should be created at need by developers as git issues using the waffle board. Initially they should *not* have a milestone attached to them unless they are needed for a definite date and this is the LATEST that they could possible be started. If you are doing this ensure that there is enough time for testing; bugs fixing etc.

## Backlog Pruning

Before the backlog pruning meeting product champions should add a 'proposal' label to tickets they would like to see in the next sprint. At the meeting we will look at these tickets as a priority and as many newly created tickets as we can. 'proposal' label will then be added or removed depending on the general consensus. (Do we need a scientist propose flag too so these don't get lost?).

Filter for proposed tickets `is:open label:proposal`

Filter for other tickets `is:open -label:proposal -label:"in progress" -label:"ready" -label:"review" -label:"completed" -label:"impeded"`

## Sprint Planning

At sprint planning we will *only* look at tickets with 'proposal' label. These will be selected in priority order and added to the ready column. Estimates will be added (should we start estimating in half days to avoid the 0.5 problem?). After sprint planning all 'proposal' labels will be removed from all tickets.

## Movement of Tickets

Developers should pick up a ticket as close to the top of the Ready column as they can (i.e. don't pick a ticket assigned to someone else). Assign the ticket to yourself and move it to in progress. When the ticket is done move it to the top of the review column (unless it is high priority in that case move it to the bottom). Then pick a ticket to review from the bottom of the review column. Review the ticket and move it either to the review complete or add the rework label and move it back to the top of the ready column (it is a courtesy to inform the person you have done this).

## Adding tickets Mid Sprint

If you are adding a ticket to the ready column mid sprint. Please make sure it is added in priority order with estimates attached. If you can get someone to read it to make sure it makes sense.

## Friday Quality Time

Developers like quality time, on Friday afternoon a developer may choose a ticket that can be completed in a couple of hours. Good candidates are 0 time tickets from the backlog. NB These tickets are not a priority it is just for fun :-)

# Discussion

## Creation of tickets
[KB] Would a flag specifying firm date be a better option, and specify the date in the ticket? If it is needed during a cycle then we might have a firm date, the date of the experiment, but really want to complete it in time for a release if at all possible, which might be a little while earlier.
[JH] Like it I say yes, if noone objects i will do this after the current sprint.

## Backlog pruning
[KB] I'm not sure a scientist propose flag is necessarily required, and could lead to a false priority based on "a scientist asked for that" compared to "a developer put that in to enable this new beam line to come on line"
[JH] Unsure about this.

## Sprint Planning
[KB] Is the suggestion here to work in units of half a day rather than days? So double all our standard estimates? I think I'm inclined to say yes, that isn't a bad idea, but I'm not sure what that would do to the calculations for availability

# 2019-10-09

## How do we know if we're using flash reviews too much? Is it a problem?

Flash reviews are for small and/or urgent changes.

Before asking for a flash review we should consider the size and urgency of the change.

When we flash review we are still adding code to the codebase no matter how small, thus our reviewing should be as rigorous and considered as normal reviews.

This rigour does not take away from the benefit of flash reviews as our process (using the slack channel) brings it to the attention of people quickly and allows us to skip the normal movement of tickets in the project board etc. meaning it is still faster.

We seem quite happy with our flash review process, but we should still be careful to not overuse it by carefully choosing when to ask for a flash review or not.

## Is the review column ordering obvious and understood?

The simple answer is no.

People had mixed ideas about how we were meant to be ordering the column.

Further to this, the ordering was inconsistent with the ready column and the new GitHub projects tool for moving tickets between columns inside the ticket puts the ticket at the bottom of the column (contradictory to our current process).

We have decided to flip the ordering so that we insert tickets into the review column at the bottom and take tickets from the top.

This makes our workflow consistent with our ready column and the GitHub tool.

## Is it useful to log "extremely" quick support issues?

Pros:

- Allows the person working on the support issue to solidify the issue further in their mind
- Allows the sharing of information and creation of a dialog about the support issue
- Allows us to refer back to information on past support tickets that occur again
- Creates a process where we can easily understand what has happened and review any changes that are to be made

Cons:

- Possibly wastes times of the person working on the support issue if it is very simple
- Some issues are ongoing so the ticket may stay around for a while and clog up the board
- Often a support issue is a repeat of other support issues so we are repeating our logging of information in new tickets when we do not need to

Ideas and answers:

- Support issues should have tickets for the pros listed above
- We are creating a new project board for support tickets so they do not clog up our development board
- Discussed: Having a process in a support board or other board for common support issues so we do not need to repeat the logging and can simply add a "+1" to it
- Suggestion: A review of a support ticket should include checks for whether the relevant information has been added to FAQs, troubleshooting or other parts of the user manual

## What do people think of the new "Pending Tasks" board?

The board is very useful for time-sensitive tasks and is good for workflow management.

A couple of people thought the name was not representative of the use case of the board.

### Sub-discussion: Why are tickets referenced on the board with a note and not simply the ticket itself?

We wanted to add the time to the ticket so the answer was to reference them and add the date as a note.

We decided that if the ticket is on the pending tasks board we should add the date to be done on/by to the name of the ticket, as in "ticket-land" we would not necessarily know that the ticket is time-sensitive.

## Our builds/system tests have failed because the db unit checker reports a bad db that has just been pushed

It shows that our continuous integration is doing its job at least partly.

We should have a process that stipulates of running the db units checker on our code before we merge a pull request.

Ideas:

- Have this on a git hook (there is a Friday ticket for this already)
- This should be on the reviewer's checklist when reviewing tickets on EPICS-ioc

## Our system tests are unhappy, this makes us unhappy

Having all these tests tangled up it is very difficult to know when a bug or problem has been introduced into the codebase by accident. We would like to be able to turn up and say "The system tests are failing which isn't like yesterday so what's been added to the codebase since then". 

First step: Work out why our tests are failing! 3 tickets should be made (one for each system tests pipeline) to review why this is happening.
Second step: Once we know why we should make a plan to improve our system tests and actively work on 

Also noted: If we could finish the parallelisation of the system tests they would be easier to run on our machines so understanding why one has failed would become easier. This would, however, increase the complexity of the system tests so it could possibly cause more issues.

## Should we prioritize reworks in the ready column?

Yes, for definite.

When we have done a review and set it for rework we should tell the assignee that we have done so. They can then prioritise their work accordingly.
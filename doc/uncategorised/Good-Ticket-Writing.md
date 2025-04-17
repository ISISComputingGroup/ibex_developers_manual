# Purpose of this guide
This description of the process is aimed to help improve communication, rather than be followed with no consideration as to what is needed for the members of the group to flourish, please edit it as required.

# Parts of a ticket

## Title
This should be a succinct representation of the content of the ticket.
Where there is a logical grouping of themes, using a `Keyword: Title` format can make it easier to find related tickets without having to create umbrella tickets

## User Story
This is *why* the work needs to be done, and for *whom*.
It will be centred around an actor who is part of the process, whether that is a user, developer, someone providing support, someone with a role will have a need and the story should highlight who has that need.
It should state what needs to happen, along with the justification of why it needs to work that way.

As a role/method of interacting with the system, I want it to behave in this way, so that something does/doesn't happen.

This should amount to a requirement, one or two lines at most.

## Acceptance Criteria
This is how we define **done**, so this is *the outcome* or *what* we need to achieve. Reading this set of checkboxes it should be easy for a developer or a reviewer to be able to say "yes it does that". These need to be clear. There should also be as few of this as is practical to match the user story. 
## Notes
This is a good place to provide extra context, who to talk to, what might impact this work and similar. This is extra information

## Design/Details
This is an aspect that is usually not included, but may be of benefit to people with less experience and knowledge of the codebase and ways of working within a team.
It is described as not included as some developers do provide this level of detail at times. (e.g. https://github.com/ISISComputingGroup/IBEX/issues/1208 gave great detail of the changes that were needed for that work). As has happened in some places, comments can be added to detail more of the technical specification, including command sets, UI designs, and so on.
Because these can be more proscriptive than just an acceptance criteria (this would be *how* to do it, not just describing when it is done) care should be taken as to when this section is included so that it does not stifle creativity or limit the approach to be taken. However, it can make the difference between being able to look at something and undertake it with confidence, or not, as well.

# Random Example

## Title
Coffee Meeting: Take a cup of black instant coffee with me
## User Story
As someone attending a coffee meeting I want a cup of black instant coffee to take with me so that I have something to drink during the meeting.
## Acceptance Criteria
- [ ] There is a cup of black coffee available for me to take
## Notes
- The nicest kettle is in the kitchen by the meeting room
- The clean mugs are usually in the cupboard over the sink
- It may be worth double checking which brands are available so that something can be brought in if necessary
## Design/Details
1. Check to see if there is a suitable coffee brand in that kitchen the day before, if not bring some from home
2. 10 minutes before the meeting head off to the meeting room to have 5 minutes to make the coffee before the meeting once you get there, as the nicest kettle is in that kitchen
3. Fill the kettle to either the min level or to the number of people wanting to use it, this can't be predicted before arriving there
4. Whilst the kettle boils, get a mug from the cupboard, and put a teaspoon of coffee powder in it
5. Once the kettle has boiled, add water to the mug and stir
## How it maps to the purposes of each section
Title: If you know what you are doing it is enough to meet the acceptance criteria
User Story: This clarifies who, and why, it's someone attending the meeting, and they want to have something drink with them
Acceptance Criteria: This is clear, there is either a cup of coffee or there isn't, Schrödinger's Coffee is not an experiment worth conducting in this scenario.
Notes: Some extra context and information
Design/Detail: This is not at so low a level that there is no room for creativity, and it assumes some knowledge that should be straightforward enough for the majority of people. But, it does specify enough that someone who has never done this before has at least a good chance of succeeding when combined with the notes as that specified which cupboard.

# When to add Design/Details
This will vary based on the task and scenario.
Sometimes that design/detail will be in other documents, and they could be referenced, especially for new items where interfaces have probably been discussed in greater detail.
If there are new team members this can be a benefit to them, as it breaks apart the system/architecture design side from the developer side.
If there are no other clear requirements anywhere, such as with some of the reverse engineering that has been undertaken in the past. That way the ticket has the history, but the wiki can stay rooted in the present.
It could be added before the ticket is considered at all by the team, but it might also be something to add after prioritisation in certain situations.

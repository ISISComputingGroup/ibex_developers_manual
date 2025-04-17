# Retrospective Notes 17/11/2021

| Chair      | Timekeeper | Note Taker |
| :--------   | :---------: | ----------: |
| [@JackEAllen](https://github.com/JackEAllen) | [@daryakoskeroglu](https://github.com/daryakoskeroglu) | [@Adam-Szw](https://github.com/Adam-Szw) | 

--- 

## Items from last retrospective

### Next Sprint will include a FRIDAY

### Timekeeper also moderates voting room
We didn't get to test it yet. We should try this at the next opportunity.

### Move some documentation into repos as to wiki?

### Large backlog of reviews this sprint a sign of insufficient training or other barriers?
We made some effort to increase amount of reviews coming through, especially among junior team members.
As we are making effort towards adding more of 'how to review' instructions to our tickets, we need
to keep in mind not to post any security risks that come with having our project be a public repository. These
could for example include IP addresses, device names etc.

### Implement repository linters to remove code format and styling from review process.

###  Use Squish only for reviews during last week of sprint
Mutual agreement that during the final week of a sprint, the squish license should be used primarily for reviews only. The priority of squish license usage during the final week of a sprint can be prioritised as:
- High: Reviews
- Medium: Reworks
- Low: New work

We tried to follow this ruleset during this sprint and it seems to have worked. We agreed to keep this in place.

### The office mic is barely legible for stand-up, is there a better solution we could use?
This issue hasn't been dealt with yet.

### Would everyone be interested in organising a secret Santa this year to get us in the festive mood?
We did the secret santa and the team enjoyed it. We are yet to organize a new year's meal.

---

## Items from current retrospective

### Centralise the snag lists to the IBEX project sharepoint
These are generally not as readily visible as the projects etc. are in GitHub

### Apart from trying to be organised next time and realise in better time when it isn't worth having a pre-planning meeting, are we happy with not having one when it feels unhelpful?
Considering how this is a rare situation, we agreed that the best way to deal with it will be asking this question at the end of the standup, so that people can have an opportunity to voice their opinions on this.

### This keeps getting brought up, but I think we should have a 'cull' of icp-write members for the sake of security in case anyone's GH account is compromised and they are difficult to reach
For the security reasons we agreed to:
- Everyone should make sure that they are using 2-factor authentication on Github
- We might want to look into removing members who have not been on the project for a long time

### Start over the rotas in the new year
We decided to go for it as nobody had an issue with that

### Some new members of the team have trouble merging branches on various repositories due to lack of permissions

### What is the best way not to forget to update submodules - should `EPICS_repo_checks` post a message to Teams on failure?
- We decided not to add message on teams.
- We might consider adding checks or 'todos' in the templates to remind people.
- Optionally we could add a pre-commit message check.

### When adding new sections or editing existing sections of the wiki, I would like descriptions to be as verbose as possible to be more accommodating to new members within the team
We can make things more verbose where we can, but we have to look out for possibility of duplicating information. Where it exists, we should favour linking other pages rather than keeping extensive amounts of information on one page.
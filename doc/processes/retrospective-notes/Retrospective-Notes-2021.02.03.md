# 2021-02-03

## Items from the retrospective before last
### Email template
- now done

## Items from last retrospective

### Friday tickets not being reviewed quickly enough, true for general tickets too.  Reviews should take precedence over rework, especially towards end of sprint. 
#### Suggestion to have Monday morning for reviews to save context switching between consecutive work days.  Developers should at least self-assign tickets to be reviewed at this time.
- Seemed to work pretty well but not everyone is always available on Mondays to do reviews
- Ended up with a lot in review because we had quite a lot of things under review
- throughout the sprint there were a lot of plateaus in the burndown chart - could be to do with interviews etc. By the end of the sprint we were quite above the line
- the dips on the burndown chart are Mondays so it must be working
- Sprint was in January - quite a lot of things that are out of our control, dark and dingy and not really able to get out much. Given the circumstances we think we did the best we could and the Monday review slot proved to be effective 

### Friday "sprint" went well and was enjoyed on the whole.  Other ongoing tasks did get in the way of people taking on a specific Friday ticket.
- it was

### Discussion about shorter sprints to concentrate on specific matters (c.f. mantid tidy-up week) "Technical Debt Sprint"?  Decided not realistic in cycle, but more likely in longer shutdowns.
- beginning of long shutdown maybe we'll do a technical debt sprint

## Items from this retrospective

### We have a number of tickets that are effectively "tidy up hotfixes". Can we have a sprint focusing on this at the start of the long shutdown? 
- would be nice to get them more properly fixed 
- there are some things we did very quickly last year, it'd be good to look at those again. 
- long shutdown probably isn't the right time as they're not that important, perhaps this shutdown would be better? 
- list will be made for these tickets

### Suggestions for streamlining planning a bit more:

- when we decide a ticket is high priority, leave it in the "proposal" column initially (just move medium/low out). we can then sort it directly into the right place in high later on
- maybe we should do away with "bottom of high column" tickets. we never get to the bottom of high. just put it in medium and save ourselves some time when we order them
  - or just make an effort to change our thinking so low is low, medium is medium and so on. Bottom of high should really be in medium. 
- when the contractors leave we could think about how effective we are doing planning - it goes on for a long time
- we should see if priority can be done using planning poker on the new poker site as this might be a bit fairer


### We should update all the Zoom invitations for all our sprint meetings - Daily Stand-Up, Planning, Pre-Planning, Review & Retrospective - to have Alternative Hosts.  That way, we don't have to create a new meeting just because the person who created the original meeting invitation isn't around.
- need to confirm this works on zoom - the issue is somebody being in another meeting they have scheduled and zoom will not let you have two meetings you have created running at the same time. The docs suggest an alternative host can start a meeting if "join before host" is not enabled
- we'll test it out

### record of systems time
- Have been trying to feed systems tickets from tasks through the project board to keep some form of review possible.  Generally it is a case of creating a controls ticket which contains non-public system details and then encapsulating it into an IBEX ticket with a reference.  This means that it can be reviewed and passed along though the IBEX board.  Currently, it is not possible for me to add an estimate of the time taken to do the ticket as a label other than zero (I think with training) without it breaking the more strict conventions of the IBEX project point checks.  
  - We could add a few more generic systems labels.  in blue, say, which are "1/2 day", "1 day", "2 days" etc. or possibly put the detail in the ticket title e.g. "Clone a new instrument machine (1 day)".  This is more of a historic reference - or these points could be added to the control systems ticket in the conventional way - but they may be a bit less visible on the IBEX project board.  The systems tickets are very often incremental and can be re-done regularly as a process so this is less attractive - although it could be a guide to the time to run the whole ticket once.
  - we could have a separate private repository and a label for them, the tickets in IBEX could point to the private repo. The point of this is so that it can be put on the IBEX project board


### if there is a support ticket which doesn't involve any code changes there is not likely to be much in the way of a sensible release note for the users
- we could simply check the label for "support" and skip the release note mechanism 
- alternatively, only generate a release note request if someone makes a pull request and not from the ticket itself

### I like the new release note PR system, should we always change the PR title to be "Ticket YYY: <paste ticket title>" rather than have "Update ReleaseNotes_Upcoming.md"? It doesn't affect the operation of the mechanism, but I think it looks nicer when listing all the PRs
- If we agree this in the retrospective we could put it as a warning on the checker
- github doesn't make this easy like they do with PR body templates 
- we should start doing it anyway 
ACTION: Dom should update the project board checks to check these

### Whether rightly or wrongly, we've stopped using the Reviews channel, are we happy with that situation?
- never really took off, was made for discussing reviewing best practices etc. 
- we don't use lunch either as no one is on site

### Do we need to think about paying for the planning poker site?
- probably, but there are alternatives, we will try them out first. 
  - trying this out at next planning meeting

### Creating a new ticket to fix errors introduced by a PR feels wholly and egregiously wrong
- resolved, confusion was caused so next time don't be afraid to change titles to make things clearer 

### How good were our estimates for individual tickets?
- ok, but musr migration took twice as long because jack was involved as well, this isn't a bad thing because now someone who isn't as experienced has been shown what to do for future migrations 
- this is probably reflected in the burndown chart


### This may not be the appropriate place to discuss this, but if so, how is "Coffee Time" working for everyone?  I notice it tends to be a few usual suspects joining, so I just wondered why that might be...  Bad timing?  People busy?  Not keen on chatting?  Too many VCs already?  This may not be a huge problem, but we do need to at least try to keep in touch.  Are people doing that separately perhaps and therefore don't feel the need for a group chat?
- difficult to stay in the zone sometimes when working as its a bit like context switching, not because we don't like talking to people its just difficult
- sometimes have meetings at that time
- do we need to have an evening round-up? 
- should we do coffee at the start of the day? or move stand up 
- maybe we should have an activity or something for a bit of fun at coffee - show and tell, something else? werewolf? suggestions on teams social channel 

# 2021-08-25

## Items from last retrospective

- Suggestion about changing of coffee - we did it during the tech debt week then stopped. If you have a late coffee you might just be saying what you're about to say in the following morning. Maybe it should be a catch up on problems - though we already do this in technical. Once we start coming onto site more we won't need to do coffee or a second standup. 
- Keeper - still need to do this - ACTION on JH 
- Issue templates - JA has a pull request sat waiting for this so we could use this. Adam also has a template. - ACTION: get this merged and see if we use it
- Burndown suggesting we haven't done enough - It was a difficult one to calculate. This sprint was a bit easier to calculate points for and we seem to be more on track. Hooray! 
- Tasks - Not tidied up yet, KB will do so before the end of the week(ACTION). 


## Items from current retrospective

### IOC tests turning into a useless metric 
We have made a ticket for this and planned/proposed it, we dealt with it at the time. 

### Checkstyle being prioritised over IOC tests
Ditto, we are dealing with it. 
They are slightly prioritised because they are much easier fixes than fixing IOC tests and it takes a lot more effort to fix IOC tests. Missing documentation in the GUI is also very important for the future. Checkstyle is an easier graph to look at because it's stable and reported on the jenkins job. We should fix both rather than concentrating on one or the other. 

DO mentioned checkstyle can be a bit heavy handed, it complains if you don't write docs for every function. Should we be doing it on all of our other languages? Yes we should, though this adds another metric that needs to pass 

We should run this on pull requests instead and make the build fail if the warnings go up. JA will put a ticket in for this for the next tech debt. We have a build for this already but it's rather broken and not plumbed in as it stands. 

### It was strange but really good that members were in the office and having a discussion on teams 
Meant that people off-site could jump in at points which helped with teamwork and hybrid working. There are some funny side effects with this if you are sat in the office like hearing things twice over but overall it worked OK. When we're back at work we should maybe worry less about distancing and use things like the big screen for standup and so on to get around that problem. 

### Avoiding re-adding release notes back into ReleaseNotes_upcoming in after a release 
We should add a ticket to write a script that will rebase all tickets to the current master/main and avoids this problem. This script should be run after doing a release. ACTION: JH create ticket 

### Happy that the Python version being incompatible was spotted while doing the release 
It was good that we did the release in the shutdown because mid cycle this could cause panic. 
We should be careful about dependency updates because we aren't necessarily building on the same machines as we're deploying to. If BR hadn't have noticed this we could have ended up with problems after creating the release or even worse deploying it. 

### planning board has columns for themes - do they work? has the automation been working
Automation has been VERY helpful and project board checks are now pretty much solely moaning about release notes rather than invalid labels. 
themes in the planning board are possibly not that useful. 

### Was the release at the start of the sprint useful?
We used to do it at the end and this time tried to do it at the beginning. Think it was useful, meant it didn't overrun from the last sprint. 

### is the "added during sprint" label helpful and if not shall we remove it
Yes and therefore No. 


### Discussion around sprint themes 
DO does not like themes because as a manager it's tricky to give people the answer to "what should I work on next" without context of the tickets in the theme. Beforehand it was just "pick something from the ready column" but now it takes longer because it's difficult to advise on the tickets we aren't sure about. We also don't talk about it during planning which we used to but we don't really have enough time to do it. We have a large team and it's hard to talk about every ticket because it takes up so much time. Themes give us an idea of things we HAVE to do in the sprint, for a migration for example beforehand there may have been things left out of the migration because we didn't get round to them. 

We have had less planning discussions but this may or may not have had implications on managers and so on as it puts more pressure on them to know about all of the tickets in the theme. 

The problem at the moment is the sprint is completely full with themed items which leaves us with no room to pull things into the sprint if needed. 

What about if we had themes but got people to prioritise the top 3-4 tickets for each theme depending on what is high priority for the themes. 

In pre planning we could ONLY discuss theme stuff to get around having stupidly long planning meetings where we discuss themes AND other proposed tickets. 

We have lots of new starters so the order of the ready column doesn't matter because most people don't pick a ticket off the top of the ready column. We could get component stewards to prioritise the ready column.

To summarise what we're going to do:
Preplanning: we will only discuss themed tickets that have been proposed by component stewards 
planning: we discuss anything that has been proposed since pre planning and generic tickets that don't fit in themes.

Once the planning meeting is over the general tickets from high/medium will go into the planning board, KB will do this, and the themed tickets will be put into the project board by the component stewards who can then order them based on priority. 

Where is this process documented? 
It's in the files in general, we should update the wiki to point at the spreadsheet showing component stewards, who is working on themes etc. 



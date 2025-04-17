## Items from last sprint: 

Can we make our deployment process clear with respect to version numbers of current and previous?  Major/Minor/Patch version.
How do we account for e.g. hotfixes, roll-backs, patches, etc.  Or a deployment of a single IOC, or a support module? (e.g. StreamDevice)

- Perhaps link to wiki page from GUI `About Box` showing versions and hotfixes (exists already).  Or an ID suffix on version number?
- Each IOC and module has a version number created during build.  Can then compare.
- How do other facilities handle this?
- Decided need to discuss in separate meeting.

-------------------------------

## Items from Current Sprint (2022_01_06)

How to account to support work?

- comment on `Support Channel` in Teams
- KVLB will review at end of sprint and account for points spent


What would everyone's opinion be on trying to bring in one or two issues each sprint to automate some of the manual tests we do as part of preparing for releases to slowly begin chipping away at them to speed up release testing?

- Use Squish as we have it
- Always good to speed up release testing
- Difficult to prioritise testing higher than instrument work
- Occasionally convert one test after creating ticket and then review
- Have a list of tests/tasks/tickets on wiki for "spare moments" e.g. on Friday afternoon
- Decided to get ISIS cycle(s) out of the way first and then have another think, probably a meeting.


Would revisiting the concept of code freezes be a good idea?

- Already do something approximating code freezes
- Discuss at meeting above if required 


Can we consider using GitHub Discussions to contain technical conversations?  I feel it may help us as a team to better organise and archive technical discussions taken place under custom categories and pin important conversations (sort of like an internal stack overflow). I believe it may also help reduce duplication of questions asked and answered within the team. 

- Group worried about number of search locations
- Any technical question should already be answered on wiki, add it if not.
- Suggested that JA give a Code Chat on the subject
- UKRI Universal Documentation Project ("UDOC") - option for our manuals(s)?


Might be interesting to just discuss the idea of the ICD lightning talks we attended this week, seemed an interesting idea.  Maybe we could put an odd slot in for one or two (e.g. one after stand-up once a week?).  Not necessarily to to do a block meeting of them but let a few technical tricks and ideas out of the bag in a 1-2 minute slot. Could also be presented to ICD if appropriate.

- For info: 4 to 6 months is frequency for ICD talks
- Book weekly slot and people can volunteer if have something to talk about
- After Stand-Up meeting is ideal, if time allows and not running in to next meeting
- Give people option not to attend if not interested
- Suggestion is to have after Stand-Up of final day of sprint


What would everyone's opinion be regarding merging the Social and random teams channels together to reduce the number of channels we have?
Is there history in one or both chats that we particularly care about and would prefer not to lose?

- Group not been using certain channels very often, so no harm in removing.  Especially "lunch" as was only used in lock-downs.
- Always option for individuals to hide any channels on own client
- OK to delete "social", "lunch" and "reviews". DONE.
- Suggestion to have "system" channel for CMM to record activities.  e.g. reclone system, fix RAM, alter GFX car, move physical machine or VM.  May be better on Sharepoint on a per instrument basis.


Can we discuss [this ticket](https://github.com/ISISComputingGroup/IBEX/issues/6973#issuecomment-1015399722) as a group to look at automating the release build?
- all documented on wiki, so assumed straightforward to create Jenkins job.
- deployment more involved and risky.  start task with just automated release and then run system tests.
- create ticket for automating release, not deployment.  Win10 deployment is very different to current system, so will revisit when in place.


If we can be more descriptive / verbose with PR titles and descriptions, I like the idea of using the auto generated release notes feature on GitHub for release tags going forward. Currently PR's vary quite a lot in how well they are written so the auto generated release notes don't look very nice.
If we can be stricter with how well we write PR's and commit messages (title and body), I would like to place the Release notes link in the release tag like we do already and then the auto generated release notes beneath that to be more descriptive with the changes included in each release tag per repository.

- with tags, can automate release notes by selecting appropriately
- summarise commits in PR
- possible to create "draft release" as nightly build?  
- can't see benefit.  difference in customer and developer release notes.  may not work for customer, as specifically created for instrument. 
- suggestion to create demonstration release using most recent release for comparison.



We probably don't need to buy a mic for the office webcam now, but it's probably worth shutting the door at standup as people walking past the office can be picked up on it now with the "low" noise suppression option ticked on zoom. Otherwise though I think it's much clearer! 

- camera angle too narrow to show all present.
- suggestion to try separate mic and camera


`DDaT` launch PC recycling and sustainability scheme (sharepoint.com) Volunteers required to re-image obsolete (but still useful) IT equipment for resale to staff or donation to charity.  Scheme currently being run from Polaris House, but maybe if/when expanded to RAL, could be an idea for a team-building exercise (or perhaps more of a bus man's holiday!)

- probably more useful team-building exercises we could do, like joint programming, or hackathon.


-------------------------------


### Extra comments:

Run out of tickets for people to pick up during sprint, so bear in mind for planning meeting.

- probably due to large tickets (e.g. deployment, release)
- ask on General channel so can help with work on current themes


Are we planning a late Christmas meal, if not then something else e.g. pizza or something on site?

- can consider now restrictions relaxed
- respect opinions if people don't want to attend or can't
- can book large conference room for social distance for activity e.g. lunch
- need ideas for numbers attending so that office capacity accounted for
- can meet at Dish on Harwell campus for those on site?


OK to pick up "Friday" ticket at any point?

- Yes if all other sprint work done
- useful for training


Sprint Review:

- Release created and deployed on time
- See how deploying early worked for the upcoming sprint/cycle - did we create more patches as a result?  Did scientists test early as that was the whole point?



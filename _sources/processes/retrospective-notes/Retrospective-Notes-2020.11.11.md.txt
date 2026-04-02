# 2020-11-11

## Last Retrospective

- Documentation for our approach for external contributions [here](/processes/dev_processes/External-Contributions)
- Invite for training course went out to all scientists. Had 3-4 extra scientists join that were new to ISIS. We should perhaps run one every couple of releases or so.
- Running the training course remotely went fine. Lessons learned: 
    - Could have used some more training machines to be set up
    - More time would have been beneficial in places
    - It was harder to bring additional trainers in a remote course. Only one can speak at a time, as opposed to in person, where the second trainer can walk around and help with individual issues.
- Supporter of the week: Can't tell at the moment how this is going, we have not really been in cycle yet
- Had another case where replies from scientists got missed because the initial email was sent from a private inbox. Please remember to use the ISIS email account for mass emails.

## Items from this Sprint

### It would be helpful to have an e-mail template to use when informing scientists that we wish to update instrument control PCs.  Obviously, the reasons for each update differ, but there are some common points we should always include:
1. why we are proposing an update
1. when we are proposing to perform the update (making sure we give plenty of notice)
1. asking scientists to respond with days/time that are most convenient to perform the upgrade
1. explain the consequences if a scientist declines the update or fails to respond.
There may be some other points we wish to include.
A template will help us to always remember these key points.

- Yes, this is a good idea. Should also include a list of issues that are being fixed with the update. DO has volunteered to add a template to the wiki.
- If you are unsure about whether an email to scientists is appropriate, do not be afraid to run it past someone else. This is a common and valuable thing to do

### Last year we did not run a short sprint over Christmas (sprints starts were 7/11/2019 and 9/1/2020) - this year we currently have a sprint scheduled for 10/12/2020. Do we wish to have a short sprint this year or do the same thing as last year? 

Christmas sprint has about 12 working days. What should we do with this time? We don't want to make this a full sprint to save us spending extra time on sprint planning etc. Options:
1. Extend sprint starting tomorrow to 6/1/2021.
1. Could do a long sprint starting from 10 Dec.? - Means we may come back in the new year and not remember what we planned
1. Extend sprint starting tomorrow by a week to 17/12/2020. New sprint starts 6/1/2021. Week before Christmas is for Fridays/Tech Debt/finishing off tickets

Decided on option 3. This will hopefully give us a nice clean slate for the new year.

### It's been a long time since we've had a Friday, can we have a week of them? Or maybe a whole sprint full? See Freddie's message above

See above

### POLARIS is happy that our sample changer update caught the fact that a sample was dropped and stopped the experiment so that it could be corrected

Good! They were happy that while they did lose time, they did not lose much time.

### Our current sprint is 2020_10_15 but our "slides" are sprint review 2020_11_11, should the ppt reflect the sprint name and not the date the sprint review was carried out? That would make correlating at any later stage easier if required.  

Yes, this is a good idea. Call the file `Sprintreview_start_<date>`. Add start and end dates on first slide

## Additional Comments

- We are happy that POLREF is now running on IBEX and SURF is planning to use it this cycle.
- We are making good progress on SANS2D. Different groups coordinating well with each other (us, scientists, network team, ...)
- We are excited about Windows 10 updates. Build is "mostly" automated, process is now documented on SysAdmin manual, everyone should in principle be able to set this up.
- What to do with trivial support issues? Creating a ticket every time seems like a lot of overhead --> Put them in a teams channel, then record them permanently in a ticket at the end of the sprint. `support-issues` channel has now been created
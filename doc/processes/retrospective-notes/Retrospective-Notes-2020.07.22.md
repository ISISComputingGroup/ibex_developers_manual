# 2020-07-22

## Previous Retrospective notes
* Still need to make the ticket for stale reviews (DO will make and propose for next sprint)
* Architectural decisions - getting better at using the [decision log](/processes/Decision-Log). Copy the style of the last decision is the current 'template'
* `added during sprint` label exists - label being used, adding a comment or to the description seems to be used appropriately and we should keep doing so
* Friday open channel - didn't really happen, but if we want to do it we should. Should make more of an effort with the new starter
* Burn down charts are good - the pinned info on teams was highlighted
* Release notes style is better - but must remember during demos that there are previous releases that need to be included when talking to the scientists
* Timings of the review meeting - this one was a short one, but we think that shortest first would be a better order for ease of timings, it would be helpful to add a rough idea of how long the slide should take (sprint review template created and uploaded)

## Addition of size labels - functionality added with no documentation
Documentation has been added since
In use on all public repositories, based on the number of lines of code, adds the size automatically on creating the PR
Some people find it useful, others see it as nonsense - use the information if you want to

## When marking as impeded need to make sure we add a reason why
Sometimes this is forgotten, brought up as a reminder

## Starting to get a lot more late arrivals to meetings
We will start on time anyway
You can always log into the meeting before it starts
Consider using snooze not dismiss (so 15-minute warning, hit snooze, 5-minute warning - log on) (Editors note - you can change the delay on your pop up from outlook if you have it open in your own calendar to something else possibly if the standard 15 minutes doesn't suit you)

## Coffee often has low attendance
Some people not necessarily willing to start the meeting if no one is there already - it is suggested that you start it and carry on working - put it in the background
Camera off is fine for coffee
Whilst working remotely we are meant to have two meetings each day, and coffee is our second one, better attendance would mean we don't have to consider something more formal
Leaving early is fine, arriving late is fine

## The burn down chart we are using shows an increasing gap in the number of points between completed tickets and the total number in the completed and review columns - we are implementing more tickets than we review
The end of the sprint will have been thrown by the release etc. but the gap increased slowly from the beginning
The number of tickets in and out should be staying static, but the number of tickets has increased as well (end of the previous sprint there were 3 tickets in review, end of this sprint there are 11)
There are some instances where there is nothing available to review either because they need specialists to review them, they are already under review, or they were by the developer looking for a review
A code chat on how to review was suggested, it has been added to the ideas list and will be done sooner - this would be a discussion rather than a presentation
Will create a channel to go through reviews, what was hard, what was easy, things that have been left off, things that should not need to be done by the reviewer
Consider doing reviews as a group again for some tickets
Flash reviews - maybe need a different process, also need to get better at rejecting flash reviews - if you can't review it in less than half an hour using just the git code view it probably isn't a flash review
We will expand the use of the flash reviews channel to include urgent reviews as well by adding a link (e.g. for test fixes) to the ticket (rather than the PR), as anything that will take more than an hour combined should be accounted for with a ticket and points

## It great to see a good number of live demos, and they were good demos too

## Were any of the tickets added regressions of existing functionality? Are there any patterns?
Yes - we caught them and fixed them in the manual testing
Previous regressions - yes, some had been seen before in other releases, some had appeared historically and not been fixed.
Macros not being saved - needs a Squish test
If it can be automated and failed then we need to need to get it automated
Need to check if we can have a squish day, but need to confirm how many instances can be used at a time
The spreadsheet is long, and not straightforward, need a system test day to automate those that we can and verify those that we can't and what can be fixed
Need to also consider other ways of recording the tests and their statuses

## Do we want rotas for the meeting roles?
Possibly useful: one for chairing, one for timekeeping, one for note-taking - create and try them

## How did the release go?
It was close to the line, and it was stressful - there was quite a bit of out of hours working to get it done
There is a mix of it feeling that it is a long time before it might be used for various reasons, however, we are deploying and going to be able to demo before the scientists need to use it which is a good thing to have achieved and probably better for our reputation
Releasing close to cycle has risks, and it was asked about releasing again before the cycle, any bugs found we can patch and fix, but not release new features as we are currently unable to test thoroughly enough for that "last minute" style of release
That kind of "last-minute" release can be done confidently, but it takes a lot of time to reach that stage of test coverage
There was a discussion about bugs being released and the impact, and how far we are from being able to test everything, OPIs are an example of untested items which are widely used

## There is a reflectometry goal being aimed for, and there is a plan for that which has increased confidence
There was a brief discussion of plans and their usefulness in tracking progression - whilst a plan might not last long, it is often reassuring to have a starting point at least
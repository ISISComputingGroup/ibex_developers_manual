# 2020-05-28

## Specific Device IOC Pages on wiki

As discussed in previous retrospective the [Specific Device IOC page](/Specific-IOCs) has grown to be about both the software and the hardware. This means that having the IOC in the title is misleading. It may also be good to review the kit we have listed there and make sure we have a good amount of info for devices and that they're well organised. I have added a [note](/processes/meetings/Technical-Debt-Stand-down) to do this in the next tech debt stand-down.

## Organisation during meetings

We can sometimes overrun or get off topic in meetings. This is especially bad on ZOOM as it's harder to pick up on social cues and there isn't someone physically kicking you out of meeting rooms. To help with this we should have a checklist of things we do at the start of each meeting, if appropriate:
* Explain the meeting's purpose
* Appoint a time keeper, responsible for saying if the meeting is overrunning or suggesting breaks when appropriate
* Appoint someone to take minutes if decisions are being made in the meeting

We should also ensure we pause if we drastically change topics so that people can have a chance to leave the meeting and notify people on teams if we feel that others might be interested in the topic.

## Onboarding

We're onboarding a new member in August, this may be tricky whilst working remotely. We have to be particularly careful that we:
* Make it obvious that lots of people are asking question all the time and that it's encouraged to do this
* Make sure we make efforts to catch up with new starters and see if they are struggling with their specific ticket

Adam mentioned that one thing he would have found very helpful as a new starter is a step by step guide on how to write an IOC, see [here](https://github.com/ISISComputingGroup/IBEX/issues/5435)

## Working Remotely

We haven't had so many unplanned tickets, which is good. This is likely due to no support and less casual interactions with other groups. Losing these casual interactions, especially with scientists, may be bad:
* There may be information we're missing from the 'bumping into' scientists, they also might be less aware of what we're up to. On the other side it might be good that people are only getting in touch when they have important information to share
* Teams isn't great for casual discussion as it's limited to chat within teams rather the whole organisation
* We have the IBEX users group in teams but it's not been widely used. We should start using it ourselves to announce things in a casual way, which will hopefully lead to more scientist use. John will use it to announce the `b.` namespace introduced in https://github.com/ISISComputingGroup/IBEX/issues/5401
* We should make sure that we responds on this teams chat quickly to encourage people to use it

## General thoughts on the sprint

* We missed the target number of points for this sprint
* Having a visible burn-down chart that is automatically updated would be good. We currently have an automatically updated spreadsheet but no chart (http://shadow.nd.rl.ac.uk/ibex/)
* We should avoid taking things out of the bucket before reviews
* Can we set up a tool to tell us how long a ticket has been sitting in review. Freddie will add functionality into the project board task to tell us when a ticket has been review for over a week
* There was some discussion on how to remember when you have tickets that you asked to be reworked that you need to re-review. It was suggested that people put a note on the ticket or look into configuring gut hub alerts for this

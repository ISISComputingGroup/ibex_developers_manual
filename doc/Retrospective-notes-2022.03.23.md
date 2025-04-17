# Sprint retrospective notes 23/03/22

## Items from last sprint

How patched is the release? were the timings good for us?
- Not very patched compared to last time we looked at it. SANS2D have a few patches but are happy.
- Overall happy with release timings. Workflow is still not documented on the wiki.

PR auto generated release notes
- Extra overhead but we should be better at titling PRs anyway for tracking

Points expected at start of meetings: 
- still trying this

Discussion tickets: 
- Now trying architecture meetings, we need another one but it might not be this sprint given we've got cycle, release and deploy
- we should do one about networks but we should hold fire as there will be changes

Should we think about splitting planning during cycle as well as review/retro? 
- We are leaving as one for now. 

Eclipse RCP training:
- has been decided that a few people are going on a training course for it. Freddie may also do the course as well as he has a license. 

Should we merge IBEX/wiki and the developers manual? 
- some things will be changed and moved around, this is still in progress. 
- instrument info moving to the dev manual, this is in progress
- main ibex manual is being rearranged a bit, "" 

Team day: 
- we have this coming up on the 25th of March

Camera in the office: 
- now even wider angle
- not pointing in the right direction at the moment 
- stack of books or mounting it on the wall might be an idea to make it even wider

## Items from this sprint

Can we set a challenge to the team to get stale reviews done and get the project board checks to stop moaning and giving warnings? 
We can cheat about this slightly to stop them getting stale
- There's always a reason things are stale? No, sometimes it's just the way it is. 
- Generally if it's at the top of review it's either been there the longest or it's very urgent.
- This is more of a reminder rather than a discussion. Why do we have things in review that have been there for months? 
  - Hard to review/not urgent/no one understands it anymore perhaps - we should get these done anyway.
  - We should say about them more in standup and get them through review
  - If it's hard to review, perhaps we should give more info in the ticket on HOW to review it.
  - This is getting better, we are moving in the right direction. Some are squish test tickets which can be tedious to review. Perhaps we should have a discussion at standup if there is a ticket that is difficult to review. 
  - pair review may be an idea to get through the tickets that take a lot of time. 

Should we hit the button to get rid of everyone from the GH org who does not have 2FA enabled
 - we need a way of doing this for `ISISBuilder`
 - we might be able to do this via an app or email rather than text message for it. 

We should have a known issues page for accelerator beam stuff being down like the MCR news that the scientists can use for update 
- Should be something we can all edit
- why don't we use the shared inbox? because people who want to know might not be scientists so we cant just email all of the scientists. 
- we should put this alongside where our shared phone number is listed and put it on that page as it might stop people from calling
- we need a discussion with the internal web admins in the computing group? to discuss this

Zoom now works if you're logged in from multiple places. hooray! 

INTER could not find the new zoom support phone number so ended up coming to the office instead. the previous number is now redundant as all landlines have been removed. 
- We should get some cards laminated again with the details on as the ones round site are out of date. ACTION: get these printed. Perhaps we could put a QR code of the our web page on it. And a picture of a goat! DKg would like to do the designing of these cards. KB will send Dkg the previous one
- 1763 should still work from the existing landlines in cabins, but will ring to zoom. We couldn't ring them back without looking up their number on the intranet
- this is inconsistent as WISH seemed to come through with their own numbers... 
- If you add them to contacts they show up as their instrument name.

We decided to move parts of the IBEX wiki into the code repo, would it be an idea to do the same to the dev wiki? 
- this makes it easier to view version history
- you can still edit it online and it makes it slightly clearer to view the structure of the wiki
- this is easy to do
- this will break the wiki check so we should keep this in mind - though this is easy as well 
- one click less to have the same info
- we should double check this won't break relative links etc. and retain history

Graylog move to SCD cloud
- created a Friday ticket for this, didn't quite get it working
- the ticket for making `graypy` more hardy should be treated with a higher priority than the instance location as it caused some scripts to fail

Hackathon to move all IOCs into support directory
- we should do this instead of the next Friday as a hackathon, they are fun
- ACTION KB will propose a date 


Sigh of relief for TS1 commissioning being pushed back
- we are doing well at supporting TS2 I think - so might be a good thing that we can carry on just doing so as it gives a chance for junior members of the team to help with support more.
- there are positives and negatives for this
- more work may need to be done in a shorter time, so there is an element of panic here too. It also mixes up our timelines slightly for things like win10 etc. 

What is making people sad/mad/glad 
- There were 49! conversations in the support issues channel. We have been very busy but we are doing well. 
- It has calmed down a bit now, we have managed to jump the hurdles well. 

- It would be good for junior members of staff to come along with support calls especially ones that require being in person 
- hard to do this remotely as we don't immediately log everything in support-issues as it is happening
- there is no shame in saying "I'm not sure let me check with the team"
- Would the Sandwich students like to come along to support calls? yes 
- There is a sense of ownership when you pick up a support call but this does not mean you're solely responsible for that problem

Call queues - has the ring timer for call queues for level 1 been reduced? It seems to ring for a very short time and then go to the next level - this can make it difficult to have time to get everything ready to answer the phone
It's too short. Perhaps we should get everyone a lab phone as it's easier to accept a call on a phone than with a headset. 
<b> we will increase the ring time for 15 seconds as 10 seconds was too short to be able to answer it before moving onto the next person </b>

In terms of the amount of support calls we got done we should be proud of ourselves as we've been off sick/on leave etc as a team. We shouldn't be disheartened by the state of the burndown - we have been doing brilliantly. 

As someone who cares about the user interface side of things I am glad that we've had lots of changes recently - they are tangible things that show up and show change in IBEX so although they might be seen as "nice to haves" they are very useful. 

Lightning talks - we forgot what was happening so that was the reason we didn't have much to talk about. SJ will put a note on the code/gui chat page

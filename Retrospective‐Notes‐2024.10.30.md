| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| CMS   | KB         |LC          |

Present:
- In person: FA, TW, JD, IG, LJ, LC
- Online: JH, SC, CMS, ES, KB

# Previous Sprint
- Automation: we now have it on the sprint board, with labels being added/removed when moving a card through columns
- Ruff/Pyright day: we did this.
- Using task table instead of task board: this seems to work quite well
- Was remarked last retro that there felt like fewer calls for lat cycle, however after doing the math it was also our most support-heavy cycle of the year

# Current Sprint
## Moving planning meetings later in the day
- Initial proposal was to move them from 10-12 to 10:30-12:30
  - This however cuts into lunch hours, meaning that those who arrive early will have to wait even longer to eat and go hungry for a bit.
  - Additionally can cause issues with people putting meeting early afternoon in diaries which might altogether remove your lunch break
- Balance is people starting early and needing to eat vs needing to travel in in the mornings later to avoid paying for peak tickets
- JD suggestion: what is stopping us from moving to an afternoon meeting?
  - This technically goes against agile methodology (theoretically no work going on between review and planning, in practice that never happens)
  - However we're not held to agile irrevocably, so why not?
  - There used to be a lot of post-planning work, but not any more
  - Could lead to there being many meetings on a single day when in-cycle which is bad for support
- Going to try it as an afternoon meeting for the next few months

## Using Gitlab for instrument config branches
- Won't let us use it due to bad commits
- would have to rewrite history on 4 instrument branches (thankfully not on any others)
- LJ willing to take a look

## ISIS Branded merchandise for new starters
- JH Hopefully getting around to it this week

## NDX security
- GR highlighted the fragility of the security on NDX machines in the teams channel
   - default user/pass was found on web search
- Bigger problem than was highlighted in the message
- going to revisit with GR present to make sure no points misrepresented

## Cabin PC passwords
- Should we have scientists share their passwords with us in keeper? There were a few instances where we needed them and had to look on a whiteboard for them
   - Generally don't need to use them but e.g. IMAT has a couple of machines we need to log into for cameras
   - A user called us on the support phone when they needed the cabin PC password, and the local contact was neither local nor contactable, so we had to tell them to read words on the whiteboard until one of them sounded like a password to us
       - Should we even be giving them out? Probably not.
- Could go round the halls once a year looking for passwords on whiteboards and adding them to keeper
- Could also just ask the scientists if they don't mind giving us the passwords

## Release numbering
- Every release for a while has been a major release and incrementing the large version number
- Could be confusing figuring out which instruments a given release was deployed to
- Will instead move to YY.MM.Patch format from next release (now 25.02.0) from next release onwards

## Moving sprint meetings based on availability
- Will bring this up again when GR present
- More labour to check, but LC willing to do a little rescheduling on further out days if the team is ok with it

## Demos
- Should not be a whole cycle after release, should put it in PI template
- It's a good way to ensure whole team is visible to science groups for more than just specific devices etc.
- Even if only 3 out of the 5 demos have people show up, will still be worth it

# Mad/Sad/Glad
Mad:
- SC mad of pyright because there's now work needed before submitting to review, but...
Glad:
- SC glad at the same time that it's teaching better python practices
- Collectively glad that old code is being updated to follow pyright
   - As such less messing around with it when you change a single file
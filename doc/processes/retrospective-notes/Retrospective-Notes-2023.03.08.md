# 2023-03-08

| Chair      | Timekeeper | Note Taker |
| :--------   | :---------: | ----------: |
| LJ | JH | HC |

## Items from [last retrospective](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Retrospective-notes-2023.02.01):

> Try to automate more of release workflow to avoid errors
 - Will be discussed in planning meeting (2023/03/09) succeeding this one. 

###
> Shorter sprints to avoid unplanned work?
 - No extra discussion concerning this.

###
> CO2 monitor, is it still effective? Perhaps worrying too much about it?
 - Discussed below.

###
> Recent AwayDay very worthwhile and productive
 - Have had some follow up from this: quick wins meeting, and also various discussions.
 - Mentions of assigning a day to tackle the various areas in groups: Thomas L volunteered to organise.

###
> Could be more ambitious with migration schedules
 - David and Kathryn on the case creating the new starter tickets. 

###
> General thought that the group is not currently working on 'large'(er) projects
 - All agreed that not taking on too much is reasonable, given cycle and TS1 ("lots" of support!)

###
> Prediction that TS1 coming back online will generate many problems for the group, having not been run for ~18 months
 - A lot of support, but surprisingly was mostly TS2 related.

## Items from this retrospective:

### Standup: standing in the conference room 
 - Generally agreed upon that it's only fair enough as remote workers are sitting: we have reached the conclusion that people are welcome to sit/stand as they please
 - Mentioned that as there is a culture of standing, unless enforced we will most likely continue standing out of habit. Thus, we will have sit-down standups for the following sprint. 
 - Evaluate our time efficiency next sprint, and consider the need for a timekeeper (or decide to have stand up standups again).

### CO2 monitor 
 - See Thomas L's picture in teams: this is the most up-to-date guidance. We often surpass the 800 mark (e.g., _open windows, reduce occupancy_) in the office, even when it's not particularly full - as we are expecting new starters next month, this is not acceptable.
 - The two solutions were seen as either living with the windows open (estate's advice, but it's winter so not particularly viable) or pushing estates for a better ventilation system.
   - Freddie to ask estates.
   - In the mean time, we will try to leave a fan running: evaluate our satisfaction with this next sprint. 

### Concerns regarding recording hotfixes
 - General agreement that it's currently a pain to record hotfixes, and too easy to accidentally skip/miss the hotfix step on the upgrade step. 
 - Agreed to remove the version numbers from the hotfix page, but migrate these elsewhere as they are useful for support calls.
 - Jack H to remove the version numbers from [Instrument Information / Hotfixes](https://github.com/ISISComputingGroup/IBEX/wiki#instrument-information--hotfixes), and add a link to each instrument's wiki page with the version numbers there instead: this will make the information there more concise.
 - Tom W to write ticket for investigating technical solutions for this.

### Database truncation
- All in agreement this is necessary
- There is a [ticket](https://github.com/ISISComputingGroup/IBEX/issues/5818) proposed for this, but it may want updating with some of the technical information mentioned in the meeting.

### Barriers which prevented [Instrument Demos](https://github.com/ISISComputingGroup/IBEX/issues/7584) from being done
 - General feeling that recording yourself is uncomfortable: proposed idea of one person recording, and another editing to overcome this.
 - Still very much considered valuable and a good idea.
 - Discussed the lack of demo meetings, and how these can be valuable for IBEX input. Decided that it's more sensible to encourage the instrument scientists to come to us, rather than imposing meetings on them.
 - Agreed actions:
   - Skip demos for this sprint: it's been long enough that we should focus on preparing for the next sprint's instead.
   - Each sprint's demos will cover the changes occurred since the last, as then we get a nice archive going forwards.
   - Create videos both for each feature in the sprint, and the sprint features as a whole (creative license for the person doing the ticket to decide which way to do this).
 - Brought up larger issue of not picking up high priority tickets. Decided this can be rectified by also keeping an eye on the 'Ready' column and the tickets at the top when checking the project board during standup. 
   - Hannah to note this in standup links file on teams so we remember going forwards.


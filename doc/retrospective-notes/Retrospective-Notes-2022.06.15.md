# 2022-06-15

| Chair      | Timekeeper | Note Taker |
| :--------   | :---------: | ----------: |
|[@LilithCole](https://github.com/LilithCole) |[@LilithCole](https://github.com/LilithCole) | [@daryakoskeroglu](https://github.com/daryakoskeroglu) |

--- 

## Items from last retrospective
## Workflow

### Windows 10 and Other Migrations.
Win10 and other migrations should be one of the main focuses over the summer.
_No change, still as it is._

### Disk cleaning Automation
Time should be spent looking into using [@ChrisM-S](https://github.com/ChrisM-S) powershell script to automate cleaning of drives, moving over IOC logs periodically as part of a cron job. 

A discussion ticket should also be written up to discuss how we could automate truncating the database without affecting active runs.

_Did not have a chance to discuss this sprint, need a discussion this sprint._

### Splitting up GitHub Issues More Finely

A discussion took place about splitting up issues that involve writing IOC's, Emulators and systems tests as the work is usually always contained within 1 large issue. It was agreed to keep this as it is and change how we approach developing the IOC, system tests and Emulators and document the process in the wiki.

The process discussed was to write the minimum functionality required to have a working IOC with only one function, and system test and gauge how long it would take to write the rest based on the time required to write one function.
It was also agreed that development should be done in a way that allows for the work to easily be split into additional issues if needed. 

_Agreed that the process will be used_

### Sprint Lengths
How we currently run sprints was discussed in relation to how we adapt the length based on cycles and support. It was agreed that [@KathrynBaker](https://github.com/orgs/ISISComputingGroup/people/KathrynBaker) will spend a couple of weeks looking into trailing a nested sprint where sub-sprints occur for each theme within the main sprint and present this in the next Retrospective.

_Kathryn did a presentation about nested and sub-sprints in this retrospective_

### Support During Cycle
Support during the cycle has been eerily quiet...

_No cycle this Sprint, hence another quiet Sprint_

### Beckhoff
Small Beckhoff in a box is missing? maybe on IMAT? 
Look into buying test license for Beckhoff.
Keeps hearing about weird errors from Beckhoffs - Pester motion control to get a fix.

_@rerpha is discussing about buying test licence for Beckhoff with the motion team._
## Equipment

New docks have arrived!

Network Cable Tester arrived works well!

_People who started using the new equipment are happy with them_

---

## Items from current retrospective

### Project board channel on MS Teams stopped working
No one is using this channel so it was agreed that it should be removed. 
@FreddieAkeroyd knows the best way to remove it from channel list.


### Rota table in "Meeting Roles and Rotas" wiki page is confusing 
"Week Commencing" column causes confusion as it only relates to the Stand-Ups.


It was agreed that @KathrynBaker will split table in 2, one for Sprint Planning meetings and other for Stand-Up meetings.

### Alternative to Plan It Poker
Plan It Poker webpage was down in the last Pre-planning meeting but it came back to life.


@KathrynBaker found a new website alternative to Plan It Poker: Scrumpy 


Benefits: add issues direct from GitHub, add comments to the chain and more user friendly.


The members decided to try for the next Sprint Planning meeting.


Kathryn demonstrated how to link to GitHub. 


No registration needed, can log in with a GitHub account but not necessary. 


### Suggestion for different ways of managing the work in Experiment Controls
@KathrynBaker did a presentation about a different approach of managing work we are doing in Experiment Controls.
Key notes from the presentation:
* Consider all the work we have to do as "program".
* Program Increment (PI) would be things to be done between now and next release.
* Sprint is still a sprint, instead of following Scrum, we can aim to reduce Work In Progress and reduce sprint length to find a better rhythm.
* Each program will have a Kanban board: Program Kanban, Program Increment Kanban, Sprint Kanban
* More information about this management approach can be found here: https://www.scaledagileframework.com/program-and-solution-kanbans/
* Rough timeline suggested:
* * Sprint 2022_05_19 We decide if we would like to try -- The voting happened on zoom, we will give it a try.
* * Sprint 2022_06_16 Make sure we are carrying nothing forward, and getting everything we need in for the next release done.
* * Sprint 2022_07_14 Build release, testing, prepare for training.
* * Sprint 2022_08_11 IBEX Training, deploy to TS1, hackathon/tech debt removal/something, PI planning, sprint planning
* * Sprint 2022_?_? Sprint retrospective for previous sprint, sprint planning 

---
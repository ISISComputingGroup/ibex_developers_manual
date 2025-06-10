# 2025-06-10
## Sprint 2025_05_08 Retrospective (2025-06-10)

| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| ~~KB~~ LC | LC     | ~~ES~~ GR  |


## Previous sprint
- **Move retro notes away from dev wiki** - TW confirms that retro notes demoted in wiki search results now. GR noted slight pain in creating page for today's notes. Agreed no further action for now. 
- **Office Spring Clean** - complete
- **SECI Tech debt day** - KB confirmed LC Booked for September
- **IBEX Training** - KB confirms working on updating materials
- **Stand-up instructions** - no further discussion
- **IP Recruitment process** - process is over, long live the process.

## Current Sprint

### Network dependency of our architecture
- GR suggested given FA comments, perhaps we should agree we are willing to be dependent up to router C
- FA confirmed that now FIT doing support out of hours, we could confirm we will rely up to hub
- Was discussion then as to whether Accelerator controls are dependent on router C or not.
- Agreed need for a nuanced position as a group on what parts of network we wish to be resilient to.
- FA highlighted Bob Mannix position used to be that they should run when disconnected from router C. FA to confirm wit Ivan current position.
- related - FA confirmed impact document has gone to HG to then be escalated by ISIS upwards

###  Moving / Mirroring on call spreadsheet to sharepoint
- TW - in order to be accessible from home when site network down
- FA - could also use Teams
- JH - Could we use ISIS Sharepoint
- General agreement Teams would be a good place for it as remains private to us ans would be accessible when network down.
- FA confirmed ISIS page has old group mobile number removed.
- KB agreed to move it to a tab of the support issues channels

### Spring clean
- thanks

### Network outages
- TW - most outages didn't take much recovery time

### Many instruments hit 100G/24hr limit on export only area
- TW - MAPS, Polaris, NIMROD all hit limit. CMS demoed NIMROD solution in code review. Agreed in code review to extend deployment
- CMS confirmed that given time it can be deployed more widely (in response to FA question). CMS expressed concern about knock on impact on how careful people may be as a result of change.
- FA - has emailed MAPS about the creation of RAW files as well as Nexus files. RAW files do not compress as well as nexus (can be one order magnitude). Not writing raw file may well solve this issues for some of these issues. Should watch for this.
- Discussion of other log files and reasons for storage and history (CMS to email FA about one specific case to check if case involving 100s file/run needed)

#### Migration of wiki
- KB - thanks for maintaining history in migration
- JH - we have migrated user manual. What should we do with IBEX wiki? KB suggested we should think about what to do with the content. Agreed some of it was related to historic project.
- JH - we have a site network copy of the ibex wiki - Gollum is serving it on Shadow. Do we need it. Agreed Gollum can be taken off and wiki was only there as other 2 were.


## 😠😢😄
- FA 😠 Network 😄we got through it all
- KB 😄 SECI free for two cycles

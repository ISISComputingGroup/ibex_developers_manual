# 2025-08-28

## Sprint 2025-08-28 Retrospective (2025-10-01)

| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| TW    | KB         | IG         |

## Items from previous Retrospective
### NDW1926 Linux build?
 - *ACTION*: FA To check with CMS how to adopt Windows 10 LTS for build server.

### ISIS Shares (\\isis\shares) organisation - have not got around to it yet. 
 - Carry over to next retro.
 
## Items from this retrospective:
###  Review of First Line Support
 - Discussion were had around the adoption of the first line support procedure. 
 - GR identified that there was a problem where some issues were not picked up and missed from being actioned.
 - GR suggested a formal handover at the end of a week, perhaps write up a Friday summary of the week.
 - GR mentioned that Top Desk is the corporate platform and maybe we should look at using it.
 - FA Mentioned Jira, but it's not free and we would need to look at licensing.
 - FA suggests adopting a system where we can enter issues and close them out.
 - *ACTION*: FA to consider options in conversation with team members.

### Developer Manual - protection of master branch
 - There was a bit of a debate in comparison between the ease of updating the manual versus the 
ideology that documentation should be at the same quality as code.
 - It was decided that instead of committing directly to master, we should have a trial period of 
creating PRs and flash-reviews. This policy should be reviewed at a later date to consider its efficacy.

### Documentation on wiki instrument-information--hotfixes
 - JH raised the question as to whether we need to our hotfix/deploy process and suggests that we
should either keep the hotfixes page up to date or remove it.
 - FA suggests creating a flash review or ticket.
 - Remove the Hotfix column.
 - Deploy scripts to not prompt to add text to the hotfix column.

### Wiki instrument information pages are significantly out of date
 - GR asked whether we should make an effort to improve them, as having a page is useful for instrument support?
 - TW posed the question as to whether we should use the existing pages as a starting point or bin them and start again?
 - *ACTION*: TW to place a warning at the top of every page stating that the current information is 
historical content and may not be up to date.

### Disc space
 - TW stated that small discs on various machines has caused repeated issues.
 - *ACTION*: GR to set up a group meeting with CMS to discuss.

### Wierd permissions on stage-deleted
 - Could we modify permissions of the stage-deleted folder or perhaps don't use it?
 - Issue bumped until CMS is available to discuss.

### Timings of deploys
 - GR commented that deployments being scheduled only a couple of weeks before cycle and during Summer holidays
can be problematic, the Summer being of particular issue.
 - We should attempt to deploy a week earlier and deliver demos earlier.

### Deploy script refinement
 - TW pointed out that occasionally a manual step in the deployment process does not get done, but 
there is no check that it actually has been done.
 - The Roadmap should incorporate procedures to address this.

### Renaming of 'server-common'
 - JH suggested that we should rename 'server-common' to 'ibex-ca-helpers'.
 - FA suggested 'ibex-epics-helpers'
 - *ACTION*: JH to find some suitable names

### Galil-old branch
 - FA suggested that a repo check on galil-old would be a good idea.
 - *ACTION*: FA to create a ticket to create a repo check on galil-old.


# 2025-10-02

## Sprint 2025-10-02 Retrospective (2025-10-28)

| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| JH    | TW         | KB         |

## Items from previous Retrospective
###  Review of First Line Support
 - FA talked to DI about `JIRA` it will do what we want, but cost is a query
 - The other solution available was not going to do what we need.

### Developer Manual - protection of master branch
 - Trial in progress

### Documentation on wiki instrument-information--hotfixes

### Wiki instrument information pages are significantly out of date
 - Warning included

### Weird permissions on stage-deleted
 - Issue bumped until CMS is available to discuss.

### Galil-old branch
 - FA has created a ticket to create a repo check on galil-old.

## Items from this retrospective:
### Disk space
- Many examples in thread, none of which are database truncation.
- Caution for network going down is in place, but not enough space necessarily for the data coming in should the network go down.
- Return again when CMS is in the room.

### Support for non-`NDH`/`NDX`
- Evidence that at one point NDCs were our responsibility, but that was not widely known about.
- Existing remote viewing/control (`Daxtens`) also getting out of support.
- See [Instrument Machine Standards](https://stfc365.sharepoint.com/:w:/r/sites/ISISExperimentControls/_layouts/15/Doc.aspx?sourcedoc=%7B6CC20F26-86D9-4F1B-8BEA-0E96B69E5A32%7D&file=Instrument%20Machine%20standards.doc&action=default&mobileredirect=true) for the existing evidence
- *Action*: FA to make sure the expected policy for support and machine names is written down and agreed by CMS, the rest of the group and DI, and then it is communicated to all stakeholders.

### 1926 Build server
- Instruments are on LTS which is on a 10 year contract, ESU can be a purchased update.
- Both are security updates not quality updates.
- Discussion moved into the fact that keeping a test server on the same architecture was useful.
- Return again when CMS relating to update deploys.
- FA suggested getting an extra machine for the time being, which was agreed.

### First Line
- Being discussed in many places, no firm decision to be found here today.

### Server Common
- JH had a different thought, rename server_common to IBEX_helpers, two dependencies group members, for those which need EPICS call ins, and one which doesn't.

### PR Templates
- Some bits of the PR templates relate to repo specific reminders, but acceptance criteria are used sporadically, should the acceptance criteria be removed from the templates?
- Consensus was `Yes`

### Location of Emulators
- JH raised the three different locations that the device emulators can exist in - within LEWiS, in the IOC support modules themselves, or in a separate directory again.
- Suggestion is to move them to within LEWiS itself, to make it easier to highlight that success from the team, and present it at various conferences.
- Only potential downside is that we don't always emulate the values that we don't interact with.
- If not tied to the EPICS aspects, then they become more obviously useful to other control system users.
- Some IOCs and similar will use multiple devices, and having the emulators in LEWiS would potentially make that clearer.
- Tests are very individual, but emulators less so.
- Being able to package the emulators with the framework provides a more modern python interface.
- FA mentioned the possibility of packaging the emulators separate so that you don't have to install all the emulators as well.
- Discussion highlighted that we will need to make sure that the versioning and so on is clear.
- *Action*: JH to schedule a technical discussion for this.

### Sysadmin docs location
- Delay until CMS is in the room.

### Work Experience Student
- FA Happy for it to be done.
- No one in the room wanted to take the supervisor job on.
- *Action*: Check in with those that are not present.

### Organisational Diagram
- Not currently appropriate given the structure of the team.

### Contact Cards
- Make the email bigger, and update the information.
- Provide a QR code that links to the user manual.
- *Action*: KB to try and find the existing template.
- *Action*: Someone update the cards and find a suitable landing page.

## Mad/Sad/Glad
- Got through cycle
- Glad that SECI is now done with
- Removal of the SECI related items should continue, e.g. SECI2IBEX, the re-organisation of the `mini-insts` etc. may be needed, needs a think and discuss for some aspects
- Sad that LC is moving on to a new role

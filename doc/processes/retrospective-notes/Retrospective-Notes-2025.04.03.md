# 2025-04-03

| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| JD    | ???        | SC         |

## Previous sprint
### Defunct emails that looks like it's associated with us but isn't.

FA has sorted this.

### Instrument Demos

FA: how to balance too early (scientists on holiday) vs too late (not enough test time)

KB: think we should book demos week after deploy.

Conclusion: try to book 2 weeks before cycle

### Instant awards scheme

LC: Yes put people forwards for awards. Nominating whole teams / more people will tend to get a bit more scrutiny.

### Tips/tricks teams channel

ES: Minor tips & tricks that aren't worth a whole wiki page, maybe a lightweight way to share these little things.

KB: creating the teams channel as we speak

FA: more curation/organization might be good long term if it gets too big.

KB: if channel gets too big then we can move things out of teams channel to somewhere else

IG: OneNote?

KB: Onenote in teams not very good

GR: Maybe let's go for a channel this sprint and then review

Various: is it searchable enough?

FA: how categorizable is it?

LJ: Make replies to top-level "theme" posts? Similar to retrospective channel?

Conclusion: try teams channel, evolve it over time as needed.

### Release timeline

GR: Let's not spend too much time discussing this

### The end of 🐐 is nigh

DK: 🐐💀 at end of financial year?

KB: No. End of project is September 2025. But most people won't be booking significant time to ibex post June.

GR: Just to be clear this is the 🐐 project, not the 🐐 product

KB: next PI we might be looking at doing things differently. August.

DK: Can we have more time for internal team/technical priorities

FA: Have a formal 80/20 split for tickets which are scientist-driven/not-scientist-driven, but there's also scope for "personal development" type time outside the ticket framework.

FA: Post ibex finish we can review some of our IBEX tech choices, some bits of 🐐 are looking a bit dated.

### Wikis

GR: 3 wikis exist, sometimes with duplicate content. Happy to tinker.

IBEX: scientist facing
Dev: dev facing
User: how to use ibex

Conclusion: go for it George.

JH: repository-specific info - migrate to `README` or docs of each repo.

LJ: Searching?

ES: Search at org level

### Pyright

JH: people will be upset but it's a good idea

TW: didn't actually cause too many issues in practice

KB: still some instruments to migrate in summer

### Standup

CMS: Move "Friday" standup tasks to "Thursday"?

LJ/KB/GR: Discussion about whether we might lose code review time

LJ: should we be stricter about actually doing the code reviews

### Staff updates vs standup

JH: Big announcements (UKRI/STFC/NatLabs level) that various people in the team miss if clashes with standup

KB: All staff meeting might take priority anyway

Various: discussion about tangentially related things

ES: is standup actually important?

KB: standup is important to connect to others

GR: We can probably justify missing one standup every so often

Conclusion: don't know and/or don't care, other meetings might take priority, as long as ops stuff e.g. nagios gets checked. "Someone" will take care of it.


## Current Sprint
### On call.
Jack H: I much prefer doing the weekend on call first as we are now, as opposed to the weekdays-then-weekend we were doing previously, feels like the worst bit is out of the way at the start. 

David K: Also better for managing cover for the weekend before cycle and the short final week of cycle - which was the original idea for changing the on-call period, IIRC.

### Centrally-hosted MySQL Database - Status?
David K: What's the status of this?  The ticket was last proposed two years ago: [IOC Log Server: Push to a central MySQL instance · Issue #5820 · ISISComputingGroup/IBEX](https://github.com/ISISComputingGroup/IBEX/issues/5820).  Is this dependent on the move to Archive Appliance?
We were recently asked to extract data after a local database had been backed-up and truncated on RIKENFE, so had to import it from the network share, which took several hours, then create CSV files of the requested data using the 'IOC log query' script.  The instrument scientist could have done all of this themselves from the Log Plotter perspective using the 'Data Export' panel if a central MySQL database had existed.

### On-site rota
George R: a) for (very good reasons on the whole) we have a situation where the only people on site to day are the ones who only work on site. I accept this might occasionally happen, but I would like to keep an eye out for recurrences of this, as it may suggest that the rota is not working and needs revisiting. 
b) Can we agree a process for how people permanently change days and advertise it

Kathryn B: I thought the rota was the guaranteed days on site, and extras as necessary or swap with someone else to maintain the minimum cover - so if you need to be in an onsite meeting on a day you would normally not be on site, you just come to site and work there instead of at home.

David K: the up-to-date rota is in a tab in the announce channel: [Onsite Rota](https://teams.microsoft.com/l/entity/1c256a65-83a6-4b5c-9ccf-78f8afb6f1e8/_djb2_msteams_prefix_2670613932?context=%7B%22channelId%22%3A%2219%3Aeaf1bd106e2d4df78f4ea9f7aa3d003d%40thread.skype%22%7D&tenantId=3f66361c-a87e-4158-8f61-99e82db3cac8)

### EPICS Collaboration on site
George R: It was great to see Evan working with a colleague from Accelerator Controls today. Can we do more to build links with other RAL EPICS users and share knowledge/expertise across groups?
Freddie A: We have had meetings with accelerator controls in the past, but these dropped off at some point, we can restart. I'd offered to host the next "EPICS Oxfordshire" meeting onsite for start of this year, but then as STFC were hosting a full collaboration meeting it was decided to postpone until later in year. 


## 😠😢😄 
- KB 😄 **Bluesky scripting** has gone really well so far, and I think the message from Diego asking for it on zoom is a great example of this ([diego.alba-venero@stfc.ac.uk via email: bluesky on Zoom](https://teams.microsoft.com/l/message/19:4e381ff6b5674230a74878b1355eec22@thread.skype/1743159129191?tenantId=3f66361c-a87e-4158-8f61-99e82db3cac8&groupId=d9946ec3-a454-424f-b673-5ffcb9f9ade0&parentMessageId=1743159129191&teamName=IBEX%20Developers&channelName=email-exp-controls&createdTime=1743159129191)
posted in IBEX Developers / email-exp-controls on 28 March 2025 10:52)

- TW 😄 We eventually had SECI free cycle!!

- CMS 😄 Teams for planning seemed to go very smoothly, should we be moving other meetings?
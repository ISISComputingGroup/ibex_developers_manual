# 2022-10-26

| Chair      | Timekeeper | Note Taker |
| :--------   | :---------: | ----------: |
| [Freddie Akeroyd](https://github.com/LilithCole) | [Jack Harper](https://github.com/rerpha) | [Lowri Jenkins](https://github.com/LowriJenkins) |

## Items from last retrospective.
 - G34 vs G06 - Opinion doesn't seem particularly strong either way.
	- Whichever is more convenient?
	- Current Booking is until Christmas.

## Items from this retrospective
- Uniforms
    - Conclusion is no

- Change to onsite rota One less person, do we want to change rota to rebalance it.
	- Yes we should before cycle
	- Perhaps a discussion for group meeting.
	- do we follow the one on teams or the one on the wall.
		

- Good first issues and Training
	- Implemented
		- Good first issues for basics
		- Training for still good training, but more complex than good first issue.
		
- Planning and Pre planning
	- Remove pre-planning until we start over-running on planning meetings again.

- Windows 11 builds
	- Whats FIT policy?
		- Doesn't exist yet?
		- Other IT departments starting to move
	- Instruments are Win10 we can just say this is what we support
	- It would be nice to know if something is fundamentally broken
		- we won't be fixing it for a 6months - a year
	- Perhaps just test squish and system tests on win11 with a win10 built client
		- have to be occasional due to squish license
			- squish only takes an hour though, so should be schedulable
	- full build node note really needed at the moment, as we're unlikely to have developers or instruments on it.

- Laptop and Desktop
	- weak laptop at home to remote into work desktop?
		- easier to not forgot.
	- do we need a machine we can take down to hall if we only have desktops on site?
		- we do, but need to do an inventory on them/IT equipment in general.
			- do we have enough build nodes?
		- we also have a little tripod table so you can use it to put laptop on where you are.
	- win11 laptop talks to win10 fine over remote desktop


- cake with Mantid
	- generally happy with the idea?
	- only concern is some people on Mantid are entirely remote and might be left out?
		- how do we avoid them and us scenario for people working remotely?
		- do benefits outweigh this or not?
	- Discussion with people from Mantid would be necessary to handle this would be wise.
		- potential approach for hybridization?
		- breakdown of how many people remote vs local?
		- if were meeting with accelerators, do we cycle between them etc?
			- periodic "joint coffee"s perhaps
	- Do we want something similar with accelerator controls people as well?
		- That might be useful since they are epics newcomers
		- do they have coffee meetings or the like?
			- they might all be on site on Wednesdays?

- Previously running column
	- relatively new, (this or last deploy?)
	- could the version and previous version be automatically be on the wiki page?
		- irrelevant to whether or not we actually want to display that information on the front page of ibex
	- Table is already noisy and cluttered, its potentially useful, but is it useful enough to clutter this table more
		- the page itself is noisy and cluttered, not necessarily specific to that table
		- The quick summary of how many release notes to check is useful
		- should it be on a separate page?
			- Instrument details pages?
	- Scientists will rarely want this, but if they do are likely to cause trouble if they can't find it.
		- instrument pages horrendously out of date and unmaintained
			- keeping it to homepage might be useful.
		- was it added for us or because scientists wanted it?
			- uncertain.
	- Add links to instrument names to instrument page and put it there?
		- Should we be updating instrument pages?
			- Info is still useful just go through it with the mentality of "when was this migrated, how old is this page"
	- Return to this discussion, currently undecided.
	- perhaps add a link to the deploy wiki page on where to find the previous version in logs after an install if you forgot to check?

- Merging Ibex.wiki and developers manual?
	- project manager vs technical
		- how often do scientists search the wiki?
			- user manual doesn't know what version is on an instrument,
				- needs time spent on it
	- helps to be able look in one place for information
		- however this is just for us, so if there's reason for it to be split then probably better to leave it as is.
		- possible that some information is in the wrong wiki.
	- for those who didn't know, wiki on the same repository as release notes.
		- this means that github search -> organisation -> wikis will find information on any of these.
	- possibility of website pointed at checked out search to git using git grep
		- or Docusaurus perhaps?
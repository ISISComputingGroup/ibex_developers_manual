# 2022-05-18

| Chair      | Timekeeper | Note Taker |
| :--------   | :---------: | ----------: |
| [@ThomasLohnert](https://github.com/ThomasLohnert) | [@davidkeymer](https://github.com/davidkeymer) | [@JackEAllen](https://github.com/JackEAllen) |

--- 

## Items from last retrospective

Cable Testers:
 - It would be good to know if we had dead cables before giving support calls.
 - Patch testing for Pearl
 - Possibly worth borrowing from SCD in short term but might be better to have our own.
 - Check with Anthony Shuttle for suggestions.
 - We're not network engineers, but useful to know that the cables we're bringing around work.

*Cable Testers have arrived and work quite well!*

Github Discussions:
 - How to use this compared with the wiki.
    - When the discussion is solved does it move to the wiki?
    - Perhaps ticket based discussions?
       - Discussions tickets are often organise a meeting about this topic, rather than just discussing it on github, using discussions wouldn't allow us to point it.
 - Private discussions probably only possibly at the organisation level or in a private repository.

 *Leave as is for the moment and remove if we can't find a use for it after a significant period of time has passed with no usage*

Should we continue drop in sessions in cycle:
 - We never really get many people, and when it is they often just ask about a support call.
    - Why do they not turn up at them, do they not find them useful or are they too busy etc. ?
       - Maybe they shouldn't happen in cycle
 - FIT don't seem to do them anymore or if they do we're not on the list.
 - They're less of a burden thanks to zoom.
    - We can ask the scientists if they want us to keep doing them at a meeting.
       - They are the customer so we should let them decide.
       - Might be a way to not spam them with emails once a month.

*A survey has been sent out to ask for feedback on this. We should have an answer by the next Retrospective meeting regarding whether we should continue with drop in sessions as they are or not.*

System Tests:
 - Still some transient errors, but they are actually passing occasionally.
   - Possibly autosave saving state or something similar?
   - At least we know they're mostly working now, so we can pay more attention to errors.

*Still seem to get transient errors, but far less frequent. Builds VHD broke on an update, but otherwise fine.*

This Sprint:
 - Test galil was very useful for the wish collimator debugging
 - Hopefully next cycle will be a bit calmer because no migrations.
    - Lets us focus on Win10 and other migrations for summer like TS1.

*The cycle has been quieter that the last with no serious issues such as the collimator. Support calls in the morning have become far less frequent.*

---

## Items from current retrospective

## Workflow

### Windows 10 and Other Migrations.
Win10 and other migrations should be one of the main focuses over the summer.

### Disk cleaning Automation
Time should be spent looking into using [@ChrisM-S](https://github.com/ChrisM-S) powershell script to automate cleaning of drives, moving over IOC logs periodically as part of a cron job. 

A discussion ticket should also be written up to discuss how we could automate truncating the database without affecting active runs.

### Splitting up GitHub Issues More Finely

A discussion took place about splitting up issues that involve writing IOC's, Emulators and systems tests as the work is usually always contained within 1 large issue. It was agreed to keep this as it is and change how we approach developing the IOC, system tests and Emulators and document the process in the wiki.

The process discussed was to write the minimum functionality required to have a working IOC with only one function, and system test and gauge how long it would take to write the rest based on the time required to write one function.
It was also agreed that development should be done in a way that allows for the work to easily be split into additional issues if needed. 

### Sprint Lengths
How we currently run sprints was discussed in relation to how we adapt the length based on cycles and support. It was agreed that [@KathrynBaker](https://github.com/orgs/ISISComputingGroup/people/KathrynBaker) will spend a couple of weeks looking into trialing a nested sprint where sub-sprints occur for each theme within the main sprint and present this in the next Retrospective.

### Support During Cycle
Support during the cycle has been eerily quiet...

### Beckhoff
Small Beckhoff in a box is missing? maybe on IMAT? 
Look into buying test license for Beckhoff.
Keeps hearing about weird errors from Beckhoffs - Pester motion control to get a fix.

## Equipment

New docks have arrived!

Network Cable Tester arrived works well!

---



# 2025-02-04

| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| TW    |            | JH         |

Present:
- In person: IG GR KB
- Online: JH TW ES CMS SC DK FA LJ LC JD

## Previous sprint

nothing - short sprint

## Current Sprint

### PI changeovers can be confusing
Christmas PI changeover was tricky - if there are any ideas to make this easier please suggest. 

### shared group laptop
it's very helpful (in fact it may even be another "excellent helper"?) to take to meetings and to the halls

### ticket priority
medium and low have been picked up ahead of high priority tickets this sprint. In this case the release tickets were dependent on each other, but that doesn't explain all of them. 
we should pick from the highest priority downwards regardless of if we want to do it or not. 

### putting code in the source code of the dev manual 
we should move these out to the _code_ repository, not the wiki repository, as they are a bit of a pain to see otherwise as you have to clone the wiki repository.

### manual system tests on release
are the statuses currently in place enough? should we split into `fail`, `fail - fix`, `fail - noted`? Yes. Issue proposed to do this and improve the template: https://github.com/ISISComputingGroup/IBEX/issues/8633

### build nodes
they are slow. we should axe off NDW1757, it's terrible. Can we have faster build nodes?
we could build over the network and split things client/server as servers have caches. The main bottleneck for build nodes at the moment is disk speed, perhaps we need more node. 
we could consider using dev machines overnight as jenkins nodes. Would have to be careful about soak testing etc. 
RIP NDW1757 

### feedback from scientists - confusing "instrument patching" / "ibex deployment" email 
can we combine these better so that its less confusing? 
we had the opposite request last time. 
we don't normally send out "done" emails as it's just extra admin. perhaps we should start doing so?

### galil-old is bad 
yes, it's bad, we should test the new one, it's hard to maintain and keep features up to date.
galil-old caused issues over the last release as it relies on VS2010.
the new galil driver isn't quite there yet, we need to test on CRISP (they're happy for us to do so)

### email sent to <check teams> unclear 
it was an old FIT email - we'll delete it.

### nice that we can pip install genie_python now
yes

### first line support
we should remind people who are on first line support the next week - we'll start doing this at standup.

### zipping up builds
Sophos is horrible and tries to read the millions of files that e.g. client builds are made up of - we should zip these up. 
we should also do this with the ibex backup from NDX to data-old. 
turns out we already do this! but we should make our nightly builds not bother with leaving the unzipped build. that will save a lot of files

### TwinCAT on developer machines
we should not bother installing it on developer machines, and leave NDXMOTION to run TwinCAT XAR so it can simulate Beckhoffs.

## Mad/Glad/Sad

glad - release done!

glad - pat testing done!

glad - interviews done! 

glad - we won't get timing system issues this cycle (allegedly) 

mad - the release was not fun

mad - partial derivatives and asymmetry is hard 




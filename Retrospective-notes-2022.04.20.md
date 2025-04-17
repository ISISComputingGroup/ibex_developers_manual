# Sprint retrospective notes 20/04/2022

## Items from last sprint

Stale Tickets:
 - We have warnings for long periods, perhaps there should be errors for even longer ones? to force us to look into ones that have been there for a long time.

2FA on on github:
 - Make sure every account we care about has it enabled because others will be kicked out.
 - Possibly send an email, though github may actually do this itself.
 - ISIS build does have 2FA.
 - Done.

Zoom contact details:
 - Check for old support number and remove it (just TS2 for now)
 - Print out new laminated ones
 - Its possible that the call queues are mangling caller ID, might need to test it.
   - Possible that if its forwarded from queue 1 to 2 it might say its from call 2.
   - This can cause issues with calling people back.
   - Some have caller ID and some don't.
 
Moving Wiki into the code repo:
 - Would be just moving the ibex wiki repository to the main repository.
 - Possibly hold off to evaluate a different solution that Jack is looking into.
   - Docusaurus, Jack may be hosting a talk on this.
      - Good built in search engine, same one as stackoverflow.

Graylog move to SCD cloud:
 - No updates to getting it working on SCD just yet.
    - Check with SCD cloud support.
    - Running in docker has been somewhat unreliable.
 - We don't currently have graylog running.

Moving IOC tests and emulators to support directory:
 - Happening on Friday.


## Items from this sprint
Cable Testers:
 - It would be good to know if we had dead cables before giving support calls.
 - Patch testing for Pearl
 - Possibly worth borrowing from SCD in short term but might be better to have our own.
 - Check with anthony shuttle for suggestions.
 - We're not network engineers, but useful to know that the cables we're bringing around work.
 - Possibly this:
   - `https://www.amazon.co.uk/dp/B07WRV3N5F/ref=sspa_dk_detail_0?psc=1&pf_rd_p=828203ef-618e-4303-a028-460d6b615038&pd_rd_wg=V07Nd&pf_rd_r=9DJ8RGN71F7P4VQGVWHY&pd_rd_w=2aYQS&pd_rd_r=4daea718-1c03-482c-89c5-3ae3a10df11c&s=diy&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOEhJUUNEMkxYVDhMJmVuY3J5cHRlZElkPUEwNTg1NzIyWlNNRlNINUlLT05XJmVuY3J5cHRlZEFkSWQ9QTA4NzIwNTYzTDFJN0Q0WlhJRjZBJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==`
    - More expensive but less risk of damaging things.

Github Discussions:
 - How to use this compared with the wiki.
    - When the discussion is solved does it move to the wiki?
    - Perhaps ticket based discussions?
       - Discussions tickets are often organise a meeting about this topic, rather than just discussing it on github, using discussions wouldn't allow us to point it.
 - Private discussions probably only possibly at the organisation level or in a private repository.

Should we continue drop in sessions in cycle:
 - We never really get many people, and when it is they often just ask about a support call.
    - Why do they not turn up at them, do they not find them useful or are they too busy etc. ?
       - Maybe they shouldn't happen in cycle
 - FIT don't seem to do them anymore or if they do we're not on the list.
 - They're less of a burden thanks to zoom.
    - We can ask the scientists if they want us to keep doing them at a meeting.
       - They are the customer so we should let them decide.
       - Might be a way to not spam them with emails once a month.

System Tests:
 - Still some transient errors, but they are actually passing occasionally.
   - Possibly autosave saving state or something similar?
   - At least we know they're mostly working now, so we can pay more attention to errors.

This Sprint:
 - Test galil was very useful for the wish collimator debugging
 - Hopefully next cycle will be a bit calmer because no migrations.
    - Lets us focus on Win10 and other migrations for summer like TS1.
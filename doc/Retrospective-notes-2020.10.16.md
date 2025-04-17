### Last retro

- We should remember to leave notes for the reviewer
- John will make a page for undocumented features
- We should put emojis next to the email in teams to say we are handling the email
- We should always reply from experimental controls where appropriate rather than our own email
- Freddie will bypass footprints and send directly to experimental controls mailbox for SANS or the Muons
- Dom to check if ticket for script generator testing environment (Ticket is [here](https://github.com/ISISComputingGroup/IBEX/issues/5701))

### As per an article in in.brief from HIFI. To quote: `Thanks to the work of the ISIS computing team, the group were then able to access the computers that control the beamline, turning their office into a replacement hutch for the week` so the solutions we put in place are being acknowledged, and are proving useful

Chris MS: Yes, nice to get that warm fuzzy feeling - notes of diamond and a hint of rabbit too

### Just a note to recall that technical chats should happen in the technical channel, as it gives people the option of dropping in if they have something to contribute or want to learn about something. It also provides an indication as to whether the conversation has been had or not so that we can see that the help has been given if needed, or not as the case may be

We should make an effort to move private chats to technical where appropriate. Though we often do this, the more effort to do so should increase knowledge sharing and allow people's input who may otherwise not be involved.

### [10/6 12:33 PM] Oram, Dominic (STFC,RAL,ISIS)

Tom, John and I had a discussion about the best way to treat patches that instrument scientists send us for general IBEX code. With a view of wanting to expedite these to encourage scientists to work with us we thought the process should be:

There must be a ticket created with the code attached in some way:

- This ticket is a support ticket as we're supporting the scientist in getting their code into IBEX but is therefore 0 points
- The ticket goes straight into review and is reviewed by one of us in the usual process
- If we're happy then it's merged, if not we put it as rework and ask the scientist to do the rework. If the scientist is not happy doing the rework we will propose it as usual for one of us to look at

I'm trialing this process with [#5776](https://github.com/ISISComputingGroup/IBEX/issues/5776)

[10/6 4:20 PM] Woods, Kevin (Tessella,RAL,ISIS)
I think this is a good idea, but I have a couple of queries:

- Is it really a 0 point ticket?  If it requires anything other than a trivial amount of effort, then it is not a 0 point ticket.
- Scientists don't always consider the wider picture.  Their solution might work for their particular needs, but often it won't easily generalise or may not be maintainable.  We should take care not to accept code that generates a high maintenance overhead.

Yes we agree, though it should not be a 0 point ticket.
Dom will write this process onto the wiki. Done [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/External-Contributions).

### As well as when preparing new instruments we should probably consider IBEX and genie_python training more regularly as a reminder and most especially for new starters

When we do IBEX training we should invite others than the targeted instrument. We should also run a yearly training course to catch any new starters and others that feel they need training.

### We now have support calls coming in via a number of channels - e-mails (whether direct or to ISIS Experiment Controls), Teams, phone calls (and Zoom voice-mail messages).  Should we have someone who is responsible for making sure each incoming issue is assigned to an individual for investigation & resolution?  The task could be done on a weekly rota basis (like the role to run the daily stand-up meetings - in fact, it could be done by the person running the daily stand-up meetings)

Traditionally this has been done by the "ISIS supporter of the week" who is also the on call person in the evening, but including more people in the role is probably a good idea

[Monday 10:15 AM] Woods, Kevin (Tessella,RAL,ISIS)

OK.  In that case, maybe all it needs is for the "ISIS supporter of the week" to make it clear that incoming issues have been assigned and/or are being dealt with.  Perhaps just a quick message in Teams?

There is a supporter of the week who should make sure everything is being handled. This is not necessarily to handle it themself, but to ensure someone has taken an action. Supporter of the week should put emojis on the dealt with emails in teams if the person handling it has forgotten.

We should all log into zoom when we start work so we can pick up calls. Freddie will move the zoom call hours to be 10-5.

### nagios being extremely slow often slows down standup while we wait for it to load. Could we get nagios moved to a faster server?

It's very * 3 painful.

It is on the list of things to move onto better servers.

We will leave it as it is and just handle it at standup.

### I really like the oversight that we get with people using the ISISExperimentControls email address. Can we expand it more to include things like the discussion being had with PEARL about migration?

This would enable sharing of information between us.

John thinks that we should trust everyone to do work and then ask if help is needed and write docs to summarise. This would avoid clutter and noise on the email. We should add any information and conversation from emails onto the ticket.

Conclusion: If a ticket has been written from an email chain then we should put it on the sharepoint and link it.

### We have a number of tickets that are still on the board, have had little movement and we just move from sprint to sprint. Even worse there are tickets in the backlog that have had work done on them a while ago but no subsequent movement. This makes me sad because it feels like we have a lot of half finished jobs that we are close to being able to call done but not quite. How can we get these tickets over the finish line? If the people that were doing them are now busy can we assign others to just finish them off? Could we do a tech debt day on just going around and finishing these tickets?

Kevin: Seconded, Attached is a list of the tickets marked as "in progress" today (13th October).  I have highlighted in red tickets that have been "in progress" since before the current sprint (I strongly suspect these tickets are not actually making any progress).  I have highlighted in yellow tickets  from the current sprint that have been "in progress" for over two weeks.

We still have some tickets like this. There have been some tickets in the backlog that were not on the board but were actually complete. There are also tickets out there we need to document and test but were "completed" a long time ago, we should not be afraid to admit we don't have the time and ask for someone else to finish it off for us.

Let's create a label saying "I don't have time to finish this can someone else pick it up" which means we don't have to take people's face off them. Done, see "To pick up" ticket.

Lets check the in progress for stale tickets.

### We've done most of a cycle with users on python 3 :)

Yes! :)

There were a few wobbles.

### We have been hitting our target for points done in a sprint more since we can see the burndown chart

Yes!

It can feel artificial and a bit micromanagementy. It is also not truly accurate.

Some feel more motivated because you see progress.

Reminds us if there's loads of support tickets we haven't put through.

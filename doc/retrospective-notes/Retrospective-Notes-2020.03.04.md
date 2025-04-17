# 2020-03-04

## We should update component stewards

Yes, this was missed after the last retrospective. Some combination of James, Kathryn and John to do.

## Squish licenses

- We are happy with what we have for the budget we have
- Floating licenses/more licenses will cost more

## There are lots of tickets completed 👍 There are lots of tickets also in ready 👎 

- Possible reasons:
   - Lots of support tickets (1/3rd of the sprint)
   - Lots of tickets leftover from EMU rush
- We are not extremely unhappy about this as we got a lot done, but it would be good to manage it better

Suggestion: To encourage throughput we prioritize reworks and reviews over current tickets as well as new tickets. 

- Pros
   - These reworks and reviews are likely a higher priority than our current ticket so it fits in with our prioritization
   - It should encourage tickets to not hang around in ready and review and decreases their time from ready t complete
   - May encourage people to document their progress more on a ticket when they are recording what they have done prior to switching to a rework
- Cons
   - More context switching
   - Switching state of a machine from one ticket to another takes time

Conclusion: This cannot be a blanket rule as there are many edge cases. For a sprint, we will try this. People should find a practical stopping point in their current ticket to do a rework if the situation arises. The metrics to decide on this will be: does everyone hate it? Has our throughput increased?

## Should we create support tickets for all work for all instruments (SECI and IBEX) whether in cycle or not and whether we're contacted individually or not

Yes, within reason.

- The documentation is useful for future issues to create context
- It should be recorded as support, otherwise, it seems we are pulling in tickets without the proper process
- Helps to capture our effort
- Support is defined as: if a scientist needs help
- SECI tickets should be recorded only if they are of relevance to IBEX
- If a support call took very little time e.g. writing the ticket would take more time it may not be worth it
   - It stops being time-effective or useful to others
- If a support call is one of a common theme we should record all them together as a tally to identify areas of the system we should improve

## We should demo more in sprint reviews

Yes, we need to take steps towards this.

- DEMO should be deployed to earlier to give people a chance to set up their demo
   - There is now a reminder for a few of us to remind the group we need to deploy at the start of the week so it is organised earlier
- We don't necessarily need to demo on DEMO it can be on our own machine
   - Though demoing on DEMO can be useful to point out issues surrounding performance, state that we did not experience on our own machine etc.
- It is a good chance for a dress rehearsal prior to scientist demos (we are a more forgiving audience)

## Should we try again with inviting scientists to sprint reviews? Relying on "proxy" product owners has failed multiple times recently

- We are happy with the current process of having separate scientist demos.
- Getting them to come is difficult and would extend reviews a lot.
- However, we should be more strict in demoing to scientists.
   - We should organise these as part of the release (added to the ticket template)

## Clean up after upgrade

Upgrade process was leaving a trail of mounted network disks. Upgrade scripts should clean up after themselves.

There is a ticket for this. https://github.com/ISISComputingGroup/IBEX/issues/5208

## Dashboard bug: This was an unnecessary own goal. Why did our testing (system, automated, manual) not catch these?

Reasons why it wasn't caught:
- Wouldn't have been seen unless we had neutrons 
- We haven't got 100% coverage
- The push for EMU made us rush
- Mistakes can be made
- Our simulation isn't very strong for pretending we have neutrons

Actions:
- We should be more aware to use TDD 
   - It is noted that it is difficult to know what to test on legacy code and that it is easy to spot a bug when you know what bug you're looking for
- If we demoed it may possibly have been caught, we should be more strict with demos

Positives:
- We were fast and reactive with our fix
- We are more aware of this now and know we should be more careful in testing and reviewing

## EMU: Switch back to SECI failed because of the presence of 32-bit Open Genie components. Is it likely to occur on other muon instruments? How should we avoid?

- This is now fixed
- There may be more banana skins
- As part of our migrations, we should test that we can go back and plan for a possible switchback
   - This has been added into the steps here: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Migrate-an-Instrument-Control-PC
- This was tricky to catch
- We should have a set of standard things to test across similar instruments e.g. motors for refl and start/stop for every one

## Linter is perceived as slow by some instruments. The linter may not really be slow, but is perceived as such by some instruments. How can we make ourselves more conscious of performance?

- We have a ticket and ideas for speeding things up. https://github.com/ISISComputingGroup/IBEX/issues/5210
- HDDs rather than SSDs have slowed us down here, there is a plan to upgrade.
- Manual tests should have time limits.
- Demoing and testing on demo should help us with this.
- We should try to be aware of how our code changes performance.
- Memory leak has added to this concern
- We should consider writing more squish performance tests
- We should check with the SAG how important they think performance enhancements are
- ScriptServer may help with the speed
   - We should add linting to the script server

## Make a standard email to send release notes out when we make a release. Release process should include sending this out.

Yes, added to the process in https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release

Standard email format (not necessarily a good email, please consider it's contents): https://github.com/ISISComputingGroup/IBEX/wiki/Instrument-scientist-release-email

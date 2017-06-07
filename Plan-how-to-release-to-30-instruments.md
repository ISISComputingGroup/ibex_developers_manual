# Plan how to deploy automatically on 30 instruments

## Preface

This document is related to Ibex issue [#2152](https://github.com/ISISComputingGroup/IBEX/issues/2152) and the content is from the subsequent discussion on 30th May 2017.

## Existing issue

We currently create a new release of Ibex roughly once per cycle. This is largely owing to the time overhead associated with creating a new release. This means that we don't reliably and regularly build releases, and it has also led to issues around getting releases ready for the correct point in cycle.

## Goals

The goal of the discussion was to answer the following questions:

- How often should we be releasing
- Should we always release to all instruments
- How should we generate releases
- How do we ensure the quality of our releases

## Discussion notes

*Based on meeting from 30th May*

### How often should we be releasing
There is a question of whether we need a separate process for patching an instrument versus creating a full release. The general consensus was that releases should be quick to generate and so creating a patch release should be straightforward. This can be done at any point during the sprint. For more immediate fixes, our current process of applying and documenting hotfixes on the fly is sufficient.

We discussed our current situation and decided that we should aim to produce releases at the end of each sprint. This is achievable in principle but raises a number of issues that we should consider moving forward:

- The current release process is too long to dedicate the necessary time to it every sprint. This needs to be addressed to move towards this goal.
- Sprints and release cycles don't always coincide. Even when they do, the end of a sprint may be too close to the start of cycle for instrument scientists to be comfortable with new releases being put on their instrument. This is not necessarily a problem, but it does mean that we have to carefully monitor how sprints and cycles align so that essential tickets can be implemented in the necessary release.

### Which machines should we deploy to?

Although our release and deployment process should allow for straightforward deployment to all 30 instruments, we don't necessarily want to release to all instruments at the same time. We may want to put the latest release on a subset of machines so that any issues can be detected without affecting all instruments. Other instruments would be updated to the latest but one release so that no machine should become out of date by multiple releases. There were several suggestions for which machines to release to:

- Half. Each half of instruments would jump forward every other sprint. The latest release would have to be pushed to instruments that require critical new functionality
- Those that need it. The instruments that need the latest release owing to bug fixes or new IOCs would be given the latest release. Other instruments would be updated to the latest-but-one release.

There wasn't a decision on which of these would be preferable.

### How should we generate releases

The build process was not discussed in depth. The feeling was that Jenkins is currently sufficient for generating releases. Our limiting factor is currently the time taken to go through the manual system testing list. The best way of reducing this time would be to automate more of the tests. Whilst this is feasible, we have made little progress owing to tests generally being added for new, rather than existing functionality. It was agreed that significant time should be invested to automate as much of this list as possible. The first step will be to have a day-long stand down where the whole team will work on automating these tests.

### How do we ensure release quality

There are many options available to us to ensure release quality. Many parts of the system are only partially tested. In the long run, we'd like to increase coverage on all of these but it makes sense to prioritise those that are going to deliver the best return on investment.

The feeling is that the GUI is easy to patch and re-release if necessary and will already receive significant testing through the automated system tests. Perhaps the most effective use of time would be to expand the number of tests in the IOC test framework. This could be done incrementally. There is a low risk to functionality which is already confirmed as working if it remains unchanged. We should add emulators and IOC framework tests to IOCs as they are changed. This does mean that additional consideration should be made when estimating the size of IOC tickets. Even a small change to an IOC could involve writing a simple emulator and a range of IOC tests.

One aspect of the system we don't currently test much are the OPIs. These should also be tested in the future using automated system tests. This is now feasible given the improvements to automatic emulator port assignment. This would provide less return than new tests in the IOC test framework, particular given the ease of changes to OPIs on-the-fly in the event of a bug.

## Plan of attack
- We have discussed a number of issues around sprint planning. These will be considered in subsequent sprints
- [Ticket #2377](https://github.com/ISISComputingGroup/IBEX/issues/2377) has been created for a stand down to continue automating our existing manual tests. The impact of this will be reviewed at a retrospective.
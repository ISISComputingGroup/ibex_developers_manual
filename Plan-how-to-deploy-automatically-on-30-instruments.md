# Plan how to deploy automatically on 30 instruments

## Preface

This document is related to Ibex issue [#2152](https://github.com/ISISComputingGroup/IBEX/issues/2152) and the content is from the subsequent discussion on 24th May 2017

## Existing issue

We are faced with a number of issues in supporting a product that needs to be simultaneously deployed to 30 different instruments within a 2-week shutdown. Several tasks are typically conducted during shutdown:

- Backing up the existing system
- Applying OS patches
- Upgrading Ibex, which includes
    - The server
    - The client
    - genie_python
    - MySQL
    - Ibex settings

This typically takes on the order of several hours per instrument in the best case, but longer if significant changes need to be applied, particularly to settings. Doing this process manually for 30 instruments will require high levels of team resource to complete during a shutdown. A lengthy deployment process also precludes any possibility of rolling out urgent changes mid-cycle.

A further issue is that the current NDX[INST] systems are VMs that vary significantly in their system setup. This makes maintaining them more difficult and the chance of system-specific issues more likely.

## Use cases

The following use cases were identified for supporting Ibex deployment to instruments:

- Deploy Ibex to a new instrument
    - Instruments with SECI already running
    - Newly commissioned systems that don't have any existing control software
- Full release update to a current Ibex instrument
    - This must include post-installation updates such as configuration format updates
- Patching a hotfix to an existing instrument

## Goals

These are the general properties we expect the proposed solution to have:

- Fast: The solution must be sufficiently quick that it can be done on 30 instruments within a 2-week shutdown. Ideally it would be significantly quicker. I would expect a full release should be achievable in under around 30 minutes
- Minimal user input: Although deployment time may be constrained by data transfer speeds, the process should be able to proceed with minimal user input.
- Parallelisation: Multiple machines can be deployed simultaneously so that overall deployment time does not scale linearly with number of instruments.
- Consistent: The solution should produce a consistent deployment that can be relied upon to be functional with minimal manual tests

## Constraints

The long-term goal is to support only Ibex and fully retire SECI. We recognise that owing to ongoing instrument requirements, this is not feasible in the short term. Instruments converted from SECI to Ibex must be able to roll back to Seci and a retirement plan agreed with the scientists. However, we should attempt to expedite this process, particularly on those instruments that have been running Ibex for more than a cycle and are comfortable with the new system.

## Current deployment architecture

![Deployment architecture](architectural_design/images/High-Level-Architectural-Design/deployment_architecture.png)

## Discussion notes

## Plan of attack

## Next steps
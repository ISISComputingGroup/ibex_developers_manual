# ADR - 12 - Forwarder Channel Access Bug Solution
## Status
Pending
## Context
The forwarder currently in use to send information from PVs to the file-writer relies on `caproto` to handle reading channel access PVs. `caproto` has a bug that prevents reconnection to a pv that has dropped and therefore needs to be replaced by a different library. This could be achieved in a couple of different ways. `PyEpics` is relatively similar to `caproto` and supports threaded operation, so a refactor to replace `caproto` with `PyEpics` and refactor any sections heavily tied to `caproto` could be undertaken. On the other hand, `caproto` could also be replaced with `aioca`, unlike `caproto` and `PyEpics`, `aioca` is an asynchronous system, this would require far greater changes, likely a full re-write rather than just re-factoring but async is usually better suited to IO tasks that are slow or ones that have a large number of connections (such as setting up a large number of PV monitors.) A full rewrite would also present the opportunity to prune some content from the forwarder which is present only for the ESS and would not be used at ISIS.

Another solution would be to use the existing forwarder but ensure it never has to connect to channel access IOCs. It is not within the scope of this project to replace all channel access within our control system with PV Access, however, the program `PVA-i-fy` could be used as a bridge between the forwarder and any channel access PV's. Testing with `PVA-i-fy` shows that it can gracefully handle reconnecting to dropped channel access PV's (including large numbers of PV's, or after a time delay.), and while slightly less graceful in some cases, it can also relatively easily handle PV's having changed data type while disconnected (important for handling of blocks). This would be a far simpler solution than both a re-write, or refactor, as it would only need the deployment and setup of `PVA-i-fy` alongside the forwarder. `PVA-i-fy` is designed to take channel access PVs on one network, and output PVA on a different one, and this can simply be locally on a machine, thus `PVA-i-fy` could in theory be deployed on either the data-streaming machine, or the NDX. `PVA-i-fy` runs natively on linux, and ships with a .sh file to start it, so would be easier to configure on linux, however, the code is java and it appears to work correctly on windows provided a batch file replacement is provided. Running on windows on the NDX would allow us to use `PVA-i-fy` to serve other systems that would benefit from all of our Channel Access PVs running in PVA.

## Decision
We will make use of `PVA-i-fy` to bypass use of `caproto` and allow the forwarder to only interact with PV Access.
- `PVA-i-fy` will run on the NDX to allow other use-cases of PV Access.
- The forwarder itself should need only changes to the forwarder-configurer to work with this.
	- The forwarder will remain otherwise unchanged.

This Decision was reached as it will be far simpler than either option involving changes to the forwarder, and also allows the use of PV Access for other currently only channel access systems. It also means we can continue to make use of the ESS' effort that went into the current forwarder without having to re-invent the wheel.

## Consequences
- A ticket/tickets will be created to setup ansible deployment of `PVA-i-fy` on the NDX machine and working out the necessary configuration `ini` ,`pvlist` and potentially `.acf` (IOC access security?)
- A ticket will be created to setup forwarder-configurer to ensure the forwarder works properly with the PVA PVs
- A ticket will be created to ensure the gateway is setup correctly to handle the duplicate PV's created by having a CA and PVA version.

--- 

Looks like PVA-i-fy handles the issue well, and it would definitely be more time efficient.

# ADR - 12 - Forwarder `aioca` vs `PyEpics`
## Status
Pending
## Context
The forwarder currently in use to send information from PVs to the file-writer relies on `caproto` to handle reading channel access PVs. `caproto` has a bug that prevents reconnection to a PV that has dropped and therefore needs to be replaced by a different library. This could be achieved in a couple of different ways. `PyEpics` is relatively similar to `caproto` and supports threaded operation, so a refactor to replace `caproto` with `PyEpics` and refactor any sections heavily tied to `caproto` could be undertaken. On the other-hand, `caproto` could also be replaced with `aioca`, unlike `caproto` and `PyEpics`, `aioca` is an asynchronous system, this would require far greater changes, likely a full re-write rather than just re-factoring but async is usually better suited to IO tasks that are slow or ones that have a large number of connections (such as setting up a large number of PV monitors.) A full rewrite would also present the opportunity to prune some content from the forwarder which is present only for the ESS and would not be used at ISIS.

## Decision

We will rewrite the forwarder to make use of `async-io`:
- Channel Access will be handled using `aioca`
- PV Access will be handled using `p4p`'s async mode.
- Sections irrelevant to ISIS (`tdct`, previous versions of `serialiser.py` files, etc.) will not be carried forward.
- Kafka interactions will be handled by `aiokafka`
- The external facing interfaces such as Kafka schemas, serialisation, and forwarder configs will not change.

This decision was made to allow for better handling in situations where large numbers of PVs are in need of forwarding, especially when changing configs. While threading may be enough to handle smaller number of PVs it could cause slow-down for large numbers of PVs unless a thread is made for each individual PV to be setup, and doing so would cause high memory usage due to the overhead required per thread. As the performance would be too slow without either threading or async, and as we expect to require a greater number of PVs in future, re-writing to make use of async will save us having to do this later.

## Consequences
- A new repository will be opened called async-forwarder
- An Issue/Issues will be created to begin creation of the new async-forwarder.
- async-forwarder is tested with the same inputs against forwarder to ensure same outputs.
    - async-forwarder is tested against the bug that was the initial cause for this re-write.




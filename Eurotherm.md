The eurotherm is one of the most common temperature controllers at ISIS. Most beamlines have at least one eurotherm if not more.

# Gotchas

- If the protocol timeouts are increased too much the IOC will go into alarm states as some scans depend on the timeout. Do not increase the timeout beyond the tested value in the protocol file!
- The eurotherm protocol uses variable terminators.
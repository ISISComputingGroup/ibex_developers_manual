The eurotherm is one of the most common temperature controllers at ISIS. Most beamlines have at least one eurotherm if not more.

# Protocol

The eurotherm protocol has variable terminators, but also depends on it's timeouts for the device to operate properly.

If the timeouts in the protocol are increased, the device will go into alarm states whenever setpoints are sent and the device will not work properly (also, the IOC will appear to take a long time to start because it sends lots of commands at startup).
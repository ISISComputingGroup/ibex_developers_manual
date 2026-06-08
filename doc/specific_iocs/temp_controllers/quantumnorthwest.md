# Quantum Northwest (NeutronIQ)

This device is a temperature-controlled multi-cuvette holder.

It is controlled by the `QNW` IOC, which supports all `TC-1`-based Quantum Northwest temperature controllers.

Temperatures of all cuvettes are controlled by a single temperature control loop, so the device only has a single
"temperature" and "temperature setpoint", not channels.

The device defaults to sending many messages asynchronously; a periodic scan task turns off most asynchronous messages,
in favour of explicit polling.

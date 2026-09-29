# Nanodac

The "Eurotherm Nanodac" controller (not to be confused with a {doc}`Eurotherm` controller) is a temperature controller.

It talks via standard Modbus/TCP; our IOC is based on support imported from ORNL.

## Control loops

The Nanodac can be configured using two "loops", and an "advanced loop". The "advanced loop" allows multi-channel {abbr}`master/slave configurations (This is the terminology used by the device itself)`.

The "advanced loop" only has very basic support implemented: changing the setpoint. The simple loops additionally allow control of e.g. PID settings.

## Modbus data types

Modbus allows reading from two areas: a 'scaled integer' area, and a floating-point area.

The formula to translate a "scaled integer" address to a "floating-point" address is {math}`32768 + (A_{integer} {\times} 2)`. The list of scaled integer addresses is given in the manual.

Note that the scaled integer area will fail to correctly read temperatures or other readbacks above {math}`327.68` for a channel with 2 d.p. of precision.

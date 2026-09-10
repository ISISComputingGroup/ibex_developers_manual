# Keithley 2400

The Keithley 2400 is a multimeter, there are various Keithleys with different models numbers which do different tasks.

## Troubleshooting

### Termination character

If a new Keithley won't talk to you then maybe you have one with a different terminating character. There is a configuration macro for setting it set both `IEOS` and `OEOS` options are `\\r` or `\\r\\n` (the extra slash is because of macro substitutions).

### Voltage, current and resistance aren't reading

The Keithleys output mode needs to be set to on. This can be done by setting Source On, on the Source mode OPI tab or doing `caput %MYPVPREFIX%KHL2400_0X:OUTPUT:MODE:SP ON`.

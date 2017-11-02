The Keithley 2400 is a multimeter, there are various Keithleys with different models numbers which do different tasks.


## Troubleshooting

### Termination character

If a new Keithley won't talk to you then maybe you have one with a different terminating character. There is a configuration macro for setting it set both `IEOS` and `OEOS` options are `\\r` or `\\r\\n` (the extra slash is because of macro substitutions).

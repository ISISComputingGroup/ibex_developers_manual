The Keithley 2400 is a multimeter, there are various Keithleys with different models numbers which do different tasks.

## Keithley 2410

This model has come up on HRPD and required a change of termination character to `\\r` and baud rate to 9600. It also required the following protocol changes (replacing the current `get_V` and `get_R` as is done with the 2420):

```
# /// Read the voltage from the data string. Format is %f (V), %f (I), %f (R), %f (Timestamp), %f (Status)
get_V {
   ExtraInput = Ignore;
   out ":MEAS:VOLT?";
   in "%f,%*f,%*f";
}

# /// Read the resistance from the data string. Format is %f (V), %f (I), %f (R), %f (Timestamp), %f (Status)
get_R {
   ExtraInput = Ignore;
   out ":MEAS:RES?";
   in "%*f,%*f,%f";
}
```

## Troubleshooting

### Termination character

If a new Keithley won't talk to you then maybe you have one with a different terminating character. There is a configuration macro for setting it set both `IEOS` and `OEOS` options are `\\r` or `\\r\\n` (the extra slash is because of macro substitutions).

## Spectra

The DAE serves spectra information via the following PV format
```
$(P)DAE:SPEC:$(PERIOD):$(SPEC):X
$(P)DAE:SPEC:$(PERIOD):$(SPEC):Y
$(P)DAE:SPEC:$(PERIOD):$(SPEC):YC
$(P)DAE:SPEC:$(PERIOD):$(SPEC):C
```
Where SPEC is the spectrum number, PERIOD the period, X is the time-of-flight axis values, Y is the counts / microsecond (i.e. divided by bin width), YC is just counts, and C is total counts for that spectrum (summed over all time-of-flight bins) 
  
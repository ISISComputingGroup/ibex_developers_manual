## Spectra

The DAE serves spectra via the following PV format
```
$(P)DAE:SPEC:$(PERIOD):$(SPEC):X
$(P)DAE:SPEC:$(PERIOD):$(SPEC):Y
$(P)DAE:SPEC:$(PERIOD):$(SPEC):YC
$(P)DAE:SPEC:$(PERIOD):$(SPEC):C
```
Where SPEC is the spectrum number, PERIOD the period, X is the time-of-flight axis values, Y is the counts / microsecond, YC is just counts for that histogram bins, and C is total counts for that spectrum
  
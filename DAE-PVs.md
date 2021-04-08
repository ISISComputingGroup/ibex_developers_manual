## Spectra

The DAE serves spectra information via the following PV format
```
$(P)DAE:SPEC:$(PERIOD):$(SPEC):X
$(P)DAE:SPEC:$(PERIOD):$(SPEC):Y
$(P)DAE:SPEC:$(PERIOD):$(SPEC):YC
$(P)DAE:SPEC:$(PERIOD):$(SPEC):C
```
Where SPEC is the spectrum number, PERIOD the period, X is the time-of-flight axis values, Y is the counts / microsecond (i.e. divided by histogram time bin width), YC is just counts in each bin (i.e. not divided by time), and C is total counts for that spectrum (summed over all time-of-flight bins). So X, Y and YC are arrays and C is a single number. X represents time bin boundaries, so if there are `N` histogram time bins there will be `N` values in `Y` and `YC` and `N + 1` values in `X`. The size of the waveform array can be determined from the `.NORD` PV field e.g. `X.NORD` 

A spectrum number exists for every detector (pixel) and monitor. In addition the scientist can associate a "monitor number" (starting at 1 and increasing sequentially) with each spectrum number that is associated with a monitor. The monitor data can then be accessed via additional PVs that have the same general format as above but used the prefix `$(P)DAE:MON:$(PERIOD):$(MON_NUM)`. So for example if monitor number 1 is spectrum number 1234 then the counts per unit time can be accessed as either `$(P)DAE:SPEC:$(PERIOD):1234:Y` or `$(P)DAE:MON:$(PERIOD):1:Y`. There are no corresponding `:DET:` names for detectors, they are always accessed as `:SPEC:`. The `:MON:` mechanism is a convenient alias for monitors, but provides no additional information to using `:SPEC:`. Some instruments can change their detector setup between experiments and depending on how they have assigned spectrum numbers this may result in a different `:SPEC:` being needed for each monitor. So using `:MON:` is usually safer.    

For most instruments `$(PERIOD)` will be `1`, however some instruments scan their devices and detector/monitor data at each scan point can be accessed via using a different value of `$(PERIOD)`. SANS, reflectometry and muon instruments regularly use multiple periods, most other instruments only occasionally if at all.

Monitors and detectors are stored separately in the NeXus data file and when this is read into Mantid a separate workspace is created for each. If periods have been used, then a "workspace group" is created. Workspace indexes always start at 0, the actual spectrum/monitor number will be stored in one of the workspace axes. As monitor numbers always start at 1 and increase numerically, index 0 of the monitor workspace will always be monitor number 1 etc. The same does not apply to the detector workspace i.e. index 0 there is not guaranteed to be spectrum 1 as if spectrum 1 is a monitor it will not be present in that workspace.   

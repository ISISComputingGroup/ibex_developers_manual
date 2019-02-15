> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers) > [Reflectometry Testing](Reflectometry-Testing)

This is a record of some of the things I have tried and done on CRISP in Feb 2019.

### Setup

Scan in sample and align beam in SECI.

Copy scan.py from LOQ to CRISP to allow in IBEX plotting. Sort out a crisp package and alter the init so that it loads it.

**Issue** I can not see how to reload my changed code while developing my scan except to restart the scripting window (which is non-ideal).

Ideally, this code should be in `crisp_inst.py` but I haven't put it there yet this is to load in the scanning library:

```
from general.Scans.Scans import *
```

### Theta scan

After the final align of the beam you should perform a theta scan to ensure that the beam is aligned.

```
scan("THETA", -0.05, 0.05, count=21, frames=100, fit=Gaussian)
```

which produces ![Theta scan showing a peak at 0.0](reflectometer\theta_scan.png).


### Sample alignment

After aligning with the laser:

1. Perform a shadow scan (this is only possible if your sample absorbs/scatters neutrons silicon does not). I could not do this with the sample I has.

1. Perform a shallow bounce scan. Set theta to a small angle (0.25) then tilt phi to find the peak in intensity. Start with widish slits otherwise you will not see anything. Command is `scan("PHI", 0.22, 0.28, count=21, frames=200)`




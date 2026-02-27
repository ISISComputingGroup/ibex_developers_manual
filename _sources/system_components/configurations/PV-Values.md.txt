# PV Values

PV values are set by the `icpconfig` code in two phases:

### Static DB access

This attempts to run between autosave and PINI. This phase is **only** important for records with PINI=YES.

Note: internally, the static PV access library required you to specify the field - it will not default to .VAL for you. There is some code in icpconfig to do this.

### Dynamic DB access

This attempts to run after the IOC is started. However, it works inconsistently for records with PINI=YES because you get a race condition between PINI running and the value being set.
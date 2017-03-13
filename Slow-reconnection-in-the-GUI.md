This document is based on the findings of [#1971](https://github.com/ISISComputingGroup/IBEX/issues/1971).

# Running on the local machine (NDXDEMO)

IOC off for between 12 and 24 hours typically gives the following results:

Camonitor connects after <5 seconds
Vanilla CS-Studio 3 and 4 OPI < 30 seconds (only one PV on OPI)
IBEX OPI ~1 minute

The different fields on the IBEX OPI reconnect at different times.

# Running on the local machine (my PC)

Similar except the IBEX OPI can take significantly longer sometimes (> 40 minutes!)

Could this be related to excessive IOC log production on my machine?

# Client running on a different machine to NDXDEMO

The client and camonitor can take a long time to reconnect, anything from a few seconds to 5 minutes.
Disabling the gateway on NDXDEMO and running a client/camonitor on the same subnet (i.e. no gateways involved) connects much quicker.
Note: this was for a spectrum data PV.

# Conclusions

ISSUE 1: Something about the gateways means that remote clients don't respond well to IOCs turning off then back on. Though starting a new client usually connects straightaway.

ISSUE 2: IBEX’s OPIs take longer to reconnect than vanilla CS-Studio does. The longer the IOC is off the worse it tends to be.
    * Is it because IBEX is doing a lot generally, e.g. logs, blocks, etc? 
    * Could it be that the PVManager has connected fine, but the GUI is not being updated immediately because the GUI thread is busy? Once the PV has been connected to the value updates come through right away though.
    * Or is it something else?
    
Anecdotal evidence suggests that the "busier" IBEX is the longer it takes to reconnect.
Busier means more logs, blocks etc. - this could relate to the amount of memory being used by JVM.

BTW: Blocks and OPI values are inconsistent on which comes back first.
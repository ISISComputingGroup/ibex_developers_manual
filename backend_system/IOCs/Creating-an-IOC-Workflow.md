> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Creating an IOC Workflow

All these tasks that need to be completed for an IOC to be regarded as complete.

1. The IOC is created (via stream driver, lvDCOM or asyn etc.)
    * [StreamDevice Instructions](Creating-an-ISIS-StreamDevice-IOC)
    * [Creating an LvDCOM IOC](Creating-IOC-wrapper-VI)
        * NB [More general LvDOM notes] (Using-LVDCOM)
1. The PV names comply with the guidelines defined in the [ISIS PV guide](ISIS-PV-Guide)
1. PVs of note are designated as interesting PVs and they have units.
1. Record level simulation is provided (see [Record simulation](Record-Simulation))
1. The IOC has a disable record (see [Disable records](Disable-records))

There is a more detailed walkthrough for creating an IOC [here](Creating-An-ISIS-IOC).

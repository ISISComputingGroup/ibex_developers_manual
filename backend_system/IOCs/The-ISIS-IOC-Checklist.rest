== The ISIS IOC Checklist ==
This list all the tasks that need to be completed for an IOC to be regarded as finished.

1. The IOC is created (via stream driver, lvDCOM or asyn etc.)
1. The PV names comply with the guidelines defined in the [wiki:ISISPVGuide PV Guide]. This can quickly be checked using [wiki:check_db_file check_db_file.py]
1. PVs of note are designated as interesting PVs and they have units.
1. Record level simulation is provided (see [wiki:RecordSimulation Record Simulation])
1. The IOC has a disable record (see [wiki:DisableRecords Disable Record])
1. Tests have been written for the IOC (LINK NEEDED)

Note: Basic simulation and disable records can be added automatically using [wiki:add_sim_records add_sim_records.py]

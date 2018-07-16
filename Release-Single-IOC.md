We may want to release a single IOC to an instrument but not release a whole build. This is the procedure to do this:

1. Add all new code to master.
1. Wait for the overnight build.
1. Copy the needed IOC and support module (and anything else) from the relevant build server directory on the ICP share to the equivalent directories on the instrument.
1. Run in a epics terminal `build_ioc_startups.py`
    - If this fails it can be because there is a duplicate IOC.  The error message is rubbish!
1. Restart the IBEX server.

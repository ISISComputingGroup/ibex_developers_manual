> [Wiki](Home) > [Deployment](Deployment) > [How to release a single IOC to an instrument](Release-Single-IOC)

We may want to release a single IOC to an instrument but not release a whole build. This is the procedure to do this:

1. Add all new code to master.
1. Wait for the overnight build.
1. Ensure that nothing has happened in the code between the release and this release that will cause it not to work
    * the easiest way to do this is to look at the merge of master on to the release branch/tag.
1. Copy the needed IOC and support module (and anything else) from the relevant build server directory on the ICP share to the equivalent directories in a release build directory
1. Copy these file on to the instrument.
1. Run in a epics terminal `build_ioc_startups.py`
    - If this fails it can be because there is a duplicate IOC.  The error message is rubbish!
1. Restart the IBEX server.

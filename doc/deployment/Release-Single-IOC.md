# Release a single IOC

We may want to release a single IOC to an instrument but not release a whole build. This is the procedure to do this:

1. Add all new code to master.
1. Wait for the overnight build.
1. Ensure that nothing has happened in the code between the release and this release that will cause it not to work
    * the easiest way to do this is to look at the merge of master on to the release branch/tag.
1. Copy the needed IOC and support module (and anything else) from the relevant build server directory on the ICP share to the equivalent directories in a release build directory. e.g. 
    - from `...Kits$\CompGroup\ICP\EPICS\EPICS_CLEAN_win7_x64\BUILD-275\EPICS\ioc\master`
    - to `...Kits$\CompGroup\ICP\Releases\Build275_Knaur_pump\ioc\master`
1. Copy these file on to the instrument.
1. Run in a epics terminal in EPICS `utils\build_ioc_startups.py`
    - If this fails it can be because there is a duplicate IOC.  The error message is rubbish!
1. Restart the IBEX server.
1. Test the IOC boots and connects

## Troubleshooting

### IOC does not Start

Look at the IOC log this should give you a clue. If there is no log message in the IOC log, i.e. it just appears to be restarting itself. Start the IOC from the command line. If you then get a pop-up message box with:

    "xxx.dll" not found 

This means that a function has been added to a module that this IOC relies on to work. Locate the function and the module it belongs to then copy over this module and try again. This can now affect not just your IOC but others that rely on this new module; Make sure that this is what you want.

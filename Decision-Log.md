> [Wiki](Home) > [Project overview](Project-overview) > [Decision Log](Decision-Log)

A place to record decisions:

1. Decide format for calibration files. Decided to update labview and add a header with comments. This is because updating Seci is not a huge amount of work (1/2 day to do all instruments) and we don't make want to make a halfway house that has to be changed in the future. We don't want to go as far as allowing manufacturer file directly in EPICs because this is hard; this option can happen in the future.

2. We will not (in general) put `@init` handlers on records. This is because it is hard to do for any records which contain intermediate logic.

3. Flow control macros will be available as a settable macro for devices on which it can be configured. The reason is that if it is set on the device we don't want to have to change the st.cmd to set the option. The consequences of this is that it allows users to turn flow control on which can cause devices to stall if the device has it switched off. The default should be not to turn it on. Since it is a configurable item it should be in the lists macros that users can set otherwise it is a support call to change this.

4. Manual config upgrades should no be added to the upgrade script not added as a text note to the dev release notes. This means that they should be included in the code so can be reviewed. We may need to version these steps so that we don't get manual upgrade steps overflowing releases. This is to prevent them getting lost.

5. `Google test` was chosen for the cxx testing framework over `cxx test` because it is actively developed, unlike cxx test which is a branch that was created for Mantid but no longer used, and it builds on windows.

6. Decided that if a motor is moving when it goes uncommunicative it should remain as moving. This is because this is the current behaviour so will be expected and it is not clear if it is moving or stopped if you can not communicate. In either case, there should be communication alarm on the PVs.

7. Decided to split genie commands into two sets basic and extended. This keeps the simplest commands in a place where users can find them and means they will not have a large choice. Extended commands are for experts and are in a separate module. This will be accessed via `g.ext` users can import this in the usual way if desired. The cons of this is that we are splitting up where advanced users can find commands but this is acceptable because they are advanced users. The other problem is deciding which commands are extended and which are not.

8. `Genie_python` should be able to deal with PVs but the names of the PVs are not guaranteed they are advanced users only. Commands utilising PVs should have comments stating that it is an extended command and that the PV name may not be stable and that it is better to use a block. Ideally these commands should be placed in the advanced package. The downside is once we let this out then it will be used; however some scripts already do similar things it is better we support officially.

9. An ENGIN-X scientist asked for access to the exp_details database to create reports detailing RB numbers and users on the instrument. They were given read-only access but warned that we didn't guarantee the schema or the lifetime of the data and it would be better to go through the BusApps API.

10. Create upper case aliases of all blocks and use these in genie_python. This avoids the extra look up of current block names and the communication problem we have seen. The downside is there are more aliases created by and used in the block server and gateway but because there are usually fewer than 100 blocks this performance downside should not matter. The added advantage is that the blockserver is removed as a dependency in `caget`/`caset`.

11. Setting a device to remote mode should **not** be done on IOC start. There should be a clear indication on the OPI that it is in remote mode (where possible) and a button to set it into remote mode. There should also be an alarm on the PV but not at IOC level when the device is in local mode. It was thought that instrument scientists did not know that IOCs were restarting (e.g. when the updated a config for collimator) and so would be surprised at the change in the device.
    - Advised by Kathryn, present John, Alistair
    - 2019/05/16

12. If a setpoint on a device has a range set by the device it should be set up by using DRVH and DRVL. This is in preference to not capping it and letting the device ignore wrong values. The last choice is to add another record on top which intercepts the value and records an error and sends the capped value. The reason is that we would like to capture the range of the device without adding the complication of another record. This is also a similar behaviour to SECI. Finally, we could, in the future, check the value set in a `cset` against these values.
    - Present, John, Tom, Aaron, David and Freddie
    - 2019/07/05

13. It was decided that as part of the motion system on ZOOM a tablet or some other handheld device will be used [see] (https://github.com/ISISComputingGroup/IBEX/issues/2937). This is required as scientists would like to be able to move axes whilst they are inside the light curtain. All safety issues on this will be handled by a deadman's handle built into the device. In further discussions [here](https://github.com/ISISComputingGroup/IBEX/issues/4238) it was decided that the trying to move the IBEX GUI to something touch friendly would be hard and instead a new cut-down GUI should be produced in Phoebus.
    - Present: Thomas, Dom, Kathryn

14. It was decided that as part of the parameter limits [ticket](https://github.com/ISISComputingGroup/IBEX/issues/4168) for the script generator we will pass all parameters as strings from java to python and handle them in the python code by providing a decorator to pass casting operations to e.g. `@cast_parameters_to(temperature=float, field=str, uamps=float)`. This will allow them to define their own casting operations to deal with funny edge cases in a nice way. It also reduces the amount of edge cases we may find with py4j handling the difference between python and java class.
    - Present: James, Tom, Alistair
    - 09/12/2019

15. We should move towards using virtual environments for our python projects see [here](Python-dependencies) for more detail.
    - Present: Dom, Tom, Freddie, John
    - 19/05/2020

16. Genie_python should be kept 2/3 compatible until the block server is converted to python 3 in case it uses it. After this the decision should be revisited to see if we can go purely 3.
    - Present: Dom, Freddie, John
    - 27/05/2020

17. Helium level meters and other such items should be put on the domain "HA" (Hall) with no instrument identifier. So that the pv would be "HA:HLM:LEVEL1" to achieve this the IOC should run with a PVPREFIX` of `HA`. This is different to central services which runs with a blank prefix because it that case it is running multiple serves for multiple domains. We don't need the machine identifies for hall based services because it is not really anything to do with the machine unlike the instrument pvs.
    - Present: Alex, John, Kathryn, Freddie, Dom
    - 08/07/2020

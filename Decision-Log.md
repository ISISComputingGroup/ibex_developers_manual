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

17. Helium level meters and other such items should be put on the domain "HA" (Hall) with no instrument identifier. So that the pv would be "HA:HLM:LEVEL1" to achieve this the IOC should run with a blank `PVPREFIX` and the IOC should have `HA` in its IOC prefix. This is to make it the same as central services which runs with a blank prefix because it runs IOCs in multiple domains. We don't need the machine identifies for hall based services because it is not really anything to do with the machine unlike the instrument pvs.
    - Present: Alex, John, Kathryn, Freddie, Dom
    - 08/07/2020

18. Motion setpoints based on bare motors will no longer be supported in IBEX. This is to make the code simpler, as we move towards many multiple axes in [#4573](https://github.com/ISISComputingGroup/IBEX/issues/4573) and motion setpoints more robust to motor failure. All motors should support the axes record so this should not be a problem. For more esoteric motors which need to be used on short notice it is fairly easy to either add a motor axes on top of the motor record by adding something on the form`< $(SM300CONFIG)/axes.cmd` or moving the axis to the required positions in a script.
    - Present: Dom, John, Kathryn, Tom
    - 14/08/2020

19. Where to put the script generator release download for scientists. Decision is to put it in github, upload it to the release page, then create a page to link to it with install instructions (either in git hub or github pages). This was chosen because it is likely to be the quickest way of getting something uploaded for people to download, and we need it before cycle. Other choice were our external web server or an STFC sit; both of these would have been slow.
    - Present: John, Alistair, Kevin, Bish, Thomas
    - 2020/08/25

20. How to manage the database architecture to avoid instrument disk filling up. A decision was made that on most instruments the data being logged by the Instrument Archive is not critical to an experiment and so it is ok if it stops logging given a network outage on the instrument (the exception here is on [Enginx](https://github.com/ISISComputingGroup/IBEX/issues/5817)). Therefore we will move the MySQL instance that the [Instrument Archive](https://github.com/ISISComputingGroup/IBEX/issues/5819) is pushing to onto a [central server](https://github.com/ISISComputingGroup/IBEX/issues/5818). This will also be done for the [IOC log messages](https://github.com/ISISComputingGroup/IBEX/issues/5820) as they are replicated on logs on the instrument anyway. In the future it would be good to have a small cache on the instrument for some of this data to avoid issues when network is lost.

    - Present: Chris M-S, David, Dom, Freddie, John, James, Kathryn, Tom W
    - 2020/10/14

21. Should we still support a phone app with the MCR news for ISIS staff to use? Decision was made that it's a lot of development effort to support a mobile app for all platforms and the only benefits it gives over a slack/teams channel is that it doesn't require a user login. Seeing as everyone on ISIS will have a teams account this doesn't really apply. We are going to use the teams channel instead and if it would be helpful to use graphs this can be implemented using a python service or similar. 

22. In one system test we are testing the restarting of each IOC to test that we do not hit a limit as we did with the 256 limit in procservcontrol. Some IOCs are failing to restart, this may be because there is no hardware to talk to or the PVs we are looking at are autosave pvs and they are not available in the IOC. We have decided to start these IOCs in recsim to try and avoid this as this test is not to test the IOC itself but to test procservcontrol of the IOC. We can then at a later date put more work into the IOCs to make them start and go into alarm correctly.

23. How to manage the [InstrumentScripts](https://github.com/ISISNeutronMuon/InstrumentScripts) repository to make sure the code is kept up to date on all instruments but at the same time be open to Instrument Scientists modifying it. Decision was made [here](https://github.com/ISISComputingGroup/IBEX/issues/5858) to do the following:
* When doing a release we will tag a release of Instrument Scripts and release it to all instruments, whether they currently use the library or not
* We will write an automated service to tell us if instruments have local changes in Instrument Scripts (which should be located in C:\Instrument\scripts), or if they are not on the release tag
* If instruments do have local changes we will discuss with them getting the changes into master for the next release
* We will block pushing to master, instead requiring people to make PRs which we will review and check for unexpected side effects to the best of our ability. Other instrument scientists are welcome to contribute to this review process

    - Present: Bish, Dom, John, Thomas L and Tom W
    - 13/11/2020

24. How to manage script definitions for the script generator, decided as part of https://github.com/ISISComputingGroup/IBEX/issues/5754

The workflow for creating or modifying script definitions is:
1. The instrument scientist creates a new or edits an existing a script definition using a text editor (e.g. Notepad++).
1. The instrument scientist saves the script definition:
   1. if using his/her office (or cabin or home) PC, the script is saved locally (to a directory of the scientist's choosing)
   1. if using the instrument control PC, the script is saved `<where?>` (to a directory of the scientist's choosing?)
1. The instrument scientist transfers the saved script definition to the script definition repository.
   * the scientist will use a command (in practice a python or batch script) to perform the transfer
   * the command will print a message to inform the instrument scientist of success or failure of the save operation
1. If the transfer:
   1. succeeds: the scientist need do nothing more
   1. fails: the scientist should contact the Experiment Controls group for support.

Notes:
1. We expect instrument scientists to create/modify script definitions.  We do not expect users to create/modify script definitions.  We should advise instrument scientists not to allow users to create/modify script definitions.
1. We will create a python/batch script to manage transfer of saved scripts to the git repository
1. We will prevent instrument scientists from committing as `spudulike`, the script will have to ask for a username (e.g. `fedID`) and password to commit with
1. Script will generate a commit message that identifies that the push was done by the script (i.e. to help us to identify situations in which someone has tried to circumvent the script by using git commands directly)
1. Script will prevent the user from setting username and password to use all the time for pushing to this repository
1. The script will do: pull, add, commit and push to master
1. Must have git and python installed
1. Must have access to repository origin

We will do the following:

- Repository storage
  - We will investigate the use of the site gitlab instance
    - This instance should allow people with a fed id to be able to edit scripts, preventing us from the need to manage who is authorised
  - Alternative is to use our own git instance
  - This must be available for external users of the script generator
- Develop structure of the repository
  - Similar to the instrument scripts directory have folders for instruments and common areas
  - The script generator itself must be changed to recognise that this is no longer a flat filesystem
- We need to know where script definitions are stored on an instrument
  - This should be standardised: have a preference for using C:\Instrument\Settings... and fall back onto a folder in the same directory as the executable
  - This should be written down in the wiki once standardised and deployed
- As we are using a similar workflow to the instrument scripts we will have similar issue
  - We should write an automated service that checks for any uncommitted changes on instruments similar to https://github.com/ISISComputingGroup/IBEX/issues/5907

Tickets to carry out the work:

- https://github.com/ISISComputingGroup/IBEX/issues/5935
- https://github.com/ISISComputingGroup/IBEX/issues/5936
- https://github.com/ISISComputingGroup/IBEX/issues/5937
- https://github.com/ISISComputingGroup/IBEX/issues/5938
- https://github.com/ISISComputingGroup/IBEX/issues/5939
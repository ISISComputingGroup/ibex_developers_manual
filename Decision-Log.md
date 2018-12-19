> [Wiki](Home) > [Project overview](Project-overview) > [Decision Log](Decision-Log)

A place to record decisions:

1. Decide format for calibration files. Decided to update labview and add a header with comments. This is because updating Seci is not a huge amount of work (1/2 day to do all instruments) and we don't make want to make a halfway house that has to be changed in the future. We don't want to go as far as allowing manufacturer file directly in EPICs because this is hard; this option can happen in the future.

2. We will not (in general) put `@init` handlers on records. This is because it is hard to do for any records which contain intermediate logic.

3. Flow control macros will be available as a settable macro for devices on which it can be configured. The reason is that if it is set on the device we don't want to have to change the st.cmd to set the option. The consequences of this is that it allows users to turn flow control on which can cause devices to stall if the device has it switched off. The default should be not to turn it on. Since it is a configurable item it should be in the lists macros that users can set otherwise it is a support call to change this.

4. Manual config upgrades should no be added to the upgrade script not added as a text note to the dev release notes. This means that they should be included in the code so can be reviewed. We may need to version these steps so that we don't get manual upgrade steps overflowing releases. This is to prevent them getting lost.

5. `Google test` was chosen for the cxx testing framework over `cxx test` because it is actively developed, unlike cxx test which is a branch that was created for Mantid but no longer used, and it builds on windows.

6. Decided that if a motor is moving when it goes uncommunicative it should remain as moving. This is because this is the current behaviour so will be expected and it is not clear if it is moving or stopped if you can not communicate. In either case, there should be communication alarm on the PVs.

7. Decided to split genie commands into two sets basic and extended. This keeps the simplest commands in a place where users can find them and means they will not have a large choice. Extended commands are for experts and are in a separate module. This will be accessed via `g.ext` users can import this in the usual way if desired.

8. `Genie_python` should be able to deal with PVs but the names of the PVs are not guaranteed they are advanced users only. Commands utilising PVs should have comments stating that it is an extended command and that the PV name may not be stable and that it is better to use a block. Ideally these commands should be placed in the advanced package.

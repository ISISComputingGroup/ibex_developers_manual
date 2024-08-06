> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > IOC and device trouble shooting

**After diagnosing the problem** If you needed to go down to the instrument please correct/update any connection information to [Specific Device IOC page](Specific-Device-IOC).

# General tips

## My IOC does not show up in the IOC list in IBEX

To update the list of IOCs in IBEX (which is stored in the database) you will need to run `make iocstartups` from `C:\Instrument\Apps\EPICS\` - this will concatenate all the `config.xml` files in the `ioc` directory for each IOC, then filter it and push it to the database. 

## My IOC fails to make with "Permission Denied"

This is likely not to do with permissions but that the file is in use elsewhere. Try running stop_ibex_server.bat and if that doesn't work find out what else may be using the file ([LockHunter](https://lockhunter.com/) is quite useful).

## My IOC fails to build with `epics/base/master/configure/RULES.Db:201: *** target pattern contains no '%'`

This could be caused by the IOC attempting to copy in invalid db files during the build check in `XXIOC-01App/Db/Makefile` that any dbs listed there exist.

## I am having an Issue with a Specific IOC

Some IOC have important details which may help see if it is listed in [Specific Device IOC](Specific-Device-IOC).

## checking stream device/asyn serial port settings

At the IOC command prompt, type:
```
dbior("drvAsyn",2)
```

## ioc fails to connect to serial COM port
Errors like
```
2022/03/29 17:19:08.570 L0 -1 autoConnect could not connect: \\.\COM106 Can't open: Access is denied.
```
*access is denied* probably means another process (an IOC or terminal emulator like hyperterm) is already using the port. After you stop the offending process, it may be a few seconds before you can connect.    

## It doesn't work What Should I Do?

1. Connect over hyperterminal (see *Connect over hyperterminal*)
1. Check command set is correct (look at documentation)
1. Start the IOC and check it is not in SIM mode
1. Set the IOC mask (see *What is Passing between the IOC and the *Stream* Device*)
1. If you don't think records are processing correctly, try setting the `TPRO` (trace processing) field of the relevant records to a non-zero value. This will print a message to the IOC log whenever the record processes.

## Any write to the PV fails

If any caput command to a pv fails with a message similar to 
```
Old : TE:NDW1801:ICEFRDGE_01:MIMIC:SKIP:SP SKIP0
New : CA.Client.Exception..................................TE:NDW1801:ICEFRDGE_01:MIMIC:SKIP.:SP. .SKIP0.
.........
    Warning: "Channel write request failed"
    Context: "op=1, channel=TE:NDW1801:ICEFRDGE_01:MIMIC:SKIP:SP, type=DBR_STRING, count=1, ctx="TE:NDW1801:ICEFRDGE_01:MIMIC:SKIP:SP""
    Source File: ../oldChannelNotify.cpp line 160
    Current Time: Tue Nov 19 2019 09:56:21.490881300
...............................................................…
```
Then you may want to check if said PV is disabled somewhere in your db file through its DISP field by another PV.

## Connect over hyperterminal

Start hyper-terminal set up connection to device. Find a command that is returns something or that changes something on the display. Run that command look for the change. Try
1. Reading
1. Writing

If it doesn't work check:

1. Protocol (RS232, RS422, RS482)
1. Baud Rate
1. Com Port
1. Stop Bits
1. Parity
1. Line ending/Termination characters. 
1. Flow control

If this doesn't work check the moxa logging (see data over the moxa connection). If this doesn't work there is a device that can be plugged into a serial port to intercept all traffic.

## It won't work in the IOC initially, but with no changes works after connecting to hyperterminal

If the IOC doesn't work on startup, but does after using hyperterminal, at a command prompt run a `mode com1` on the appropriate com port (example is for COM1) before and after running hyperterminal. If there is a change that isn't duplicated by starting the IOC, then there is possibly a setting missing in asyn.

## It did work and then freezes ##

This may be due to a low control issue e.g. `Xon`/`Xoff` has been incorrectly specified and some binary character
happens to match `Xoff`. You should see asyn still sending character when you enable trace, but non getting through. If you run the `dbior` command at level 2 you may see `waiting as seen Xoff`.

## The device is sensitive to input commands

Some devices has sensitivity to the rate at which you poll them. Typically the devices manual will detail appropriate command spacing, and the ability to use `wait [time in ms];` after `in` or `out` commands in the protocol file is available. However, it is important to ensure your records and their types and error handling have been correctly defined. For instance in the event of a type error, since this is handled outside of the protocol file, it will bypass any structures you have in place to slow polling rates.

## What is Passing between the IOC and the *Stream* Device

It is possible to put stream into a debug mode where everything sent and received is written to the console. To do this simply add to you st.cmd file (defined on your asyn port) :

```
asynSetTraceMask("L0",-1,0x9) 
asynSetTraceIOMask("L0",-1,0x2)
```

where <port> is the port name you used in the asyn setup eg `drvAsynSerialPortConfigure(<port>...)`

This will include the terminator character, if you don't see it it is not being sent or received.
If no reply is given this will include a message "No reply from device in XXXms"

See [Asyn trace mask](ASYN-Trace-Masks-(Debugging-IOC,-ASYN)) for more details on specifying trace masks  

To stop printing these commands to the log use:

```
asynSetTraceMask("L0",-1,0x0) 
asynSetTraceIOMask("L0",-1,0x0)
```

## Is the MOXA seeing anything?

It is sometime useful to see if the moxa is seeing any traffic. If you are in the cabin you can look at the flashing lights (remember to take away 4 to convert from com number to port number). There is one light for send and one for receive both should flash.

If you want to do it remotely then you can by using the moxa web page. The address is on the [nagios page (standard log on)](https://varanus.isis.cclrc.ac.uk/nagios/). Look at Hosts -> MOXA_<Instrument name> the IP address is at top of the page in the middle. Enter the IP in a web browser and enter password from password page.
Then Monitor -> Asyn shows received and sent byte count.

## Environment Variable not getting set from MASTER_RELEASE

Varibles are transferred from `...EPICS\configure\MASTER_RELEASE` to `...EPICS\ioc\master\<IOCNAME>\iocBoot\<IOCNAME>\envPaths` when the ioc is made. You will have to delete the file to get the newest macros in and the paths have to exist.

## I get a `UDF` alarm on by `bi` record that's getting its value from a `calcout`

This was observed whilst programming the GEMORC IOC. We had records like so:

```
record(calc, "$(P)CALC")
{
	field(INPA, "$(P)LONGIN1")
	field(INPB, "$(P)LONGIN2")
	field(CALC, "A+B==0")	
	field(OUT, "$(P)BI")
}

record(bi, "$(P)BI")
{
	field(ZNAM, "No")
	field(ONAM, "Yes")
}
```

The result was a `UDF` alarm on the `bi` because the `RVAL` wasn't being updated in line with the `VAL`. We tried a lot of things to sort this. In the end we changed the `OUT` field of the `CALC` to a `FLNK` and added the following field to the `bi`: `field(INP, "$(P)CALC")`. We don't know why this solution worked over the many others we tried.

## IOC Crashes on debug the exception in "Unhandled exception at ... : Stack cookie instrumentation code detected a stack-based buffer overrun."

This is caused when something bad happens to the stack. There are many underlying causes to this, in my case it was that the IOC had loaded a dll which used an incorrect version of visual studio in its build see [here](https://docs.microsoft.com/en-us/cpp/c-runtime-library/potential-errors-passing-crt-objects-across-dll-boundaries?view=msvc-160). The dlls that are loaded (with their paths) can be seen in debug -> Windows -> Modules in VS. To check if it is this error delete the offending dll and try the process again. To fix the error convert the IOC to use build dependencies instead of the master release list, instructions are in [Reducing Build Dependencies](Reducing-Build-Dependencies)

In some cases you may be using a vendor DLL and have no control over which version of VS it is built with. If this is the case you may get an access violation when freeing memory allocated by the DLL. The easiest way round this if there is no way to rebuild the DLL is just to take the memory hit of not freeing the resource.

## Log shows `currentTime::getCurrentTime(): XXX sec time discontinuity detected`

The log for all IOCs shows the message:

```
currentTime::getCurrentTime(): XXX sec time discontinuity detected
```

It is caused by the time going backwards due to a correction; the underlying cause is unknown. However, this seems to disappear once the host machine is restarted.

## My IOC is not starting/reacting at all when launching from console/ProcServ 

If your IOC running in procserv is unresponsive (does not start up, `ctrl + x` from console does nothing) but you can still start the IOC manually from the IOCBoot directory, it is possible another process is using the port allocated to this IOC by procserv. 
1. You can find the port procserv is trying to use for a given IOC under `EPICS\iocstartup\procserv.bat`
1. In a command window, type `netstat -ano`. This gives you a list of ports currently in use and the IDs of processes using them
1. Search that list for the port from step 1. This will give you the ID of the process using it.
1. Find the process by it's ID in task manager.

## Asyn reports an `asynStatus` value of greater than 5

The `asynStatus` enum only contains values 0 to 5. But these are extended in `asyn/asynPortDriver/paramErrors.h` to include a few more useful statuses.

# Autosave

## Lost autosave values (especially on Galils)

This is based on ticket: https://github.com/ISISComputingGroup/IBEX/issues/2180

Possible symptoms include:

- Autosaved values mysteriously changing when the IOC is restarted
    - This includes Galils not retaining their position
- Errors of the form `[DATE] dbFindRecord for 'MY_PV.FIELD' failed
- Autosave files containing just a header and `<END>` tag

This has been observed primarily on Galils since they create custom monitor sets but it is feasible the issue could be seen elsewhere. The Galils pass macros to their monitor sets. If no macros are passed (e.g. if `GALILADDR0n` is not set) then no monitor will be created and no values will be saved. This will mean the device (e.g. the motor) will start with its default values. If the macro is reintroduced then those default values will become the new autosave values. The previous values can be recovered by restoring a previous autosave file (e.g. copy `GALIL_02_settings.sav_170309-144116` to `GALIL_02_settings.sav` and restart the IOC).

Galils also will not autosave any settings or values if they are set to `DEVSIM` or `RECSIM` mode. 

## comparing current to previous autosaved values

When an IOC starts, it copies the last autosave values to a date stamped file such as `GALIL_02_settings.sav_170309-144116` You can compare the current running IOC values to any of these files by using the `asVerify` command that is built as part of the `autosave` module and should be in your path after a `config_env` e.g.
```
asVerify  C:\Instrument\Var\autosave\GALIL_02\GALIL_02_settings.sav_170309-144116
```
There is no command to apply an autosave file to the current PVS, this is because it may be a bit dangerous as boot time autosave can apply values without forcing a process of a PV, whereas using a `caput` could have different results. Thus it is better to stop ioc, update autosave file, start ioc as described for galil above. 
  
# Motors

## Limit switches not active at the limit position

https://github.com/ISISComputingGroup/IBEX/issues/2174

In the motor record (`C:\Instrument\Apps\EPICS\support\motor\master\motorApp\MotorSrc\motorRecord.cc`) the limit flag is only activated if the motor's limit switch bit is active and motor's command direction (CDIR) is correct. Correct in this context means that the motor is moving out of range. That is, the motor is moving in a positive direction past an upper limit or in a negative direction past the lower limit. The command direction is only set when a command (e.g. home, move) is sent. If the IOC is restarted, the value isn't saved (and cannot be auto saved) so the limit flag behaviour will depend on the initial value of the command direction.

In summary, being at the limit position is insufficient to cause the limit flag to be active. This is expected behaviour, though can be slightly unintuitive at first.

## Readbacks from device keep twitching

This may be because of variances in the signal returned from the motor. This is true, for example, on the jaws set on Merlin. It also causes the motor status label on the bumpstrip to keep switching. Note that leaving it in this state can increase dramatically the amount of information sent to the archiver.

To fix, use caput for the relevant PV in the motor record:

- `IN:[INST]:MOT:MTR0n0m.MDEL`: Sets the motor deadband. This will stop the position readback from oscillating
- `IN:[INST]:MOT:MTR0n0m.ADEL`: Sets the archiver deadband. This will stop values being written to the archiver unless the value changes by more than the deadband value
- `IN:[INST]:MOT:MTR0n0m_EDEL_SP`: Sets the encoder deadband. No readbacks will be updated unless the encoder varies by this amount.

## McLennan OPI controls all red

- Does the panel on the front of the controller display a letter?
    - `r`
        - Can happen owing to a communication issue when the IOC starts if the baud rate/stop bits aren't set correctly
    - `t`
        - Tracking abort. Usually happens if the encoder resolution is incorrect. Is the `ERES` macro fraction the right way around?
    - `n`
        - Observed once on Merlin after the McLennan had been idle for a long time. Only happened after homing the motor. Restarting the controller (with the IOC stopped) fixed the issue
    - No
        - Try restarting the IOC, then move the motor through a significant operation (a home or jog to limit). Sometimes restarting the IOC is enough, sometimes the move causes the underlying issue to reveal itself (see `n` above)

## which process owns a serial port

From an administrator (i.e. gamekeeper) prompt, run the `sysinternals` handle command like:

```
handle.exe -a | findstr "Serial pid:"
```

This will print a list of PIDs and any matches to a serial port allocated, take the pid number above the relevant \Device\Serial  line 


# Logging

## I Changed the logging setting but it uses old settings

To sync up changes in logging from the DB file to the logging you must:

1. Restart the IOC so the logging info fields are pushed to the database
1. If any new PVs are being archived or settings have been changed the ARINST needs restarting
1. The ARACCESS needs restarting so it picks up the configuration changes from the database

## There was an error which I have fixed but I missed a log file

To regenerate log files set the date in the `c:\Logs\LOG_last_active_time` to the time you want to start generating files from, if this is more than delta days ago (2nd line of the log file) increase this number too. Then restart the ARACCESS

## I want to Generate a Log file from some PVs Now

This can be done between two dates see `...EPICS\ISIS\inst_servers\master\ArchiverAccess\log_file_generator.py` as an example.

## Value logs from IOC not produced/ARACCESS not creating log files/ENGINX Stress Rig not writing log files

Certain IOCs can be made to generate log files using the [ARACCESS component](Logging-from-the-archive), if these are no longer being produced then check:

- ARCCESS console (restart it) This should show a little blurb and should have start and stop lines, e.g.
    ```
    [2020-09-24 09:20:21] @@@ @@@ @@@ @@@ @@@
    [2020-09-24 09:20:21] @@@ Received a sigChild for process 25052. The process was killed by signal 9
    [2020-09-24 09:20:21] @@@ Current time: 2020-09-24 09:20:21
    [2020-09-24 09:20:21] @@@ Child process is shutting down, a new one will be restarted shortly
    [2020-09-24 09:20:21] @@@ ^R or ^X restarts the child, ^Q quits the server
    [2020-09-24 09:20:22] @@@ Restarting child "ARACCESS"
    [2020-09-24 09:20:22] @@@    (as C:\Windows\system32\cmd.exe)
    [2020-09-24 09:20:22] @@@ The PID of new child "ARACCESS" is: 20124
    [2020-09-24 09:20:22] @@@ @@@ @@@ @@@ @@@
    [2020-09-24 09:20:23] [1600935623.82] INFO: Creating a new connection pool: DBSVR_127.0.0.1_archive_report
    [2020-09-24 09:20:24] [1600935624.74] INFO: Creating a new connection pool: DBSVR_127.0.0.1_iocdb_iocdb
    [2020-09-24 09:20:25] [1600935625.00] INFO: Reading config for ioc: INSTRON_01
    [2020-09-24 09:20:25] [1600935625.00] INFO: Logging configuration (pvs as read from the archive)
    [2020-09-24 09:20:25]   - file (log on end): C:\logs\INSTRON_01\INSTRON_01_{start_time}.dat
    [2020-09-24 09:20:25]   - file (continuous): C:\logs\INSTRON_01\INSTRON_01_{start_time}_continuous.dat
    [2020-09-24 09:20:25]   - trigger pv: IN:ENGINX:INSTRON_01:LOG:RECORD:SP.VAL
    [2020-09-24 09:20:25]   - trigger pv: Logging from pv IN:ENGINX:INSTRON_01:LOG:SCAN.VAL with a default on error of 1s
    [2020-09-24 09:20:25]   - file headers: [u'Cross Sectional Area = {1:.6f}', u'Gauge Length for Strain = {2:.6f}', u'RB Number = {0}', u'']
    [2020-09-24 09:20:25]   - pvs in fileheader ['IN:ENGINX:ED:RBNUMBER.VAL', 'IN:ENGINX:INSTRON_01:STRESS:AREA.VAL',         'IN:ENGINX:INSTRON_01:STRAIN:LENGTH.VAL']
    [2020-09-24 09:20:25]   - table headers: ['Date/time', u'Run Number', u'Position (mm)', u'Load (MPa)', u'Strain (%)']
    [2020-09-24 09:20:25]   - table line: {time}	{2}	{0:.6f}	{1:.6f}	{3:.6f}
    [2020-09-24 09:20:25]   - pvs in table line ['IN:ENGINX:INSTRON_01:POS.VAL', 'IN:ENGINX:INSTRON_01:STRESS.VAL', 'IN:ENGINX:DAE:RUNNUMBER.VAL', 'IN:ENGINX:INSTRON_01:STRAIN.VAL']
    [2020-09-24 09:20:25] [1600935625.01] INFO: Last active: 2020-09-24T09:19:31 (13469489)
    ```
   - If this doesn't show both start and stop lines which that it is set to auto start in the default block component
- Start and stop the logging and see if it says it is creating a file, e.g. `INFO: Writing log file '...'` is this in the expected place
- Check the PVs it says it is logging and monitoring do they exist?
- Next check the ARINST level is it up (check `http://localhost:4812/groups`)
    - if not restart it, this means that there is no data stored for the run
- Next step is to check that the data is getting into the database (probably plot on log plotter)

- Write tip on Wiki for importing a database dump file into local database.  Commands and output:


## Reading historical PV values from local database _after_ it has been backed up and truncated

This can be done by _importing_ the backed-up database (ususally on a network drive) into a local developer's copy, then reading/plotting from there.
Example command from a request to read chopper values on MERLIN:

```
mysql.exe -u root -p < [insert network back-up path here]\ndxMERLIN\ibex_database_backup_2024_01_30\ibex_db_sqldump_2024_01_30.sql
Enter password: ************
```

The local database can then be truncated to remove the import.
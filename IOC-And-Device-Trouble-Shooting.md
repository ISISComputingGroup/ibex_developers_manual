> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > IOC and device trouble shooting

# General tips

## It doesn't work What Should I Do?

1. Connect over hyperterminal (see *Connect over hyperterminal*)
1. Check command set is correct (look at documentation)
1. Start the IOC and check it is not in SIM mode
1. Set the IOC mask (see *What is Passing between the IOC and the *Stream* Device*)

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

## It won't work in the IOC initially, but with no changes works after connecting to hyperterimnal

If the IOC doesn't work on startup, but does after using hyperterminal, at a command prompt run a `mode com1` on the appropriate com port (example is for COM1) before and after running hyperterminal. If there is a change that isn't duplicated by starting the IOC, then there is possibly a setting missing in asyn.

## What is Passing between the IOC and the *Stream* Device

It is possible to put stream into a debug mode where everything sent and received is written to the console. To do this simply add to you st.cmd file (defined on your aysn port) :

```
asynSetTraceMask("L0",-1,0x9) 
asynSetTraceIOMask("L0",-1,0x2)
```

where <port> is the port name you used in the asyn setup eg `drvAsynSerialPortConfigure(<port>...`

This will include the terminator character, if you don't see it it is not being sent or received.
If no reply is given this will include a message "No reply from device in XXXms"

See [[ASYN-Trace-Masks]] for more details on specifying trace masks  

## Is the MOXA seeing anything?

It is sometime useful to see if the moxa is seeing any traffic. If you are in the cabin you can look at the flashing lights (remember to take away 4 to convert from com number to port number). There is one light for send and one for receive both should flash.

If you want to do it remotely then you can by using the moxa web page. The address is on the [nagios page (standard log on)](https://varanus.isis.cclrc.ac.uk/nagios/). Look at Hosts -> MOXA_<Instrument name> the IP address is at top of the page in the middle. Enter the IP in a web browser and enter password from password page.
Then Monitor -> Asyn shows received and sent byte count.

## Environment Variable not getting set from MASTER_RELEASE

Varibles are transferred from `...EPICS\configure\MASTER_RELEASE` to `...EPICS\ioc\master\<IOCNAME>\iocBoot\<IOCNAME>\envPaths` when the ioc is made. You will have to delete the file to get the newest macros in and the paths have to exist.

# Autosave

## Lost autosave values (especially on Galils)

This is based on ticket: https://github.com/ISISComputingGroup/IBEX/issues/2180

Possible symptoms include:

- Autosaved values mysteriously changing when the IOC is restarted
    - This includes Galils not retaining their position
- Errors of the form `[DATE] dbFindRecord for 'MY_PV.FIELD' failed
- Autosave files containing just a header and `<END>` tag

This has been observed primarily on Galils since they create custom monitor sets but it is feasible the issue could be seen elsewhere. The Galils pass macros to their monitor sets. If no macros are passed (e.g. if `GALILADDR0n` is not set) then no monitor will be created and no values will be saved. This will mean the device (e.g. the motor) will start with its default values. If the macro is reintroduced then those default values will become the new autosave values. The previous values can be recovered by restoring a previous autosave file (e.g. copy `GALIL_02_settings.sav_170309-144116` to `GALIL_02_settings.sav` and restart the IOC).

# Motors

## Limit switches not active at the limit position

https://github.com/ISISComputingGroup/IBEX/issues/2174

In the motor record (`C:\Instrument\Apps\EPICS\support\motor\master\motorApp\MotorSrc\motorRecord.cc`) the limit flag is only activated if the motor's limit switch bit is active and motor's command direction (CDIR) is correct. Correct in this context means that the motor is moving out of range. That is, the motor is moving in a positive direction past an upper limit or in a negative direction past the lower limit. The command direction is only set when a command (e.g. home, move) is sent. If the IOC is restarted, the value isn't saved (and cannot be auto saved) so the limit flag behaviour will depend on the initial value of the command direction.

In summary, being at the limit position is insufficient to cause the limit flag to be active. This is expected behaviour, though can be slightly unintuitive at first.

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
> [Wiki](Home) > [Project tools](Project-tools) > [Restore motor positions from archive](Restore-Motor-Positions-from-Archive)

**NOTE** (edge case): If you are applying positions obtained with this script via SECI, be careful as the user offsets may be different for each axis i.e. the difference needs to be added to the recovered position.

This tool can be used to restore motor positions from the archive and put them on the current motor axis. It works by running in an epics terminal the commands:

```
cd C:\Instrument\Apps\EPICS\ISIS\inst_servers\master\scripts
%PYTHON3% restore_motor_positions.py <arguments>
```

The arguments are:

```
Find positions of motors in the past and restore those to current positions --time 2018-01-10T09:00:00 --host ndximat
--prefix IN:IMAT: --controller 01

optional arguments:
  -h, --help            show this help message and exit
  --time TIME, -t TIME  Time to restore from iso date, 2018-12-20T16:01:02
  --host HOST           Host to get data from defaults to localhost
  --prefix PREFIX, -p PREFIX
                        Prefix for motor controller, if not specified current instrument.
  --controller CONTROLLER, -c CONTROLLER
                        Controller number, for single controller get
```

When it is run it will look at the database at the time you have requested and find the first point before this, it will then look 1 hour into the future and find when the motor next moves. It will then print this as a summary table for you to look at, e.g.:

```
name         motor  : db value     diff from    - last update         next update         alarm
                    :              current val  - (sample time)       (within window)
Coarse North MTR0101:       30.700        0.000 - 2021-00-03 15:02:00 2021-00-03 15:02:01 NONE
Coarse East  MTR0102:       89.433        0.000 - 2021-58-03 14:02:19 -                   NONE
Coarse South MTR0103:       -1.000        0.000 - 2021-58-03 14:02:39 2021-00-03 15:02:36 NONE
Coarse West  MTR0104:       35.000        0.000 - 2021-33-29 15:01:53 -                   NONE
Gimbal Z     MTR0105:      -28.000        0.000 - 2021-33-29 15:01:53 -                   NONE
Gimbal Theta MTR0106:       10.000        0.000 - 2021-33-29 15:01:53 -                   NONE
Gimbal chi   MTR0107:       10.000        0.000 - 2021-33-29 15:01:53 -                   NONE
Front Guide  MTR0108:       45.000        0.000 - 2021-33-29 15:01:53 -                   NONE
```

Where:

- `name`: name of the motor (description)
- `motor`: is the pv root
- `db value`: is the value from the database
- `diff from current value`: is the difference between the current pv's value and the db value
- `last update`: is the time at which the sample was requested
- `next update`: is the next time the pv changes, `-` means it did not change in the window which is set to be an hour
- `alarm`: is the alarms logged severity in the database

Once this summary has been printed each motor will be considered in turn and the user can choose to restore or not the positions for that motor. This looks something like:

```
       Motor: Coarse North - MTR0101
 Current pos: 30.700000000000003
Recorded pos: 30.700000000000003  (alarm NONE )
  last moved: 2021-02-03 15:00:00.955650  next move 2021-02-03 15:00:01.055938
Set motor to record position? [Y/N]
```

You should check that the motor has not moved for a while and is not moving for a while after this time. If it does move think about plotting the values at that time. You should check that the value is reasonable. If this is good then the position should be restored. If for any reason this fails to set the motor position make sure that the axis motor calibration is set to `use` not `set`.

It should also produce a log in the `var\logs` directory listing the redefines and summary table.

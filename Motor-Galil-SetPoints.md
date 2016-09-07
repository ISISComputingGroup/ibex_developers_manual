> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Galil/motors setpoints

# Motors, Galil and Set Points

The Galil IOCs (01..08) enable IBEX to talk to motors for various purposes. To make it more user friendly the Galil IOC can be enhanced by adding set points which label set positions within the motors range.
A simulation of motors and set points can be added to your local instrument. I had trouble setting this up so this is an approximation of what I did. 
The locations in the source are:

* Galil support - `EPICS\support\galil\master`
* Galil IOCs - `EPICS\ioc\master\GALIL`
* Setpoint Support - `EPICS\support\motionSetPoints\master`

## Setup

First you must set in your global macros (`C:\Instrument\Settings\config\<instrument name>\configurations\globals.txt`) the following macros:

    SIMULATE=1
    GALILNUMCRATES=6
    GALIL_01__GALILADDR01=None
    GALIL_02__GALILADDR02=None
    GALIL_03__GALILADDR03=None
    GALIL_04__GALILADDR04=None 
    GALIL_05__GALILADDR05=None
    GALIL_06__GALILADDR06=None
    GALIL_07__GALILADDR07=None

This set a simulation mode on 6 crates of motors. You will need all 6 crates because motion setpoints are only available for GALIL_06.

Copy from NDXdemo the galil and motionsSetPoint configuration from `\\ndxdemo\c$\Instrument\Settings\config\NDXDEMO\configurations\galil` then move MotionSetPoint from the dir out into the configuration root.

Create an empty directory `C:\Instrument\Var`

Next start your instrument (or restart if it is already running).

Look at the motors perspective to see if they are all pink (all rows should be up to and including 6).

This will also set up motion set points using the command file ```C:\Instrument\Settings\config\NDW1407\configurations\galil\motionsetpoints.cmd```. For instance ```NDW1407:HGV27692:LKUP:MON3:POSN:SP``` is the set point for the Position monitor 3 (note however that this line is commented out in the original file from NDXDEMO).

If you want to see the monitor point on a synoptic. Create a synoptic with a component of type "movingmonitor" with the component target name of "In Out Monitor". To use monitor 3 which is currently set up for motor MTR0601 the macros should be set to:
* M = 3
* CHANNUM = ? (I set it to 3)
* MM = MOT:MTR0601
(check the `motionsetpoints.cmd` file to see what corresponds to what)




> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Motor setpoints](Motor-SetPoints)

# Motors, Galil and Set Points

The Galil IOCs (01..08) enable IBEX to talk to motors for various purposes. To make it more user friendly the Galil IOC can be enhanced by adding set points which label set positions within the motors range.
A simulation of motors and set points can be added to your local instrument. I had trouble setting this up so this is an approximation of what I did. 
The locations in the source are:

* Galil support - `EPICS\support\galil\master`
* Galil IOCs - `EPICS\ioc\master\GALIL`
* Setpoint Support - `EPICS\support\motionSetPoints\master`

## Setup

First you must create a configuration which starts GALIL_06 in DEVSIM with MTRCTRL set to 6. (motion setpoints are only available for GALIL_06).

Copy from NDXdemo the galil and motionsSetPoint configuration from `\\ndxdemo\c$\Instrument\Settings\config\NDXDEMO\configurations\galil` then move MotionSetPoint from the dir out into the configuration root.

Create an empty directory `C:\Instrument\Var`

Next start your instrument (or restart if it is already running).

Look at the motors perspective to see if they are all pink (all rows should be up to and including 6).

To setup the motion setpoints see [Motion Set points](Motion-Set-points)

## Alternative move command

This was done particularly for the muon barndoors. They do not move the "motor" by sending pulses from the
galil, rather there is a program running in the galil that changes the bias voltage and then readback is done
via a galil analogue output line. To allow control of this via the galil, it is now possible to change the command
used by the galil for setting the motor - this is done using a PV like  $(P)MOTMTR0101_MOVE_CMD   and a %f within this
string will be replaced with the requested position. A real galil would have this internally doing something like "PRA=%f" for "position relative axis A" - this can bet set to any valid galil command sequence.  
  

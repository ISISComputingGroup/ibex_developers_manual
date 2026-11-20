# EnginX Sample Positioner

The sample positioner on EnginX allows the sample to be moved into position. It is not controlled by IBEX through the motor record but instead via lvdcom this is to allow them to use the EnginX jog box. when plugged in the jog box allows the operator (once SECI mode is selected) to jog the positions of various axes at various speeds; the controller has a speed control and an enable jog button. There is user information for the sample positioner in the {external+ibex_user_manual:doc}`user manual <inst_specific/Engin-X-Sample-Stack>`.

Under the hood the IBEX `SamPos` IOC uses lvdcom to talk with the LabVIEW vi. The LabVIEW vi then talks through the table of motors to the galil controller. The controller runs a special program which allows the jog box to work as well as normal positioning.

## Galil Program

The program should be burnt in to the controller see the readme text in the LabVIEW modules `LabVIEW Modules\Instruments\Enginx\Galil Programs`. The program is also in there and is called `jogboxwithpos.gal` this is the one to upload it is a compressed version of a more commented program `Jog Box.dmc`. You will also need to set and burn the values of `MultX` and `TwkX` the values are stored in that `readme`.

## Redefining positioner variables (X, S, Omega etc.)

This can be done with the `EnginX - Positioner - Galil Remote.vi` (found in the Positioner folder of the EnginX Positioner in LabVIEW Modules) input the value to redefine to in the setpoint and then press the define button directly below.
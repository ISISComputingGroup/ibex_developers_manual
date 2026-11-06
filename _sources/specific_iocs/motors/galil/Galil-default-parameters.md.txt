# Galil default parameters

The Galil IOC has a number of (quite obscure) parameters. The ISIS defaults for these are stated here. Parameters that are not on this list either vary so much per axis that a sensible default is hard to reach or are happy at the motor record default.

| Parameter     | Description | Default (Commissioning) | Default (Running) | Reasoning  |
|:------------- |------------ | ----------------------- | ----------------- |----------- |
| ESTALLTIME    | Throws an error when the encoder has not moved after specified time | 1 | Small enough to catch errors when they occur | Give some slack so that doesn't throw errors, tighten when required |
| EDEL          | In motion if encoder has moved by this amount | 2*ERES | Could be increased if motor is particularly jittery | A motor shouldn't be jittering by more than 1 encoder step |
| JAH           | When on the axis will jog a specified amount after a home | No | Same | We don't want to do this at ISIS |
| JAH_VAL       | The amount to jog after home | Don't Care | Same | Doesn't do anything when above PV not set |
| EGUAFTLIMIT   | The distance between a limit switch and a hard stop | 0.001 | Increased if a large deceleration would be bad | A very small amount will definitely stop the axis |
| HOMEVAL       | What position to send the device after a home | 0 | Same | [Home is defined as zero across ISIS](https://github.com/ISISComputingGroup/IBEX/issues/2471) |
| OFFONERRORLIMIT | Turns the motor off when position error is greater than specified | Off | Same | Would be useful if the IOC sent a new position on start up but currently doesn't |
| ERROR LIMIT   | The position error to turn the motor off at | Don't Care | Same | Doesn't do anything when above PV not set |
| WLP           | Stops the motor from moving when it hits any limit | On | Off | Provides a safety net during commissioning but means you cannot move off a limit when running |
| AUTOONOFF     | Automatically turns the motor on for a move and off when complete | On | Off when the motor needs to be constantly energised e.g. it will fall under gravity | Better to turn the motor off when not in use |
| ONDELAY       | If AUTOONOFF set, how long to wait after the motor is turned on to begin a move | 0.2 | 0 | Used to make sure the amp is ready for the move. Generally we do not need to wait. |
| OFFDELAY       | If AUTOONOFF set, how long to wait after stopped before turning off | 0.2 | 2 | Should wait some time if you're doing correction moves immediately |
| ON_CMD | If on will leave the motor on at all times | Off | Off when the motor needs to be constantly energised e.g. it will fall under gravity (Make sure the AUTOONOFF is Off) | Better to turn the motor off when not in use |
| K1, K2, K3, FV, FC, FA, FN, ZP, ZN, CT, AF | Used for ceramic motors | 0 | Change if ceramic | This is the Galil's default when not ceramic motors |
| FV, FA | Changes the output voltages based on the acceleration/velocity | 0 | Change if required | Most axes in ISIS do not require this |
| IL, TL | Used for setting limits on the integrator and torque | 9.998 | Change if required | Most axes at ISIS do not need a limit so set the highest possible |
| CP | Used for ceramic motors but effects all motors. At the end of a move if the motor is within this value of the setpoint then the motor is switched off | -1.0 | Change if ceramic | -ve turns off the motor-off command (Can be set via the engineering view) |
| VBAS | The minimum speed the motor should go at (NOTE THAT ACCEL IS CALCULATED BASED ON THIS) | 0 | Same | Most motors should be happy at any speed below maximum |
| BDST | The distance to move to correct for backlash | 0 | Same | Most axes shouldn't need to correct |
| BVEL | The velocity to move when correcting for backlash | Don't care | Same | Doesn't do anything when BDST not set |
| BACC | The acceleration to move with when correcting for backlash | Don't care | Same | Doesn't do anything when BDST not set |
| DHLM | The high soft limit | 2147483647 * MRES | Slightly before the forward limit switch | When commissioning turn off. When running we don't normally want to hit the physical limits. |
| DLLM | The low soft limit | -2147483648 * MRES | Slightly before the reverse limit switch | When commissioning turn off. When running we don't normally want to hit the physical limits. |
| UEIP | Use an encoder | Off | On | When starting to commission you are not using the encoder, when running you should if there is one |
| RTRY | The number of times to retry getting to the setpoint | 0 | 10 | When commissioning don't want to run 'closed loop' otherwise 10 tries is normally enough to get to position |

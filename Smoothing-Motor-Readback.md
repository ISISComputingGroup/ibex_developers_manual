Several Galil systems use analogue feedback as the encoder, this is effectively an absolute encoder (so no need to set a rehome etc) but the readback can be noisy and this has caused issues in the past with positions looking like they are drifting.

To solve this issue, the readbacks can be smoothed using an epics compress record and this fed into the motor record by using its optional readback link functionality. So the motor record sets values as usual, but using a different route for readback. A few notes on the system:
- when the motor record is using the readback link, it is in "no encoder" mode i.e. it thinks it is in open loop. The only visible effect of this is that on startup it didn't sync the setpoint correctly, this has been remidied by forcing a delayed write to the motor record SYNC field after ioc startup. This needs to be delayed so channel access and other things have started.
- a readback delay needs to be set on the motor record, this is because the compress record averaged values will be a bit scewed by the motion that has just occurred otherwise and so the retry calculation will be incorrect.

For with setup of MTR0105 for example you would

* have a non-zero max retries count - default is 10
* set a readback delay, currently using 5 seconds
* set readback resolution to 1
* set a readback link value - for MTR0105 on WISH this is `IN:WISH:MOT:MTR0105:EPOS_AV CP MS`
* set `use encoder` to `no` (do this before setting readback)
* set `use readback` to `yes`

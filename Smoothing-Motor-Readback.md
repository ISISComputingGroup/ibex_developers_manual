Several Galil systems use analogue feedback as the encoder, this is effectively an absolute encoder (so no need to rehome etc) but the readback can be noisy and this has caused issues in the past with setpoints looking like they are drifting. The WISH instrument is an example.

We did look at smoothing the values within an EPICS db using the compress record etc. and linking this to an alternative motor readback [as per old notes](Smoothing-Motor-Readback-old), but it turned out the jaws were so noisy it swamped the Galil and we had to add smoothing there.


To set this up for `MTR0105` on WISH for example you would:

* have a non-zero `max retries` count - default is 10
* set a `readback delay`, currently using 5 seconds
* set `readback resolution` to 1 (we have handled this in the `_EPOS_CALC` record)
* set a `readback link` value - for MTR0105 on WISH this is `IN:WISH:MOT:MTR0105:EPOS_AV CP MS`
* set `use encoder` to `no`
* set `use readback` to `yes`

Setting `use encoder` to `no` before enabling readback is probably a better sequence of operations, but not crucial. If you set readback to yes it automatically sets encoder to no, but i had a case when it seemed to get a bit confused. If it does make sure values are correct and then just restart ioc and autosave will apply them correctly. Bear in mind that these are settings and so autosave at 30 second intervals, so don't restart too soon after a change  

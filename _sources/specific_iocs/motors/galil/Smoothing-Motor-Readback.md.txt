# Smoothing motor readback

Several Galil systems use analogue feedback as the encoder, this is effectively an absolute encoder (so no need to rehome etc) but the readback can be noisy and this has caused issues in the past with setpoints looking like they are drifting. The WISH instrument is an example.

We did look at smoothing the values within an EPICS db using the compress record etc. and linking this to an alternative motor readback [as per old notes](#smoothing_galil_readback_old_approach), but it turned out the jaws were so noisy it swamped the Galil and we had to add smoothing there.

The data is smoothed using the same algorithm available in an epics analogue input (ai) record i.e. a first-order infinite impulse response (IIR) digital filter.
```
New_Val =  Old_VAL * SMOO + (1 - SMOO) * New_Data
```
So `SMOO == 0` is no smoothing. During a move the un-smoothed encoder position is returned by the galil IOC to the motor record, but once motion has stopped the smoothing algorithm is activated to smooth the the data. For the system to work it needs to:
* be setup to retry moves (which is our default)
* have a readback delay set (something like 2 seconds)
The readback delay is important as this is how long the motor record waits (settle time) after a move has finished before it uses the position for the next task (retry in our case). So the readback delay is how much time we are averaging the encoder readback of the stationary motor for before we decide on any correction/retry to get to the requested setpoint.
* have an non-zero smoothing factor. 
   
To set this up for `MTR0105` on WISH for example you would:
* Set max retries (MTR0105.RTRY) to > 0 (typically 10)
* Set `readback delay` (MTR0105.DLY) to a reasonable averaging period (e.g. 2 seconds)
* Set encoder smoothing factor MTR0105_ENC_SMOO_SP to > 0 e.g. 0.5
You may need to experiment a bit with delay and smoothing. Bear in mind that these are autosaved at 30 second intervals, so don't restart IOC too soon after a change or you will lose them.  

{#smoothing_galil_readback_old_approach}
## Old approach

```{note}
This is the old proposed way and not currently used, but some of its implementation is in place
```

To solve this issue, the readbacks can be smoothed using an EPICS compress record and this fed into the motor record by using its optional readback link functionality. So the motor record internally sets values as usual, but using a different route for readback. A few notes on the system:
* the motor record `REP` field is monitored via the `_EPOS_CALC` PV, stored in a circular buffer in a compress record and then a configurable number are averaged to provide an `EPOS_AV` PV. The linking is done via a channel access monitor, so assumes that the readback is noisy and that the noisy rate is sufficient to generate a good number of values to average. It would be possible to explicitly scan this record if you wished to average a less noisy signal.    
* when the motor record is using the readback link, it is in "no encoder" mode i.e. it thinks it is in open loop. The only visible effect of this is that on startup it didn't sync the last setpoint to the current readback, this has been resolved by forcing a delayed write to the motor record SYNC field after ioc startup (see `_EPOS_INIT` and `_EPOS_SYNC` PVs). This needs to be delayed so channel access and other things have started.
* a readback delay needs to be set on the motor record, this is because the compress record averaged values will be a bit biased by the motion that has just occurred otherwise and so any retry calculation distance will be incorrect.

To set this up for `MTR0105` on WISH for example you would:

* have a non-zero `max retries` count - default is 10
* set a `readback delay`, currently using 5 seconds
* set `readback resolution` to 1 (we have handled this in the `_EPOS_CALC` record)
* set a `readback link` value - for MTR0105 on WISH this is `IN:WISH:MOT:MTR0105:EPOS_AV CP MS`
* set `use encoder` to `no`
* set `use readback` to `yes`

Setting `use encoder` to `no` before enabling readback is probably a better sequence of operations, but not crucial. If you set readback to yes it automatically sets encoder to no, but i had a case when it seemed to get a bit confused. If it does make sure values are correct and then just restart ioc and autosave will apply them correctly. Bear in mind that these are settings and so autosave at 30 second intervals, so don't restart too soon after a change  


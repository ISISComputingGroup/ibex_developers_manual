Several Galil systems use analogue feedback as the encoder, this is effectively an absolute encoder (so no need to rehome etc) but the readback can be noisy and this has caused issues in the past with setpoints looking like they are drifting. The WISH instrument is an example.

We did look at smoothing the values within an EPICS db using the compress record etc. and linking this to an alternative motor readback [as per old notes](Smoothing-Motor-Readback-old), but it turned out the jaws were so noisy it swamped the Galil and we had to add smoothing there.

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

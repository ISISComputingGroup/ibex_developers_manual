# Asyn Interpose functions

ASYN interpose functions can apply logic to data read from the device that is then passed to e.g. stream device. 

## Throttle Interpose

Sometime a device has a maximum rate at which it can accept commands and/or that commands must be separated by a minimum delay. Though it is possible to add delays into Db files and/or stream device protocol, but this can get messy or things get missed. The throttle interpose function allows you to specify a minimum time between writes to the device, if another write occurs too quickly a sleep is inserted to bring up to minimum delay.

syntax is
```
asynInterposeThrottleConfig(port, address, min_delay_between_commands)
```

so you would add e.g. `asynInterposeThrottleConfig("L0", 0, 0.1)` to the `st.cmd` after port `L0` is created.

To see when a delay is being inserted, enable the filter debug output as per https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/ASYN-Trace-Masks-(Debugging-IOC,-ASYN) so e.g. set trace mask to `0xD` rather than `0x9`


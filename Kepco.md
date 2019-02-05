> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Kepco](Kepco)

Kepcos are power supplies coming in various sizes and models. The two major differences are analogue (they have analogue dials at the front) and digital (digital readbacks). They run in two modes:

1. Voltage Mode
    - Setting voltage will mean the KEPCO will supply will try to maintain the requested (+ve or -ve)
    - In voltage mode, the current that is set will be the maximum allowed current. I.e. If the resistance is low then to reach the desired voltage a current larger than the setpoint will be needed, so the KEPCO will not reach the desired voltage.
1. Current Mode
    - Setting a current will mean the KEPCO will supply the given current.
    - In current mode, the voltage that is set will be the maximum allowed current.

## Troubleshooting

### Current/voltage will not go negative when I set the current/voltage

If the device is in voltage mode then the sign of the current will be set by the voltage, not the current and vice-versa. 

### Current/voltage does not reach the value set

For voltage mode, check the current setting is high enough (see voltage mode above). In current mode, check that the voltage is set high enough (see current mode above).

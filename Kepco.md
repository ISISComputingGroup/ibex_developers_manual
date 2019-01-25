> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Kepco](Kepco)

Kepcos are power supplies coming in various sizes and models. The two major differences are analogue (they have analogue dials at the front) and digital (digital readbacks). They run in two modes:

1. Voltage Mode
    - Setting  voltage will mean the KEPCO will supply that voltage as long as it is not above the magnitude of the set current. E.g. If the resistance is low then to reach the desired voltage a current larger than the setpoint will be needed, the KEPCO will refuse to allow this.
1. Current Mode
    - Setting a current will mean the KEPCO will supply the given current as long as it is not above the magnitude of the set voltage.

## Troubleshooting

### Current/voltage will not go negative when I set the /voltage

If the device is in voltage mode then the sign of the current will be set by the voltage, not the current and vice-versa. 

### Current/voltage does not reach the value set

For a voltage check the current setting and readback and for current check the voltage setting and readback. This setting is the largest allowed value that the unit will produce.


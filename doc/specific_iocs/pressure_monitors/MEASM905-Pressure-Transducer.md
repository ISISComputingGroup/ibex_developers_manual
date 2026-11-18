# MEASM905 Pressure Transducer

This device is used on PEARL as a read-only pressure monitor, as part of the larger pressure control rig. 

In its current implementation, the device uses ASCII protocol to receive a simple command for a pressure reading.

```{note}
For the units permanently associated with PEARL, a bespoke db25 to Moxa cable has been created (via a white adapter box), as it uses a different pinout from RS232.

For all other units, a standard DB9 Moxa cable (without null modem) is used.
```

The PEARL handbook specifies that this device can use three different protocols: It currently uses the "M905 Protocol 1" to talk to the device.

## Connection troubleshooting

The box can be set to talk to one of three internal "ports" (these are ports internal to the device, not to be confused with MOXA/COM ports). If it is configured to talk to the wrong "port", it will completely fail to communicate.

The "port" can be checked and changed via the physical front panel of the device - usually "port 1" will be required:

<img src=measm905_1.png width="500">
<img src=measm905_2.png width="500">
<img src=measm905_3.png width="500">
<img src=measm905_4.png width="500">

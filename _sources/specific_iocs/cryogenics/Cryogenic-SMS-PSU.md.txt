# Cryosms PSU

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

cryosms/*
```

```{seealso}
See also [design notes](cryosms/Cryogenic-SMS-PSU-design) for background on the implementation of this IOC.
```

It was originally designed to be used for the HIFI main instrument cryomagnet, but has also been used to control the Oxford Instruments 9T magnet.

## Troubleshooting

### Driver gets stuck in `Processing` at a ramp rate transition, at high field

Firstly, check which ramp file is in use and check at which fields the ramp rate transitions to verify the driver is stuck at one of these transition points.

The lowest allowable ramp rate in the power supply is `0.0008 A/s`. Other allowable ramp rates are discrete values - when a ramp rate is sent to the power supply, it will select the next lowest possible ramp rate. Unfortunately, the absolute lowest ramp rate (`0.0008 A/s`) seems to be broken on the hardware, which reports a rate of `2^30` in this case. Therefore, the lowest ramp rate in the ramp table must be higher than the **second** lowest ramp rate allowable by the hardware. 

**Always check with cryogenics before increasing any ramp rates, as it is possible to cause a magnet quench by selecting a too-high ramp rate.**

### PSU COM Ports disappearing

Symptom: The COM ports for the Cryogenic Inc. Power Supplies are missing from the Device Manager (these are inbuilt USB to serial adapters within the devices, they install a driver which allows them to appear as COM ports)
Solution: Turn the PSU off at the main switch, unplug the USB cable from the PSU, unplug any connections via hubs and their power as well, reconnect everything and power everything on, and the COM ports should be available again

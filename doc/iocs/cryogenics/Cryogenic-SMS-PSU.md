# Cryosms PSU

See also [design notes](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU-design) for background on the implementation of this IOC.

It was originally designed to be used for the HIFI main instrument cryomagnet, but has also been used to control the Oxford Instruments 9T magnet.

## Troubleshooting

### Driver gets stuck in `Processing` at a ramp rate transition, at high field

Firstly, check which ramp file is in use and check at which fields the ramp rate transitions to verify the driver is stuck at one of these transition points.

The lowest allowable ramp rate in the power supply is `0.0008 A/s`. Other allowable ramp rates are discrete values - when a ramp rate is sent to the power supply, it will select the next lowest possible ramp rate. Unfortunately, the absolute lowest ramp rate (`0.0008 A/s`) seems to be broken on the hardware, which reports a rate of `2^30` in this case. Therefore, the lowest ramp rate in the ramp table must be higher than the **second** lowest ramp rate allowable by the hardware. 

**Always check with cryogenics before increasing any ramp rates, as it is possible to cause a magnet quench by selecting a too-high ramp rate.**
> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [CRISP Spin Flipper](CRISP-Spin-Flipper)

The [CRISP Spin Flipper](https://github.com/ISISComputingGroup/EPICS-Flipprps) is generally referred to as 'FLIPPRPS' in IOC and support files. It is a simple device for running polarised neutron experiments that can be set to either "up" or "down", presumably to polarise neutrons in one of those directions. The IOC is a stream device.

The current polarity setting cannot be read from the device, so the value of the POLARITY PV is used to display the current polarity on the wiki. This may result in the GUI and the device becoming out-of-sync if the PV is set to something whilst the device is disconnected.

The spin flipper is run from a script and coordination with the Kepco is done in that script. 

### CRISP Spin Flipper Support Repository
- https://github.com/ISISComputingGroup/EPICS-Flipprps
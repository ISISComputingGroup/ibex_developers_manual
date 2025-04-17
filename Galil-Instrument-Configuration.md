> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Galil](Galil) > Galil Instrument Configuration

On startup, Galil IOCs are configured at a higher level by reading from files that live in the instrument config area under `<INST>/configuration/galil`.

The following settings are configured in this way:

### Required:
- [Galil Controller Config](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Galil#startup)

### Optional extensions:
- [Axis (Alias)](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Axis)
- [Barn Doors](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Barndoors-and-Momentum-Slits-on-MUON-Front-End)
- [Bump Strip](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Bump-Strip)
- [Jaws](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Jaws)
- [Motion Set Points](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Motion-Set-points) 
- [Sample Changer](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Sample-Changer-Support-Module)
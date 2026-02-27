# Galil Instrument Configuration

On startup, Galil IOCs are configured at a higher level by reading from files that live in the instrument config area under `<INST>/configuration/galil`.

The following settings are configured in this way:

## Required:
- [Galil Controller Config](#galil_startup)

## Optional extensions:
- [Axis (Alias)](../../motor_extensions/Axis)
- [Barn Doors](../../motor_extensions/jaws/Barndoors-and-Momentum-Slits-on-MUON-Front-End)
- [Bump Strip](../../motor_extensions/Bump-Strip)
- [Jaws](../../motor_extensions/Jaws)
- [Motion Set Points](../../motor_extensions/Motion-Set-points) 
- [Sample Changer](../../motor_extensions/Sample-Changer-Support-Module)
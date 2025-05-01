# Beckhoff

Beckhoff motor controllers are the most complex in use at ISIS and will be the standard going forward. A Beckhoff controller is basically a generic PLC that includes a number of useful functions out of the box for running motors. The generality of a Beckhoff means that it will most likely be used in the future for measuring and controlling other hardware outside of motion. A more detailed presentation has been given about Beckhoffs in a [Code Chat](/processes/meetings/Code-Chats-and-Lightning-Talks) entitled Layers, Onions and Ogres.

Current Beckhoff installations are:
| Instrument | Device |
| -----------|--------|
| LARMOR | Rotation Bench |
| IMAT | Large sample bench, controlling rotation and height |
| SANS2D | Guides (5 in total) - note apertures are still Galil-controlled| 
| CHIPIR | Filter set | 
| SANDALS | Jaws and Sample changer | 
| CRISP | Jaws (running old firmware for now) | 
| MUONFE | Barn doors (in progress) | 
| INTER | Secondary flight path upgrade (INTER tank) | 
| SURF | Critical axis (in progress) |



## Code on the controller
Unlike most other devices (except the Galil) the computing group has some oversight over the PLC code written on the controller. It has been agreed that this code will mostly be written by IDD, with oversight from computing to guide good programming practices, assist in debugging etc. The ISIS first version of this code is stored [here](https://github.com/ISISComputingGroup/BeckhoffPLCCode/) however this is now not used and going forward the code is written in collaboration with the ESS and stored [here](https://bitbucket.org/europeanspallationsource/tc_generic_structure/src/master/).
### Documentation
- [Axis and Controller Commissioning Guide](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/Ee_aMxb5CF1Dlz-NUGW3OVgB0K7vQjXXwZDwSl5DSHN48w?e=GjqNEb&isSPOFile=1) document describing setting up a controller and TwinCAT solution for a new system and configuring real and virtual axes within TwinCAT environment.

## Troubleshooting
see [Beckhoff troubleshooting](beckhoff/Beckhoff-troubleshooting)

## Testing
See [Beckhoff testing](beckhoff/Beckhoff-testing)

## Commissioning a new Beckhoff on a beamline
see [Beckhoff Commissioning](beckhoff/Beckhoff-commissioning)

## IOC
### Beckhoff config area

The config area contains a directory used for storing `.cmd` files for use with the `TC` IOC (in the same way as a galil or other motor controller). On an instrument it should look like this: `\instrument\settings\config\<instname>\configurations\twincat\`. 

### Quirks

- The Beckhoff uses whether it has been homed to set `ATHM` in the motor record, rather than just using the raw datum switch. 
- The "limits" shown on the table of motors summary view are not necessarily actual physical limit switches being engaged - the Beckhoff has more complex rules on whether motors can move back or forwards
- The motor record sets `UEIP` (use encoder if present) to false to avoid using the encoder resolution to scale values. We have no control over whether to use or not use an encoder with a Beckhoff, the internal code handles it
- Axes marked with `(V)` are virtual axes. 

## Updating

Some discussion has been had on how we handle updates to the Beckhoff PLC code and `twincatMotor` etc. this is documented [here](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/EXnBTNmcqqVCkIXXxjSvYdwBD3ZihXKDE0pZpiErGnkJ1g?e=4%3AWjCJxN&at=9&CID=0DF00AB8-D565-4B81-9AA2-C0DD226434CA&wdLOR=c76050FF1-1FF0-4AC8-A94C-0127E17DD337)

## Further Information

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1

beckhoff/*
```

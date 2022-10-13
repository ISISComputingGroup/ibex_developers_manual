
> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff)

Beckhoff motor controllers are the most complex in use at ISIS and will be the standard going forward. A Beckhoff controller is basically a generic PLC that includes a number of useful functions out of the box for running motors. The generality of a beckhoff means that it will most likely be used in the future for measuring and controlling other hardware outside of motion. A more detailed presentation has been given about Beckhoffs in a [Code Chat](Code-Chats-and-Lightning-Talks) entitled Layers, Onions and Ogres.

## Documentation
- [Axis and Controller Commissioning Guide](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/Ee_aMxb5CF1Dlz-NUGW3OVgB0K7vQjXXwZDwSl5DSHN48w?e=GjqNEb&isSPOFile=1) document describing setting up a controller and TwinCAT solution for a new system and configuring real and virtual axes within TwinCAT environment.

## Code on the controller
Unlike most other devices (except the Galil) the computing group has some oversight over the PLC code written on the controller. It has been agreed that this code will mostly be written by IDD, with oversight from computing to guide good programming practices, assist in debugging etc. The ISIS first version of this code is stored [here](https://github.com/ISISComputingGroup/BeckhoffPLCCode/) however this is now not used and going forward the code is written in collaboration with the ESS and stored [here](https://bitbucket.org/europeanspallationsource/tc_generic_structure/src/master/).

## Troubleshooting
see [Beckhoff troubleshooting](Beckhoff-troubleshooting)

## Testing
See [Beckhoff testing](Beckhoff-testing)

## Commissioning a new Beckhoff on a beamline
see [Beckhoff Commissioning](Beckhoff-Commissioning)

## IOC
### Beckhoff config area

The config area contains a directory used for storing `.tpy` files for use with `tcIoc`. On an instrument it should look like this: `\instrument\settings\config\<instname>\configurations\twincat\`. The TC IOC will search in this directory using the given `TPY_FILE` macro. The generated DB file also gets created in this directory by `tcIoc`. 

## Updating

Some discussion has been had on how we handle updates to the Beckhoff PLC code and `tcIoc` etc. this is documented [here](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/EXnBTNmcqqVCkIXXxjSvYdwBD3ZihXKDE0pZpiErGnkJ1g?e=4%3AWjCJxN&at=9&CID=0DF00AB8-D565-4B81-9AA2-C0DD226434CA&wdLOR=c76050FF1-1FF0-4AC8-A94C-0127E17DD337)


> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff)

Beckhoff motor controllers are the most complex in use at ISIS and will be the standard going forward. A Beckhoff controller is basically a generic PLC that includes a number of useful functions out of the box for running motors. The generality of a beckhoff means that it will most likely be used in the future for measuring and controlling other hardware outside of motion. A more detailed presentation has been given about Beckhoffs in a [Code Chat](Code-Chats) entitled Layers, Onions and Ogres.

## Documentation
- [Axis and Controller Commissioning Guide](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/Ee_aMxb5CF1Dlz-NUGW3OVgB0K7vQjXXwZDwSl5DSHN48w?e=GjqNEb&isSPOFile=1) document describing setting up a controller and TwinCAT solution for a new system and configuring real and virtual axes within TwinCAT environment.

## Code on the controller
Unlike most other devices (except the Galil) the computing group has some oversight over the PLC code written on the controller. It has been agreed that this code will mostly be written by IDD, with oversight from computing to guide good programming practices, assist in debugging etc. The ISIS first version of this code is stored at https://github.com/ISISComputingGroup/BeckhoffPLCCode/, which has an accompanying wiki to discuss specifics of the codebase. However, going forward the code will be written in collaboration with the ESS and stored [here](https://bitbucket.org/europeanspallationsource/tc_generic_structure/src/master/).


## Testing
See [Beckhoff testing](Beckhoff-testing)

## Commissioning a new Beckhoff on a beamline
see [Beckhoff Commissioning](Beckhoff-Commissioning)


## IOC

The current Beckhoff applications that are being run through `tcIOC` and the CI pipeline discussed above are:
* [dummy_PLC](https://github.com/ISISComputingGroup/BeckhoffPLCCode/tree/dummy_PLC)- a PLC that does very little, basically used to test that fundamental tcIOC comms works
* [old_ISIS_code](https://github.com/ISISComputingGroup/BeckhoffPLCCode/tree/Ticket5052_refactor_test_runner) - this is the old ISIS prototype motion code that is currently on the CRISP jaws. Hopefully this code can be removed once the jaws are moved on.
* [ESS_base_code](https://bitbucket.org/europeanspallationsource/tc_generic_structure/) (now linked to by `main` of the `BeckhoffTestRunner` repository) - this is the collaboration code that we will be using go forward.

<details>
<summary> MCAG (defunct) - click to expand </summary>

This IOC was originally written by ESS. It uses an ASCII protocol over TCP/IP to do the communication and is very specifically designed for motion. There is a simulator which can be run using the following steps:

- `cd EPICS\support\MCAG_Base_Project\master\epics\simulator`
- `doit.bat`
- Start the IOC (host macros needs to be set to 127.0.0.1:5024)

~Currently this is only being run on IMAT. It should soon be replaced by the collaboration code.~ - **It has been replaced by the new code, so is now defunct.**
</details>


### Beckhoff config area

The config area contains a directory used for storing `.tpy` files for use with `tcIoc`. On an instrument it should look like this: `\instrument\settings\config\<instname>\configurations\twincat\`. The TWINCAT IOC will search in this directory using the given `TPY_FILE` macro. The generated DB file also gets created in this directory by `tcIoc`. 

## Updating

Some discussion has been had on how we handle updates to the Beckhoff PLC code and `tcIoc` etc. this is documented [here](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/EXnBTNmcqqVCkIXXxjSvYdwBD3ZihXKDE0pZpiErGnkJ1g?e=4%3AWjCJxN&at=9&CID=0DF00AB8-D565-4B81-9AA2-C0DD226434CA&wdLOR=c76050FF1-1FF0-4AC8-A94C-0127E17DD337)

## Troubleshooting

As we don't really handle any logic minus the motor record aliasing, there isn't much to go wrong (in theory) - sometimes for numerous reasons such as motion logic changing etc. the `.tpy` file that maps over memory addresses to human readable names can go out of date.  

### "TPY file needs updating"
If nothing whatsoever is working, moves aren't sending and enabling/disabling is not working, an outdated `.tpy` file could be the cause. 

To remedy this: 
1. Stop the `TC` IOC from IBEX.
1. Obtain a valid/up to date `.tpy` file, either sent from the motion team or from the controller (usually under `C:\TwinCAT\3.1\Boot\Plc\`, named `port_852.tpy`, you can remote desktop in using the PLC's IP address and use a file explorer to copy it from its Windows environment)
1. Place above `.tpy` file in `C:\Instrument\Settings\Config\NDX<instname>\configurations\twincat\` - it will need to be called whatever it was before or whatever it was in the config (it's passed in via a macro) - it's usually called `tc_project_app.tpy`
1. Start the `TC` IOC again from IBEX. This should re-generate the `.db` file in the above directory and you should now have working communication. The table of motors may take a while to update so to check if things are working it may be easiest to use the `Beckhoff Engineering` device screen. If this does not exist on an instrument, create it. 

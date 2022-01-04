
> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff)

Beckhoff motor controllers are the most complex in use at ISIS and will be the standard going forward. A Beckhoff controller is basically a generic PLC that includes a number of useful functions out of the box for running motors. The generality of a beckhoff means that it will most likely be used in the future for measuring and controlling other hardware outside of motion. A more detailed presentation has been given about Beckhoffs in a [Code Chat](Code-Chats) entitled Layers, Onions and Ogres.

## Documentation
- [Axis and Controller Commissioning Guide](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/Ee_aMxb5CF1Dlz-NUGW3OVgB0K7vQjXXwZDwSl5DSHN48w?e=GjqNEb&isSPOFile=1) document describing setting up a controller and TwinCAT solution for a new system and configuring real and virtual axes within TwinCAT environment.

## Code on the controller
Unlike most other devices (except the Galil) the computing group has some oversight over the PLC code written on the controller. It has been agreed that this code will mostly be written by IDD, with oversight from computing to guide good programming practices, assist in debugging etc. The ISIS first version of this code is stored at https://github.com/ISISComputingGroup/BeckhoffPLCCode/, which has an accompanying wiki to discuss specifics of the codebase. However, going forward the code will be written in collaboration with the ESS and stored [here](https://bitbucket.org/europeanspallationsource/tc_generic_structure/src/master/).


## Testing
See [Beckhoff testing](Beckhoff-testing)

## Commissioning steps
These steps are for commissioning a Beckhoff on a beamline. 

### Networking
Beckhoffs are connected to NDX machines via private networks, in much the same way as the Galils. By convention Beckhoffs live in the `192.168.1.22X` range, starting at 1 for the first controller (`192.168.1.221`) 

### ADS routes
To actually communicate via the ADS transport layer you will need to set up a route on the instrument PC. To do so: 
1. Install the XAR tools if not already installed. A copy of these will be hosted on `<public share>\third_party_installers\special_drivers\beckhoff\`. All of the defaults are fine so this should be a case of just clicking through the wizard and installing the drivers that show up. 
2. Set up an ADS route on the NDX: 
  - `Right-click TwinCAT icon in system tray -> Router -> Edit Routes -> Add...` with these settings:
    - Advanced settings ticked, click the IP Address radio button, enter the IP address (mentioned above) 
    - Static Target routes and remote routes (default) 
    - Everything else can be left as defaults
3. To confirm that this has been set up remote into the controller itself on the aforementioned IP address and check that the route to the NDX has been added automatically. You should not need to manually add a route in the controller. 

### IOC setup
The IOC should be able to talk via ADS at this point but will need setting up in the respective configs. 
- A `.tpy` file will be used for `tCioc` to actually talk to the hardware via ADS - this should be placed in the instrument's twincat config area
- A `MTRCTRL` number will need to be given - this is the normal controller number
- `Beckhoff_plc_code` should be specified as a macro, this may be removed in future releases, more information on this is available below however it should be set to `1` for instruments running the latest code. 

#### Fields that aren't automatically populated
Although commissioning a Beckhoff is far simpler than a Galil from an IBEX perspective, there are some fields that need to be set manually for each axis.  These are: 
- Engineering units (`.EGU`) - [ticket to populate](https://github.com/ISISComputingGroup/IBEX/issues/6855)
- Axis description (`.DESC`) - [ticket to populate](https://github.com/ISISComputingGroup/IBEX/issues/6860)
- Velocity (`.VELO`) - [ticket to populate](https://github.com/ISISComputingGroup/IBEX/issues/6861)

These can be set via a `caput` and will be autosaved thereafter.

#### Axes, motion setpoints
These are loaded in the usual way, you'll need to put your `axes.cmd` and `motionSetpoints.cmd` files alongside the `tpy` file (in the twincat config directory)

#### If a controller has more than 8 axes
If a controller with more than 8 axes is going to be used, the TWINCAT IOC will alias records to the next controller number so they are shown in the GUI. For this to work you need to make sure that the next available controller number is not (and never will be, so long as the TWINCAT IOC uses it) used. 

## IOC(s)

There are currently two IOCs that we have to communicate with Beckhoffs.

### [tcIoc](tcIOC)

The current Beckhoff applications that are being run through `tcIOC` and the CI pipeline discussed above are:
* [dummy_PLC](https://github.com/ISISComputingGroup/BeckhoffPLCCode/tree/dummy_PLC)- a PLC that does very little, basically used to test that fundamental tcIOC comms works
* [old_ISIS_code](https://github.com/ISISComputingGroup/BeckhoffPLCCode/tree/Ticket5052_refactor_test_runner) - this is the old ISIS prototype motion code that is currently on the CRISP jaws. Hopefully this code can be removed once the jaws are moved on.
* [ESS_base_code](https://bitbucket.org/europeanspallationsource/tc_generic_structure/) (now linked to by `main` of the `BeckhoffTestRunner` repository) - this is the collaboration code that we will be using go forward.

### MCAG (defunct)

This IOC was originally written by ESS. It uses an ASCII protocol over TCP/IP to do the communication and is very specifically designed for motion. There is a simulator which can be run using the following steps:

- `cd EPICS\support\MCAG_Base_Project\master\epics\simulator`
- `doit.bat`
- Start the IOC (host macros needs to be set to 127.0.0.1:5024)

~Currently this is only being run on IMAT. It should soon be replaced by the collaboration code.~ - **It has been replaced by the new code, so is now defunct.**


### Beckhoff config area

The config area contains a directory used for storing `.tpy` files for use with `tcIoc`. On an instrument it should look like this: `\instrument\settings\config\<instname>\configurations\twincat\`. The TWINCAT IOC will search in this directory using the given `TPY_FILE` macro. The generated DB file also gets created in this directory by `tcIoc`. 

## Updating

Some discussion has been had on how we handle updates to the Beckhoff PLC code and `tcIoc` etc. this is documented [here](https://stfc365.sharepoint.com/:w:/s/ISISMechatronics/EXnBTNmcqqVCkIXXxjSvYdwBD3ZihXKDE0pZpiErGnkJ1g?e=4%3AWjCJxN&at=9&CID=0DF00AB8-D565-4B81-9AA2-C0DD226434CA&wdLOR=c76050FF1-1FF0-4AC8-A94C-0127E17DD337)
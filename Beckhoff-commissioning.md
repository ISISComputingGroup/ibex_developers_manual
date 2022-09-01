> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff) > [Beckhoff commissioning](Beckhoff-Commissioning)

## Commissioning steps
These steps are for commissioning a Beckhoff on a beamline. 

### Networking
Beckhoffs are connected to NDX machines via private networks, in much the same way as the Galils. By convention Beckhoffs live in the `192.168.1.22X` range, starting at 1 for the first controller (`192.168.1.221`) 

### ADS routes
To actually communicate via the ADS transport layer you will need to set up a route on the instrument PC. To do so: 
1. Install the XAR tools if not already installed. A copy of these will be hosted on `<public share>\third_party_installers\special_drivers\beckhoff\`. All of the defaults are fine so this should be a case of just clicking through the wizard and installing the drivers that show up. 
2. Set up an ADS route on the NDX: 
  - `Right-click TwinCAT icon in system tray -> Router -> Edit Routes -> Add...` with these settings:
    - Advanced settings ticked, click the IP Address radio button, then enter the IP address (mentioned above) on box at top. Press the return key after entering this in the box - this seems to work better than pressing the refresh button.  
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
- ~Velocity (`.VELO`) - [ticket to populate](https://github.com/ISISComputingGroup/IBEX/issues/6861)~ - now done!

These can be set via a `caput` and will be autosaved thereafter.

#### Axes, motion setpoints, jaws
These are loaded in the usual way, you'll need to put your `axes.cmd` and `motionSetpoints.cmd` files alongside the `tpy` file (in the `twincat` config directory)

#### Jaws

Jaws controlled by Beckhoffs don't actually require any logic to calculate gaps & centres, as this is done on the controller using virtual axes for the gaps and centres, so instead we load in a `$(JAWS)/db/jaws_alias.db` file instead of the usual `jaws.db`. This takes macros for the (virtual) axes to use as the gaps and centres.

#### If a controller has more than 8 axes
If a controller with more than 8 axes is going to be used, the TC IOC will alias records to the next controller number so they are shown in the GUI. For this to work you need to make sure that the next available controller number is not (and never will be, so long as the TC IOC uses it) used. 

#### Arbitrary fields 

It was decided during [A meeting with the motion team](https://github.com/ISISComputingGroup/IBEX/issues/6916) that extra fields, for example LARMOR's air signals + bump strips will be exposed via a separate `PROG` file within the PLC, which would then propagate to the `tpy` file, and therefore get picked up by `TcIOC`. At the time of writing the approach with these is to place a block on them on an instrument within the same config area which will log them over time. This has the benefit of giving them a human readable name too. We may decide to automate this in the future. 

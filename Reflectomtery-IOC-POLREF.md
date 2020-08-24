> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [POLREF](Reflectomtery-IOC-POLREF)

Specific information about POLREF.

### Slit 3/Beam blocker

Slit 3 is a tall set of normal jaws sitting on the bench. In horizontal sample mode the centre of the jaws is set using the `S3OFFSET` parameter which sets the distance from beam to the jaws, (usually set to 0). The bench movement means that the centre of the jaws rarely needs to change except during a slit scan.
Slit 3 can also be set into beam blocker mode; south jaw in horizontal mode, east or west jaws in vertical sample mode. In this state the beam blocked jaws will move independently of the slit centre using `S3S` and `S3N` or `S3W` and `S3W`. They retain the natural jaw directions so that positive is away from the centre of the jaw.

### Components on the Bench

Components that are on the bench do not track the beam in the same way as normal components. They rely on the underlying bench to track the beam and then their positions are just relative to the bench. This will in effect look the same as if they were tracking the beam but they don't.

### Blocks

Blocks that may be confusing:

- `Height`: Distance from the sample centre of rotation to the sample. This is used to align the sample with the beam.
- `Height2`: Distance between the beam and the centre of rotation; usually set a 0. This moves the course z stage tracking the beam.

### Parameter Autosave

It is hard to know which parameters to autosave and which not to. Probably with use we will find out. I have gone with Theta and polariser angles are not autosaved all other heights and offsets are. So that when coming back from SECI the setpoints will mirror those in SECI quite closely. Other axis parameters, direct parameters and slits are not autosaved so they come back as they are, except for bench angle offset and seesaw which are autosaved.


# Initial Testing

Spreadsheet is here.

Issues were:

1. On running the routine for transferring the SECI motor setups to IBEX, all the encoders were turned off. This may be a one off thing but still it should happen.
    - This was because I ran the original motor setup in sim mode. Yes this should not happen, I have added it to the information page so it won’t happen again.
1. There was a request for a command in python for interrogating a motor e.g “pos Phi”  and it tells you all sorts of things about phi like its position offset limits etc. that could then be used in a script.
    - We will probably never get to this if we put it on our list. I will send some details describing how you might create such a script let me know if you need help.
1. There again also seemed to be an issue with High and low limits being the wrong way around as well as directions not being correct after the transfer. 
    - For all axes on the spreadsheet I have confirmed that they are wrong in SECI; there is nothing we can do about this.
1. Where Dual position was marked in the SECI motor table there were issues of odd behaviour in IBEX that will need fixing. This affects the PolREF current sheet.
    - [Ticket 5647](https://github.com/ISISComputingGroup/IBEX/issues/5647) 
1. The major issue was that the IBEX setpoints were not transferred back to SECI when switching form IBEX back to SECI. The current positions were. This means that if someone reboots SECI and then presses move then the beamline will move unexpectedly. This is not good and needs a fix of some kind as it could lead to crash’s I know future wise we should all be in IBEX but for the next year I can see people switching back and forth,
    - I think that a script the user can run in OpenGenie is probably the best idea so that they have control over when they want they readbacks to be the same as the setpoint. Please read and approve [5648](https://github.com/ISISComputingGroup/IBEX/issues/5648). 
1. Labels that were the wrong way around such as the laser Gimbal axes theta and chi. We swapped them but not necessarily in the config, Also for some reason the PolREF sample stage had phi and Psi the wrong way around and again I am not sure they were swapped to the correct position fully.
    - Gimbal is wrong in SECI
    - PSI and CHI was my mistake in the config the motors are gonio upper and lower and I guessed the wrong way round. Now fixed in config.
1. Stop_ibex_server_start_seci does not finish. It starts seci but waits for SECI to finish, which is not what we want. Make it start in separate consol.
    - https://github.com/ISISComputingGroup/IBEX/issues/5651 
1. There was an error loading programs into SECI this has been fixed by combining programs in the galil.
1. There is something wrong with the bench movement. We think that it is because it was not synced and the max bench angle had not been implemented. (Extra note we tried moving it and then unsynced the movement of the slide, then reveresed the slide we never resynced the movement)
    - We should retest this after completing [5541](https://github.com/ISISComputingGroup/IBEX/issues/5541) 
1. Jaw 1 was synchronised and should not be (jaws in general are not synchronised to avoid clashing).
    - Changed in config
1. Some errors in the logs for which I have created tickets
    - [5649](https://github.com/ISISComputingGroup/IBEX/issues/5649)
    - [5650](https://github.com/ISISComputingGroup/IBEX/issues/5650)
1. Height and Height2 point at the same thing on the OPI
    - Corrected in master
1. Check backlash on slits is ok, currently move is towards centre of slit them slowly out to position.

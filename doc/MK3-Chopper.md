> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [MK3 Chopper](MK3-Chopper)

The MK3 Chopper is a standard chopper and used by multiple beamlines. The chopper is run from a system pc which is running server software and is connected to use .Net remoting. The code on the server is controlled by the electronic systems design group. 

To connect to the server the IOC instantiates a remote object of type IBeamLine and uses this to interrogate the server. This is held in `MK3ChopperSkeleton.dll` held in the support directory. To set up the remote a configuration file is needed and this is currently held in `c:\LabVIEW Modules\Drivers\ISIS MK3 Disc Chopper\MK3_Chopper.config`. There is a test server which can be found in the passwords file along with an instrument setting.

The IOC connects from the driver to the Mk3BridgeLib.dll (in support) using a c interface. The Mk3BridgeLib uses the Chopper C# object which uses the skeleton lib.

# User Control

The user can only start/stop/park and unpark the mk3chopper using the panel on the chopper itself. It also has to be put into remote mode before any commands can be sent to it. [This is limited by the hardware control but may be expanded by the chopper group at some point. Email has been sent to them Sep 2019](https://github.com/ISISComputingGroup/IBEX/issues/4389)

# Troubleshooting

## User cannot set Frequency

When trying to set a frequency if the frequency readback does not change start by looking at the log file. If the file read `Current User Demand Delay Too Large for Angle , Direction & Speed` it means that the phase for the chopper is too large for the current frequency. I believe that the phase must be smaller than `1/frequency` e.g. for the instrument running at 50Hz it needs to be smaller than 20,000us. 

> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [MK3 Chopper](MK3-Chopper)

The MK3 Chopper is a standard chopper and used by multiple beamlines. The chopper is run from a system pc which is running server software and is connected to use .Net remoting. The code on the server is controlled by the electronic systems design group. 

To connect to the server the IOC instantiates a remote object of type IBeamLine and uses this to interrogate the server. This is held in `MK3ChopperSkeleton.dll` held in the support directory. To set up the remote a configuration file is needed and this is currently held in `c:\LabVIEW Modules\Drivers\ISIS MK3 Disc Chopper\MK3_Chopper.config`. There is a test server which can be found in the passwords file along with an instrument setting.

The IOC connects from the driver to the Mk3BridgeLib.dll (in support) using a c interface. The Mk3BridgeLib uses the Chopper C# object which uses the skeleton lib.

# Notes

This can currently only been built in VS2010 because the solution file is 2010.


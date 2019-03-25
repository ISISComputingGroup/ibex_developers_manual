> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff)

Beckhoff motor controllers are the most complex in use at ISIS and will be the standard going forward. A Beckhoff controller is basically a generic PLC that includes a number of useful functions out of the box for running motors. The generality of a beckhoff means that it will most likely be used in the future for measuring and controlling other hardware outside of motion. A more detailed presentation has been given about Beckhoffs in a [Code Chat](Code-Chat).

## Code on the controller
Unlike most other devices (except the Galil) the computing group has some oversight over the PLC code written on the controller. It has been agreed that this code will mostly be written by IDD, with oversight from computing to guide good programming practices, assist in debugging etc. This code is stored in https://github.com/ISISComputingGroup/BeckhoffPLCCode/, which has an accompanying wiki to discuss specifics of the codebase.

### Building and simulating the code
Beckhoff code can be run as a simulated system on a developer machine by downloading [TwinCAT 3](https://infosys.beckhoff.com/english.php?content=../content/1033/tcinfosys3/html/startpage.htm&id=) (which is really just a Visual Studio plugin). TwinCAT provides an `automation interface` to communicate with the TwinCAT environment using DCOM. A C# builder program has been written to build Beckhoff code using this interface and is currently being run on the ndw1926 on Jenkins. C# was chosen as this is the language that all Beckhoff examples are written. Beckhoff claim to support a Python interface but no examples or solid documentation could be found. A quirk of using this DCOM interface is that the Jenkins slave must be run as an interactive user and thus not as a service. To do this there is a bat file that should run on startup inside `C:\Users\ibexbuilder\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

## IOC(s)

There are currently two IOCs that we have to communicate with Beckhoffs.

### tcIOC

This IOC was originally written at LIGO and is in a stable state. It's more targeted at the use of Beckhoffs as generic PLCs and has little motion support. It constructs db records by examining the PLC project on the controller and communicates with it using ADS (Beckhoff's own protocol). More detail can be found at https://github.com/ISISComputingGroup/EPICS-tcIoc.

### MCAG

This IOC was originally written by ESS and is still in heavy development there. It uses an ASCII protocol over TCP/IP to do the communication and is very specifically designed for motion. There is a simulator which can be run using the following steps:

- `cd EPICS\support\MCAG_Base_Project\master\epics\simulator`
- `doit.bat`
- Start the IOC (host macros needs to be set to 127.0.0.1:5024)




> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff)

Beckhoff motor controllers are the most complex in use at ISIS and will be the standard going forward. A Beckhoff controller is basically a generic PLC that includes a number of useful functions out of the box for running motors. The generality of a beckhoff means that it will most likely be used in the future for measuring and controlling other hardware outside of motion. A more detailed presentation has been given about Beckhoffs in a [Code Chat](Code-Chats) entitled Layers, Onions and Ogres.

## Code on the controller
Unlike most other devices (except the Galil) the computing group has some oversight over the PLC code written on the controller. It has been agreed that this code will mostly be written by IDD, with oversight from computing to guide good programming practices, assist in debugging etc. The ISIS first version of this code is stored at https://github.com/ISISComputingGroup/BeckhoffPLCCode/, which has an accompanying wiki to discuss specifics of the codebase. However, going forward the code will be written in collaboration with the ESS and stored [here](https://bitbucket.org/europeanspallationsource/tc_generic_structure/src/master/).

### Building and simulating the code
Beckhoff code can be run as a simulated system on a developer machine by doing the following: 

 1. Download and install [TwinCAT 3 XAE](https://www.beckhoff.com/forms/twincat3/warenkorb.aspx?lg=en&title=TC31-Full-Setup.3.1.4022.30&version=3.1.4022.30) more information can be found about this [here](https://infosys.beckhoff.com/english.php?content=../content/1033/tcinfosys3/html/startpage.htm&id=). You will need to either create an account or register yourself as a guest. The XAE is really just a Visual Studio plugin.
 1. Start the Twincat XAE. This can be done by clicking on the TwinCat icon in the system tray.
 1. Open the Twincat project that you are interested in. For example there is a simple test PLC [here](https://github.com/ISISComputingGroup/BeckhoffPLCCode/tree/master/dummy_PLC)
 1. Ensure that you have the following toolbars enabled in the XAE:
    - `TwinCAT PLC`
    - `TwinCAT XAE Base`
1. Click the `Activate Configuration` button ![Activate](beckhoff/Activate.PNG)
2. TwinCAT will ask you to enter a code to get a trial license. You will need to do this once a week.
3. If prompted if you wish to start the system in `Run Mode` click `Ok`. Otherwise start run mode using the button next to `Activate Configuration` ![Run](beckhoff/Run.PNG)
4. You now have a simulated beckhoff PLC running on your PC. This behaves the same as real hardware and so all development can be done against it. You could now also run an IOC up talking to this local PLC.
5. To see what is happening inside this PLC in more detail, and to change values, you can use the login button ![Login](beckhoff/Login.PNG)

### Continuous Integration

Beckhoff provides an `automation interface` which can do any of the things you can do in the Twincat XAE automatically through DCOM. A C# (Beckhoff do not fully support a Python interface 😢) program (`AutomationTools`) has been written to leverage this interface in the following way to write integration tests for the Beckhoff:

![Overview](beckhoff/beckhoff_overview.png)

1. Jenkins will pull the Beckhoff PLC code from github
2. `build.bat` is run to first build the `AutomationTools` themselves then to build the PLC code using the `automation interface`. This build will also create a `*.tpy` file, which outlines how to connect to the PLC and can be used to configure the IOC itself.
3. The IOC test framework is started. This will first use the `AutomationTools` program to run a local simulated PLC. Then startup and test the Beckhoff twincat in the usual way.

This is currently being run on the ndw1926 node on Jenkins. A quirk of using this DCOM interface is that the Jenkins slave must be run as an interactive user and thus not as a service. To do this there is a bat file that should run on startup inside `C:\Users\ibexbuilder\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

## Testing

To run tests locally you must build the solution in the `BeckhoffPLCCode -> util_scripts -> AutomationTools` directory to create the AutomationTools binary (used by the IOCTestFramework to run the Beckhoff emulator). Once this is done you can run the following command in your `BeckhoffPLCCode` directory to begin testing:

```
python %EPICS_KIT_ROOT%\\support\\IocTestFramework\\master\\run_tests.py -tp ".\\dummy_PLC\\tests"
```

## Networking
Beckhoffs are connected to NDX machines via private networks, in much the same way as the Galils. By convention Beckhoffs live in the `192.168.1.22X` range. 

## IOC(s)

There are currently two IOCs that we have to communicate with Beckhoffs.

### [tcIoc](tcIOC)

### MCAG

This IOC was originally written by ESS. It uses an ASCII protocol over TCP/IP to do the communication and is very specifically designed for motion. There is a simulator which can be run using the following steps:

- `cd EPICS\support\MCAG_Base_Project\master\epics\simulator`
- `doit.bat`
- Start the IOC (host macros needs to be set to 127.0.0.1:5024)

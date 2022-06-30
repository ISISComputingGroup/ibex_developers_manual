
> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff) > [Beckhoff testing](Beckhoff-testing)

# Beckhoff testing

Note: you may need to disable some windows features, such as Hyper-V, Windows Hypervisor Platform etc.

For reference, here is a working setup and its features: 

![windows features](https://user-images.githubusercontent.com/14823767/149163247-309eb8de-41d4-4a06-b9ff-9009865ab340.png)


## Building and simulating the code
Beckhoff code can be run as a simulated system on a developer machine by doing the following: 

 1. Download and install [TwinCAT 3 XAE](https://stfc365.sharepoint.com/sites/ISISMechatronics/Shared%20Documents/Forms/AllItems.aspx?viewid=a9a65e76%2D4335%2D479e%2Da1eb%2De12265e5cad6&id=%2Fsites%2FISISMechatronics%2FShared%20Documents%2FTwinCAT%20Development%2FTwinCAT%20Software) more information can be found about this [here](https://infosys.beckhoff.com) (click TwinCAT 3 on the left). If you do not have permission ask IDD. The XAE is really just a Visual Studio plugin.
 1. Start the Twincat XAE. This can be done by clicking on the TwinCat icon in the system tray.
 1. Open the Twincat project that you are interested in. For example the PLC_solution [here](https://github.com/ISISComputingGroup/BeckhoffTestRunner)
 1. Ensure that you have the following toolbars enabled in the XAE (`Tools > Customize...`):
    - `TwinCAT PLC`
    - `TwinCAT XAE Base`
    - (optionally) `TwinCAT XAE Remote Manager`
1. Click the `Activate Configuration` button ![Activate](beckhoff/Activate.PNG) - Note you may need to do [this](https://control.com/forums/threads/twincat-3-error-when-switched-to-run-mode.43467/) if it moans about ticks. You may also need to disable Hyper-V and disable Intel Virtualisation from within BIOS on your machine if this error persists.  
To revert this run: `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All` in an elevated Powershell window. You may also need to execute `win8settick.bat` in `C:\TwinCAT\3.1\System` as administrator and reboot. 
2. TwinCAT will ask you to enter a code to get a trial license. You will need to do this once a week.
3. If prompted if you wish to start the system in `Run Mode` click `Ok`. Otherwise start run mode using the button next to `Activate Configuration` ![Run](beckhoff/Run.PNG)
4. You now have a simulated beckhoff PLC running on your PC. This behaves the same as real hardware and so all development can be done against it. You could now also run an IOC up talking to this local PLC.
5. To see what is happening inside this PLC in more detail, and to change values, you can use the login button ![Login](beckhoff/Login.PNG)

### Continuous Integration

Beckhoff PLC code is being developed by people who do not have CI expertise and have their own repository structures yet we want integration into some form of CI to be as easy as possible. This lent itself to the following structure:
* A `BeckhoffTestRunner` repository that is owned by us and contains the jenkinsfile and other utilities required for CI
* Every branch on this repository (apart from master) then pulls a different PLC project down (note each project could be from a different repository or from separate branches on the same repository)
* The jenkinsfile can then do the one or both of the following:
   * Build the project (currently assumed to be called `solution.sln` at the top of pulled PLC project)
   * Run any [IOCTestFramework](https://github.com/ISISComputingGroup/EPICS-IOC_Test_Framework) tests (currently assumed to be in a `tests` folder at the top of the pulled PLC project) - these will likely be written by us

This means that the workflow for adding new PLC projects into CI is:
1. A PLC developer writes their code (making sure the solution is called `solution.sln`)
2. They give us a link to the repo and branch that contains the code
3. We create a new branch on `BeckhoffTestRunner` and modify it to point at their repo
4. At this point they have CI for building their code
5. We make a decision about whether the code requires any system tests and if so add some into their repository

To actually run tests we use the Beckhoff `automation interface` which can do any of the things you can do in the Twincat XAE automatically through DCOM. AC# (Beckhoff do not fully support a Python interface 😢) program (`twinCATAutomationTools`) has been written to leverage this interface in the following way to write integration tests for the Beckhoff:

![Overview](beckhoff/beckhoff_overview.png)

1. Jenkins will pull a branch of [BeckhoffTestRunner](https://github.com/ISISComputingGroup/BeckhoffTestRunner).
2. `build.bat` is run to do the following:
   1. Build the `TwincatAutomationTools` solution, [twinCATAutomationTools](https://github.com/Simon-Cooper/twinCATAutomationTools)
   1. Use the `twinCATAutomationTools` to import the `test_config` into the generic Twincat Solution and build the PLC code using the `automation interface`. This build will also create a `*.tpy` file, which outlines how to connect to the PLC and can be used to configure the IOC itself.
3. The IOC test framework is started. This will use the `TwinCATAutomationTools` program to run a local simulated PLC. Then startup and test the Beckhoff twincat in the usual way.

This is currently being run on the ndw1926 node on Jenkins. A quirk of using this DCOM interface is that the Jenkins slave must be run as an interactive user and thus not as a service. To do this there is a bat file that should run on startup inside `C:\Users\ibexbuilder\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

To run a PLC locally you need a license. A trial license can be activated on a developer's machine by manually running through the building and running steps above until you are prompted to supply a captcha phrase to generate a license.

## Testing
1. clone `BeckhoffTestRunner` using `git clone --recursive https://github.com/ISISComputingGroup/BeckhoffTestRunner.git`
1. Then in `BeckhoffTestRunner` run: 
`git submodule update --init --recursive --remote`
1. To run tests locally you must build the `twinCATAutomationTools` tools then use them to set up a working simulated PLC. This can be done by running `build.bat` (best done not in an EPICS terminal). 
1. Create an epics terminal, and then run the following command in your `BeckhoffTestRunner` directory to begin testing:

```
python %EPICS_KIT_ROOT%\\support\\IocTestFramework\\master\\run_tests.py -tp ".\\tests"
```

Note that the IOC tests do not stop the PLC at the end of the run, however this isn't a problem as the PLC is restarted when the IOC tests start. If this fails to start the PLC it may be because you do not have a trial license. Debug the issue by manually running through the building and running steps above.
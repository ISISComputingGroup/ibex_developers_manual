> [Wiki](Home) > [The Backend System](The-Backend-System) > [Creating and Basics of IOCs](IOCs)

# Before Creating an IOC #

Remember, EPICS is a collaboration! Why create an IOC when you can just use one that's already out there? If the device is not ISIS specific, before thinking about creating an IOC check whether it is listed [here](https://epics.anl.gov/modules/manufacturer.php) and, if not, email the mailing list [here](https://epics.anl.gov/tech-talk/index.php).


# Creating an IOC #

Building a new IOC? Before you get started, take a look at the relevant [instrument page](https://github.com/ISISComputingGroup/IBEX/wiki) to see if there's any useful information for the device you're about to write an IOC for. Otherwise, let's get going. If you have problems see [See IOC and device Troubleshooting](IOC-And-Device-Trouble-Shooting).

There are two sorts of IOCs, EPICs and pycaspy. For EPICs type see the automatic creation below for pycaspy see the [pycaspy ioc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/ioc-pcaspy).

Need more than 1 IOC? See [IOC Duplication](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Duplicating-IOCs)

## Automatically
If you're building a new StreamDevice IOC you can use the [IOC Generator script](https://github.com/ISISComputingGroup/IBEX-device-generator), for developer info see the [wiki](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/IOC-Generator).

## Manually
If you're not creating a StreamDevice IOC or you would like to know how an IOC could be created manually see:
* [Creating an ISIS StreamDevice IOC](Creating-an-ISIS-StreamDevice-IOC)
* [Creating an LvDCOM IOC](Creating-IOC-wrapper-VI)
* [Creating a simple IOC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/EPICS-basics#creating-a-simple-ioc) - usual basic way to make an IOC on new EPICS installation, not the way we do it in ISIS.

## Fleshing out the IOC
1. You can now flesh out your IOC to work. I would encourage you to do this in a TDD style (if not write the tests afterwards) and make sure you follow the [conventions](IOCs#conventions). To write in a TDD style use:
    * [IOC Testing framework](IOC-Testing-Framework)
    * [Emulating devices](Emulating-Devices)

    If you used the script to create your IOC an empty emulator and IOC tests will have been created for you.

1. [Record simulation](Record-Simulation)

1. [IOC Finishing Touches](IOC-Finishing-Touches)
    * Additional for motors:
        1. [Adding motor IOC to global motor moving and stop all](Adding-motor-IOC-to-global-motor-moving-and-stop-all)
        1. [Add support for motor extras, e.g. axes](Add-support-for-motor-extras)    

1. [Running (and testing) IOC](Running-IOCs)

1. Add any manuals used to the [manuals directory](Manuals)

1. Add a page about the device in the correct categories in [Specific Device IOC](Specific-Device-IOC)

1. [Create an OPI](OPI-Creation) and send it to instrument scientists for approval.

# Conventions

* [IOC naming](IOC-Naming)

* [IOC descriptions](IOC-Descriptions)

* [ISIS PV guide](ISIS-PV-Guide)

* [PV naming](PV-Naming)

* [PV units & standards](PV-Units-&-Standards)

* [Macro naming](Macro-Naming)

* [IOC Startup](IOC-Startup)

# Other

* [aSub records](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/aSub-records)
* [Motor IOCs](Motor-IOCs)
* [Libraries to include](IOC-Libraries-to-include-with-order)
* Creating a MODBUS IOC (page removed at some point)
* [Using LVDCOM](Using-LVDCOM)
* [Convert Record](convert-record)
* [Stream Device Tips and Tricks](Stream-Device-Tips-and-Tricks)
* [IOC Utilities](IOC-Utilities) includes general templates
* [Removing or Renaming an IOC module ](Removing-or-Renaming-IOC-module)
* [IOC Testing framework](IOC-Testing-Framework)
* [Complexity of LabVIEW Drivers](Complexity-of-LabVIEW-Drivers)
* [Typical start up log for an ioc](IOC-Start-Example)
* [Some Design thoughts for a serial/Ethernet IOC](Some-Design-thoughts-for-a-serial-or-Ethernet-IOC)
* [Reducing build dependencies for older iocs](Reducing-Build-Dependencies)
* [Template Substitutions](Template-Substitutions)
* [Creating a State Machine](Creating-a-State-Machine-(Sequencer))
* [Limited range on PV](PV-with-a-limited-range)

# Remake and run IOC

When modifying and testing an IOC it helps if you chain the commands to make and run the IOC like below:
```
cd C:\Instrument\Apps\EPICS\support\<IOC name>\master && make clean uninstall && make && cd C:\Instrument\Apps\EPICS\ioc\master\<IOC name>\ && make clean uninstall && make && cd C:\Instrument\Apps\EPICS\ioc\master\<IOC name>\iocBoot\ioc<name>\ && runioc.bat
```

# Debugging IOCs

Debug builds of IOCs are built in jenkins and can be deployed to instruments, see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Deploying-a-DEBUG-build-IOC).

It can be useful to add a `msgBox` to pause so you can attach a debugger, see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/IOC-Utilities#pausing-an-ioc-at-startup) for instructions. If your error is during or after the db load is to call `runioc.bat a` this will start he ioc but run `a` as the start script. Now attach the debug and in the console type `< st.cmd`.
 To attach the debugger start the IOC, open visual studio with the code in you wish to debug, set breakpoints as you wish and in the top toolbar select "Debug >> Attach to process" find your process in the list and attach. You can control the debugger as you would other debuggers using the buttons on a toolbar just below the toolbar you clicked on with "Debug" in it.

# Specific IOC Information

For information on specific IOCs see [Specific Device IOC](Specific-Device-IOC)

# Further reading ##

* [EPICS record reference manual](http://www.aps.anl.gov/epics/EpicsDocumentation/AppDevManuals/RecordRef/Recordref-1.html)
* [IOC doxygen Documentation](http://epics.isis.rl.ac.uk/doxygen/main/)
* [IOC message logging](Ioc-message-logging)
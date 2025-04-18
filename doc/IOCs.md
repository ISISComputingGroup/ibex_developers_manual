# EPICS IOCs & Support Modules

```{toctree}
:glob:
:titlesonly:
:hidden:

iocs/*
```

## Before Creating an IOC

Remember, EPICS is a collaboration! Why create an IOC when you can just use one that's already out there? If the device is not ISIS specific, before thinking about creating an IOC check whether it is listed [here](https://epics.anl.gov/modules/manufacturer.php) and, if not, email the mailing list [here](https://epics.anl.gov/tech-talk/index.php).


## Creating an IOC

Building a new IOC? Before you get started, take a look at the relevant [instrument page](https://github.com/ISISComputingGroup/IBEX/wiki) to see if there's any useful information for the device you're about to write an IOC for. Otherwise, let's get going. If you have problems see [See IOC and device Troubleshooting](iocs/Troubleshooting).

There are two sorts of IOCs, EPICs and pycaspy. For EPICs type see the automatic creation below for pycaspy see the [pycaspy ioc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/ioc-pcaspy).

Need more than 1 IOC? See [IOC Duplication](iocs/creation/Duplicating-IOCs)

### Automatically
If you're building a new StreamDevice IOC you can use the [IOC Generator script](https://github.com/ISISComputingGroup/IBEX-device-generator).

### Manually
If you're not creating a StreamDevice IOC or you would like to know how an IOC could be created manually see:
* [Creating an ISIS StreamDevice IOC](iocs/creation/Creating-an-ISIS-StreamDevice-IOC)
* [Creating an LvDCOM IOC](iocs/creation/Creating-IOC-wrapper-VI)

### Fleshing out the IOC
1. You can now flesh out your IOC to work. I would encourage you to do this in a TDD style (if not write the tests afterwards) and make sure you follow the [conventions](iocs/Conventions). To write in a TDD style use:
    * [IOC Testing framework](iocs/testing/IOC-Testing-Framework)
    * [Emulating devices](iocs/testing/Emulating-Devices)

    If you used the script to create your IOC an empty emulator and IOC tests will have been created for you.

1. [Record simulation](iocs/testing/Record-Simulation)

1. [IOC Finishing Touches](iocs/creation/IOC-Finishing-Touches)
    * Additional for motors:
        1. [Adding motor IOC to global motor moving and stop all](iocs/tips_tricks/Adding-motor-IOC-to-global-motor-moving-and-stop-all)
        1. [Add support for motor extras, e.g. axes](iocs/tips_tricks/Add-support-for-motor-extras)    

1. [Running (and testing) IOC](iocs/testing/Running-IOCs)

1. Add any manuals used to the [manuals directory](iocs/conventions/Manuals)

1. Add a page about the device in the correct categories in [Specific Device IOC](Specific-IOCs)

1. [Create an OPI](client/opis/OPI-Creation) and send it to instrument scientists for approval.

## Conventions

* [IOC naming](iocs/conventions/IOC-Naming)

* [IOC descriptions](iocs/conventions/IOC-Descriptions)

* [ISIS PV guide](iocs/conventions/ISIS-PV-Guide)

* [PV naming](iocs/conventions/PV-Naming)

* [PV units & standards](iocs/conventions/PV-Units-&-Standards)

* [Macro naming](iocs/conventions/Macro-Naming)

* [IOC Startup](iocs/conventions/IOC-Startup)

## Other

* [aSub records](iocs/tools/aSub-records)
* [Motor IOCs](specific_iocs/Motors)
* [Libraries to include](iocs/compiling/IOC-Libraries-to-include-with-order)
* [Using LVDCOM](iocs/creation/Creating-IOC-wrapper-VI)
* [Convert Record](iocs/tools/Convert-Record)
* [Stream Device Tips and Tricks](iocs/tips_tricks/Stream-Device-Tips-and-Tricks)
* [IOC Utilities](iocs/tools/Utilities-Library) includes general templates
* [Removing or Renaming an IOC module](iocs/compiling/Removing-or-Renaming-IOC-module)
* [IOC Testing framework](iocs/testing/IOC-Testing-Framework)
* [Complexity of LabVIEW Drivers](system_components/labview/Complexity-of-LabVIEW-Drivers)
* [Typical start up log for an ioc](iocs/troubleshooting/IOC-Start-Example)
* [Some Design thoughts for a serial/Ethernet IOC](iocs/tips_tricks/Some-Design-thoughts-for-a-serial-or-Ethernet-IOC)
* [Reducing build dependencies for older iocs](iocs/compiling/Reducing-Build-Dependencies)
* [Template Substitutions](iocs/tools/Template-Substitutions)
* [Creating a State Machine](iocs/tools/Creating-a-State-Machine-(Sequencer))
* [Limited range on PV](iocs/tips_tricks/PV-with-a-limited-range)

## Remake and run IOC

When modifying and testing an IOC it helps if you chain the commands to make and run the IOC like below:
```
cd C:\Instrument\Apps\EPICS\support\<IOC name>\master && make clean uninstall && make && cd C:\Instrument\Apps\EPICS\ioc\master\<IOC name>\ && make clean uninstall && make && cd C:\Instrument\Apps\EPICS\ioc\master\<IOC name>\iocBoot\ioc<name>\ && runioc.bat
```

## Debugging IOCs

Debug builds of IOCs are built in jenkins and can be deployed to instruments, see [here](deployment/patch/Deploying-a-DEBUG-build-IOC).

It can be useful to add a `msgBox` to pause so you can attach a debugger, see [here](#pausing_an_ioc_at_startup) for instructions. If your error is during or after the db load is to call `runioc.bat a` this will start he ioc but run `a` as the start script. Now attach the debug and in the console type `< st.cmd`.
 To attach the debugger start the IOC, open visual studio with the code in you wish to debug, set breakpoints as you wish and in the top toolbar select "Debug >> Attach to process" find your process in the list and attach. You can control the debugger as you would other debuggers using the buttons on a toolbar just below the toolbar you clicked on with "Debug" in it.

## Specific IOC Information

For information on specific IOCs see [Specific Device IOC](Specific-IOCs)

## Further reading

* [EPICS record reference manual](http://www.aps.anl.gov/epics/EpicsDocumentation/AppDevManuals/RecordRef/Recordref-1.html)
* [IOC doxygen Documentation](http://epics.isis.rl.ac.uk/doxygen/main/)
* [IOC message logging](system_components/IOC-message-logging)
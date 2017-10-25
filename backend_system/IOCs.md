> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs)

## Creating an IOC ##
Building a new IOC? Before you get started, take a look at the relevant [instrument page](https://github.com/ISISComputingGroup/IBEX/wiki) to see if there's any useful information for the device you're about to write an IOC for. Otherwise, let's get going. If you have problems see [See IOC and device Troubleshooting](IOC-And-Device-Trouble-Shooting).

1. [The Workflow - step 1!](Creating-an-IOC-Workflow)
    * [Some Design thoughts for a serial/Ethernet IOC](Some-Design-thoughts-for-a-serial-or-Ethernet-IOC)
    * [Creating an ISIS StreamDevice IOC](Creating-an-ISIS-StreamDevice-IOC)
    * [Creating an LvDCOM IOC](Creating-IOC-wrapper-VI)
1. You can now flesh out your IOC to work. I would encourage you to do this in a TDD style (if not write the tests afterwards). Use:
    * [IOC Testing framework](IOC-Testing-Framework)
    * [Emulating devices](Emulating-Devices)

1. [IOC Finishing Touches](IOC-Finishing-Touches)
    * Additional for motors [Adding motor IOC to global motor moving and stop all](/Adding-motor-IOC-to-global-motor-moving-and-stop-all)

1. [Record simulation](Record-Simulation)

1. [Disable records](Disable-records)

1. [Running (and testing) IOC](Running-IOCs)

1. [Add logging](Logging-from-the-archive)

1. Add any manuals used to the [manuals dir and list](Manuals)

## Conventions

* [IOC naming](IOC-Naming)

* [ISIS PV guide](ISIS-PV-Guide)

* [PV naming](PV-Naming)

* [PV units & standards](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/PV-Units-&-Standards)

* [Macro naming](Macro-Naming)

## Other

* [Libraries to include](IOC-Libraries-to-include-with-order)
* [Creating a MODBUS IOC](MODBUS-IOC) 
* [Using LVDCOM](Using-LVDCOM)
* [Convert Record](convert-record)
* [Multi-value Protocols Tricks](Multi-value-Protocols)
* [IOC Utilities](IOC-Utilities)
* [Removing or Renaming an IOC module ](Removing-or-Renaming-IOC-module)
* [IOC Testing framework](IOC-Testing-Framework)
* [Creating soft motors to control real motors](Creating-soft-motors-to-control-real-motors)
* [Complexity of LabVIEW Drivers](Complexity-of-LabVIEW-Drivers)
* [Typical start up log for an ioc](IOC-Start-Example)
## Specific IOC Information

[Manuals](Manuals)

* [Barndoors and Momentum Slits on MUON Front End](Barndoors-and-Momentum-Slits-on-MUON-Front-End)
* [Polaris Jaws](Polaris-Jaws)
* [EnginX Jaws](EnginX-Jaws)
* [Motors and SetPoints](Motor-SetPoints)
* [Lakeshore 336](Lakeshore336)
* [Mecury iTC](MercuryiTC)
* [TPG26x](TPG26x)
* [Julabo](Julabo)
* [Danfysik](Danfysik)
* [Neocera LTC-21](Neocera-LTC-21)
* [Instron stress rig](Instron-stress-rig)
* [SDTest](SDTest)
* [SCM](SCM)

## Further reading ##

* [EPICS record reference manual](http://www.aps.anl.gov/epics/EpicsDocumentation/AppDevManuals/RecordRef/Recordref-1.html)
* [IOC doxygen Documentation](http://epics.isis.rl.ac.uk/doxygen/main/)
* [IOC message logging](Ioc-message-logging)
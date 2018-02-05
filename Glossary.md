> [Wiki](Home) > [Glossary](Glossary)

Glossary
========

ACF
---
**A**ccess **C**ontrol **F**ile.  A file used by the [Gateway](#Gateway) which contains rules for access.

[ActiveMQ](ActiveMQ)
----------
A messaging system that is used in a number of places throughout IBEX.  Specifically, [The Alarm Server](Alarms) and [The IOC Log Server](Ioc-message-logging).  See [ActiveMQ Homepage](http://activemq.apache.org/) for more information on the technology.

Archive Engine
--------------
A [CSS](#CSS) component that archives [PV](#PV) values.  Implemented in [IBEX](#IBEX) in the [Block Archive](#Block Archive) and [Instrument Archive](#Instrument Archive)

[Autosave](Autosave)
----------
A system to record PV values and reinstate them on startup of an IOC.

Backdoor
--------
A method of changing the internal parameters of an emulator to mimic the behaviour of the actual device.

[Barndoors](Barndoors-and-Momentum-Slits-on-MUON-Front-End)
-----------
Slits used on each of the Muon instruments to control the neutron flux to the sample.  Each "jaw" pivots on one edge, much like a door on a hinge.

Block Archive
-------------
Archives block values using the [CSS Archive Engine](#Archive Engine) and restarts whenever block definitions and/or the configuration changes. 

BlockServer
-----------


Branch
------

[CALab](https://www.helmholtz-berlin.de/zentrum/locations/it/software/exsteuer/calab/index_en.html)
-----
**C**hannel **A**ccess **Lab**oratory.  A library which enables [EPICS](#EPICS) and [LabVIEW](#LabVIEW) to communicate with each other.

[Calibration Files](Calibration-Files)
-------------------
Files which contain information about how pieces of sample environment equipment translate their readings into useful data. e.g. temperature sensor calibration files which enable translation from electrical measurements to temperature values.

Channel Access (CA)
-------------------
A Protocol that defines how [PV](#PV) data is transferred between a server and client in an [EPICS](#EPICS) control system.

[Chopper](Choppers)
-------
A device, usually a spinning disc of thick metal with a narrow slot, which allows selection of a particular energy range of neutrons by varying its speed.

[CLF](https://www.clf.stfc.ac.uk/Pages/home.aspx)
-----
**C**entral **L**aser **F**acility.  A department at RAL that also uses the [EPICS](EPICS) control system.

[Code Chats](Code-Chats)
------------
Short meetings and presentations held within the group to discuss various aspects of the control system, or other related technologies.

Collision Detection
-------------------
A method for detecting collisions between moving beamline components by simulating the requested move beforehand.  See [Collision Detection Project](Collision-Detection-Project.md) for more information.  

Commit
------


Component
---------


[Config-Checker](Config-Checker)
----------------
A Python script to highlight potential issues with current configurations when a new version of [IBEX](#IBEX) is installed.

[Config-Upgrader](Config-Upgrader)
----------------
A Python script to upgrade current configurations to be compatible with new versions of [IBEX](#IBEX).

ConServer
---------


[CSS](http://controlsystemstudio.org/)
-----
"**C**ontrol **S**ystem **S**tudio is an [Eclipse](#Eclipse)-based collection of tools to monitor and operate large scale control systems, such as the ones in the accelerator community. It's a product of the collaboration between different laboratories and universities."

DB File
-------
A file containing the definition of [PVs](#PV) for a specific [IOC](#IOC) using [records](#Record). 

Dial values
-----------


[Eclipse](http://www.eclipse.org/)
---------
An IDE and collection of tools for development of GUIs.  [CSS](#CSS) and the IBEX client are based on it.

Emulator
--------
A software implementation of hardware.  Usually used to help write and test an [IOC](#IOC) and [OPI](#OPI).  See [Emulating-Devices](Emulating-Devices) for more information.

[EPICS](EPICS)
-------
**E**xperimental **P**hysics and **I**ndustrial **C**ontrol **S**ystem.  A client/server control system using [Channel Access](#Channel Access) as its communication protocol, forming a distributed real-time database of machine values ([PVs](#PV)).
It is a collection of software tools collaboratively developed which can be integrated to provide a comprehensive and scalable control system.

Field
-----


[Gateway](Access-Gateway)
---------
A service that controls access between two or more networks.

Genie-Python
------------
An implementation of the [OpenGenie](http://www.opengenie.org) scripting language in Python, or at least its commands specific to instrument control.  Documentation [here](http://shadow.nd.rl.ac.uk/genie_python/sphinx/genie_python.html).

IBEX
----
The new ISIS instrument control system.  Primarily based on [EPICS](#EPICS) as the underlying technology.

Instrument Archive
------------------
Archives [PV](#PV) values using the [CSS Archive Engine](#Archive Engine) which have the ARCHIVE [Field](#Field) set in their [Record](#Record).  

IOC
---
**I**nput**O**utput**C**ontroller.  A process which reads and writes [PVs](#PV).  Often interfaces with hardware (e.g. sample environment equipment) to enable it to be controlled remotely.

[LabVIEW](http://www.ni.com/labview/)
---------
**Lab**oratory**V**irtual**I**nstrument**E**ngineering**W**orkbench.  A graphical programming language in which the device drivers for [SECI](#SECI) are written.

[LeWIS](https://github.com/DMSC-Instrument-Data/lewis)
-------
**Le**t's **W**rite **I**ntricate **S**imulators.  A Python framework for producing and running [emulators](#Emulator).  See [Emulating-Devices](Emulating-Devices) for more information.

Macro
-----


Mini-Inst
---------
A term used to describe an instrument which uses components from both the [SECI](#SECI) and [IBEX](#IBEX) control systems.  For example, an [IOC](#IOC) wrapped with a [VI](#VI) on a [SECI](#SECI) instrument (using [CALab](#CALab)).

[Momentum Slits](Barndoors-and-Momentum-Slits-on-MUON-Front-End)
----------------
Slits used on the Muon front-end to control the neutron momentum to the three instruments.

MySQL
-----


[Nicos](http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-2.0/dirhtml/)
-------
A network-based control system.  Some elements of it are used in the [script server](#Script Server).

OPI
---
**Op**erator **I**nterface.  A file used in [CSS](#CSS) to enable a user to interact with an IOC graphically.

Plugin
------


ProcServ
--------


PV
--
**P**rocess **V**ariable.  A named piece of data and the primary object of the [Channel Access Protocol](#Channel Access), often associated with a piece of equipment (e.g. status, readback, setpoint, parameter).

PVLIST
------
A file used by the [Gateway](#Gateway) which specifies which rules to follow that are defined in the [ACF](#ACF).

Record
------
Used to define a [PV](#PV) in a [DB File](#DB File).

Release
-------
The version of [IBEX](#IBEX) to be deployed.

Repository ("Repo")
-------------------


Script Server
-------------

SECI
----
**S**ample **E**nvironment **C**ontrol **I**nterface.  The current instrument control system, currently being replaced by IBEX.  Written in C# and incorporating [LabVIEW](#LabVIEW) drivers for the sample environment equipment.  User manual [here](http://www.facilities.rl.ac.uk/isis/projects/uip/UserManuals/Forms/AllItems.aspx).

Sequencer
---------
An [EPICS](#EPICS) module to provide support for [SNL](#SNL) files.

SNL
---
**S**tate **N**otation **L**anguage.  A "C-like" language to enable [State Machines](#State Machine) to be written which can then be integrated into [IOCs](#IOC).

Soft Motor
----------
An software implementation of a motor axis to enable conversion between two coordinate systems.

State Machine
-------------
A software design in which a program executes _only_ its well-defined states with strict rules governing the changes between them.  Written in [SNL](#SNL) in this case.

Substitution File
-----------------
A template for creating [DB files](#DB File) using [macros](#Macro).

Synoptic
--------


Ticket
------


User Values
-----------


Vagrant
-------
A tool for building and managing [virtual machine](#Virtual Machine) environments.  See [homepage](https://www.vagrantup.com) for more information.

Virtual Box
-----------
A tool for running [virtual machines](#Virtual Machine).

VI
--
**V**irtual **I**nstrument.  A [LabVIEW](#LabVIEW) program, usually a device driver for interacting with sample environment equipment.

Virtual Machine
---------------
An entire computer system running, without its own dedicated hardware, as software on a host computer.  Each of the ISIS control machines (NDX...) is a virtual machine, as well as many other servers used as part of the development process.

ZeroMQ
------
Another messaging broker that is used in [NICOS](#Nicos)

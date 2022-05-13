> [Wiki](Home) > [Glossary](Glossary)

Glossary
========

ACF
---
**A**ccess **C**ontrol **F**ile.  A file used by the [Gateway](#gateway) which contains rules for access.

[ActiveMQ](ActiveMQ)
----------
A messaging system that is used in a number of places throughout IBEX.  Specifically, [The Alarm Server](Alarms) and [The IOC Log Server](Ioc-message-logging).  See [ActiveMQ Homepage](http://activemq.apache.org/) for more information on the technology.

Alarm
-----

Archive Engine
--------------
A [CSS](#css) component that archives [PV](#pv) values.  Implemented in [IBEX](#ibex) in the [Block Archive](#block-archive) and [Instrument Archive](#instrument-archive)

[Autosave](Autosave)
----------
A system to record PV values and reinstate them on startup of an IOC.

[Axis](Axis)
----------
In IBEX, the term axis refers to a degree-of-freedom within an experimental system.  See [Axes in IBEX](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Glossary/Axes%20in%20IBEX%20V1R0M0.pdf) for more detail.

Backdoor
--------
A method of changing the internal parameters of an emulator to mimic the behaviour of the actual device.

[Barndoors](Barndoors-and-Momentum-Slits-on-MUON-Front-End)
-----------
Slits used on each of the Muon instruments to control the neutron flux to the sample.  Each "jaw" pivots on one edge, much like a door on a hinge.

Block
-----

Block Archive
-------------
Archives block values using the [CSS Archive Engine](#archive-engine) and restarts whenever block definitions and/or the configuration changes. 

[BlockServer](BlockServer)
-------------
A [Channel Access](#channel-access-(ca)) Server (CAS) that allows [blocks](#block) to be configured and [configurations](#configuration) to be created and loaded.

Branch
------

[CALab](https://www.helmholtz-berlin.de/zentrum/locations/it/software/exsteuer/calab/index_en.html)
-----
**C**hannel **A**ccess **Lab**oratory.  A library which enables [EPICS](#epics) and [LabVIEW](#labview) to communicate with each other.

[Calibration Files](Calibration-Files)
-------------------
Files which contain information about how pieces of sample environment equipment translate their readings into useful data. e.g. temperature sensor calibration files which enable translation from electrical measurements to temperature values.

Channel Access (CA)
-------------------
A protocol that defines how [PV](#pv) data is transferred between a server and client in an [EPICS](#epics) control system.

[Chopper](Choppers)
-------
A device, usually a spinning disc of thick metal with a narrow slot, which allows selection of a particular energy range of neutrons by varying its speed.

[CLF](https://www.clf.stfc.ac.uk/Pages/home.aspx)
-----
**C**entral **L**aser **F**acility.  A department at RAL that also uses the [EPICS](#epics) control system.

[Code Chats](Code-Chats)
------------
Short meetings and presentations held within the group to discuss various aspects of the control system, or other related technologies.

Collision Detection
-------------------
A method for detecting collisions between moving beamline components by simulating the requested move beforehand.  See [Collision Detection Project](Collision-Detection-Project) for more information.  

Commit
------


Component
---------


[Config-Checker](Config-Checker)
----------------
A Python script to highlight potential issues with current configurations when a new version of [IBEX](#ibex) is installed.

[Config-Upgrader](Config-Upgrader)
----------------
A Python script to upgrade current configurations to be compatible with new versions of [IBEX](#ibex).

Configuration
-------------

ConServer
---------


[CSS](http://controlsystemstudio.org/)
-----
"**C**ontrol **S**ystem **S**tudio is an [Eclipse](#eclipse)-based collection of tools to monitor and operate large scale control systems, such as the ones in the accelerator community. It's a product of the collaboration between different laboratories and universities."

[Database Server](the-databaseserver)
-----------------

DataWeb
-------

DB File
-------
A file containing the definition of [PVs](#pv) for a specific [IOC](#ioc) using [records](#record). 

Dial values
-----------


[Eclipse](http://www.eclipse.org/)
---------
An IDE and collection of tools for development of [GUIs](#gui).  [CSS](#css) and the [IBEX](#ibex) client are based on it.

Emulator
--------
A software implementation of hardware.  Usually used to help write and test an [IOC](#ioc) and [OPI](#opi).  See [Emulating-Devices](Emulating-Devices) for more information.

[EPICS](EPICS)
-------
**E**xperimental **P**hysics and **I**ndustrial **C**ontrol **S**ystem.  A client/server control system using [Channel Access](#channel-access-(ca)) as its communication protocol, forming a distributed real-time database of machine values ([PVs](#pv)).
It is a collection of software tools collaboratively developed which can be integrated to provide a comprehensive and scalable control system.

Field
-----


[Gateway](Access-Gateway)
---------
A service that controls access between two or more networks.

Genie-Python
------------
An implementation of the [OpenGenie](http://www.opengenie.org) scripting language in Python, or at least its commands specific to instrument control.  Documentation [here](http://shadow.nd.rl.ac.uk/genie_python/sphinx/genie_python.html).

GIT
---

Github
------

GUI
---
**G**raphical **U**ser **I**nterface.  AKA "[The GUI](The-GUI)" or [IBEX](#ibex) Client.  A program which provides a graphical method of interacting with the [IBEX](#ibex) Server.

IBEX
----
The new ISIS instrument control system.  Primarily based on [EPICS](#epics) as the underlying technology.

Inhibitor
---------

Instrument Archive
------------------
Archives [PV](#pv) values using the [CSS Archive Engine](#archive-engine) which have the ARCHIVE [Field](#field) set in their [Record](#record).  

IOC
---
**I**nput**O**utput**C**ontroller.  A process which reads and writes [PVs](#pv).  Often interfaces with hardware (e.g. sample environment equipment) to enable it to be controlled remotely.

Java
----

Jenkins
-------

Journal Viewer
--------------

Journal viewer is an overloaded term. There are two, one as [part of the ibex GUI](The-Journal-Viewer) and the other is a standalone application supported by the instrument scientists, we only provide data for this.

Journal Parser
--------------

The journal parser is a program that runs as part of the end run processes. It looks parses the journal produced by the `isisicp` and adds the details to the database in the journal schema.

[LabVIEW](http://www.ni.com/labview/)
---------
**Lab**oratory**V**irtual**I**nstrument**E**ngineering**W**orkbench.  A graphical programming language in which the device drivers for [SECI](#seci) are written.

[LeWIS](https://github.com/DMSC-Instrument-Data/lewis)
-------
**Le**t's **W**rite **I**ntricate **S**imulators.  A Python framework for producing and running [emulators](#emulator).  See [Emulating-Devices](Emulating-Devices) for more information.

Macro
-----
A named abstraction for a variable setting, e.g. the macro is PORT, referenced as `$(PORT)`, but the data it is abstracting could be `COM11` or `192.168.0.0`. Regex is used to define the format of the macro in the GUI to ensure that you don't try to use the wrong data type or formatting where the variable is referenced.

Mini-Inst
---------
A term used to describe an instrument which uses components from both the [SECI](#seci) and [IBEX](#ibex) control systems.  For example, an [IOC](#ioc) wrapped with a [VI](#vi) on a [SECI](#seci) instrument (using [CALab](#calab)).

[Momentum Slits](Barndoors-and-Momentum-Slits-on-MUON-Front-End)
----------------
Slits used on the Muon front-end to control the neutron momentum to the three instruments.

MySQL
-----


[Nicos](Nicos)
-------
A network-based control system.  Some elements of it are used in the [script server](#script-server).  See [homepage](http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-2.0/dirhtml/) for more information.

OPI
---
**Op**erator **I**nterface.  A file used in [CSS](#css) to enable a user to interact with an IOC graphically.

Perspective
-----------


Plugin
------


ProcServ
--------


PV
--
**P**rocess **V**ariable.  A named piece of data and the primary object of the [Channel Access Protocol](#channel-access-(ca)), often associated with a piece of equipment (e.g. status, readback, setpoint, parameter).

PVLIST
------
A file used by the [Gateway](#gateway) which specifies which rules to follow that are defined in the [ACF](#acf).

Record
------
Used to define a [PV](#pv) in a [DB File](#db-file).

Release
-------
The version of [IBEX](#ibex) to be deployed.

Repository ("Repo")
-------------------


Script Server
-------------

SECI
----
**S**ample **E**nvironment **C**ontrol **I**nterface.  The current instrument control system, currently being replaced by IBEX.  Written in C# and incorporating [LabVIEW](#labview) drivers for the sample environment equipment.  User manual [here](http://www.facilities.rl.ac.uk/isis/projects/uip/UserManuals/Forms/AllItems.aspx).

Sequencer
---------
An [EPICS](#epics) module to provide support for [SNL](#snl) files.

SNL
---
**S**tate **N**otation **L**anguage.  A "C-like" language to enable [State Machines](#state-machine) to be written which can then be integrated into [IOCs](#ioc).

Soft Motor
----------
An software implementation of a motor axis to enable conversion between two coordinate systems.

State Machine
-------------
A software design in which a program executes _only_ its well-defined states with strict rules governing the changes between them.  Written in [SNL](#snl) in this case.

Substitution File
-----------------
A template for creating [DB files](#db-file) using [macros](#macro).

Synoptic
--------
A graphical representation of an ISIS beamline, showing permanent components as well as Sample Environment equipment.  It is shown in a [perspective](#perspective) view in the [IBEX](#ibex) client.

Ticket
------


Umbrella Ticket
---------------


User Values
-----------


Vagrant
-------
A tool for building and managing [virtual machine](#virtual-machine) environments.  See [homepage](https://www.vagrantup.com) for more information.

Virtual Box
-----------
A tool for running [virtual machines](#virtual-machine).

VI
--
**V**irtual **I**nstrument.  A [LabVIEW](#labview) program, usually a device driver for interacting with sample environment equipment.

Virtual Machine
---------------
An entire computer system running, without its own dedicated hardware, as software on a host computer.  Each of the ISIS control machines (NDX...) is a virtual machine, as well as many other servers used as part of the development process.

[Web Dashboard](Web-Dashboard)
---------------

ZeroMQ
------
Another messaging broker that is used in [NICOS](#nicos)

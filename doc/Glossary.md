# Glossary

## ACF

**Access Control File**.  A file used by the [Gateway](#gateway) which contains rules for access.

## [ActiveMQ](/system_components/ActiveMQ)

A messaging system that is used in a number of places throughout IBEX.  Specifically, [The Alarm Server](system_components/Alarms) and [The IOC Log Server](system_components/IOC-message-logging).  See [ActiveMQ Homepage](http://activemq.apache.org/) for more information on the technology.

## Alarm

See [the Alarm Server](/system_components/Alarms)

## Archive Engine

A [CSS](#css) component that archives [PV](#pv) values.  Implemented in [IBEX](#ibex) in the [Block Archive](#block-archive) and [Instrument Archive](#instrument-archive)

## [Autosave](/iocs/tools/Autosave)

A system to record PV values and reinstate them on startup of an IOC.

## [Axis](/specific_iocs/motor_extensions/Axis)

In IBEX, the term axis refers to a degree-of-freedom within an experimental system.  See [Axes in IBEX](https://stfc365.sharepoint.com/sites/IBEXSAG/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FIBEXSAG%2FShared%20Documents%2FAxes%20in%20IBEX%20V1R0M0%2Epdf&parent=%2Fsites%2FIBEXSAG%2FShared%20Documents) for more detail.

## Backdoor

A method of changing the internal parameters of an emulator to mimic the behaviour of the actual device.

## [Barndoors](/specific_iocs/motor_extensions/jaws/Barndoors-and-Momentum-Slits-on-MUON-Front-End)

Slits used on each of the Muon instruments to control the neutron flux to the sample.  Each "jaw" pivots on one edge, much like a door on a hinge.

## BDD

Behaviour-driven development. See the [Agile Alliance definition of BDD](https://www.agilealliance.org/glossary/bdd/),
and [how we use BDD for testing in Squish](/client/testing/System-Testing-with-Squish-BDD).

## Block

## Block Archive

Archives block values using the [CSS Archive Engine](#archive-engine) and restarts whenever block definitions and/or the configuration changes. 

## [BlockServer](/system_components/BlockServer)

A [Channel Access](#channel-access-ca) Server (CAS) that allows [blocks](#block) to be configured and [configurations](#configuration) to be created and loaded.

## Branch

## [CALab](https://www.helmholtz-berlin.de/zentrum/locations/it/software/exsteuer/calab/index_en.html)

**Channel Access Laboratory**.  A library which enables [EPICS](#epics) and [LabVIEW](#labview) to communicate with each other.

## [Calibration Files](/system_components/configurations/Calibration-Files)

Files which contain information about how pieces of sample environment equipment translate their readings into useful data. e.g. temperature sensor calibration files which enable translation from electrical measurements to temperature values.

## Channel Access (CA)

A protocol that defines how [PV](#pv) data is transferred between a server and client in an [EPICS](#epics) control system.

## [Chopper](specific_iocs/Choppers)

A device, usually a spinning disc of thick metal with a narrow slot, which allows selection of a particular energy range of neutrons by varying its speed.

## [CLF](https://www.clf.stfc.ac.uk/Pages/home.aspx)

**Central Laser Facility**.  A department at RAL that also uses the [EPICS](#epics) control system.

## [Code Chats](processes/meetings/Code-Chats-and-Lightning-Talks)

Short meetings and presentations held within the group to discuss various aspects of the control system, or other related technologies.

## Collision Detection

A method for detecting collisions between moving beamline components by simulating the requested move beforehand.  See [Collision Detection Project](/specific_iocs/motor_extensions/Collision-Detection-Project) for more information.  

## Commit

A commit is a snapshot of your repository at a certain point in time. It is also a git command, which saves all of your staged changes on a project. There are various ways to perform a git commit, more info can be found here: [Git Guides - git commit](https://github.com/git-guides/git-commit)

## Component

## [Config-Checker](/tools/Config-Checker)

A Python script to highlight potential issues with current configurations when a new version of [IBEX](#ibex) is installed.

## [Config-Upgrader](/tools/Config-Upgrader)

A Python script to upgrade current configurations to be compatible with new versions of [IBEX](#ibex).

## Configuration

## ConServer

## [CSS](http://controlsystemstudio.org/)

"**Control System Studio** is an [Eclipse](#eclipse)-based collection of tools to monitor and operate large scale control systems, such as the ones in the accelerator community. It's a product of the collaboration between different laboratories and universities."

## [DAE](/specific_iocs/DAE-and-the-ICP)

The Data Acquisition Electronics (DAE) is the physical hardware that reads the neutron events out of the detectors. IBEX communicates with this hardware via the Instrument Control Program (ICP). This program is also responsible for combining the neutron and sample environment data into the NeXus file. 

## [Database Server](/system_components/DatabaseServer)

## DataWeb

## DB File

A file containing the definition of [PVs](#pv) for a specific [IOC](#ioc) using [records](#record). 

## Dial values


## [Eclipse](http://www.eclipse.org/)

An IDE and collection of tools for development of [GUIs](#gui).  [CSS](#css) and the [IBEX](#ibex) client are based on it.

## Emulator

A software implementation of hardware.  Usually used to help write and test an [IOC](#ioc) and [OPI](#opi).  See [Emulating-Devices](/iocs/testing/Emulating-Devices) for more information.

## EPICS

**Experimental Physics and Industrial Control System**.  A client/server control system using [Channel Access](#channel-access-ca) as its communication protocol, forming a distributed real-time database of machine values ([PVs](#pv)).
It is a collection of software tools collaboratively developed which can be integrated to provide a comprehensive and scalable control system.

## Field

## [Gateway](/system_components/Gateway)

A service that controls access between two or more networks.

## Genie Python

An implementation of the [OpenGenie](http://www.opengenie.org) scripting language in Python, or at least its commands specific to instrument control.  Documentation at {external+genie_python:doc}`genie_python`.

## GIT

Git is a distributed version control software. Version control is a way to save changes over time without overwriting previous versions. More info can be found here: [Git Guides: Git](https://github.com/git-guides)

## Github

While Git takes care of the underlying version control, GitHub is the collaboration platform built on top of it. It's where most of IBEX source code is kept, along with some other projects. [Git Guides: Git](https://github.com/git-guides)

## GUI

**Graphical User Interface**.  AKA "[The GUI](Client)" or [IBEX](#ibex) Client.  A program which provides a graphical method of interacting with the [IBEX](#ibex) Server.

## IBEX

The new ISIS instrument control system.  Primarily based on [EPICS](#epics) as the underlying technology.

## Inhibitor

## Instrument Archive

Archives [PV](#pv) values using the [CSS Archive Engine](#archive-engine) which have the ARCHIVE [Field](#field) set in their [Record](#record).  

## IOC

**Input  Output Controller**.  A process which reads and writes [PVs](#pv).  Often interfaces with hardware (e.g. sample environment equipment) to enable it to be controlled remotely.

## Java

## Jenkins

## Journal Viewer

Journal viewer is an overloaded term. There are two, one as [part of the ibex GUI](/system_components/Journal-Viewer) and the other is a standalone application supported by the instrument scientists, we only provide data for this (at `http://journals.isis.cclrc.ac.uk/jv/`)

## Journal Parser

The journal parser is a program that runs as part of the end run processes. It looks parses the journal produced by the `isisicp` and adds the details to the database in the journal schema.

## [LabVIEW](/system_components/LabVIEW)

**Laboratory Virtual Instrument Engineering Workbench**.  A graphical programming language in which the device drivers for [SECI](#seci) were written. A small number of drivers still use LabVIEW, despite SECI having been retired.

## [LeWIS](https://github.com/DMSC-Instrument-Data/lewis)

**Let's Write Intricate Simulators**.  A Python framework for producing and running [emulators](#emulator).  See [Emulating-Devices](/iocs/testing/Emulating-Devices) for more information.

## Macro

A named abstraction for a variable setting, e.g. the macro is PORT, referenced as `$(PORT)`, but the data it is abstracting could be `COM11` or `192.168.0.0`. Regex is used to define the format of the macro in the GUI to ensure that you don't try to use the wrong data type or formatting where the variable is referenced.

## Mini-Inst

A term used to describe an instrument which runs a minimal set of IBEX services, as opposed to a full IBEX installation.

## [Momentum Slits](specific_iocs/motor_extensions/jaws/Barndoors-and-Momentum-Slits-on-MUON-Front-End)

Slits used on the Muon front-end to control the muon momentum to the three instruments.

## MySQL

## [Nicos](/system_components/Nicos)

A network-based control system.  Some elements of it are used in the [script server](#script-server).  See [homepage](http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-2.0/dirhtml/) for more information.

## OPI

**Operator Interface**.  A file used in [CSS](#css) to enable a user to interact with an IOC graphically.

## Perspective

## Plugin

## ProcServ

## PV

**Process Variable**.  A named piece of data and the primary object of the [Channel Access Protocol](#channel-access-ca), often associated with a piece of equipment (e.g. status, readback, setpoint, parameter).

## PVLIST

A file used by the [Gateway](#gateway) which specifies which rules to follow that are defined in the [ACF](#acf).

## Record

Used to define a [PV](#pv) in a [DB File](#db-file).

## Release

The version of [IBEX](#ibex) to be deployed.

## Repository ("Repo")

## Script Server

## SECI

**Sample Environment Control Interface**. An old instrument control system, used before IBEX. No longer in use on any instruments. Written in C# and incorporating [LabVIEW](#labview) drivers for the sample environment equipment.

## SECoP

**Sample Environment Communication Protocol**. See {external+secop:doc}`SECoP docs <index>` for details.

## Sequencer

An [EPICS](#epics) module to provide support for [SNL](#snl) files.

## SNL

**State Notation Language**.  A "C-like" language to enable [State Machines](#state-machine) to be written which can then be integrated into [IOCs](#ioc).

## Soft Motor

An software implementation of a motor axis to enable conversion between two coordinate systems.

## State Machine

A software design in which a program executes _only_ its well-defined states with strict rules governing the changes between them.  Written in [SNL](#snl) in this case.

## Substitution File

A template for creating [DB files](#db-file) using [macros](#macro).

## Synoptic

A graphical representation of an ISIS beamline, showing permanent components as well as Sample Environment equipment.  It is shown in a [perspective](#perspective) view in the [IBEX](#ibex) client.

## Ticket

## Umbrella Ticket

## User Values

## uv

See {ref}`uv`

## Vagrant

A tool for building and managing [virtual machine](#virtual-machine) environments.  See [homepage](https://www.vagrantup.com) for more information.

## Virtual Box

A tool for running [virtual machines](#virtual-machine).

## VI

**Virtual Instrument**.  A [LabVIEW](#labview) program, usually a device driver for interacting with sample environment equipment.

## Virtual Machine

An entire computer system running, without its own dedicated hardware, as software on a host computer.  Each of the ISIS control machines (NDX...) is a virtual machine, as well as many other servers used as part of the development process.

## [Web Dashboard](/webdashboard/Web-Dashboard)

## ZeroMQ

Another messaging broker that is used in [NICOS](#nicos)

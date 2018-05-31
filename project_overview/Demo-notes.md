> [Wiki](Home) > [Project overview](Project-Overview) > How to demonstrate IBEX

# Notes for demonstrating IBEX (the ISIS instrument control system)

Anyone doing a demo of IBEX should use these notes, so that 

* You are familiar with the scope of the demo (i.e. what should be covered)
* You review it and rehearse it in advance (i.e. you are clear about what you will present)
* You don’t forget to mention any important aspects of the system
   * keep a copy of these notes in front of you as you do the demo
* You don’t forget where key files (e.g. demo scripts) are located, etc.
* Instrument scientists get a consistent picture irrespective of where & when the demo is performed.
* If a question takes you “off piste”, you can easily find your way back to the main thread of the demo.
* We can enhance the script in the light of experience (e.g. better answers to questions)
   * jot down any important points arising from any demos that you do and add them back into this document for the benefit of others.

## Overview

Provide the audience with a quick tour of the IBEX GUI

* Explain that the GUI is a client application
   * It displays data that is provided to it by server applications
   * The server applications are called IOCs (Input-Output Controllers)
   * IOCs are similar, in some respects, to LabVIEW VIs
   * The IOCs run on the control PC (i.e. the NDX... machine)
   * The GUI can run on the control PC.  It can also run on other client PCs located elsewhere on the network.

* Highlight the main areas of the GUI
   * Dashboard - very similar to the SECI dashboard
   * Blocks & Groups - again, very similar to SECI
   * System Views - a number of different views of the system.  Some views are similar to SECI; others are new.
   * Clicking on the list of View buttons (on the left-hand side of the GUI window) changes the view

* Highlight the IBEX menu
   * IBEX - use to switch instrument, restore the default view or exit IBEX
   * Configuration - use to edit configurations, load a new configuration or delete a configuration
   * Synoptic - use to edit synoptics, load a new synoptic or delete a synoptic.
   * IOC - use to start or stop IOCs
   * Run Control - use to view and edit run-control settings
   * Help - point out the About Box.  User should use it to report the server & client version numbers if they encounter problems.

## Dashboard

The dashboard is very similar to the SECI dashboard
* It uses the same colour coding as the SECI dashboard
* It displays the same status messages as the SECI dashboard
* Information about the current experiment comes from the DAE set up (we'll touch on this later)
* Beam status information comes from the beam logger IOC

## Beam Status

Describe the Beam Status view
* Clicking on the Beam Status button displays the Beam Status view
* The Beam Status view always appears in the main display area
* The Beam Status view comprises 3 panes
   * The main pane, taking up most of the display in the Beam Status graph.  It shows the Synchrotron current and the currents to TS1 and TS2.  You can toggle the display to show graphs for the last hour or last 24 hours.
   * The top right pane shows the ISIS MCR news.  It is just a simple scrolling window showing the published MCR news.
   * The lower right pane shows beam status details.  It consists of 3 sections: one for the Synchrotron, one for TS1 and one for TS2.  The sections are collapsible, so you can collapse any section that is of no interest to you.
   * Beam status information comes from the beam logger IOC, which replaces the old LabVIEW beam logger VI.
   * The beam logger IOC is already serving beam status information to all instruments (not just those running IBEX)
   * The beam logger IOC actually runs on the accelerator control system

## IOC Log View

Describe the IOC Log view
* The IOC Log system provides a unified way of managing status and information messages from the devices attached to the instrument.
* Copies of status and information messages from the DAE are also routed via the IOC Log system.
* The IOC Log messages are primarily intended for diagnosing problems with attached devices.
* The IOC Log view provides you with a convenient means of viewing those messages
      * Demonstrate how messages can be filtered and searched (by date/time, severity, etc.)
      * Messages are automatically saved to a log on the control PC
      * **N.B.** Messages are held in a log which is quite separate from experimental data

## DAE View

Describe the DAE view
* The DAE view allows scientists to set up and control the operation of the DAE.
* The DAE view is very similar to the DAE VI in SECI.
* The DAE view comprises 6 tabs.
   * Run Summary
     Displays run summary information and any recent log messages.
   * Experiment Setup
     <add description here>.
   * Run Information
     <add description here>.
   * Spectra Plots
     <add description here>.
   * Diagnostics
     <add description here>.
   * Vetos
     <add description here>.

* As previously noted, copies of status and information messages from the DAE are also routed via the IOC Log system.

## Blocks & Groups

Blocks & groups in the new GUI work in the same way as they do in SECI.
* Blocks and groups are displayed at the top (and centre-right) of the GUI window.
* Blocks & groups are part of your configuration.  You define blocks & groups by creating and editing configurations.
* In EPICS, an IOC makes information about the status of a device available by publishing *process variables*.  In general, an IOC will use many process variables to fully describe the state of a device.  Typically, you won't be interested in all of these - just a sub-set.  Show how the GUI allows you to select which process variables that are of interest and to define these as *blocks*.
* Once a PV has been defined as a block, show how it can be assigned to a group.
* Make it clear that blocks are automatically logged (just as they are in SECI).  Note also that the logging of blocks is independent of the message log.
* Show how blocks can be viewed in the LogPlotter - so the user can always view the history of a block.
* Show how a set of defined blocks & groups can be saved as a configuration.
* Show how a previously saved configuration can be re-loaded.
* Explain what is saved in a configuration:
   * groups, blocks, links to settings files, synoptic view
* Demonstrate sub-configurations
* Demonstrate Management Mode.

## Scripting

In the new GUI, scripting is built-in.  You don't need a separate windows to run a script (although some users prefer to have a separate window).
* Click on the Scripting button to display the Scripting view
   * point out the scripting area
* The scripting language is Python
* Python brings a number of advantages over Genie
   * *what are they? - we need to enumerate them*
* Python equivalents of the most common Genie commands (e.g. cset) have been created
   * demonstrate that, for example, ``cset arg`` becomes ``cset(arg)``
   * it is not difficult to convert a Genie script into a Python script
   * display a *before (Genie)* and *after (Python)* script.  Emphasize how similar they are.
* Any block (or PV) can be used in a Python script
* Demonstrate running a Python script
   * use a script that you prepared earlier: **don't wing it!**
   * point out use of Genie-like commands where possible
   * show how to pull in data from blocks (or PVs)
   * read data from previously saved file if beam is off
   * manipulate data in Python - show off what Python can do
   * display data in a graph
   * copy/paste a graph into MS Word (or similar)

## Device Support

EPICS provides support for a wide range of devices.  For many devices we can simply download the appropriate driver from the EPICS web-site.  Because the source code for these drivers is available, we can, if necessary, adapt an EPICS driver for our specific purposes.
* In EPICS, drivers & IOCs combine to provide control of devices attached an instrument.  In addition, we use CSS to create OPIs (graphical user interfaces) for devices.  In combination, drivers, IOCs and OPIs provide the functionality of a LabVIEW VI.
* We currently have EPICS drivers for Galil motor controllers, Eurotherms, Julabo water baths, CAEN, Kepco & Thurlby power supplies.  We also have controllers for PLCs, jaws-sets, sample changers, rotation stages and goniometers.
* EPICS drivers and controllers for additional devices can be developed as required.
* Adopting EPICS does **not** mean throwing away existing LabVIEW drivers.
   * We have created a communication interface, called lvDCOM, to enable EPICS to communicate with LabVIEW VIs.
   * Where a device has a complex or specially customised LabVIEW driver, lvDCOM allows us to continue using the LabVIEW VI.  Any data that the VI makes available to EPICS can be defined as a block and used in the normal manner.
* Demonstrate an existing EPICS IOC/OPI: for example the Eurotherm IOC & OPI – demonstrate simple operation, ramping, calibration, etc.
* Demonstrate interaction between EPICS and a VI: for example <insert example here>
* Demonstrate starting & stopping of IOCs.  Show how startup messages, etc. are captured in the message log.
* Discuss settings files and their relation to IOCs and VIs.

## Synoptic View or Instrument Overview

The synoptic view provides an interactive overview of an instrument.
* The synoptic view shows all the devices (or a defined sub-set of devices) attached to an instrument.
* The synoptic view is configurable (via the Synoptic Editor).  Show how you can create different views for different instrument setups.
* Incident neutrons are shown coming from the left.
* Each device is represented by its own icon and a small number of key parameters.
* Show how you can drill-down by clicking on each device icon to get more detail.
      * Clicking on a device icon displays the device UI, which will display additional controls and information that cannot easily be included on the top-level synoptic display
      * Device UIs are sometimes referred to as OPIs (OPIs are analogous to LabVIEW VI screens)
      * Demonstrate how some devices (e.g. motors) allow you to drill-down to deeper levels (beware: some of the deeper level screens can get very complex)
      * Show how the Up, Next and Prev buttons are used to navigate around the various layers of the synoptic view.

## Motors View

The motors view provides a convenient way to view the status of all the motors used on an instrument.
* The motors view is very similar to the *Table of Motors* used in SECI by some instruments.
* Each row corresponds to a single Galil motor controller.  The number of rows displayed will depend on the number of Galil controllers attached to the instrument.
* The columns list the Galil controller ports (up to 8 ports per Galil)
* Each entry in the table represents a single Galil controller port (one (or zero) motors per port)
      * Each entry identifies the motor by its unique ID number
      * Each entry displays the current value of the motor's position and its current set-point.
      * A grey entry represents an unused port (no motor is attached, or motor is switched off)
      * A pink entry represents a port in use: motor is attached, but stationary
      * A green entry represents an active port: motor is attached and is moving
* Show how you can drill-down by clicking on each motor entry to get more detail.

## EPICS & Extensibility

EPICS is a framework for creating *distributed* control systems.  The ability to have more than one PC controlling different parts of an instrument is inherent to EPICS.
* The default position will continue to be that we will use a single PC to control all of the devices attached an instrument.
* However, there are some situations where it is advantageous to have specialist items of equipment controlled by a separate PC.  For example
   * the interchangeable cameras on IMAT
   * the LARMOR spin-echo system
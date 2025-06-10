# New Starter's Guide

## Welcome to IBEX!

1. [Using the Developer Wiki](#using-the-developer-wiki) 
   1. [Searching the Codebase](#searching-the-codebase)
2. [Getting Set Up](#getting-set-up)
   1. [Using Git](#using-git)
   2. [Creating Useful Shortcuts](#creating-useful-shortcuts)
   3. [Office Admin Links](#office-admin-links)
3. [Familiarising with IBEX](#familiarising-with-ibex)
   1. [Introduction](#introduction)
   2. [Components and Technical Concepts](#components-and-technical-concepts)
4. [EPICS Introduction](#epics-introduction)
   1. [Further EPICS](#epics-introduction)
   2. [Input/Output Controller (IOC) Resources](#input-output-controller-resources)
5. [Control System Studio](#control-system-studio)

This page is designed to be used as a comprehensive reference to getting started in the Instrument Controls team. Written by new-ish starters, for the newest starters. It's a collection of useful resources which will speed up your onboarding and get you developing. 

## Using the Developer Wiki

There are many how-to guides in the Developer's manual. Being able to use the wiki is as much a skill as learning to use any of our tools. If you're stuck, this can be really useful - try searching for different keywords from your ticket. 

### Searching the Codebase

Another mode of attack is searching through our codebase for particular code snippets, which is equally useful! You don't need to reinvent the wheel - you can search to see how code has been already written for a similar purpose, find examples of how unfamiliar concepts are used, or see our coding conventions for certain processes. This is also a good way to locate files if you don't know where they live, but know some keywords they may contain! 

You can do this by searching in [ISISComputingGroup](https://github.com/ISISComputingGroup/) and clicking on the 'Code' tab (as seen above).

## Getting Set Up

First off you're going to need all the developer tools we use, a copy of the existing codebase, and the Eclipse GUI for IBEX*.

- [Installing the Backend System](First-Time-Build)

Don't forget to come back afterwards!

### Using Git

We use Git for version control of the codebase. For IBEX-flavoured Git resources, see:

- [Our Github resources](../processes/Git-and-GitHub)
- [IBEX Git workflow](../processes/git_and_github/Git-workflow)

If you're not familiar with it, learn it!

- [Github's own Git tutorials](https://try.github.io/)
- [Friendly git sandbox](https://learngitbranching.js.org/) - the 'remote' tutorials in particular
- [Nice intro to Git & version control](https://swcarpentry.github.io/git-novice/01-basics/index.html)

### Creating Useful Shortcuts

There's a couple files/commands you'll find yourself using a *lot*. It's handy to create desktop shortcuts for these frequently used links:

- `EPICSTerm` (The EPICS terminal window where IOCs are built and run)
- `start_ibex_server`
- `stop_ibex_server`

These can be found in `C:\Instrument\Apps\EPICS`.

### Office Admin Links

As a new starter you should add your name and picture to the training slides in `<shares>\ISIS_Experiment_Controls_Public\training`. If you do not know where this share is, please ask.

- [ISIS Sharepoint](https://stfc365.sharepoint.com/sites/isis-hub/) - Shared ISIS documents, manuals, meeting minutes etc
- [Oracle Login](https://portal.ssc.rcuk.ac.uk/) - Book leave, create timesheets
- [Flexi Time](https://flexiral.stfc.ac.uk/FCDWeb/) - If you're on Flexi time and need to view/edit your work history
- [Health & Safety Training](https://lmsweb.stfc.ac.uk/moodle/login/index.php)

Here's some useful bits and bobs for how our team operates and the conventions we use in our work.

- [IBEX Processes](../Processes) - Logistics of the day-to-day
- [IBEX Project Board](https://github.com/orgs/ISISComputingGroup/projects) - Where our tickets live
- [Tickets and their Workflow](../processes/dev_processes/Tickets-and-their-Workflow)
- [Useful Tools](../Tools)

## Familiarising with IBEX

### Introduction

While that's installing, get to know the IBEX components. Get to know EPICS. It's the software environment that IBEX uses to control the ISIS instruments. 

Ironically, to get a well-explained overview of what IBEX is, and how to interact with it as a dev, the {external+ibex_user_manual:doc}`IBEX user manual <index>` is a really nice place to start. In particular, see:

- {external+ibex_user_manual:doc}`IBEX Key Concepts <Concepts>`
- {external+ibex_user_manual:doc}`IBEX-GUI-Features`
- {external+ibex_user_manual:doc}`How To Do Things In IBEX <How-To>`

There are some training materials available that we use to train scientists on IBEX, which is also a nice way to get started:

- IBEX training: `<shares>\ISIS_Experiment_Controls_Public\training` (if you do not know where the share is, please ask)

### Components and Technical Concepts

Some pages to read over: 

- [System Components](../System-components)
- [Useful tools](../Tools)

Pages to skim over. Read in detail only when needed:

- [Settings and Configurations](../system_components/Settings-and-Configurations)
- [Data Generation and Storage](../systems/inst_control/Data-Generation-and-Storage-on-Instrument-PCs-(NDX's))
- [Information for User Scientists](https://github.com/ISISComputingGroup/IBEX/wiki)

Every section after this line contains reference information that you do not necessarily have to read before you do your first ticket, but it is where you should take a look when you find out you need to learn new things in order to do your work.

## EPICS Introduction

There is much to learn about EPICS and it can be difficult to know what you're looking for. You do not have to read these resources until you get to writing your first IOC. Here are some overviews:

- Old but still good overview - [https://epics.anl.gov/docs/GSWE.php](https://epics.anl.gov/docs/GSWE.php)
- More recent overview [http://www.aps.anl.gov/epics/docs/training.php](http://www.aps.anl.gov/epics/docs/training.php) in particular [http://www.aps.anl.gov/epics/docs/USPAS2014.php](http://www.aps.anl.gov/epics/docs/USPAS2014.php)
- [Powerpoint EPICS overview](https://epics.anl.gov/docs/USPAS2014/1-Monday/EPICS_Intro.pdf)
- [Training Course](https://epics.anl.gov/docs/USPAS2014.php)
- [Database Principles (what's a record? And more)](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/Database-1.pdf)
- [Database Principles II (with examples)](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/Database-2.pdf)

### Further EPICS

- [State Notation Language 1](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_1_EPICSAutomation.pdf) [State Notation Language 2](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_2_Sequencer.pdf)
- [ASYN/Stream Device overview](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_2_Sequencer.pdf)
- [YouTube Videos covering the epics.gov.anl slideshows](https://epics.anl.gov/docs/APS2015.php)

### Input Output Controller Resources

When building an IOC, emulator, or writing tests, much can be learned by looking at existing IOCs: these can be found in `C:\Instrument\Apps\EPICS\ioc\master`.

However, there are also several places online to find good sources for learning and referencing. 

- [Creating & Basics of IOCs](../IOCs) - Our guide to creating IOCs and how they work. Lots of useful tips!
- [Protocol Files and Record Types](http://epics.web.psi.ch/software/streamdevice/doc/protocol.html) - Excellent reference for when you're mixing up your %d's and %f's. Bookmark this one!
- [Sequencer - State Notation in IOCs](http://www-csr.bessy.de/control/SoftDist/sequencer/Tutorial.html#pv-names-using-program-parameters) - All about implementing a state machine into an IOC, if needed.

## Control System Studio

We use a number of parts of Control System Studio (CSS) in our GUI (Alarms, Databrowser etc.). Most of these resources require little developer interaction apart from creating Operator Interfaces (OPIs) - GUIs, essentially - for the instrument controllers. It can be useful to create a desktop shortcut of this too.

Here's an overview and a get started guide.

- [Creating OPIs](/client/opis/OPI-Creation) - An introduction for how we use CSS and to set it up on your computer
- [Overview of CS-Studio](https://epics.anl.gov/docs/USPAS2014/1-Monday/CSS_1_Overview.pdf)
- [Intro to using CS-Studio](http://www.aps.anl.gov/epics/docs/USPAS2014/1-Monday/CSS_2_First_Steps.pdf)

You can find CSS at `C:\Instrument\Apps\EPICS\CSS\master`.
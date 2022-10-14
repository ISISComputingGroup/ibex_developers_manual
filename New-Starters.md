# Welcome to IBEX!

1. [Using the Developer Wiki](#using-the-developer-wiki)
2. [Getting Set Up](#getting-set-up)
   1. [Git](#git)
   2. [Creating Useful Shortcuts](#creating-useful-shortcuts)
3. [Familiarising IBEX](#familiarising-ibex)
4. [EPICS Introduction](#epics-introduction)
   1. [Further EPICS](#epics-introduction)
5. [Input/Output Controller (IOC) Resources](#input-output-controller-resources)
6. [Control System Studio](#control-system-studio)
7. [Office Admin Links](#office-admin-links)
8. [More about IBEX](#more-about-ibex)

This page is designed to be used as a comprehensive reference to getting started in the Instrument Controls team. Written by new-ish starters, for the newest starters. It's a collection of useful resources which will speed up your onboarding and get you developing. 

## Using the Developer Wiki

There are many how-to guides in the Developer's manual. If you're searching for a particular nugget of information and can't find the relevant page, double check the results in the 'Wikis' tab:

![Wiki Search Results](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/wiki_halp.png)

## Getting Set Up

First off you're going to need all the developer tools we use, a copy of the existing codebase, and the Eclipse GUI for IBEX*.

- [Installing the Backend System](First-time-installing-and-building-(Windows))

### Git

We use Git for version control of the codebase. For IBEX-flavoured git help, see:

- [Our Github resources](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Working-with-Git-and-GitHub)
- [IBEX Git workflow](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Git-workflow)

If you're not familiar with it, learn it!

- [Github's own Git tutorials](https://try.github.io/)
- [Friendly git sandbox](https://learngitbranching.js.org/) - the remote tutorials in partiular
- [Nice intro to the concept of Git & version control](https://swcarpentry.github.io/git-novice/01-basics/index.html)

### Creating Useful Shortcuts

There's a couple files/commands you'll find yourself using a lot. You can make desktop shortcuts to these that will make your like a lot easier!

- `EPICSTerm` (The EPICS terminal window where IOCs are built and run)
- `start_ibex_server`
- `stop_ibex_server`

These are found in `C:\Instrument\Apps\EPICS`

## Familiarising IBEX

###### IBEX: Introduction

While that's installing, get to know the IBEX components. Get to know EPICS. It's the software environment that IBEX uses to control the ISIS instruments. 

Ironically, to get a well-explained overview of what IBEX is, and how to interact with it as a dev, the [IBEX User Manual]([Home · ISISComputingGroup/ibex_user_manual Wiki · GitHub](https://github.com/ISISComputingGroup/ibex_user_manual/wiki)) is a really nice place to start. In particular, see:

- [IBEX Key Concepts](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Key-Concepts-in-IBEX)
- [IBEX GUI Features](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/IBEX-GUI-Features)
- [How To Do Things In IBEX](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/How-To-Do-Things-In-IBEX)

###### IBEX: EPICS and technical bits

From a more technical perspective, some pages to read over: 

- [System Components](System-Components)
- [Useful tools](Useful-tools)

Pages to skim over. Read in detail only when needed:

- [Settings and Configurations](Settings-and-Configurations)
- [Data Generation and Storage](Data-Generation-and-Storage)
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

## IOC (Input Output Controller) Resources

When building an IOC, emulator, or writing tests, much can be learned by looking at existing IOCs. However, there are also several places online to find good sources for learning and referencing. 

- [Creating & Basics of IOCs](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/IOCs) - Our guide to creating IOCs and how they work. Lots of useful tips!
- [Protocol Files and Record Types](http://epics.web.psi.ch/software/streamdevice/doc/protocol.html) - Excellent reference for when you're mixing up your %d's and %f's. Bookmark this one!
- [Sequencer - State Notation in IOCs](http://www-csr.bessy.de/control/SoftDist/sequencer/Tutorial.html#pv-names-using-program-parameters) - All about implementing a state machine into an IOC, if needed.

## Control System Studio

We use a number of parts of CSS in our GUI (Alarms, Databrowser etc.). Most of these resources require little developer interaction apart from creating Operator Interfaces (OPIs - GUIs, essentially) for the instrument controllers. Here's an overview and get started guide.

- [Overview of CS-Studio](https://epics.anl.gov/docs/USPAS2014/1-Monday/CSS_1_Overview.pdf)
- [Intro to using CS-Studio](http://www.aps.anl.gov/epics/docs/USPAS2014/1-Monday/CSS_2_First_Steps.pdf)
- [Creating OPIs](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/OPI-Creation)

## Office Admin Links

As a new starter you should add your name and picture to the training [slides](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FTraining&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View=%7BF2C33C51-70E6-4343-B937-2C59A2568306%7D).

- [ISIS Sharepoint](https://www.facilities.rl.ac.uk/isis/default.aspx) - Shared ISIS documents, manuals, meeting minutes etc
- [Oracle Login](https://portal.ssc.rcuk.ac.uk/) - Book leave, create timesheets
- [Flexi Time](https://flexiral.stfc.ac.uk/FCDWeb/) - If you're on Flexi time and need to view/edit your work history

## More about IBEX

There are some training materials available that we use to train scientists on IBEX. It is a good way to get started on learn about what IBEX is and the features that are available in it.

- [IBEX training](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FTraining&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306})

## Our workflow

Here's some useful bits and bobs for how our team operates, and the conventions we use in our development process.

- [IBEX Project Board](https://github.com/ISISComputingGroup/IBEX/projects/1) - Work tickets

- [Standards and Conventions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Standards-&-Conventions)
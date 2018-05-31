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



This page is designed to be used as a comprehensive reference to getting started in the Instrument Controls team. Written by new-ish starters, for the newest starters. It's a collection of useful resources which will speed up your onboarding and get you developing. 

## Using the Developer Wiki

There are many how-to guides in the Developer's manual. If you're searching for a particular nugget of information and can't find the relevant page, double check the results in the 'Wikis' tab:


![Wiki Search Results](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/wiki_halp.png)


## Getting Set Up

First off you're going to need all the developer tools we use, a copy of the existing codebase, and the Eclipse GUI for IBEX*.

- [Installing the Backend System](The-Backend-System)

### Git

We use Git for version control of the codebase. If you're not familiar with it, learn it!

- [Our Github resources/cribsheets](Working-with-git-and-github)
- [Github's own Git tutorial](https://try.github.io/levels/1/challenges/2)

### Creating Useful Shortcuts

It's handy to create desktop shortcuts for frequently used links:

- EPICSTerm (The terminal window where IOCs are built and run)
- start_ibex_server
- stop_ibex_server

These are found in `C:\Instrument\Apps\EPICS`


*it's just a goat. 


## Familiarising IBEX

While that's installing, get to know the IBEX components. Get to know EPICS. It's the software environment that IBEX uses to control the ISIS instruments. 

- [The Backend System](The-Backend-System)
- [Information for User Scientists](https://github.com/ISISComputingGroup/IBEX/wiki)
- [User Guide to IBEX](https://github.com/ISISComputingGroup/ibex_user_manual/wiki)



## EPICS Introduction

There is much to learn about EPICS and it can be difficult to know what you're looking for. Here are some overviews:

- [Powerpoint EPICS overview](https://epics.anl.gov/docs/USPAS2014/1-Monday/EPICS_Intro.pdf)
- [Training Course](https://epics.anl.gov/docs/USPAS2014.php)
- [Database Principles (what's a record? And more)](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/Database-1.pdf)
- [Database Principles II (with examples)](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/Database-2.pdf)

### Further EPICS

- [State Notation Language 1](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_1_EPICSAutomation.pdf) [State Notation Language 2](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_2_Sequencer.pdf)
- [ASYN/Stream Device overview](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_2_Sequencer.pdf)
- [YouTube Videos covering the epics.gov.anl slideshows](https://epics.anl.gov/docs/APS2015.php)


## Input Output Controller Resources

When building an IOC, emulator, or writing tests, much can be learned by looking at existing IOCs. However, there are also several places online to find good sources for learning and referencing. 

- [Protocol Files and Record Types](http://epics.web.psi.ch/software/streamdevice/doc/protocol.html) - Excellent reference for when you're mixing up your %d's and %f's. Bookmark this one!
- [Sequencer - State Notation in IOCs](http://www-csr.bessy.de/control/SoftDist/sequencer/Tutorial.html#pv-names-using-program-parameters) - All about implementing a state machine into an IOC, if needed.



## Control System Studio

We use a number of parts of CSS in our GUI (Alarms, Databrowser etc.). Most of these resources require little developer interaction apart from creating Operator Interfaces (OPIs - GUIs, essentially) for the instrument controllers. Here's an overview and get started guide.

- [Overview of CS-Studio](https://epics.anl.gov/docs/USPAS2014/1-Monday/CSS_1_Overview.pdf)
- [Intro to using CS-Studio](http://www.aps.anl.gov/epics/docs/USPAS2014/1-Monday/CSS_2_First_Steps.pdf)

## Office Admin Links

- [Waffle Board](https://waffle.io/ISISComputingGroup/IBEX) - Work tickets
- [Slack Channel](https://ibex-icp.slack.com/messages/C055HTCCU/) - Office-related chat
- [ISIS Sharepoint](https://www.facilities.rl.ac.uk/isis/default.aspx) - Shared ISIS documents, manuals, meeting minutes etc
- [Oracle Login](https://sso.ssc.rcuk.ac.uk/sso/pages/login.jsp) - Book leave, create timesheets
- [Flexi Time](http://flexiral.stfc.ac.uk/) - If you're on Flexi time and need to view/edit your work history



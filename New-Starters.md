## Welcome!

This page is designed to be used as a comprehensive reference to getting started in the Instrument Controls team. Written by new-ish starters, for the newest starters. It's a collection of useful resources which will speed up your onboarding and get you developing. 

## Using the Developer Wiki

There are many how-to guides in this developer Wiki. If you're searching for a particular nugget of information and there doesn't seem to be any information on it, double check results in the 'Wikis' tab:


![Wiki Search Results](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/wiki_halp.png)


## Getting Set Up

First off you're going to need all the developer tools we use, a copy of the existing codebase, and the Eclipse GUI for IBEX*.

- [Installing the Backend System](The-Backend-System)

### Git

We use Git for version control of the codebase. If you're not familiar with it, learn it!

- [Our Github resources/cribsheets](Working-with-git-and-github)
- [Github's own Git tutorial](https://try.github.io/levels/1/challenges/2)

### Useful shortcuts

It's handy to create desktop shortcuts for frequently used links:

- EPICSTerm (The terminal window where IOCs are built and run)
- start_ibex_server
- stop_ibex_server

These are found in `C:\Instrument\Apps\EPICS`


*it's just a goat. 

## Familiarising EPICS

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

### EPICS++

- [State Notation Language 1](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_1_EPICSAutomation.pdf) [State Notation Language 2](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_2_Sequencer.pdf)
- [ASYN/Stream Device overview](https://epics.anl.gov/docs/USPAS2014/2-Tuesday/SNL_2_Sequencer.pdf)
- [YouTube Videos covering the epics.gov.anl slideshows](https://epics.anl.gov/docs/APS2015.php)

## Control System Studio

We use CSS to create Operator Interfaces (OPIs - GUIs, essentially) for the instrument controllers. Here's an overview and get started guide.

- [Overview of CS-Studio](https://epics.anl.gov/docs/USPAS2014/1-Monday/CSS_1_Overview.pdf)
- [Intro to using CS-Studio](www.aps.anl.gov/epics/docs/USPAS2014/1-Monday/CSS_2_First_Steps.pdf)

## Input/Output Controller Resources

When building an IOC, emulator, or writing tests, much can be learned by looking at existing IOCs. However, there are several places to find good sources for learning and referencing. 

- [Protocol Files and Record Types](http://epics.web.psi.ch/software/streamdevice/doc/protocol.html) - Excellent reference for when you're mixing up your %d's and %f's.
- [Sequencer - State Notation in IOCs](http://www-csr.bessy.de/control/SoftDist/sequencer/Tutorial.html#pv-names-using-program-parameters) - All about implementing a state machine into an IOC, if needed.

> [Wiki](Home) > [Deployment](Deployment) > Migrate an Instrument Control PC

# Migrate an Instrument from SECI to IBEX

This document describes the steps and actions necessary to migrate an existing instrument control PC running SECI to IBEX. The migration process consists of 3 phases:

1. Planning - discovering, assessing and planning what needs to be done to migrate the instrument successfully
1. Preparation - implementing device support, creating configs & scripts, training the scientists
1. Migration - installing and configuring IBEX for the instrument

## Planning

Each instrument at ISIS is unique.  Although they share many similarities, there are many differences, enough to require that each migration be tackled as a unique undertaking.  In the planning phase you need to determine the scope of the migration, identify and assess the tasks that need to be done and to plan how each will be done.  Typical tasks in this phase are:

1. Meet with the scientist(s) to draw up a list of devices that are used on the instrument.  
   * It is important to determine which devices are permanent fixtures on the instrument and which are moveable (i.e. are shared with other instruments).
   * Of the moveable devices, try to find out which are used frequently and which devices are used only rarely.
   * Identify devices (if any) that are unique to that instrument.
   * Also ask the scientists which devices they plan to use in the coming cycles (this will help to prioritise work during the preparation phase).
   * Discuss with the scientist how they use these devices.  For example, do they need a GUI to view and set device parameters or will they do that via scripts?  Are some devices used for monitoring purposes only?
   * Ask the scientists if they use 5-digit or 8-digit run numbers.  Not many instruments still use 5-digit run numbers.  If they do use 5-digit run numbers, explain that they need to switch to 8-digit run numbers during the migration.  The control server will need an upgrade to the ICP program to enable 8-digit run numbers.  
1. Add the instrument to the list of instruments on the [IBEX Wiki](https://github.com/ISISComputingGroup/IBEX/wiki).
   1. Create a wiki page for the instrument (use the existing instrument pages as an example).
   1. Document the list of devices used on the instrument.  Identify which devices are already supported in IBEX and which will require support to be implemented.
   1. Record any other information you discovered during your conversation with the scientists on the wiki page.
1. Ask the scientist(s) about the SECI configs and Open-Genie scripts they use on their instrument.  
   1. Draw up a list of active configs and scripts.  They might have many configs and scripts, but some of these will be obsolete and no longer used.  There is no point in migrating obsolete configs and scripts - try to identify the ones in current use.
   1. Ask the scientists for copies of the active configs and scripts.  
   1. Add the list of active configs and scripts to the instrument wiki page.

## Preparation

In the preparation phase, the team will create software components to support the devices identified during the planning phase.  Towards the end of the preparation phase, you should work with the team to create IBEX configurations and genie_python scripts that correspond to the SECI configs and Open-Genie scripts.

1. Discuss the list of devices (identified in step 1 of the planning phase) with the team.  
   * Some devices might already be supported; 
   * some may be supported already, but will need that support to be extended 
   * others will not be currently supported.  
   * look at the lab view:
       * to identify non-standard behaviour
       * to identify rough size of the command set
Agree with the team how support will be implemented (e.g. by creating or extending IOCs and OPIs, or by using lvDCOM to interface to LabVIEW).
1. Discuss the time required to implement the required support (it might take several sprints)
1. Create any tickets required to implement the necessary support.
1. Identify when IBEX is likely to support the required devices (i.e. identify the first cycle after the required devices are supported in IBEX).
1. Tell Facilities IT (Anthony Shuttle) that an instrument is due to be migrated and ask them to put the instrument on a sub-network.  This is required so that we can use TCP/IP to communicate with the Galils.  Facilities IT will need notice of about 4-6 weeks.
1. If the instrument still uses 5-digit run numbers, update the ICP program to the latest version.
1. Check the computer that IBEX will be installed on ensuring that it has enough hard disk space.
1. As the target cycle approaches
   1. set up a PC to test the new version of IBEX.
      1. create IBEX configurations to correspond to their SECI equivalents
      1. create genie-python scripts to correspond to their Open-Genie equivalents
      1. test these configurations & scripts on the test PC
      1. demonstrate the configurations & scripts to the instrument scientists and check that they are happy with the migrated configurations & scripts
   1. arrange one or more training sessions with the scientists to help them understand how to 
      1. use IBEX
      1. create configurations & components
      1. write genie_python scripts 

## Migration

In the migration phase, IBEX will be physically installed and configured on the instrument control PC.  Experiments will switch over from being controlled with SECI to IBEX.

1. Consult with the scientists and agree a date for the physical migration to take place.  This will most likely be a shutdown period between two cycles.  Allow two or three days for the migration to take place (you will need to time to install and configure IBEX and to test it with the migrated configurations and scripts).
1. Before installing IBEX on the instrument control PC, make sure you have a full backup of the existing SECI system (including associated configs and scripts).  Ideally, do this a day or two ahead of the agreed migration date.
1. Retain the existing SECI system (including associated configs and scripts) on the instrument control PC (in case you need to revert back).
1. Check that there is sufficient space on the instrument control PC to install IBEX.
1. On the agreed date, install and configure IBEX (as described in the [Deployment](Deployment) page).
1. Install the IBEX configurations and genie-python scripts created during the preparation phase.
1. Test the new IBEX installation
1. Ask the scientists to confirm that the instrument is behaving as expected.

# How to review

To check an instrument migration/deployment as a reviewer:
- Ensure the instrument page has been updated and is showing the correct version that the instrument is running.
- Check with the person that originally did the ticket that they have contacted the instrument scientist.
- If the instrument is up, have a look around their configurations and synoptics and check that they are sensible.
- Ensure there are no outstanding tickets blocking the instrument migration.
- Ensure that blocks point at e.g. `...X` rather than `...X:SP:RBV` (unless it's clear that the block needs to point at the setpoint readback)

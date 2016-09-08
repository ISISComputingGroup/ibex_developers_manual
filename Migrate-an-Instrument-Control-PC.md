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
   * Also ask the scientists which devices they plan to use in the coming cycles (this will help to prioritise work during the preparation phase).
1. Add the instrument to the list of instruments on the [IBEX Wiki](https://github.com/ISISComputingGroup/IBEX/wiki).
   1. Create a wiki page for the instrument (use the existing instrument pages as an example).
   1. Document the list of devices used on the instrument.  Identify which devices are already supported in IBEX and which will require support to be implemented.
   1. Record any other information you discovered during your conversation with the scientists on the wiki page.
1. Ask the scientist(s) about the SECI configs and Open-Genie scripts they use on their instrument.  
   1. Draw up a list of active configs and scripts.  They might have many configs and scripts, but some of these will be obsolete and no longer used.  There is no point in migrating obsolete configs and scripts - try to identify the ones in current use.
   1. Ask the scientists for copies of the active configs and scripts.  
   1. Add the list of active configs and scripts to the instrument wiki page.

## Preparation

Prepare ...

## Migration

Migrate ...

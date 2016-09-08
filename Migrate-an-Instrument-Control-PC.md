> [Wiki](Home) > [Deployment](Deployment) > Migrate an Instrument Control PC

# Migrate an Instrument from SECI to IBEX

This document describes the steps and actions necessary to migrate an existing instrument control PC running SECI to IBEX. The migration process consists of 3 phases:

1. Planning - discovering, assessing and planning what needs to be done to migrate the instrument successfully
1. Preparation - implementing device support, creating configs & scripts, training the scientists
1. Migration - installing and configuring IBEX for the instrument

## Planning

Each instrument at ISIS is unique.  Although they share many similarities, there are many differences, enough to require that each migration be tackled as a unique undertaking.  In the planning phase you need to determine the scope of the migration, identify and assess the tasks that need to be done and to plan how each will be done.  Typical tasks in this phase are:

1. Meet with the scientist(s) to draw up a list of devices that are used on the instrument.  It is important to determine which devices are permanent fixtures on the instrument and which are moveable (i.e. are shared with other instruments).  Of the moveable devices, try to find out which are used frequently and which devices are used only rarely.  Also ask the scientists which devices 

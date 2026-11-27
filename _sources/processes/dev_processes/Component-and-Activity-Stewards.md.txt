# Component & Activity Stewards

This page lists the component & activity stewards.

## What is a component / activity steward?
A Component or Activity Steward is the individual responsible for the development and quality of a component or activity.  The role itself is [defined in more detail](#definition_component_steward) below but, in essence, it means that the named individual is responsible for the "well-being" of a component or activity.  Knowing who the relevant steward is means you have a first point of contact for finding out about that particular component or activity.

After a component/activity has been completed and stable for a cycle then the steward should retire for that activity/component. 

## List of Components/Activities & Stewards
The list of components/activities and stewards is not set in stone.  It will change over time.

Component/Activity | Steward |
--- | --- |
**Instrument Migrations** | |
MUSR Migration | LC |
OFFSPEC Migration | JH |
HIFI Migration | TBC |
CHRONUS Migration | LC & DK |
ARGUS Migration | LC & DK |
SXD Migration | LJ |
CHIPIR Migration | JH |
--- | --- |
**IBEX Core components** |  |
Script Server (NICOS) | |
Graphing/Scripting |  |
Script Generator |  |
IBEX GUI |  |
CSS & Phoebus | |
EPICS base and support modules | FA |
Delay tickets | |
Blockserver/Other server items |  |
Linter |  |
Squish |  |
Motion Control | JH |
Reflectometry | JH |
Dataweb |  |
--- | --- |
**Other items which impact significantly and directly on IBEX** |  |
Detector systems monitoring |  |
HIFI Cryomagnet | LC |
Systems (Hardware, OS, etc.) | CMS |
Lewis |  |

{#definition_component_steward}
## Definition of the role of Component / Activity Steward
The role of Component or Activity Steward is to be the individual responsible for the development and quality of a component or activity.  An example of a component is the Blockserver, or a major part of the IBEX GUI.  An example of an activity might be ensuring that an instrument is ready to migrate to IBEX (i.e. by ensuring that IBEX support the devices used on that instrument).

Being responsible does not mean that you are the sole developer or the only person who ever works on the component.  Rather it means that you are the individual responsible for the "well-being" of the component, on an on-going basis.  In other words, making sure that the component fulfils and continues to fulfil its requirements, meets quality standards, has up-to-date and accurate documentation, that bugs get fixed, etc.  It may also mean having to liaise with other members of the team, or with colleagues in other groups to make sure that components, services or hardware required by your component are identified, planned and in place at the right time.

Similarly, for an activity, you are not expected to be the only person who contributes to that activity.  Instead, you are the individual responsible for identifying the actions that need to be taken to complete the activity and helping the team plan the work required.

In both cases, component or activity, you will be involved in creating or identifying the stories that guide the development of the component or activity and discussing the relative prioritisation of those stories (i.e. when the work should be scheduled).  Depending on your role in the team, you might be responsible for several components or activities.

In practice, it is likely that you will perform a large fraction of the planning, design, development, testing and documentation, but there is no reason why others should not contribute - after all, two (or even more) heads can be better than one.  The benefit of involving other individuals is that they can propose new ideas, suggest alternative approaches, bring specific expertise or just generally help share the load.  Indeed, it is important that more than one person has knowledge of a component; someone who can take over, if necessary, if you are absent or busy working on something else - you should actively seek to involve others in the development or implementation of your component or activity.

The Component or Activity Steward does not act alone.  You need to coordinate your activities with other members of the team, including the project manager, keeping them informed about overall progress, events and problems.  For example, explaining to the team the timescales involved, whether specific events have critical timings or dependencies, whether special resources are required.  If you encounter a problem, let people know - they might be able to help.  It is important that others are kept informed about the state of your component or activity, so that they can take account of these matters for their own components or activities.

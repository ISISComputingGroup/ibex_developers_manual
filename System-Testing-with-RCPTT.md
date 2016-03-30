## Getting Started

Download the latest testing tool from the [Eclipse RCPTT website](https://www.eclipse.org/rcptt/download/).

Unpack the testing tool as you would for the Eclipse IDE.

## Configure the Application Under Test (AUT)

In the bottom of the RCPTT window, under applications, right click and add IBEX as the AUT. The location will be something like `C:\Instrument\Dev\Client\ibex_gui\base\uk.ac.stfc.isis.ibex.client.product\target\products\ibex.product\win32\win32\x86_64`. The name should be filled out automatically as `uk.ac.stfc.isis.ibex.product.product`. Click 'Finish'.

## Create Some Tests

In RCPTT create a new 'RCP Testing Tool Project' called IBEX_System_Tests.

Next create a new 'Test Suite' called All_Tests.

Next create a new 'Context' of type 'Workspace'. Under 'Workspace Options' tick 'Clear workspace'.

Create another 'Context' this time of type 'Launch'. Under options select 'Terminate existing launches' and 'Clear launch configurations'.

Add both of these contexts to 'Default Contexts' under 'Project Settings'.
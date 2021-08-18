# Local Files
Some processes require files to be created in user directory, which can be typically found at path similar to this:

`C:\Users\USERNAME\AppData\Local\IBEX`

This folder can contain data like temporary files and folders which is for use of the IBEX GUI client.

# Startup Processes
There are some processes happening during startup of IBEX client as part of application's lifecycle.
As part of ticket [#6577](https://github.com/ISISComputingGroup/IBEX/issues/6577) of particular interest
are classes: `ApplicationWorkbenchWindowAdvisor` and `ApplicationWorkbenchAdvisor` in package `uk.ac.stfc.isis.ibex.e4.product`.

In order to detect that multiple instances of IBEX client are running, a temporary file is created in local folder, in `tmp` directory.
A correctly started IBEX client will produce a temporary file in that folder which can be then detected by other instances of the client,
prompting a confirmation dialog.
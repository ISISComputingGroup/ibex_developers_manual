> [Wiki](Home) > [The GUI](The-GUI) > [Local files and Startup](Local-files-and-start-up)

# Local Files
Some processes require files to be created in user directory, which can be by default found at this path:

`C:\Users\USERNAME\AppData\Local\IBEX`

This path can be changed using preferences.
This folder can contain data like temporary files for use of the IBEX GUI client.
Note that this folder can be safely deleted as it is automatically generated when necessary.

# Startup Processes
There are some processes happening during startup of IBEX client as part of application's lifecycle.
As part of ticket [#6577](https://github.com/ISISComputingGroup/IBEX/issues/6577) of particular interest
are classes: `ApplicationWorkbenchWindowAdvisor` and `ApplicationWorkbenchAdvisor` in package `uk.ac.stfc.isis.ibex.e4.product`.

In order to detect that multiple instances of IBEX client are running, a file in the folder contains [PIDs](https://en.wikipedia.org/wiki/Process_identifier) of currently running IBEX instances. Every new instance of the client will check process list for PIDs that
are in the file. If a match is found then it means that another instance is already running and user should be prompted for confirmation to
start another client instance.
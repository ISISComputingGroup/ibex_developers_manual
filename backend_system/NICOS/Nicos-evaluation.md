> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > Nicos evaluation

This is based on the BackendRequirements page.

# What it does

Feature                                                                               | Supported? | Comments
------------------------------------------------------------------------------------- | --------- | -------------------------------------
Accept multiple clients                                                               | Yes       |
Serve up a list of available commands for the specified instrument over some protocol | No        | The current method of finding available commands is through calling a ListCommands() python method. This gives a human readable list and not enough info to construct a sensible client command list. (See further modifications)
The commands are instrument specific scripts written by the instrument scientists and/or controls team, and are stored on the server | Yes |
New commands can be added relatively quickly without requiring changes to the client | Yes | NICOS clients are dumb and only send text to the server that interprets any commands and sends a response. Means that no client updates are required.
Accept and queue up jobs from clients and add them to the job queue | Yes |
Provide feedback on the status of the job queue | Yes |
Provide feedback on the status of the current job (% done, current line etc.) | Partial | Provides feedback on the current line but not % progress.
Iterate through the job queue | Yes |
Execute the jobs, one at a time from the queue | Yes |
Allow the job queue to be edited (e.g. reordered, jobs skipped or repeated) | No | Jobs can be deleted individually and cleared (actually marks jobs to ‘block’ and thus be skipped).
Allow the current job to be suspended or aborted | Yes |
Allow individual jobs to be edited (excluding the current job?) | Yes | Jobs can be edited, including the current job, but only commands that have not been run before (e.g. not those previously run in loops)
Provide a description of what existing jobs consist of (to allow editing) | Yes |
Provide an estimate of how long a job will take | Yes | A minimum time estimate is given when the script is sent through a dry run but not when properly submitted.
Provide the elapsed time for the current job | No | Logs of when scripts are started are available but not a simple command for elapsed time.
Run a black-box script as a job (see submitted scripts section below) | Yes | 
Provide script validation, e.g. allow a dry run of a script or job | Yes | Jobs can be sent through dry runs but there is no validation of code when it is first sent to the server.

# Submitted Scripts

Feature | Supported? | Comments
------- | ---------- | --------
Script server aware - created by a script generator | No | There is no back-end support for this but could be implemented in front end.
Script server aware - written by hand | Yes | NICOS provides a number of commands that are able to pause midway and provide feedback (for example their own sleep method).
Black-box scripts - written by hand | Yes | Any valid Python code can be run on the server, they can also be paused between lines (but not within lines).

# General NICOS notes
NICOS uses a bespoke protocol across a TCP connection for communication between client and server. Scripts are sent to the server as pure python which are run on the server in a dedicated scripting thread.
 
There are a number of functionalities which are in NICOS but are not mentioned in this design document. Some of which may be useful to an ISIS scripting system but some may need to be removed/disabled.

- **Setups** - These appear very similar to the concept of configurations under IBEX. They give information on what devices are available and code to be run on instrument start-up. This will most likely be surpassed by configurations in IBEX.

- **Devices** - Comparable to IOCs in IBEX. NICOS has many different types for different devices, as well as some ‘System’ devices such as Experiment and Instrument which provide info on the current experiment and instrument. This will most likely be surpassed by IOCs in IBEX.

- **Server Modes** - NICOS provides a system for managing script permissions. There is one master that is allowed instrument control, a slave which is allowed to view and a maintenance account which is allowed to override control from master. A simulation account is also used for dry runs. 

- **Async Commands** - Code can also be asynchronously executed in the currently running script namespace (but outside of the script thread). This gives the ability to quickly change the instrument state on the fly but also brings up the potential for threads fighting for control. 

## Opinions

### Required NICOS Modifications

In contrast to other systems NICOS is very simple in the way it expects scripts to be inputted as it only requires pure python.  This means that there would be very little work required to start using the system. The following would need to be done at a minimum to get the system working:

- Get the NICOS server running as part of an instrument build

- Get the NICOS console client  working as part of an IBEX build (not necessarily integrated into the IBEX app)

- Add genie python commands to the available command list

### Further Modifications
- **Removal of unnecessary features** – Many of NICOS’ features are already implemented differently in our control system and will need to be removed or disabled within NICOS. This may prove difficult depending on how tightly coupled features are to the system, more analysis is required.

- **Provide a programmatic interface for creating ‘server-aware’ commands** – There are commands within NICOS that allow more server control (such as the sleep command that allows pausing midway and reports on how long left to sleep) and a wrapper that does some error checking on commands. However, this may need to be expanded to make it easier for breakpoints and return information to be added to new commands. This could be done with a python object that new commands inherit from? To more accurately allow the server to simulate commands they will also need to be ‘server-aware’

- **Make Genie Python ‘Server Aware’** – For genie python commands to be able to pause mid-command and to send information such as command progress they will need to be rewritten and incorporated into NICOS.

- **GUI** – The NICOS GUI, although good, is written in PyQT and cannot easily be integrated into IBEX. A plugin will have to be written to allow NICOS access. The Scan Server client could be a candidate for this interface but would require large amounts of modification as it is written to provide xml data to the server and not generic python, it would be easier to write a client from scratch. It could be possible to use a PyDev console to connect to NICOS as a start for this but a more graphical interface will be required in the future.

- **Available Commands** - Although the list of commands can be gathered from the server by sending a specific python command this would not be easily parsed by a client to show available commands. This is not an issue for users that are comfortable in using a python command line but will be useful for any simple-to-use ‘Script Builder’ client. To do this a new TCP command will need to be created which provides available commands in a more machine friendly format (e.g. xml). Another option would be to extend the already available ListCommands() method but this would be more complex as it would require to send some Python calls and parse the result before being able to display available commands to the user.

- **Provide more script feedback** – Feedback from the current script is limited  to the script’s contents, what line is currently running and a string describing the current action. Additional information such as % progress and estimated run time should be included.

- **Provide better management of job queue** – Currently the user has the ability to delete items from the queue. This could be expanded to allow copying and moving in the queue.

- **Additional script validation** – Scripts can be validated by users by performing a ‘dry run’, which will also give estimates of how long the script will take. However, there is no guarantee that a user has performed this check before running a script properly.
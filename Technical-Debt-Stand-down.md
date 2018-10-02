> [Wiki](Home) > [Processes](Processes) > [Technical Debt Stand-down](Technical-Debt-Stand-down)

A technical debt stand-down day is a day devoted to fixing technical debt in the system. The format is:

1. Choose a day where most people are free
1. Choose a topic: examples
    - Squish tests
    - Eclipse/CSS interaction
    - Tech debt tickets
    - Block server exception handling
    - Deployment/release process
        - Automatically add release numbers based on the name of the release branch
        - On install if only one component is release then fall back to later components e.g. if only 4.4.1 GUI is available install 4.4.0 server and genie_python
    - Bugs
    - Emulator/IOC tests
    - Excess logging
    - Dataweb/dashboard improvements
    - Server submodule clean
        - Add readmes to submodules in the server 
        - Remove unneeded submodules.
        - Create automated dependency map
        - Put all tools in one place (See [duplicated code](Code-Duplication))
        - Think about moving ISIS things to support

People pick up tickets when they get in often working in pairs. There is an extra standup at 4pm to discuss what has been done. This is the moment to choose to either:

- stop working on a ticket (commit everything to a branch and add it to the ticket to be picked up later)
- move it into the current sprint
- ensure a ticket is reviewed

Try to make sure all tickets by the end of the day are in a good state.

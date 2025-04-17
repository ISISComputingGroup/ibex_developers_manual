> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers) > 
[Reflectometry Troubleshooting and FAQ](Reflectometry-Troubleshooting-and-FAQ)


# Troubleshooting

## Error and Warnings

Error and warnings that the IOC produces more details

### The component XXX appears to be in the middle of a parking sequence"

```
The component <component name> appears to be in the middle of a parking sequence N of N steps. 
The error was found on axis <axis name> but other axes may be involved. Please contact an 
instrument scientists and have them move the component back into the beam before anything 
else is moved. The positions can be found in the configuration file. The autosave position 
has now been overwritten so restarting the reflectometry server will not work.
```

This error means that an axis that was parking or unparking itself but the reflectometry IOC was restarted before it was finished. To resolve this you need to find out where the axis currently is and move it to either completely parked or completely in the beam. This needs to be done carefully if there are clash conditions for the movement. The positions the component was going to move through can be found in the configuration file, several axes may be involved so make sure you move all axes for the component. The axes should be moved using the table of motors.

Once the component is in the desired place please restart the IOC and it should come back up without a problem.

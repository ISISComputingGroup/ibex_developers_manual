# Newport

The Newport XPS-D is currently in use on Larmor to control 2 rotation stages. The IOC for this, `NWPRTXPS` uses the support already present in the motor support module. Like the galil, settings are saved into autosave rather than supplied as macros.

## Commissioning / First Time Configuration

On first setup you will need to set up the controller to find an IP address through DCHP, to do this see the manual on the share. You should then reserve the IP address it has in the DHCP server (Chris MS, Freddie or FIT can do this) and put a label on the controller with the IP address and MAC address. **Note that the IP address that the controller is currently labelled with is only reserved in TS2.**

Once you have done this you can then log into the controller web interface and set up the axes (again see the manual). In setting up the axes you will give them a group name and a positioner name, you will need to enter these on the IOC for each axes in the form `Group.Positioner`. If you are unsure of the Group/Positioner you can find it in `Front Panel`->`Move` in the controller web interface.

## Quirks of the device

When the device is disconnected the motor PVs will report random values and will cycle between MAJOR alarm and COMMS ERROR alarm. You will know the device has connected when it settles into a MAJOR alarm state and the logs stop reporting disconnected. When returning after a power cycle the axes will need to be homed twice to get them back into a useable state.

## Troubleshooting

You can move the device and see additional errors via the controller web interface. By stopping the IOC and moving it through the web interface you can confirm that the hardware is working correctly. You can also view this webpage whilst the IOC is driving it to see what values it's changing.

If the axis does not get to the set value and you see:
```
SendAndReceive unexpected response =-17,GroupMoveAbsolute (Axis.Pos,380),EndOfAPI
2020/11/26 17:12:35.129  Error performing GroupMoveAbsolute[0,0] -17
```
In the log then the axis is hitting the limit set in the controller, you can change this limit in the web interface under the stages tab and then editing the `.ini` file for stage and restarting the controller.